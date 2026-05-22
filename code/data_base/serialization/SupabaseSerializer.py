from code.entities.product.Product import Product

import supabase


class SupabaseSerializer:
    def __init__(self, client: supabase.Client):
        self.__client = client

    def serialize_products(self, products: list[Product]):

        for product in products:
            dict_products = {'id': product.id,
                             'name': product.name,
                             'warehouse': product.warehouse,
                             'description': product.description}

            self.__client.table("Product").insert(dict_products).execute()


