from pydantic import BaseModel

class Deal(BaseModel):
	title: str
	original_price: float
	discount_price: float

class DealList(BaseModel):
	deal_list: list[Deal]