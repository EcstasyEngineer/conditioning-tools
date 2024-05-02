from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from config import settings

Base = declarative_base()

class Line(Base):
    __tablename__ = 'lines'

    id = Column(Integer, primary_key=True)
    template_text = Column(Text, nullable=False, unique=False)
    real_text = Column(Text, nullable=False, unique=True)
    service = Column(String(255), nullable=False) # examples: Polly, 11L
    voice = Column(String(255), nullable=False) # examples: Salli, Joanna, Ivy, Natasha, etc.
    subject = Column(String(3)) # examples: 1PS, 1PP, 2PS, 2PP, 3PS, 3PP
    dominant = Column(String(100)) # examples: Master, Mistress, Sir, Goddess, etc.
    theme = Column(String(255), nullable=False)
    difficulty = Column(String(10), nullable=False) # BASIC, LIGHT, MODERATE, DEEP, EXTREME
    audio_file_path = Column(String(255), nullable=False)

# Setup the database connection
engine = create_engine(settings['database']['url'])
Base.metadata.create_all(engine)  # This line creates tables based on the models defined

# Session = sessionmaker(bind=engine)
# session = Session()

# # Example of how to add a new line to the database
# new_line = Line(
#     text="You are getting very relaxed.",
#     service="Polly",
#     voice="Salli",
#     subject="2PS",
#     theme="Relaxation",
#     difficulty="LIGHT",
#     audio_file_path="/path/to/audio.mp3"
# )

# session.add(new_line)
# session.commit()

# # Closing the session when done
# session.close()
