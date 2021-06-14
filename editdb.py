#-------------------------------------------------------------------------------
# editDB.py
#-------------------------------------------------------------------------------

from os import path,environ
from sys import argv, stderr, exit
from sqlalchemy import create_engine, or_
from sqlalchemy.orm import session, sessionmaker
from database import Participants
from Util import Event, Date # come back to this to import
from sqlalchemy import update
from urllib.parse import unquote
import datetime

#------------------------------------------------------------------------------
# Establish Connection
#------------------------------------------------------------------------------

# Connect to the DB
def connectDB():
    try:
        databaseUrl = environ.get('DATABASE_URL',None)
        engine = create_engine(databaseUrl)
        # engine = create_engine('postgresql://wabs:swab@localhost:5432/clubcal')
        Session = sessionmaker(bind=engine)
        session = Session()
        return (session, engine)
    except Exception as e:
        print(e, file=stderr)
        exit(1)

def disconnectDB(session, engine):
    session.close()
    engine.dispose()

#------------------------------------------------------------------------------
# Insertion into tables
#------------------------------------------------------------------------------


# Insert into "events" table 
def add_participant(email, name, lptype, date, subject):
    session, engine = connectDB()
    try:
        participant = Participants(email=email, name=name, 
                        lptype=lptype, date=date, topic=subject)
        session.add(participant)
        session.commit()

    except Exception as e:
        session.rollback()
        print(e, file=stderr)
        exit(1)

    finally:
        disconnectDB(session , engine)

#------------------------------------------------------------------------------
# Deleting from Tables
#------------------------------------------------------------------------------

# Delete a participant by id
def del_participant(id):
    session, engine = connectDB()
    try:
        session.query(Participants).filter(Participants.id==id).delete()
        session.commit()
    
    except Exception as e:
        session.rollback()
        print(e, file=stderr)
        exit(1) 

    finally:
        disconnectDB(session , engine)
