from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.sql import func
from app.core.database import Base


class Product(Base):
    """
    Product model represents items in inventory.

    Attributes:
        id: Primary key
        name: Product display name
        sku: Unique stock keeping unit code
        description: Product details
        quantity: Current stock level
        min_threshold: Alert when stock drops below this
        created_at: Timestamp of creation
        updated_at: Timestamp of last update
    """

    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, index=True)
    sku = Column(String(100), unique=True, nullable=False, index=True)
    description = Column(Text, nullable=True)

    quantity = Column(Integer, nullable=False, default=0)
    min_threshold = Column(Integer, nullable=False, default=10)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    def __repr__(self):
        return f"<Product(id={self.id}, name='{self.name}', sku='{self.sku}', quantity={self.quantity})>"

    @property
    def is_low_stock(self) -> bool:
        """Check if the product stock is below the minimum threshold."""
        return self.quantity < self.min_threshold

    @property
    def is_out_of_stock(self) -> bool:
        """Check if the product is out of stock."""
        return self.quantity <= 0
