# main.py
from fastapi import FastAPI, Request
from pydantic import BaseModel
from Backend.utils import dummy_ai_response, generate_affiliate_links

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

@app.post("/ask")
async def ask_product(req: QueryRequest):
    user_query = req.query
    product = dummy_ai_response(user_query)
    links = generate_affiliate_links(product)

    return {
        "product": product,
        "response": f"Best product for you: {product}",
        "amazon_link": links["amazon"],
        "flipkart_link": links["flipkart"]
    }