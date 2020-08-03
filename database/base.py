from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



# hide data
db_path = "postgresql+psycopg2://testusr:password@postgres/testdb"
db = create_engine(db_path)
Base = declarative_base()

Session = sessionmaker(bind=db)
session = Session()

