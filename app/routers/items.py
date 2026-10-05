from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import models, schemas, auth
from ..database import get_db

router = APIRouter(prefix="/items", tags=["Items (CRUD)"])


# Create an item
@router.post("/", response_model=schemas.ItemOut,
             status_code=status.HTTP_201_CREATED)
def create_item(item: schemas.ItemCreate,
                db: Session = Depends(get_db),
                current_user: models.User = Depends(auth.get_current_user)):
    new_item = models.Item(**item.model_dump(), owner_id=current_user.id)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item


# Read all items of the logged-in user
@router.get("/", response_model=List[schemas.ItemOut])
def get_items(db: Session = Depends(get_db),
              current_user: models.User = Depends(auth.get_current_user)):
    return db.query(models.Item).filter(
        models.Item.owner_id == current_user.id).all()


# Read one item
@router.get("/{item_id}", response_model=schemas.ItemOut)
def get_item(item_id: int,
             db: Session = Depends(get_db),
             current_user: models.User = Depends(auth.get_current_user)):
    item = db.query(models.Item).filter(
        models.Item.id == item_id,
        models.Item.owner_id == current_user.id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


# Update an item
@router.put("/{item_id}", response_model=schemas.ItemOut)
def update_item(item_id: int, updated: schemas.ItemUpdate,
                db: Session = Depends(get_db),
                current_user: models.User = Depends(auth.get_current_user)):
    item = db.query(models.Item).filter(
        models.Item.id == item_id,
        models.Item.owner_id == current_user.id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    for key, value in updated.model_dump(exclude_unset=True).items():
        setattr(item, key, value)
    db.commit()
    db.refresh(item)
    return item


# Delete an item
@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int,
                db: Session = Depends(get_db),
                current_user: models.User = Depends(auth.get_current_user)):
    item = db.query(models.Item).filter(
        models.Item.id == item_id,
        models.Item.owner_id == current_user.id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(item)
    db.commit()