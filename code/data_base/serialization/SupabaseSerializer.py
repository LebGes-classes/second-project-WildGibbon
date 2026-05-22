import postgrest

class SupabaseSerializer:
    def serialize_entities(self, entities: list, table: postgrest.SyncRequestBuilder):
        table.delete().neq("ctid", "(0,0)").execute()

        for entity in entities:
            dict_entity = {i[0].split("_")[-1]: i[1] for i in entity.__dict__.items()}

            table.insert(dict_entity).execute()


