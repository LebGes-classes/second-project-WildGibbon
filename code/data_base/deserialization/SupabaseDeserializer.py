import postgrest


class SupabaseDeserializer:
    def get_entities(self, class_name, table: postgrest.SyncRequestBuilder):
        response = table.select("*").execute()
        data = response.data

        products = [class_name(**item) for item in data]

        return products