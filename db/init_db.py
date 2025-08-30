from .setup import engine, Base
from models.user import User
from models.item import Item
from models.location import Location  

def init_db():
 print("Creating database tables...")
 Base.metadata.create_all(engine)
 print("Done. ")

 if __name__ == "__main__":
     init_db()
