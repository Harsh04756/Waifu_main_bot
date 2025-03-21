from pymongo import MongoClient  
from config import MONGO_URL  

# MongoDB se connect karna  
client = MongoClient(MONGO_URL)  
db = client["WaifuChanBot"]  

# Collections (Tables)  
users = db["users"]       # Users ka data store karega  
waifus = db["waifus"]     # Waifus ka data store karega
