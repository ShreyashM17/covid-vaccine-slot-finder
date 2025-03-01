# COVID Vaccine Slot Finder (Django Web App)

## Overview

The COVID Vaccine Slot Finder is a Django-based web application that allows users to find available COVID-19 vaccination slots in their area. The application requires user authentication and email verification before accessing its features.

## Features

- **User Authentication & Verification**: Users must sign up and verify their email before logging in.
- **Email Verification**: A verification link is sent to the user's registered email for account activation.
- **Real-time Slot Availability**: Fetches updated slot information using the CoWIN API.
- **Search by PIN Code or District**: Users can find slots based on their location.
- **Secure Password Storage**: Passwords are stored in an encrypted format for security.

## Prerequisites

- **Python 3.x**
- **Django Framework**
- **SMTP Email Configuration** (for verification emails)

## Installation

**Clone the Repository**:
   ```bash
   git clone https://github.com/ShreyashM17/covid-vaccine-slot-finder.git
  ```

## Email SMTP Setup:

### Navigate to ```settings.py``` and update the email configuration:
```
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # Update as needed
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@example.com'  # Add your sender email
EMAIL_HOST_PASSWORD = 'your-app-password'  # Add your app password
```
### Replace ```EMAIL_HOST_USER``` and ```EMAIL_HOST_PASSWORD``` with your email credentials.
