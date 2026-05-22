from code.entities.product.Product import Product


class SupabaseDeserializer:
    def __init__(self, client):
        self.client = client

    def get_products(self):
        response = self.client.table("Product").select("*").execute()
        data = response.data

        products = [Product(**item) for item in data]

        return products