def clear(db, table_name: str) -> None: 
    collection = db[table_name]
    collection.remove({})
