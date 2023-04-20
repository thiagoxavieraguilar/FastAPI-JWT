from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os 

load_dotenv()
DB_URL = os.environ.get('DB_URL')

engine = create_engine(DB_URL, pool_pre_ping=True)
Session = sessionmaker(bind=engine)
