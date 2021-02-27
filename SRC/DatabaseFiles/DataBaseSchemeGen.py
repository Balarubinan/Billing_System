from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()
# lazy connect happens.....meaning  the database might not actually be connected
# right after this statement
db = create_engine('sqlite:///BillingTest1DB.db', echo=False)


# from sqlalchemy import Column, Integer, String, Date


class User(Base):
    """implement this table after core functionality"""
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    password = Column(String)

    def __repr__(self):
        """this is a string to be returned when this class is printed as such"""
        return "id ", self.id, "name ", self.password


class ItemList(Base):
    __tablename__ = "ItemList"
    name = Column(String, primary_key=True)
    rate = Column(BigInteger)
    avail = Column(Boolean)

    def __repr__(self):
        return "Name " + self.name + " Rate " + self.rate + " avail " + self.avail


class PrintedForms(Base):
    """print files are stored as blob data (pickle) """
    """store this externally if the system slowdown is seen"""
    __tablename__ = "PrintedForms"
    print_inv_no = Column(String,primary_key=True)
    date = Column(Date)
    file = Column(BLOB)

    def __repr__(self):
        return "inv_no " + self.inv_no + " date" + self.date

class Invoice(Base):
    """Stores the currently pending invoices"""
    __tablename__="InvoiceTable"
    inv_no=Column(String,primary_key=True)
    ToStation=Column(String)
    CNE=Column(String)
    CNR=Column(String)
    CLR=Column(String)
    date=Column(Date)
    branch=Column(String)
    # check if number encoding for choices speeds it up
    LRType=Column(String)
    # not nessaccry as only ttl amt is needed
    # CNRGST=Column(Float)
    # CNEGST=Column(Float)
    # Hcharge=Column(Float)
    # Crossing=Column(Float)
    Freight = Column(Float)
    Totalamt=Column(Float)
    Items=relationship("InvoiceItems",cascade="all, delete, delete-orphan")


class InvoiceItems(Base):
    """Move the data from this table to a backup table every month or so"""
    __tablename__ = "InvoiceItems"
    inv_no=Column(String, ForeignKey('InvoiceTable.inv_no'))
    name = Column(String, primary_key=True)
    rate = Column(BigInteger)
    avail = Column(Boolean)
    qty = Column(Integer)


class CountVariable(Base):
    __tablename__="Vars"
    id=Column(Integer,primary_key=True)
    last_invoice_num = Column(Integer, default=1)
    last_print_invoice_num = Column(Integer, default=1)
    last_CLR = Column(Integer, default=1)


# changing schema persists the data => that's so cool

# creates the database actually!
# uncomment only the first time of creation of the database!
Base.metadata.create_all(db)
# check if you need to explicity close DB connections!


