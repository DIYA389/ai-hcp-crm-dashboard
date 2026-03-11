from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from database import Base

class Interaction(Base):
    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True)
    hcp_name = Column(String)
    interaction_type = Column(String)
    date = Column(String)
    time = Column(String)
    attendees = Column(Text)
    topics_discussed = Column(Text)
    sentiment = Column(String)
    materials_shared = Column(Text)
    follow_up = Column(Text)

# NEW TABLE (prompt history)
class PromptHistory(Base):

    __tablename__ = "prompt_history"

    id = Column(Integer, primary_key=True, index=True)

    prompt = Column(Text)

    created_at = Column(DateTime, default=datetime.utcnow)    