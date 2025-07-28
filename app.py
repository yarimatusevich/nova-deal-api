from nova_service import initialize_service, query_nova
from models import DealList
from fastapi import FastAPI
app = FastAPI()

"""
Initializes Nova Act api and creates a prompt for it to retrieve the top 5 deals for the user input
FastAPI automatically converts the DealList Pydantic model into JSON format
"""
@app.get("/{product_name}", response_model=DealList | None)
def search_deals(product_name: str) -> DealList | None:
    initialize_service()

    deals = query_nova(query=product_name)

    return deals