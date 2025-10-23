from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime


class ProductBase(BaseModel):
    """Shared properties for Product"""

    name: str = Field(..., min_length=1, max_length=200, description="Product name")
    sku: str = Field(
        ..., min_length=1, max_length=100, description="Stock Keeping Unit"
    )
    description: str | None = Field(None, description="Product description")
    quantity: int = Field(default=0, ge=0, description="Available quantity in stock")
    min_threshold: int = Field(
        default=10, ge=10, description="Minimum stock alert level"
    )


class ProductCreate(ProductBase):
    """
    Schema for creating a new product.
    Inherits all fields from ProductBase.
    """

    pass


class ProductUpdate(BaseModel):
    """
    Schema for updating a product.
    All fields are optional (partial update).
    """

    name: str | None = Field(None, min_length=1, max_length=200)
    sku: str | None = Field(None, min_length=1, max_length=100)
    description: str | None = Field(None)
    quantity: int | None = Field(None, ge=0)
    min_threshold: int | None = Field(None, ge=0)


class ProductInDB(ProductBase):
    """
    Schema for product as stored in database.
    Includes ID and timestamps.
    """

    id: int
    created_at: datetime
    updated_at: datetime | None = None

    model_config = ConfigDict(from_attributes=True)


class ProductResponse(ProductInDB):
    """
    Schema for API responses.
    Includes computed status fields.
    """

    is_low_stock: bool
    is_out_of_stock: bool
