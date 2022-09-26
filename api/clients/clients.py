from fastapi import APIRouter, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from api.deps import get_db
from services.service import *
from loguru import logger

# from sqlalchemy.orm import Session
#
# from app import schemas, crud
# from app.api.deps import get_db

router = APIRouter()
security = HTTPBasic()


@router.get("/get_subs_profile_data")
def index(msisdn: str, out_contract_name: str, user_login: str, target_date: str, in_contract_sign: str,
          credentials: HTTPBasicCredentials = Depends(security),
          db=Depends(get_db)):
    logger.debug(credentials)
    subs_profile_data = get_subs_profile_data(msisdn, user_login, out_contract_name, target_date, in_contract_sign, db)
    return {"Hello": "World", 'msisdn': msisdn}

# @router.get("", response_model=List[schemas.ProductResponse])
# def read_products(db: Session = Depends(get_db), skip: int = 0, limit: int = 100) -> Any:
#     """
#     Retrieve all products.
#     """
#     products = crud.product.get_multi(db, skip=skip, limit=limit)
#     return products
#
#
# @router.post("", response_model=schemas.ProductResponse)
# def create_product(*, db: Session = Depends(get_db), product_in: schemas.ProductCreate) -> Any:
#     """
#     Create new products.
#     """
#     product = crud.product.create(db, obj_in=product_in)
#     return product
#
#
# @router.put("", response_model=schemas.ProductResponse)
# def update_product(*, db: Session = Depends(get_db), product_in: schemas.ProductUpdate) -> Any:
#     """
#     Update existing products.
#     """
#     product = crud.product.get(db, model_id=product_in.id)
#     if not product:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="The product with this ID does not exist in the system.",
#         )
#     product = crud.product.update(db, db_obj=product, obj_in=product_in)
#     return product
#
#
# @router.delete("", response_model=schemas.Message)
# def delete_product(*, db: Session = Depends(get_db), id: int) -> Any:
#     """
#     Delete existing product.
#     """
#     product = crud.product.get(db, model_id=id)
#     if not product:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="The product with this ID does not exist in the system.",
#         )
#     crud.product.remove(db, model_id=product.id)
#     return {"message": f"Product with ID = {id} deleted."}
