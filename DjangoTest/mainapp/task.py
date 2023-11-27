import logging
import requests

from celery import shared_task
from dateutil import parser
from django.utils.timezone import make_aware
from mainapp import models as mainapp_models
from config.celery import celery_app

logger = logging.getLogger(__name__)


def receive_data():
    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=60min&apikey=4376J0VR4FZGGC2F'
    # url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo'
    r = requests.get(url)
    data = r.json()
    return data


def make_res_dict(data):
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
    return res


@celery_app.task
def add_data_db() -> None:
    data = receive_data()
    data_for_db = make_res_dict(data)
    model = mainapp_models.Quotes
    for el in data_for_db:
        if not model.objects.filter(time_quote=make_aware(parser.parse(el['datetime']))):
            new_data = mainapp_models.Quotes(
                simbol=el['symbol'],
                time_quote=make_aware(parser.parse(el['datetime'])),
                open=el['open'],
                high=el['high'],
                low=el['low'],
                close=el['close'],
                volume=el['volume']
            )
            new_data.save()
    return None
