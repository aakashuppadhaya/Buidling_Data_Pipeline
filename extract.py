import yfinance as yf
from datetime import datetime

def comp_det():
    my_file = open("competitors.txt", "r")
    content = my_file.read()
    content_list = content.split("\n")
    my_file.close()
    return content_list
def convert_tocsv(price_history,i,company_name):
    path_out='/home/aakash/data_pipeline/'
    now = datetime.now()
    dt_string = now.strftime("%d-%m-%Y %H:%M:%S")
    price_history.to_csv(path_out+company_name+'_'+'Nasdaq'+'_'+i+'_'+dt_string+'.csv')

l=comp_det()
for i in l:
    l=yf.Ticker(i)
    company_name = l.info['longName']
    price_history = yf.Ticker(i).history(period='5d')# we can scale this paramter as per the requirement
    convert_tocsv(price_history,i,company_name)

