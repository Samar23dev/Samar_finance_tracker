"""
Mailgun Email Service - API-based email (bypasses SMTP port blocks on Render)
"""

import requests
from django.utils.html import strip_tags
from decouple import config
import logging
import threading

logger = logging.getLogger(__name__)


class MailgunEmailService:
    """
    Email service using Mailgun API
    Uses HTTP API (port 443) instead of SMTP to bypass Render's port blocks
    Free tier: 5,000 emails/month
    """
    
    def __init__(self):
        self.api_key = config('MAILGUN_API_KEY', default='')
        self.domain = config('MAILGUN_DOMAIN', default='')
        self.from_email = config('DEFAULT_FROM_EMAIL', default='noreply@financetracker.com')
        
        if not self.api_key or not self.domain:
            logger.warning("Mailgun not configured. Set MAILGUN_API_KEY and MAILGUN_DOMAIN.")
            print("⚠️  Mailgun not configured. Emails will be logged to console.")
        else:
            print(f"✅ Mailgun configured: {self.domain}")
    
    def send_email_async(self, to_email, subject, html_content, plain_content=None):
        """Send email asynchronously in a separate thread"""
        thread = threading.Thread(
            target=self._send_email_thread,
            args=(to_email, subject, html_content, plain_content)
        )
        thread.daemon = True
        thread.start()
        return True  # Return immediately
    
    def _send_email_thread(self, to_email, subject, html_content, plain_content=None):
        """Internal method to send email in a thread"""
        try:
            if not self.api_key or not self.domain:
                logger.error("Mailgun not configured")
                print(f"\n{'='*60}")
                print(f"📧 EMAIL (Console): {subject}")
                print(f"To: {to_email}")
                print(f"{'='*60}\n")
                return False
            
            # Create plain text version if not provided
            if not plain_content:
                plain_content = strip_tags(html_content)
            
            # Mailgun API endpoint
            url = f"https://api.mailgun.net/v3/{self.domain}/messages"
            
            # Send email via Mailgun API
            response = requests.post(
                url,
                auth=("api", self.api_key),
                data={
                    "from": self.from_email,
                    "to": to_email,
                    "subject": subject,
                    "text": plain_content,
                    "html": html_content
                },
                timeout=10
            )
            
            if response.status_code == 200:
                logger.info(f"Email sent successfully via Mailgun: {subject} to {to_email}")
                print(f"\n{'='*60}")
                print(f"✅ EMAIL SENT (Mailgun API): {subject}")
                print(f"To: {to_email}")
                print(f"Status: {response.status_code}")
                print(f"Message ID: {response.json().get('id', 'N/A')}")
                print(f"{'='*60}\n")
            else:
                logger.error(f"Mailgun returned status {response.status_code}: {response.text}")
                print(f"\n{'='*60}")
                print(f"❌ EMAIL FAILED (Mailgun): {subject}")
                print(f"Status: {response.status_code}")
                print(f"Error: {response.text}")
                print(f"{'='*60}\n")
                
        except Exception as e:
            logger.error(f"Failed to send email via Mailgun: {str(e)}")
            print(f"\n{'='*60}")
            print(f"❌ EMAIL FAILED (Mailgun): {subject}")
            print(f"To: {to_email}")
            print(f"Error: {str(e)}")
            print(f"{'='*60}\n")
    
    def send_email(self, to_email, subject, html_content, plain_content=None):
        """Send email using Mailgun API - bypasses SMTP port blocks"""
        return self.send_email_async(to_email, subject, html_content, plain_content)


# Create singleton instance
email_service = MailgunEmailService()
