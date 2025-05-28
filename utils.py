# utils.py

def dummy_ai_response(query: str) -> str:
    # Simulate a response from your fine-tuned model
    if "smartphone" in query.lower():
        return "Samsung Galaxy M14"
    elif "headphones" in query.lower():
        return "boAt Rockerz 550"
    else:
        return "Generic Product"

def generate_affiliate_links(product_name: str) -> dict:
    # Clean the product name for URL compatibility
    product_query = product_name.replace(" ", "+")
    
    # Add your actual affiliate IDs here
    amazon_ref_id = "youramazonid-21"
    flipkart_ref_id = "yourflipkartid"

    amazon_link = f"https://www.amazon.in/s?k={product_query}&tag={amazon_ref_id}"
    flipkart_link = f"https://www.flipkart.com/search?q={product_query}&affid={flipkart_ref_id}"

    return {
        "amazon": amazon_link,
        "flipkart": flipkart_link
    }