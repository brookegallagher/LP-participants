#-------------------------------------------------------------------------------
# makeDB.py
#-------------------------------------------------------------------------------
from os import path, remove, environ
from sys import argv, stderr, exit
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base, Participants

#-------------------------------------------------------------------------------

def makeDB():
    try: 
        databaseUrl = environ.get('DATABASE_URL',None)
        engine = create_engine(databaseUrl)
        # engine = create_engine('postgresql://wabs:swab@localhost:5432/clubcal')

        Session = sessionmaker(bind=engine)
        session = Session()

        Base.metadata.create_all(engine)
        
    except Exception as e:
        print(e, file=stderr)
        exit(1)
