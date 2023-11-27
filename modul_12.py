import requests
from pprint import pprint

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=60min&apikey=4376J0VR4FZGGC2F'
#url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo'
r = requests.get(url)
data = r.json()
symbol = data['Meta Data']['2. Symbol']
dict_data = data['Time Series (60min)']
res = []
for key in dict_data.keys():
    res_dict = {}
    res_dict['symbol'] = symbol
    res_dict['datetime'] = key
    res_dict['open'] = dict_data[key]['1. open']
    res_dict['high'] = dict_data[key]['2. high']
    res_dict['low'] = dict_data[key]['3. low']
    res_dict['close'] = dict_data[key]['4. close']
    res_dict['volume'] = dict_data[key]['5. volume']
    res.append(res_dict)

#pprint(data)
#print(symbol)
#pprint(dict_data)
pprint(res)
