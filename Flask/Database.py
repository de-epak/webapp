import pyodbc
import sqlalchemy as sal
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from dataclasses import dataclass


#sal.create_engine(‘dialect+driver://username:password@host:port/database’)
eng = sal.create_engine("mssql+pyodbc://localhost\SQLEXPRESS/New db?driver=SQL Server?Trusted_Connection=yes")
Base = declarative_base()

@dataclass
class Car(Base):
    __tablename__ = "Cars"

    Id = Column(Integer, primary_key=True)
    Name = Column(String)  
    Price = Column(Integer)

    def serialize():
        pass
        
    
Base.metadata.bind = eng        
Base.metadata.create_all() 

Session = sessionmaker(bind=eng)
