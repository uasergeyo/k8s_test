from datetime import datetime
from random import random
import schedule
from db import Numbers



def run():
    entry = {
        'ts': datetime.now(),
        'number': random()
    }
    print(entry)

    new_number = Numbers(**entry)
    new_number.save()

schedule.every(10).seconds.do(run)

while True:
    schedule.run_pending()