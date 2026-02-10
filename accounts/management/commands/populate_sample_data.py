"""
Management command to populate database with sample Indian users and transactions
"""
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from transactions.models import Category, Transaction, Budget
from decimal import Decimal
from datetime import datetime, timedelta
import random

User = get_user_model()


class Command(BaseCommand):
    help = 'Populate database with sample Indian users and transaction data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('Starting data population...'))

        # Sample Indian users
        users_data = [
            {
                'username': 'rahul_sharma',
                'email': 'rahul.sharma@example.com',
                'first_name': 'Rahul',
                'last_name': 'Sharma',
                'password': 'demo123456'
            },
            {
                'username': 'priya_patel',
                'email': 'priya.patel@example.com',
                'first_name': 'Priya',
                'last_name': 'Patel',
                'password': 'demo123456'
            },
            {
                'username': 'amit_kumar',
                'email': 'amit.kumar@example.com',
                'first_name': 'Amit',
                'last_name': 'Kumar',
                'password': 'demo123456'
            },
            {
                'username': 'sneha_reddy',
                'email': 'sneha.reddy@example.com',
                'first_name': 'Sneha',
                'last_name': 'Reddy',
                'password': 'demo123456'
            },
            {
                'username': 'vikram_singh',
                'email': 'vikram.singh@example.com',
                'first_name': 'Vikram',
                'last_name': 'Singh',
                'password': 'demo123456'
            }
        ]

        # Create users
        created_users = []
        for user_data in users_data:
            user, created = User.objects.get_or_create(
                username=user_data['username'],
                defaults={
                    'email': user_data['email'],
                    'first_name': user_data['first_name'],
                    'last_name': user_data['last_name']
                }
            )
            if created:
                user.set_password(user_data['password'])
                user.save()
                self.stdout.write(self.style.SUCCESS(f'Created user: {user.username}'))
            else:
                self.stdout.write(self.style.WARNING(f'User already exists: {user.username}'))
            created_users.append(user)

        # Indian expense categories
        categories_data = [
            {'name': 'Groceries', 'type': 'expense', 'description': 'Daily groceries and household items'},
            {'name': 'Rent', 'type': 'expense', 'description': 'Monthly house rent'},
            {'name': 'Transportation', 'type': 'expense', 'description': 'Auto, metro, petrol'},
            {'name': 'Food & Dining', 'type': 'expense', 'description': 'Restaurants and food delivery'},
            {'name': 'Utilities', 'type': 'expense', 'description': 'Electricity, water, gas'},
            {'name': 'Mobile & Internet', 'type': 'expense', 'description': 'Phone and internet bills'},
            {'name': 'Healthcare', 'type': 'expense', 'description': 'Medical expenses'},
            {'name': 'Entertainment', 'type': 'expense', 'description': 'Movies, OTT subscriptions'},
            {'name': 'Shopping', 'type': 'expense', 'description': 'Clothing and accessories'},
            {'name': 'Education', 'type': 'expense', 'description': 'Courses and books'},
            {'name': 'Salary', 'type': 'income', 'description': 'Monthly salary'},
            {'name': 'Freelance', 'type': 'income', 'description': 'Freelance income'},
            {'name': 'Investment Returns', 'type': 'income', 'description': 'Returns from investments'},
        ]

        # Create categories for each user
        for user in created_users:
            for cat_data in categories_data:
                category, created = Category.objects.get_or_create(
                    user=user,
                    name=cat_data['name'],
                    defaults={
                        'type': cat_data['type'],
                        'description': cat_data['description']
                    }
                )
                if created:
                    self.stdout.write(f'  Created category: {category.name} for {user.username}')

        # Sample transactions for each user
        for user in created_users:
            user_categories = Category.objects.filter(user=user)
            
            # Income transactions
            income_cats = user_categories.filter(type='income')
            for i in range(3):
                date = datetime.now() - timedelta(days=30*i)
                for cat in income_cats:
                    if cat.name == 'Salary':
                        amount = Decimal(random.randint(50000, 150000))
                    elif cat.name == 'Freelance':
                        amount = Decimal(random.randint(10000, 50000))
                    else:
                        amount = Decimal(random.randint(5000, 25000))
                    
                    Transaction.objects.create(
                        user=user,
                        category=cat,
                        amount=amount,
                        description=f'{cat.name} - {date.strftime("%B %Y")}',
                        date=date,
                        type='income',
                        currency='INR'
                    )

            # Expense transactions
            expense_cats = user_categories.filter(type='expense')
            expense_data = {
                'Groceries': [(2000, 5000, 'BigBasket order'), (1500, 3000, 'Local market'), (1000, 2500, 'DMart shopping')],
                'Rent': [(15000, 35000, 'Monthly rent payment')],
                'Transportation': [(500, 2000, 'Metro recharge'), (1000, 3000, 'Petrol'), (200, 800, 'Auto fare')],
                'Food & Dining': [(300, 1500, 'Swiggy order'), (500, 2000, 'Restaurant dinner'), (200, 800, 'Zomato lunch')],
                'Utilities': [(1500, 3500, 'Electricity bill'), (500, 1200, 'Water bill')],
                'Mobile & Internet': [(500, 1500, 'Jio recharge'), (800, 2000, 'Broadband bill')],
                'Healthcare': [(500, 5000, 'Doctor consultation'), (1000, 3000, 'Medicines')],
                'Entertainment': [(200, 800, 'Netflix subscription'), (300, 1200, 'Movie tickets')],
                'Shopping': [(1000, 5000, 'Myntra order'), (500, 2500, 'Amazon shopping')],
                'Education': [(500, 3000, 'Online course'), (300, 1500, 'Books')],
            }

            for i in range(60):  # Last 60 days
                date = datetime.now() - timedelta(days=i)
                
                # Random expenses for the day
                num_expenses = random.randint(1, 4)
                for _ in range(num_expenses):
                    cat = random.choice(expense_cats)
                    
                    if cat.name in expense_data:
                        expense_options = expense_data[cat.name]
                        min_amt, max_amt, desc_template = random.choice(expense_options)
                        amount = Decimal(random.randint(min_amt, max_amt))
                        description = desc_template
                    else:
                        amount = Decimal(random.randint(500, 3000))
                        description = f'{cat.name} expense'
                    
                    Transaction.objects.create(
                        user=user,
                        category=cat,
                        amount=amount,
                        description=description,
                        date=date,
                        type='expense',
                        currency='INR'
                    )

            # Create budgets
            budget_data = [
                ('Groceries', 15000),
                ('Food & Dining', 8000),
                ('Transportation', 5000),
                ('Entertainment', 3000),
                ('Shopping', 10000),
            ]

            for cat_name, budget_amount in budget_data:
                try:
                    category = user_categories.get(name=cat_name)
                    Budget.objects.get_or_create(
                        user=user,
                        category=category,
                        defaults={
                            'amount': Decimal(budget_amount),
                            'period': 'monthly',
                            'start_date': datetime.now().date(),
                            'end_date': (datetime.now() + timedelta(days=30)).date()
                        }
                    )
                    self.stdout.write(f'  Created budget for {cat_name}: ₹{budget_amount}')
                except Category.DoesNotExist:
                    pass

            self.stdout.write(self.style.SUCCESS(f'✓ Populated data for {user.username}'))

        self.stdout.write(self.style.SUCCESS('\n=== Data Population Complete! ==='))
        self.stdout.write(self.style.SUCCESS(f'Created {len(created_users)} users with transactions and budgets'))
        self.stdout.write(self.style.WARNING('\nDemo Login Credentials:'))
        self.stdout.write('Username: rahul_sharma | Password: demo123456')
        self.stdout.write('Username: priya_patel | Password: demo123456')
        self.stdout.write('Username: amit_kumar | Password: demo123456')
        self.stdout.write('Username: sneha_reddy | Password: demo123456')
        self.stdout.write('Username: vikram_singh | Password: demo123456')
