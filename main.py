from pymongo import MongoClient

from utils.xacts import clear
from classes.user import User

def main():
    client = MongoClient() 
    db = client.test_db 

    clear(db, "users")

    user = User("1").__dict__
    db["users"].insert_one(user)
    print(db.users.find_one())

main()