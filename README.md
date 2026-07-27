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
