import requests
import json
import pandas as pd
def stock(ticker):
    key = 'Your API KEY'
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+ticker+'&apikey='+key+'&datatype=csv'
    data = pd.read_csv(url)         #for csv read
    #print(data)                    #printing the csv data
    '''#print(url)
    #response = requests.get(url)
    #print(response, response.text, type(response.text))
    #j_response = json.loads(response.text)
    #print(j_response, type(j_response))'''
    #data.to_csv('AAPL.csv')        #exporting into a new csv file

    return data

if __name__ == "__main__":
    ticker = input("Company ticker:")
    stock(ticker)



    
