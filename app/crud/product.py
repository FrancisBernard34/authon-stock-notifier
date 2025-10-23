from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.product import Product
from app.schemas.product import ProductCreate, ProductUpdate


def get_product(db: Session, product_id: int) -> Optional[Product]:
    """Get a single product by ID"""
    return db.query(Product).filter(Product.id == product_id).first()


def get_product_by_sku(db: Session, sku: str) -> Optional[Product]:
    """Get a product by SKU"""
    return db.query(Product).filter(Product.sku == sku).first()


def get_products(db: Session, skip: int = 0, limit: int = 100) -> List[Product]:
    """
    Get all products with pagination.

    Args:
        skip: Number of records to skip (offset)
        limit: Maximum number of records to return
    """
    return db.query(Product).offset(skip).limit(limit).all()


def create_product(db: Session, product: ProductCreate) -> Product:
    """
    Create a new product.

    Raises:
        IntegrityError: If SKU already exists
    """
    db_product = Product(
        name=product.name,
        sku=product.sku,
        description=product.description,
        quantity=product.quantity,
        min_threshold=product.min_threshold,
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def update_product(
    db: Session, product_id: int, product_update: ProductUpdate
) -> Optional[Product]:
    """
    Update a product (partial update - only provided fields).

    Returns:
        Updated product or None if not found
    """
    db_product = get_product(db, product_id)
    if not db_product:
        return None

    update_data = product_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_product, field, value)

    db.commit()
    db.refresh(db_product)
    return db_product


def delete_product(db: Session, product_id: int) -> bool:
    """
    Delete a product.

    Returns:
        True if deleted, False if not found
    """
    db_product = get_product(db, product_id)
    if not db_product:
        return False

    db.delete(db_product)
    db.commit()
    return True
