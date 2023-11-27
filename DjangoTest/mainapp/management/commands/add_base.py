from django.core.management.base import BaseCommand
from dateutil import parser
from django.utils.timezone import make_aware
from mainapp import models as mainapp_models
from mainapp.task import receive_data, make_res_dict


class Command(BaseCommand):
    help = 'Внесение записей в БД'

    def handle(self, *args, **kwargs):
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
