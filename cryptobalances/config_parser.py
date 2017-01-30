# -*- coding: utf-8 -*-
import os.path
import json


def get_api_url(currency):
    # Here, an exception (TypeError) can be thrown out of the fact that
    # function read_config() returns None if file has not been open
    return read_config()['api_urls'][currency]


def read_config():
    try:
        with open(os.path.join(os.path.dirname(__file__), 'data/config.json'), "r") as fd:
            return json.loads(fd.read())
    except ValueError as error:
        print(error)
    except OSError as error:
        print(error)
    except IOError as error:
        print(error)
