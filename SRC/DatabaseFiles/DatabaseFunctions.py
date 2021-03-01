from SRC.DatabaseFiles.DataBaseSchemeGen import *
from sqlalchemy.orm import sessionmaker
from pickle import load, dump
import os

# engine=create_engine('sqlite:///./DatabaseFiles/BillingTest1DB.db')
Base.metadata.create_all(db)
SessMaker = sessionmaker(db)
session=SessMaker()

# vars_dict = load(open('DatabaseFiles/fileTMP/variables.pkl', 'rb'))
# print(vars_dict)



def write_to_invoice(data_dict:dict):
    try:
        data_dict['Items'] = [InvoiceItems(inv_no=data_dict['inv_no'], name=x[1], rate=x[2], qty=x[0]) for x in
                              data_dict['Items']]
        record=Invoice(**data_dict)
        session.add(record)
        session.commit()
    except(Exception) as e:
        print("ERR INVOICE WRITE",e)

def fetch_from_invoice(station,sdate,edate,branch):
    try:
        # shows a red error line but works fine
        if station is None:
            if "All" in branch:
                results = session.query(Invoice).filter(Invoice.date >= sdate,
                                                    Invoice.date <= edate)
            else:
                results = session.query(Invoice).filter(Invoice.date >= sdate,
                                                        Invoice.date <= edate,Invoice.branch == branch)
        else:
            if "All" in branch:
                results = session.query(Invoice).filter(Invoice.ToStation==station,Invoice.date >= sdate,
                                                        Invoice.date <= edate)
            else:
                results = session.query(Invoice).filter(Invoice.ToStation==station,Invoice.date >= sdate,
                                                        Invoice.date <= edate, Invoice.branch == branch)
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


def del_by_using_record(record):
    try:
        session.delete(record)
        session.commit()
    except(Exception) as e:
        print("ERR DEL BY RECORD ", e)

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
        item = ItemList(name=name, rate=rate, avail=True)
        session.add(item)
        session.commit()
    except(Exception) as e:
        print("ERR ITEMLIST WRITE ",e)

def update_item_list(name,new_rate):
    try:
        item = session.query(ItemList).filter(name == name)
        item.rate=new_rate
        session.commit()
    except(Exception) as e:
        print("ERR ITEMLIST UPDATE",e)


def fetch_all_ItemsList():
    # return a dictionary of items with values as rates
    # TEST CODE
    try:

        return {'item1': 80, 'item2': 770, 'item3': 900, 'item4': 100}
    except:
        pass


def sno_get_next():
    # write a function to fetch the last serila number for the current table!!
    try:
        return -1
    except:
        pass


def get_next_invno():
    # write a function to fetch the last invoice number from the Vars table!!
    try:
        vars_dict['last_inv_no'] += 1
        return (vars_dict['last_inv_no'])
    except:
        print("ERROR get next invoice")


def get_last_CLR():
    # implement a function fo circulary allocate LCR numbers
    try:
        return vars_dict['last_CLR']
    except(Exception) as e:
        print("ERROR get_last", e)


def inc_CLR():
    # write a function to update the last CLR number
    try:
        vars_dict['last_CLR'] += 1
        print(vars_dict['last_CLR'], "is the value")
        dump_dict()
        return vars_dict['last_CLR']
    except(Exception) as e:
        print("inc ERROR ", e)


def dump_dict():
    file = open('DatabaseFiles/fileTMP/variables.pkl', 'wb')
    dump(vars_dict, file)
    file.close()

# for x in range(5):
#     inc_CLR()
# print("Las ",get_last_CLR())


# functions seem to work!!
# write_to_invoice({"CNE":"BALA1","inv_no":"111","ITEMS":['a','b','c']})
# del_one_from_invoice(111)
# check date arithmetic errors
