"""
Management command to add all existing users to Mailgun authorized recipients
"""
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from accounts.mailgun_service import email_service

User = get_user_model()


class Command(BaseCommand):
    help = 'Add all users to Mailgun authorized recipients'

    def handle(self, *args, **options):
        users = User.objects.all()
        
        self.stdout.write(f"Found {users.count()} users")
        
        added = 0
        failed = 0
        
        for user in users:
            if user.email:
                self.stdout.write(f"Adding {user.email}...")
                if email_service.add_authorized_recipient(user.email):
                    added += 1
                else:
                    failed += 1
            else:
                self.stdout.write(f"Skipping {user.username} (no email)")
        
        self.stdout.write(self.style.SUCCESS(f'\n✅ Added {added} recipients'))
        if failed > 0:
            self.stdout.write(self.style.WARNING(f'⚠️  Failed: {failed}'))
