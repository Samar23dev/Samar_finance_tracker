# Requirements Document: Finance Tracker

## Introduction

The Finance Tracker is a full-stack web application that enables users to manage their personal finances through transaction tracking, budgeting, and financial reporting. The system provides a modern, intuitive interface for users to monitor income and expenses, set budget goals, and visualize financial trends over time.

## Glossary

- **System**: The Finance Tracker application (backend API and frontend UI)
- **User**: An authenticated individual using the application to track personal finances
- **Transaction**: A financial record representing income or expense with amount, date, category, and description
- **Category**: A classification for transactions (e.g., "Groceries", "Salary") with associated type (income/expense)
- **Budget**: A spending limit set for an expense category over a specific time period
- **Dashboard**: The main overview interface displaying financial summaries and visualizations
- **API**: The Django REST Framework backend providing data and business logic
- **Frontend**: The React single-page application providing the user interface
- **Admin**: A privileged user with access to the Django admin interface

## Requirements

### Requirement 1: User Authentication and Authorization

**User Story:** As a user, I want to securely register, login, and manage my account, so that my financial data remains private and accessible only to me.

#### Acceptance Criteria

1. WHEN a new user provides valid registration details (username, email, password), THE System SHALL create a new user account with encrypted credentials
2. WHEN a user provides valid login credentials, THE System SHALL authenticate the user and return an authentication token
3. WHEN an authenticated user makes API requests, THE System SHALL validate the authentication token and authorize access
4. WHEN a user logs out, THE System SHALL invalidate the authentication token
5. THE System SHALL isolate all financial data by user, preventing access to other users' data
6. WHEN a user updates their profile information, THE System SHALL persist the changes to the database
7. IF invalid credentials are provided during login, THEN THE System SHALL return an authentication error without revealing whether the username or password was incorrect

### Requirement 2: Transaction Management

**User Story:** As a user, I want to create, view, edit, and delete financial transactions, so that I can maintain an accurate record of my income and expenses.

#### Acceptance Criteria

1. WHEN a user creates a transaction with valid data (amount, date, category, type, description), THE System SHALL persist the transaction to the database
2. WHEN a user requests their transactions, THE System SHALL return only transactions belonging to that user
3. WHEN a user edits a transaction, THE System SHALL populate the form with existing transaction data
4. WHEN a user updates a transaction, THE System SHALL persist the changes and maintain data integrity
5. WHEN a user updates a transaction, THE System SHALL automatically refresh budget calculations
6. WHEN a user filters transactions by type (income/expense), THE System SHALL return only transactions matching the specified type
7. WHEN a user filters transactions by category, THE System SHALL return only transactions in the specified category
8. WHEN a user filters transactions by date range, THE System SHALL return only transactions within the specified period
9. WHEN a user searches transactions by description, THE System SHALL return transactions containing the search term
10. WHEN a user deletes a transaction, THE System SHALL remove it from the database and refresh budget calculations
11. THE System SHALL support decimal precision of 12 digits with 2 decimal places for transaction amounts
12. THE System SHALL accept negative amounts for transactions to represent refunds or corrections
13. WHEN displaying transactions, THE System SHALL paginate results for performance
14. WHEN a transaction is created, updated, or deleted, THE System SHALL trigger budget recalculation events

### Requirement 3: Category Management

**User Story:** As a user, I want to organize my transactions into categories with visual identifiers, so that I can better understand my spending patterns.

#### Acceptance Criteria

1. WHEN a user creates a category with valid data (name, type, color, description), THE System SHALL persist the category to the database
2. THE System SHALL support both income and expense category types
3. WHEN a user assigns a color to a category, THE System SHALL store the color value for visual representation
4. WHEN a user requests their categories, THE System SHALL return only categories belonging to that user
5. WHEN a user updates a category, THE System SHALL persist the changes to all existing transactions in that category
6. IF a user attempts to delete a category with existing transactions, THEN THE System SHALL prevent deletion and return an error message
7. WHEN a user deletes a category with no transactions, THE System SHALL remove it from the database

### Requirement 4: Dashboard and Visualization

**User Story:** As a user, I want to see a visual overview of my financial status, so that I can quickly understand my current financial situation.

#### Acceptance Criteria

1. WHEN a user accesses the dashboard, THE System SHALL calculate and display total income for the current period
2. WHEN a user accesses the dashboard, THE System SHALL calculate and display total expenses for the current period
3. WHEN a user accesses the dashboard, THE System SHALL calculate and display net savings (income minus expenses)
4. WHEN a user accesses the dashboard, THE System SHALL display a pie chart showing expense distribution by category
5. WHEN a user accesses the dashboard, THE System SHALL display the 5 most recent transactions
6. THE System SHALL update dashboard data in real-time when transactions are added, modified, or deleted
7. WHEN displaying financial amounts, THE System SHALL format numbers with appropriate currency symbols and decimal precision

### Requirement 5: Financial Reporting

**User Story:** As a user, I want to view historical financial reports with visualizations, so that I can analyze trends and make informed financial decisions.

#### Acceptance Criteria

1. WHEN a user requests a monthly report, THE System SHALL calculate income and expenses for each of the last 12 months
2. WHEN displaying monthly data, THE System SHALL show income, expenses, and net savings for each month
3. WHEN a user views the report, THE System SHALL display a bar chart comparing income vs expenses over time
4. WHEN displaying monthly savings, THE System SHALL indicate positive savings with success styling and negative savings with warning styling
5. THE System SHALL aggregate transactions by month regardless of the specific day of the transaction
6. WHEN no transactions exist for a month, THE System SHALL display zero values for that month

### Requirement 6: Budget Management and Tracking

**User Story:** As a user, I want to set budget goals for expense categories and track my progress in real-time, so that I can control spending and meet financial targets.

#### Acceptance Criteria

1. WHEN a user creates a budget with valid data (category, amount, period, alert threshold), THE System SHALL persist the budget to the database
2. THE System SHALL support multiple budget periods: daily, weekly, monthly, and yearly
3. WHEN a user sets an alert threshold (1-100%), THE System SHALL store the threshold for budget monitoring
4. WHEN calculating budget progress, THE System SHALL sum all transactions in the budget category for the current period
5. WHEN budget spending reaches the alert threshold, THE System SHALL display a warning indicator
6. WHEN budget spending exceeds 100%, THE System SHALL display an error indicator
7. WHEN displaying budget progress, THE System SHALL show a visual progress bar indicating percentage spent
8. WHEN a user updates a budget, THE System SHALL recalculate progress based on the new budget amount
9. WHEN a user deletes a budget, THE System SHALL remove it without affecting the underlying transactions
10. THE System SHALL calculate budget progress in real-time as transactions are added, modified, or deleted
11. WHEN a transaction is created, updated, or deleted, THE System SHALL automatically refresh budget displays across all components
12. THE System SHALL use event-based communication to synchronize budget data between components

### Requirement 7: Database Schema and Data Integrity

**User Story:** As a system architect, I want a robust database schema with proper relationships and constraints, so that data integrity is maintained and the system scales reliably.

#### Acceptance Criteria

1. THE System SHALL use PostgreSQL as the primary database with ACID compliance
2. THE System SHALL define a User model with fields for authentication and profile information
3. THE System SHALL define a Category model with foreign key relationship to User
4. THE System SHALL define a Transaction model with foreign key relationships to User and Category
5. THE System SHALL define a Budget model with foreign key relationships to User and Category
6. THE System SHALL define a RecurringTransaction model for future recurring transaction support
7. WHEN a user is deleted, THE System SHALL cascade delete all associated data (transactions, categories, budgets)
8. WHEN a category is deleted, THE System SHALL prevent deletion if transactions exist in that category
9. THE System SHALL automatically timestamp all records with created_at and updated_at fields
10. THE System SHALL use decimal fields with precision (12, 2) for all monetary amounts

### Requirement 8: API Design and Security

**User Story:** As a frontend developer, I want a well-designed REST API with proper authentication and error handling, so that I can build a reliable user interface.

#### Acceptance Criteria

1. THE System SHALL provide RESTful API endpoints following standard HTTP methods (GET, POST, PUT, DELETE)
2. THE System SHALL use token-based authentication for all protected endpoints
3. WHEN an unauthenticated request is made to a protected endpoint, THE System SHALL return a 401 Unauthorized response
4. WHEN invalid data is submitted, THE System SHALL return a 400 Bad Request response with validation errors
5. THE System SHALL enable CORS for the React frontend origin
6. THE System SHALL serialize all model data using Django REST Framework serializers
7. THE System SHALL validate all input data before persisting to the database
8. WHEN API errors occur, THE System SHALL return structured error responses with appropriate HTTP status codes
9. THE System SHALL provide pagination parameters for list endpoints
10. THE System SHALL include API documentation through Django REST Framework's browsable API

### Requirement 9: Frontend User Interface

**User Story:** As a user, I want a modern, responsive, and intuitive interface, so that I can easily manage my finances without technical difficulties.

#### Acceptance Criteria

1. THE System SHALL provide a single-page application built with React
2. WHEN a user navigates between sections, THE System SHALL update the view without full page reloads
3. THE System SHALL display a collapsible sidebar navigation for accessing different features
4. THE System SHALL use modern design patterns including gradients, glassmorphism, and smooth animations
5. WHEN data is loading, THE System SHALL display loading indicators to provide feedback
6. WHEN errors occur, THE System SHALL display user-friendly error messages with visual feedback
7. THE System SHALL use Chart.js for rendering financial visualizations (pie charts, bar charts)
8. THE System SHALL style the interface using Tailwind CSS for consistent design
9. WHEN forms are submitted, THE System SHALL validate input on the client side before API submission
10. THE System SHALL provide responsive design that works on desktop and tablet devices

### Requirement 10: Sample Data and Testing Support

**User Story:** As a developer, I want sample data generation capabilities, so that I can test the application with realistic financial scenarios.

#### Acceptance Criteria

1. THE System SHALL provide a script to populate the database with sample data
2. WHEN sample data is generated, THE System SHALL create realistic categories for common income and expense types
3. WHEN sample data is generated, THE System SHALL create transactions spanning 12 months with realistic amounts
4. WHEN sample data is generated, THE System SHALL create budget goals with appropriate thresholds
5. THE System SHALL generate sample data that demonstrates all features including edge cases
6. THE System SHALL create sample data with varied transaction amounts including negative values
7. THE System SHALL ensure sample data maintains referential integrity across all models

### Requirement 11: Multiple Currency Support

**User Story:** As a user, I want to track transactions in multiple currencies, so that I can manage finances across different countries and currencies.

#### Acceptance Criteria

1. WHEN a user creates a transaction, THE System SHALL allow selection from 10 supported currencies (USD, EUR, GBP, JPY, INR, CAD, AUD, CHF, CNY, SEK)
2. WHEN a user creates a budget, THE System SHALL allow selection of currency for the budget amount
3. WHEN displaying transactions, THE System SHALL show the appropriate currency symbol with the amount
4. THE System SHALL store currency information with each transaction and budget in the database
5. WHEN a user filters or searches transactions, THE System SHALL maintain currency information in results
6. THE System SHALL display currency symbols correctly: $ (USD), € (EUR), £ (GBP), ¥ (JPY/CNY), ₹ (INR), C$ (CAD), A$ (AUD), Fr (CHF), kr (SEK)
7. THE System SHALL default to USD when no currency is specified

### Requirement 12: Receipt Upload and Management

**User Story:** As a user, I want to upload and store receipts for my transactions, so that I can maintain proof of purchases and reference them later.

#### Acceptance Criteria

1. WHEN a user creates or edits a transaction, THE System SHALL provide a file upload field for receipts
2. THE System SHALL accept image files (JPG, PNG) and PDF documents as receipt uploads
3. THE System SHALL enforce a maximum file size of 5MB for receipt uploads
4. WHEN a receipt is uploaded, THE System SHALL store the file in an organized directory structure by date (YYYY/MM)
5. WHEN displaying transactions with receipts, THE System SHALL provide a "View" link to open the receipt in a new tab
6. WHEN a user clicks the receipt link, THE System SHALL serve the file securely through Django's media URL
7. THE System SHALL configure MEDIA_ROOT and MEDIA_URL for proper file storage and retrieval
8. IF a user deletes a transaction with a receipt, THEN THE System SHALL maintain the receipt file (soft delete approach)
9. THE System SHALL validate file types on both frontend and backend to prevent malicious uploads

### Requirement 13: Email Notification System

**User Story:** As a user, I want to receive email notifications about important financial events, so that I can stay informed about my budget status and account activity.

#### Acceptance Criteria

1. THE System SHALL integrate with SendGrid for email delivery
2. WHEN a user's spending reaches their budget alert threshold, THE System SHALL send a budget alert email
3. WHEN a user's spending exceeds their budget limit, THE System SHALL send a budget exceeded email
4. WHEN a new user registers, THE System SHALL send a welcome email with feature overview
5. WHEN a user signs up via Google OAuth, THE System SHALL send a welcome email
6. THE System SHALL provide a management command to send weekly summary emails to all users
7. WHEN sending emails, THE System SHALL use beautiful HTML templates with proper formatting
8. THE System SHALL include relevant financial data in emails (budget amounts, spending totals, percentages)
9. IF SendGrid is not configured, THEN THE System SHALL fall back to console email backend for development
10. THE System SHALL configure FROM_EMAIL and SENDGRID_API_KEY through environment variables
11. WHEN budget alerts are triggered, THE System SHALL automatically send notifications without manual intervention

### Requirement 14: Google OAuth Integration

**User Story:** As a user, I want to sign in using my Google account, so that I can access the application quickly without creating a new password.

#### Acceptance Criteria

1. THE System SHALL integrate django-allauth for OAuth authentication
2. WHEN a user clicks "Sign in with Google", THE System SHALL redirect to Google's authentication page
3. WHEN Google authentication succeeds, THE System SHALL verify the ID token on the backend
4. IF the Google account is new, THEN THE System SHALL create a new user account with Google profile information
5. IF the Google account exists, THEN THE System SHALL authenticate the existing user
6. WHEN a user authenticates via Google, THE System SHALL return an authentication token for API access
7. THE System SHALL auto-populate user profile fields (email, first name, last name) from Google account data
8. THE System SHALL display the Google Sign-In button on both login and registration pages
9. THE System SHALL configure GOOGLE_CLIENT_ID and GOOGLE_CLIENT_SECRET through environment variables
10. THE System SHALL handle OAuth errors gracefully with user-friendly error messages
11. THE System SHALL support both new user registration and existing user login through Google OAuth
12. WHEN a Google OAuth user is created, THE System SHALL send a welcome email notification

### Requirement 15: Admin User Management

**User Story:** As an administrator, I want to manage user accounts through a dedicated admin interface, so that I can maintain the system and support users effectively.

#### Acceptance Criteria

1. THE System SHALL provide admin-only API endpoints for user management
2. WHEN an admin requests the user list, THE System SHALL return all users with their profile information
3. WHEN an admin views user details, THE System SHALL include is_staff and is_superuser status
4. WHEN an admin updates a user, THE System SHALL allow modification of username, email, and admin status
5. WHEN an admin deletes a user, THE System SHALL prevent deletion of their own account
6. THE System SHALL restrict admin endpoints to users with is_staff=True permission
7. THE System SHALL provide an AdminDashboard component in the frontend with user statistics
8. THE System SHALL provide an AdminUserManagement component for viewing and managing users
9. WHEN displaying admin features, THE System SHALL use distinct visual styling (red/pink gradient)
10. THE System SHALL show admin navigation only to authenticated admin users


---

## Implementation Status

### Phase 1: Core Features (Days 1-2) ✅ COMPLETE

**Completed Requirements:**
- ✅ Requirement 1: User Authentication and Authorization
- ✅ Requirement 2: Transaction Management
- ✅ Requirement 3: Category Management
- ✅ Requirement 4: Dashboard and Visualization
- ✅ Requirement 5: Financial Reporting
- ✅ Requirement 6: Budget Management and Tracking
- ✅ Requirement 7: Database Schema and Data Integrity
- ✅ Requirement 8: API Design and Security
- ✅ Requirement 9: Frontend User Interface
- ✅ Requirement 10: Sample Data and Testing Support

**Key Deliverables:**
- Django REST API with 25+ endpoints
- PostgreSQL database with proper relationships
- Token-based authentication
- React single-page application with modern UI
- Chart.js visualizations (pie charts, bar charts)
- Tailwind CSS styling with gradients and animations
- Sample data generation scripts

### Phase 2: Day 3 Features ✅ COMPLETE

**Completed Requirements:**
- ✅ Requirement 11: Multiple Currency Support
- ✅ Requirement 12: Receipt Upload and Management
- ✅ Requirement 13: Email Notification System
- ✅ Requirement 14: Google OAuth Integration
- ✅ Requirement 15: Admin User Management

**Key Deliverables:**
- 10 currency support (USD, EUR, GBP, JPY, INR, CAD, AUD, CHF, CNY, SEK)
- Receipt upload with JPG, PNG, PDF support (max 5MB)
- SendGrid email integration with HTML templates
- Budget alert notifications (threshold & exceeded)
- Welcome emails for new users
- Weekly summary email command
- Google OAuth with django-allauth
- Google Sign-In button on login/register pages
- Admin dashboard with user management
- Admin API endpoints with proper permissions

### Technical Stack

**Backend:**
- Django 6.0.2
- Django REST Framework
- PostgreSQL database
- django-allauth for OAuth
- SendGrid for emails
- Token authentication

**Frontend:**
- React 18
- Vite build tool
- Tailwind CSS (CDN)
- Chart.js for visualizations
- Google Sign-In library

**Development Tools:**
- Python 3.x
- Node.js & npm
- Git version control

### Configuration

**Environment Variables Required:**
```env
# Database
DATABASE_NAME=finance_tracker
DATABASE_USER=postgres
DATABASE_PASSWORD=your_password

# Django
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Optional: Email Notifications
SENDGRID_API_KEY=your_sendgrid_api_key
FROM_EMAIL=noreply@financetracker.com

# Optional: Google OAuth
GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret
```

### Testing

**Automated Tests:**
- `test_day3_features.py` - Tests all Day 3 features
- `test_admin_api.py` - Tests admin endpoints
- All tests passing ✅

**Manual Testing:**
- Backend API: http://localhost:8000
- Frontend UI: http://localhost:5173 (or 5174)
- Admin credentials: adminsamar / samar123

### Documentation

**Available Documentation:**
- `ALL_FEATURES_COMPLETE.md` - Complete feature overview
- `DAY_3_FEATURES_COMPLETE.md` - Day 3 feature details
- `GOOGLE_OAUTH_SETUP_GUIDE.md` - OAuth configuration guide
- `API_DOCUMENTATION.md` - API endpoint reference
- `QUICK_START.md` - Quick start guide

### Known Limitations

1. **Currency Conversion:** System stores amounts in original currency but does not perform automatic conversion between currencies
2. **Receipt OCR:** Receipt files are stored but text extraction is not implemented
3. **Email Scheduling:** Weekly summaries require manual command execution (no cron job configured)
4. **Mobile Responsive:** UI optimized for desktop and tablet, mobile optimization pending

### Future Enhancements

**Potential Features:**
- Real-time currency conversion using exchange rate APIs
- Receipt OCR for automatic transaction data extraction
- Scheduled email notifications with cron jobs
- Additional OAuth providers (Facebook, GitHub, Microsoft)
- Mobile-responsive design improvements
- Export functionality (CSV, PDF reports)
- Multi-language support (i18n)
- Dark mode theme
- Transaction tags and advanced filtering
- Savings goals and financial planning tools

---

## Acceptance Sign-off

**Project Status:** ✅ ALL REQUIREMENTS COMPLETE

**Phase 1 (Days 1-2):** ✅ Delivered and Tested  
**Phase 2 (Day 3):** ✅ Delivered and Tested

**Total Requirements:** 15/15 Complete (100%)  
**Total Features:** All core + Day 3 features implemented  
**Test Coverage:** Automated tests passing  
**Documentation:** Complete and up-to-date

**Ready for:** Production deployment (with proper environment configuration)

---

*Last Updated: February 9, 2026*  
*Specification Version: 2.0*  
*Implementation Status: Complete*
