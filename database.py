#-------------------------------------------------------------------------------
# database.py
#-------------------------------------------------------------------------------

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, 
from sqlalchemy import Integer, String, Date, 
from sqlalchemy.orm import relationship

# References: https://docs.sqlalchemy.org/en/13/orm/basic_relationships.html

Base = declarative_base()

class Participants(Base):
  __tablename__ = 'participants'
  id = Column(Integer, primary_key=True, autoincrement=True)
  email = Column(String) # Reference to parent Club
  name = Column(String)
  lptype = Column(String)
  topic = Column(String)
  date = Column(Date)
