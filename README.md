# Authon Stock Notifier

Product stock monitoring system with automated WhatsApp and email notifications.

## Tech Stack
- **FastAPI** - Modern web framework for building APIs
- **SQLAlchemy** - SQL toolkit and ORM
- **SQLite** - Lightweight database (can be upgraded to PostgreSQL)
- **Alembic** - Database migration tool
- **n8n** - Workflow automation for WhatsApp notifications
- **Pydantic** - Data validation and settings management

## Prerequisites

- Python 3.12 or higher
- pip (Python package installer)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository-url>
cd authon-stock-notifier
```

### 2. Create Virtual Environment

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On Linux/Mac:
source venv/bin/activate

# On Windows:
# venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```bash
touch .env
```

Add the following variables to `.env`:

```env
# Database
DATABASE_URL=sqlite:///./stock_automation.db

# API Configuration
API_V1_PREFIX=/api/v1
PROJECT_NAME=Stock Automation API

# Email Configuration (Optional)
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your-email@gmail.com
SMTP_PASSWORD=your-app-password
EMAIL_FROM=your-email@gmail.com

# Alert Configuration
ALERT_EMAILS=recipient1@example.com,recipient2@example.com
ALERT_PHONE=+1234567890

# n8n Webhook (Optional)
N8N_WEBHOOK_URL=https://your-n8n-instance.com/webhook/stock-alert
```

### 5. Run Database Migrations

```bash
# Apply migrations to create database tables
alembic upgrade head
```

### 6. Run the Application

```bash
# Development mode with auto-reload
uvicorn main:app --reload

# Production mode
uvicorn main:app --host 0.0.0.0 --port 8000
```

The API will be available at:
- **API**: http://localhost:8000
- **Interactive Docs**: http://localhost:8000/docs
- **Alternative Docs**: http://localhost:8000/redoc

## Project Structure

```
authon-stock-notifier/
├── alembic/              # Database migrations
│   ├── versions/         # Migration files
│   └── env.py           # Alembic configuration
├── app/
│   ├── api/             # API endpoints
│   ├── core/            # Core functionality (config, database)
│   ├── crud/            # Database operations
│   ├── models/          # SQLAlchemy models
│   └── schemas/         # Pydantic schemas
├── tests/               # Test files
├── main.py             # Application entry point
├── alembic.ini         # Alembic configuration
├── requirements.txt    # Python dependencies
└── .env               # Environment variables (not in git)
```

## API Endpoints

### Health Check
- `GET /` - Basic status check
- `GET /health` - Detailed health check with database status

### Products
- `GET /api/v1/products/` - List all products
- `POST /api/v1/products/` - Create new product
- `GET /api/v1/products/{id}` - Get product by ID
- `PUT /api/v1/products/{id}` - Update product
- `DELETE /api/v1/products/{id}` - Delete product

## Database Migrations

### Creating a New Migration

After modifying models:

```bash
# Generate migration automatically
alembic revision --autogenerate -m "Description of changes"

# Review the generated migration file in alembic/versions/

# Apply the migration
alembic upgrade head
```

### Common Migration Commands

```bash
# Check current migration version
alembic current

# View migration history
alembic history

# Rollback one migration
alembic downgrade -1

# Rollback to specific version
alembic downgrade <revision_id>

# Upgrade to latest
alembic upgrade head
```

## Development

### Running Tests

```bash
pytest
```

### Code Formatting

```bash
# Format code with black
black .
```

### Type Checking

This project uses Pyright for type checking. Configuration is in `pyrightconfig.json`.

## Troubleshooting

### Import Errors in IDE

If your IDE shows "Import could not be resolved" errors:

1. Make sure your IDE is using the virtual environment Python interpreter
2. Path should be: `./venv/bin/python` (or `venv\Scripts\python.exe` on Windows)
3. Restart your IDE/language server

### Database Errors

If you see "no such table" errors:

```bash
# Run migrations
alembic upgrade head
```

If migrations fail:

```bash
# Delete the database and start fresh (WARNING: loses all data)
rm stock_automation.db
alembic upgrade head
```

### Virtual Environment Issues

If you have issues with the virtual environment:

```bash
# Remove and recreate
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Contributing

1. Create a new branch for your feature
2. Make your changes
3. Run tests and formatting
4. Create a pull request

## License

[Add your license here]

## Contact

[Add contact information]