# Assuming the structure of your project and the presence of these modules
from config import settings
from data.loader import insert_into_db
from data.models import Line, Base  # Assuming your model definitions are here
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import boto3
import os

from tts.tts_engine import text_to_file
from utils.tools import template_to_text

# Setup database connection
engine = create_engine(settings['storage']['url'])
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# AWS Polly client setup
polly_client = boto3.client(
    'polly',
    aws_access_key_id=settings['aws']['access_key_id'],
    aws_secret_access_key=settings['aws']['secret_access_key'],
    region_name=settings['aws']['region_name']
)

# Example usage
theme=["gratitude", "discipline", "broken", "bimbo", "empty"]
dominant="Master"
subject = "1PS"
with open(os.path.join("preconverted",f'{theme}.txt'), 'r') as file:
    for line in file:
        real_text, contains_subject, contains_dominant= template_to_text(line)
        audio_path = text_to_file(real_text)
        insert_into_db(line, real_text, subject, dominant, 'theme', 'MODERATE', "Polly", "Salli", audio_path)

session.close()
