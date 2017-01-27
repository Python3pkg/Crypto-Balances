# -*- coding: utf-8 -*-
import json
from urllib.request import urlopen
from urllib.error import URLError, HTTPError


def pull_request(identifier):
    api_url = 'http://dogechain.info/api/v1/address/balance/{identifier}'

    try:
        with urlopen(api_url.format(identifier=identifier), timeout=60) as f:
            response = json.loads(f.read().decode('utf-8'))
            if response['message'] is 'NOTOK':
                return "{}. {}".format(response['message'], response['result'])
            return response['result']
    except HTTPError as error:
        return error.reason
    except URLError as error:
        return error.reason
    except (ValueError, KeyError) as error:
        return error
