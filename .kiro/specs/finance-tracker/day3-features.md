# Day 3: Additional Features - Requirements

## Overview
Implement advanced features to enhance the Finance Tracker application with OAuth authentication, email notifications, receipt management, and multi-currency support.

## Feature 1: Multiple Currencies Support

**Priority**: HIGH (Easiest to implement, foundational for other features)

### User Stories
- As a user, I want to select a currency when creating a transaction, so I can track expenses in different currencies
- As a user, I want to see currency symbols in reports and dashboards
- As a user, I want to set a preferred default currency in my profile

### Acceptance Criteria
1. WHEN creating a transaction, THE System SHALL allow selection from supported currencies (USD, EUR, GBP, JPY, INR, CAD, AUD, etc.)
2. WHEN displaying transaction amounts, THE System SHALL show the appropriate currency symbol
3. WHEN generating reports, THE System SHALL group transactions by currency
4. WHEN a user sets a preferred currency, THE System SHALL use it as default for new transactions
5. THE System SHALL store currency code (ISO 4217) with each transaction

### Technical Implementation
- ✅ Transaction model already has `currency` field (CharField, max_length=3, default='USD')
- ✅ User model already has `preferred_currency` field
- Add currency dropdown to transaction form in frontend
- Add currency display in transaction list and reports
- Add currency filter in reports

### Files to Modify
- `finance-tracker-frontend/src/App.jsx` - Add currency dropdown to transaction form
- `finance-tracker-frontend/src/App.jsx` - Display currency in transaction list
- `finance-tracker-frontend/src/App.jsx` - Add currency grouping in reports

---

## Feature 2: Receipt Uploading

**Priority**: HIGH (Builds on existing infrastructure)

### User Stories
- As a user, I want to upload receipt images when creating transactions, so I can keep proof of purchases
- As a user, I want to view uploaded receipts, so I can verify transaction details
- As a user, I want to download receipts, so I can use them for tax purposes

### Acceptance Criteria
1. WHEN creating/editing a transaction, THE System SHALL allow uploading image files (JPG, PNG, PDF)
2. WHEN a receipt is uploaded, THE System SHALL store it securely with the transaction
3. WHEN viewing a transaction with a receipt, THE System SHALL display a preview/download link
4. THE System SHALL limit receipt file size to 5MB
5. THE System SHALL validate file types before upload
6. WHEN a transaction is deleted, THE System SHALL also delete associated receipts

### Technical Implementation
- ✅ Transaction model already has `receipt` field (ImageField)
- Configure MEDIA_ROOT and MEDIA_URL in settings
- Add file upload input to transaction form
- Add receipt preview/download in transaction list
- Configure Django to serve media files in development

### Files to Modify
- `finance_tracker/settings.py` - Configure MEDIA_ROOT and MEDIA_URL
- `finance_tracker/urls.py` - Add media URL pattern for development
- `transactions/serializers.py` - Handle file upload in serializer
- `finance-tracker-frontend/src/App.jsx` - Add file input to transaction form
- `finance-tracker-frontend/src/App.jsx` - Display receipt preview/download

---

## Feature 3: Email Notification System

**Priority**: MEDIUM (Requires external service setup)

### User Stories
- As a user, I want to receive email alerts when I exceed budget thresholds, so I can control spending
- As a user, I want to receive weekly financial summaries, so I stay informed about my finances
- As a user, I want to control notification preferences, so I only receive relevant emails

### Acceptance Criteria
1. WHEN a budget reaches alert threshold, THE System SHALL send an email notification
2. WHEN a budget is exceeded, THE System SHALL send an urgent email notification
3. WHEN enabled, THE System SHALL send weekly summary emails with income/expense totals
4. THE System SHALL respect user notification preferences (email_notifications, budget_alert_notifications)
5. THE System SHALL use professional email templates with branding
6. THE System SHALL handle email delivery failures gracefully

### Technical Implementation
- Install SendGrid Python library
- Create notification service module
- Create email templates (HTML)
- Add signal handlers for budget alerts
- Add management command for weekly summaries
- Add notification preferences to user profile

### Files to Create
- `accounts/notifications.py` - Email notification service
- `accounts/email_templates/` - HTML email templates
- `accounts/management/commands/send_weekly_summary.py` - Weekly summary command

### Files to Modify
- `requirements.txt` - Add sendgrid
- `finance_tracker/settings.py` - Add SendGrid configuration
- `transactions/api_views.py` - Trigger notifications on transaction create
- `finance-tracker-frontend/src/App.jsx` - Add notification preferences to profile

---

## Feature 4: OAuth Integration (Google)

**Priority**: MEDIUM (Most complex, requires external setup)

### User Stories
- As a new user, I want to sign up using my Google account, so I can register quickly without creating a password
- As an existing user, I want to link my Google account, so I can login with either method
- As a user, I want a seamless OAuth flow, so the experience is smooth and secure

### Acceptance Criteria
1. WHEN a user clicks "Sign in with Google", THE System SHALL redirect to Google OAuth consent screen
2. WHEN Google authentication succeeds, THE System SHALL create or link a user account
3. WHEN a new user signs up via Google, THE System SHALL create an account with Google profile data
4. WHEN an existing user signs in via Google, THE System SHALL authenticate and return a token
5. THE System SHALL handle OAuth errors gracefully with user-friendly messages
6. THE System SHALL store OAuth tokens securely

### Technical Implementation
- Install django-allauth and dependencies
- Configure Google OAuth application in Google Cloud Console
- Add OAuth endpoints to API
- Add "Sign in with Google" button to frontend
- Handle OAuth callback and token exchange
- Create or link user accounts based on Google email

### Files to Create
- `accounts/oauth_views.py` - OAuth callback handlers

### Files to Modify
- `requirements.txt` - Add django-allauth, google-auth
- `finance_tracker/settings.py` - Configure allauth and Google OAuth
- `finance_tracker/urls.py` - Add allauth URLs
- `accounts/api_views.py` - Add OAuth endpoints
- `finance-tracker-frontend/src/App.jsx` - Add Google sign-in button

---

## Implementation Order

### Phase 1: Multiple Currencies (30 minutes)
1. Add currency dropdown to transaction form
2. Display currency in transaction list
3. Add currency filter in reports
4. Test with different currencies

### Phase 2: Receipt Uploading (45 minutes)
1. Configure media settings
2. Add file upload to transaction form
3. Update serializer to handle files
4. Add receipt preview/download UI
5. Test file upload and retrieval

### Phase 3: Email Notifications (1 hour)
1. Install SendGrid
2. Create notification service
3. Create email templates
4. Add budget alert logic
5. Add notification preferences UI
6. Test email delivery

### Phase 4: OAuth Integration (1.5 hours)
1. Install django-allauth
2. Configure Google OAuth in settings
3. Create OAuth endpoints
4. Add Google sign-in button
5. Handle OAuth callback
6. Test OAuth flow

---

## Environment Variables Needed

```env
# SendGrid (for notifications)
SENDGRID_API_KEY=your_sendgrid_api_key
FROM_EMAIL=noreply@financetracker.com

# Google OAuth (for authentication)
GOOGLE_OAUTH_CLIENT_ID=your_google_client_id
GOOGLE_OAUTH_CLIENT_SECRET=your_google_client_secret
GOOGLE_OAUTH_REDIRECT_URI=http://localhost:8000/api/auth/google/callback/
```

---

## Testing Checklist

### Multiple Currencies
- [ ] Create transaction with USD
- [ ] Create transaction with EUR
- [ ] Create transaction with GBP
- [ ] Verify currency symbols display correctly
- [ ] Verify reports group by currency

### Receipt Uploading
- [ ] Upload JPG receipt
- [ ] Upload PNG receipt
- [ ] Upload PDF receipt
- [ ] Verify file size limit (5MB)
- [ ] View receipt preview
- [ ] Download receipt
- [ ] Delete transaction with receipt

### Email Notifications
- [ ] Trigger budget alert at threshold
- [ ] Trigger budget exceeded alert
- [ ] Verify email delivery
- [ ] Test notification preferences
- [ ] Verify email template formatting

### OAuth Integration
- [ ] Sign up with Google (new user)
- [ ] Sign in with Google (existing user)
- [ ] Verify user profile data from Google
- [ ] Test OAuth error handling
- [ ] Verify token security

---

## Success Criteria

All Day 3 features implemented and tested:
✅ Users can create transactions in multiple currencies
✅ Users can upload and view receipts
✅ Users receive email notifications for budget alerts
✅ Users can sign up/login with Google OAuth

