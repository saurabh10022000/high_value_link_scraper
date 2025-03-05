from sqlalchemy import Column, Integer, String, JSON
from database import Base

class Link(Base):
    __tablename__ = "links"
    
    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, index=True)
    text = Column(String)
    score = Column(Integer)
    matched_keywords = Column(JSON)
