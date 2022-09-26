from requests import exceptions
from zeep import Client
from zeep.plugins import HistoryPlugin

from loguru import logger
from lxml import etree

from core import settings


class ZeepClient:
    def __init__(self):
        try:
            self.client = Client(settings.wsdlLink)
        except exceptions.ConnectTimeout:
            logger.error('Timeout connection to server')
        except exceptions.ConnectionError:
            logger.exception('Error connection to server')
        except Exception:
            logger.exception('Exceprion!!!')

    def close(self):
        self.client.transport.session.close()
