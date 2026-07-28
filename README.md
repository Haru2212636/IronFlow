# IronFlow - Simple Workout & Strength Tracker

## Project Overview
IronFlow is a web application designed for fitness enthusiasts to log their daily training sessions. [cite: 273]

## Development Environment
- Framework: Django
- Package Manager: uv
- Python Version: 3.11.8

## Tools Configuration
- Formatter: Black [cite: 29]
- Linter: Pylint [cite: 32]
- Testing: pytest & pytest-django [cite: 68, 69]
- Code Coverage: coverage.py [cite: 90]

## Database Schema Spec
The system implements the following database models to manage customer related data:
- **Country**: Stores country information (`country`, `last_update`).
- **City**: Belongs to a Country (`city`, `country_id`, `last_update`).
- **Address**: Stores physical address and contact info (`address`, `address2`, `district`, `city_id`, `postal_code`, `phone`, `last_update`).
- **Customer**: Manages customer profiles linked to an Address (`store_id`, `first_name`, `last_name`, `email`, `address_id`, `active`, `create_date`, `last_update`).
## Exercise 11: Deployment Architecture & Instructions

### Architecture Decisions
- **Hosting / Environment**: Deployed in a production-ready environment using Waitress (WSGI server) on Linux.
- **Application Server**: `waitress` is used for handling incoming HTTP production requests efficiently[cite: 1].
- **Static File Handling**: Static assets (CSS, JS, HTMX) are aggregated using `collectstatic` and served directly via `whitenoise` middleware[cite: 1].
- **Media Files Handling**: Not applicable for current version (no user upload required).

### Deployment Steps
1. Install production dependencies:
   ```bash
   uv add whitenoise waitress

