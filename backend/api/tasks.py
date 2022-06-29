from celery import shared_task
import requests

@shared_task
def set_price_10():
    return 10.00
