import os
from dotenv import load_dotenv
from models import DealList
from nova_act import NovaAct

def initialize_service() -> None:
	load_dotenv()
	os.getenv("NOVA_ACT_API_KEY")

def query_nova(query: str) -> DealList | None:
	with NovaAct(starting_page="https://www.amazon.com") as nova:
		nova.act("Find the search bar at the top, middle of the webpage.")
		nova.act(f"Type '{query}' into the search bar and press search.")
		nova.act("On the left of the webpage there will be filters configuration options, find them.")
		nova.act("A button title all discounts will be located there, select it. If you do not see it scroll down.")
		result = nova.act(
			prompt="Return the first five deals listed",
			schema=DealList.model_json_schema()
		)

		print(result)

		if not result.matches_schema:
			return None

		return DealList.model_validate(result)