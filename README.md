# FastAPI Template

A simple, clean FastAPI template to get you started quickly.

## Features

- ✨ FastAPI with automatic API documentation
- ⚙️ Environment-based configuration
- 🏥 Health check endpoints
- 🚀 Ready to run locally or deploy

## Quick Start

### 1. Use This Template

Click the "Use this template" button on GitHub to create your new repository.

### 2. Clone and Setup

```bash
# Clone your new repository
git clone https://github.com/lgt/fastapi-template
cd your-new-project

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Copy environment file
cp .env.example .env
```

### 3. Configure Your App

Edit `.env` file:
```bash
API_TITLE=Your App Name
API_VERSION=1.0.0
DEBUG=True
```

### 4. Run the Application

```bash
# Start the server
python main.py

# Or using uvicorn directly
uvicorn main:app --reload
```

Visit http://localhost:8000 to see your API running!

## API Documentation

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Endpoints

- `GET /` - Root endpoint with app info
- `GET /api/v1/health` - Basic health check
- `GET /api/v1/health/detailed` - Detailed health check

## Project Structure

```
├── api/
│   └── routes/
│       └── health.py       # Health check routes
├── core/
│   └── config.py          # App configuration
├── main.py                # FastAPI application
├── requirements.txt       # Python dependencies
└── .env.example          # Environment variables template
```

## Adding New Routes

1. Create a new router file in `api/routes/`
2. Import and include it in `main.py`:

```python
from api.routes.your_new_route import router as your_router
app.include_router(your_router, prefix="/api/v1")
```

## Customization

### Update App Information
Edit `core/config.py` to change default values or add new configuration options.

### Add Dependencies
Add new packages to `requirements.txt` and run:
```bash
pip install -r requirements.txt
```

### Environment Variables
Add new environment variables to `.env.example` and update `core/config.py`.

## Deployment

### Simple Deployment
```bash
pip install -r requirements.txt
python main.py
```

### Production Deployment
```bash
pip install gunicorn
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

Happy coding! 🚀