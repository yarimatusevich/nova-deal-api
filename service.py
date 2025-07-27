from nova_act import NovaAct
from dotenv import load_dotenv
import os
from pydantic import BaseModel

class Deal(BaseModel):
	listing_title: str
	original_price: float
	discount_price: float
	url: str

class DealList(BaseModel):
	deal_list: list[Deal]

# authenticating service
load_dotenv()
os.getenv("NOVA_ACT_API_KEY")

"""
Provides instructions for NOVA act on how to find the deal using the search terms provided by user
Returns a list of 5 deals that it found for the product requested by user
"""
def request_nova(query: str):
	with NovaAct(starting_page="https://www.amazon.com") as nova:
		nova.act("Find the search bar at the top, middle of the webpage.")
		nova.act(f"Type 'RTX 2080' into the search bar and press search.")
		nova.act("On the left of the webpage there will be filters configuration options, find them.")
		nova.act("A button title all discounts will be located there, select it. If you do not see it scroll down.")
		result = nova.act("Return the first five deals listed",
						  schema=DealList.model_json_schema())

		if not result.matches_schema:
			return None # result does not match

		deal_list = DealList.model_validate(result.parsed_response)
		return deal_list

request_nova("{query}")