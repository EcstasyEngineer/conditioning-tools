from sqlalchemy import create_engine
from config import settings

engine = create_engine(settings['database']['url'])

# Add more database handling functions here.
