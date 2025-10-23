from fastapi import FastAPI
from app.core.config import settings
from app.core.database import engine
from sqlalchemy import text
from app.api import products

# Base.metadata.create_all(bind=engine) # Now handled by Alembic

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_PREFIX}/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.include_router(products.router, prefix=settings.API_V1_PREFIX)


@app.get("/")
def read_root() -> dict[str, str]:
    """Health check endpoint"""
    return {"message": "Stock Automation API", "status": "running", "docs": "/docs"}


@app.get("/health")
def health_check() -> dict[str, str]:
    """Detailed health check"""
    db_status = "disconnected"
    try:
        # Try to execute a simple query to check database connection
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
            db_status = "connected"
    except Exception as e:
        db_status = f"error: {str(e)}"

    return {
        "status": "healthy" if db_status == "connected" else "degraded",
        "database": db_status,
    }
