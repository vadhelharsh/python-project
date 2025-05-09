from sqlalchemy import Table, Column ,Integer , String, create_engine ,DateTime , UniqueConstraint
from sqlalchemy.orm import Session , relationship , declarative_base , sessionmaker

engine = create_engine('sqlite:///hospital_database.db', echo=True)
base = declarative_base()
class Patient(base):
    __tablename__ = "patient"
    id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname= Column(String)
    age = Column(Integer)
    gender = Column(String)
    emergencyNumber = Column(Integer, unique=True)
    dateAndTime = Column(String, nullable=False)
    hospitalName = Column(String, nullable=False)
    wardName = Column(String, nullable=False)
    bedNumber = Column(Integer, nullable=False)
    currentCondition = Column(String, nullable= False)
    fundRequired = Column(Integer,nullable=False)
    Urgency = Column(String, nullable=False)
    intialDiagnosis = Column(String, nullable=False)
    hospitalLink = Column(String)

base.metadata.create_all(engine)
Session = sessionmaker(bind = engine)
# session = Session()
