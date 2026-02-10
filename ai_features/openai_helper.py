"""
Google Gemini AI helper for chat and file analysis
"""
from google import genai
from google.genai import types
from decouple import config
import PyPDF2
import csv
import io


class GeminiHelper:
    def __init__(self):
        self.api_key = config('GEMINI_API_KEY', default='')
        if self.api_key:
            self.client = genai.Client(api_key=self.api_key)
        else:
            self.client = None
    
    def chat(self, user_message, user_context=""):
        """Chat with Gemini AI"""
        if not self.api_key:
            return "Please add GEMINI_API_KEY to your environment variables. Get it free at https://ai.google.dev/"
        
        try:
            prompt = f"""You are a helpful financial advisor. 
Help users with their finances, budgeting, and money management.
{user_context}
Be friendly and give practical advice.

User question: {user_message}"""
            
            response = self.client.models.generate_content(
                model='gemini-2.5-flash',
                contents=prompt
            )
            return response.text
        except Exception as e:
            return f"Error: {str(e)}"
    
    def analyze_bank_statement(self, file_obj, file_name):
        """Analyze uploaded bank statement"""
        if not self.api_key:
            return "Please add GEMINI_API_KEY to your environment variables. Get it free at https://ai.google.dev/"
        
        try:
            # Extract text from file
            if file_name.endswith('.pdf'):
                text = self._extract_pdf_text(file_obj)
            elif file_name.endswith('.csv'):
                text = self._extract_csv_text(file_obj)
            else:
                return "Unsupported file format. Please upload PDF or CSV."
            
            # Send to Gemini for analysis
            prompt = f"""Analyze this bank statement and provide:
1. Total income
2. Total expenses  
3. Top spending categories
4. Financial recommendations

Bank Statement:
{text[:3000]}

Provide a clear, formatted analysis."""
            
            response = self.client.models.generate_content(
                model='gemini-2.5-flash',
                contents=prompt
            )
            return response.text
        except Exception as e:
            return f"Error analyzing file: {str(e)}"
    
    def _extract_pdf_text(self, file_obj):
        """Extract text from PDF"""
        try:
            pdf_reader = PyPDF2.PdfReader(file_obj)
            text = ""
            for page in pdf_reader.pages[:5]:  # First 5 pages only
                text += page.extract_text()
            return text
        except:
            return "Could not extract text from PDF"
    
    def _extract_csv_text(self, file_obj):
        """Extract text from CSV"""
        try:
            content = file_obj.read().decode('utf-8')
            return content[:3000]  # First 3000 chars
        except:
            return "Could not read CSV file"
    
    def auto_create_transactions(self, user, file_obj, file_name):
        """Auto-create transactions from bank statement using AI"""
        from transactions.models import Transaction, Category
        from datetime import datetime
        
        try:
            # Extract text
            if file_name.endswith('.csv'):
                text = self._extract_csv_text(file_obj)
            elif file_name.endswith('.pdf'):
                text = self._extract_pdf_text(file_obj)
            else:
                return 0
            
            # Ask AI to extract transactions in JSON format
            prompt = f"""Extract all transactions from this bank statement and return them as a JSON array.
Each transaction should have: date (YYYY-MM-DD), description, amount (positive for income, negative for expense), category.

Bank Statement:
{text[:3000]}

Return ONLY valid JSON array, no other text. Example:
[{{"date":"2026-02-01","description":"Salary","amount":5000,"category":"Income"}},{{"date":"2026-02-02","description":"Grocery","amount":-150,"category":"Food & Dining"}}]"""
            
            response = self.client.models.generate_content(
                model='gemini-2.5-flash',
                contents=prompt
            )
            
            # Parse JSON response
            import json
            import re
            
            # Extract JSON from response
            json_text = response.text.strip()
            # Remove markdown code blocks if present
            json_text = re.sub(r'```json\s*', '', json_text)
            json_text = re.sub(r'```\s*$', '', json_text)
            
            transactions_data = json.loads(json_text)
            
            # Create transactions
            created_count = 0
            for trans in transactions_data:
                try:
                    # Get or create category
                    category_name = trans.get('category', 'Other')
                    trans_type = 'income' if trans['amount'] > 0 else 'expense'
                    
                    category, _ = Category.objects.get_or_create(
                        user=user,
                        name=category_name,
                        defaults={'type': trans_type}
                    )
                    
                    # Parse date
                    date = datetime.strptime(trans['date'], '%Y-%m-%d').date()
                    
                    # Check for duplicates
                    exists = Transaction.objects.filter(
                        user=user,
                        date=date,
                        amount=abs(trans['amount']),
                        description=trans['description']
                    ).exists()
                    
                    if not exists:
                        Transaction.objects.create(
                            user=user,
                            category=category,
                            amount=abs(trans['amount']),
                            description=trans['description'],
                            date=date,
                            type=trans_type,
                            currency=user.preferred_currency
                        )
                        created_count += 1
                except:
                    continue
            
            return created_count
        except Exception as e:
            print(f"Auto-create error: {e}")
            return 0


# Singleton
ai_helper = GeminiHelper()
