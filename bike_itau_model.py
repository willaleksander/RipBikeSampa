from sqlalchemy import Column, DateTime, String, Integer, Boolean, Float, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
import datetime
import os
 
 
Base = declarative_base()
 
 
class EstacaoBikeItau(Base):
	__tablename__ = 'estacao'
	idEstacao = Column(Integer, primary_key=True)
	nome = Column(String)
	endereco = Column(String)
	latitude = Column(Float)
	longitude = Column(Float)
	numBicicletas = Column(Integer)
 
class MovimentacaoBikeItau(Base):
	__tablename__ = 'movimentacao'
	id = Column(Integer, primary_key=True)
	statusOnline = Column(String)
	statusOperacao = Column(String)
	vagasOcupadas = Column(Integer)
	vagasDisponiveis = Column(Integer)
	timestamp = Column(DateTime, default=datetime.datetime.now())
	idEstacao = Column(Integer, ForeignKey('estacao.idEstacao'))
	# Use cascade='delete,all' to propagate the deletion of a Department onto its Employees
	estacao = relationship(
		EstacaoBikeItau,
		backref=backref('movimentacoes',
						 uselist=True,
						 cascade='delete,all'))
 
 
from sqlalchemy import create_engine
os.chdir(os.path.dirname(os.path.abspath(__file__)))
engine = create_engine('sqlite:///bike_itau.sqlite')
engine.connect().connection.connection.text_factory = str
 
from sqlalchemy.orm import sessionmaker
session = sessionmaker()
session.configure(bind=engine)
Base.metadata.create_all(engine)
