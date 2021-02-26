from sqlalchemy import *
from DatabaseFiles.DataBaseSchemeGen import *
from sqlalchemy.orm import sessionmaker

engine=create_engine('sqlite:///BillingTest1DB.db')
SessMaker=sessionmaker(engine)
session=SessMaker()


def write_to_invoice(data_dict:dict):
    try:
        record=Invoice(**data_dict)
        session.add(record)
        session.commit()
    except(Exception) as e:
        print("ERR INVOICE WRITE",e)

def fetch_from_invoice(station,date,branch):
    try:
        # shows a red error line but works fine
        results=session.query(Invoice).filter(Invoice.ToStation == station)
        # every item in the results is an object of the Invoice instance
        return results
    except(Exception) as e:
        print("ERR INVOICE FETCH", e)

def edit_invoice(invo_no):
    # needed??
    pass

def del_from_invoice(sdate,edate,station):
    try:
        selected=session.query(Invoice).filter(date>sdate,date<edate,Invoice.ToStation==station).delete()
        # for x in selected:
        #     session.delete(x)
        session.commit()
    except(Exception) as e:
        print("ERR INVOICE DELETE",e)

def del_one_from_invoice(inv_no):
    try:
        selected=session.query(Invoice).filter(Invoice.inv_no==inv_no).delete()
        # session.delete(selected)
        session.commit()
    except(Exception) as e:
        print("ERR INVOICE DELETE ONE ", e)

def write_to_print(print_no,date,file):
    try:
        P=PrintedForms(print_inv_no=print_no,date=date,file=file)
        session.add(P)
        session.commit()
    except(Exception) as e:
        print("ERR PRINTFORM WRITE",e)

def write_to_item_list(name,rate):
    try:
        # avail is set to true for now
        # if it's not needed simply delete it from the schema
        item=ItemList(name=name,rate=rate,avail="True")
        session.add(item)
        session.commit()
    except(Exception) as e:
        print("ERR ITEMLIST WRITE ",e)

def update_item_list(name,new_rate):
    try:
        item=session.query(ItemList).filter(name=name)
        item.rate=new_rate
        session.commit()
    except(Exception) as e:
        print("ERR ITEMLIST UPDATE",e)


# functions seem to work!!
# write_to_invoice({"CNE":"BALA1","inv_no":"111"})
# del_one_from_invoice(111)
# check date arithmetic errors
