from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Database 
engine = create_engine('sqlite:///lost_and_found.db')
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()