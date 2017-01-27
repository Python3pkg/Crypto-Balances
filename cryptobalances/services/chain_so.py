# -*- coding: utf-8 -*-
import json
from urllib.request import urlopen
from urllib.error import URLError, HTTPError


def pull_request(currency, identifier):
    api_url = 'https://chain.so/api/v2/get_address_balance/{network}/{identifier}'

    try:
        with urlopen(api_url.format(network=currency, identifier=identifier), timeout=60) as f:
            return json.loads(f.read().decode('utf-8'))['data']['confirmed_balance']
    except HTTPError as error:
        response = json.loads(error.read().decode('utf-8'))
        return "{}. {}".format(response['data']['network'], response['data']['address'])
    except URLError as error:
        return error.reason
    except (ValueError, KeyError) as error:
        return error
