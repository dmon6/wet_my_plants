from datetime import datetime as dt
import random


class DerekWateringService(object):

    def __init__(self):
        print('in service class')

    def get_last_water_time(self):
        return dt.utcnow().isoformat()[:19].replace('T', ' ')

    def get_moisture(self):
        new_rand = random.randrange(0, 99)
        return new_rand