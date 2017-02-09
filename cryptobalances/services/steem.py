# -*- coding: utf-8 -*-
import json
from urllib.request import urlopen
from urllib.error import URLError, HTTPError
from cryptobalances.config import get_api_url


def pull_request(currency, identifier):
    try:
        data = '{{"jsonrpc": "2.0", "method": "get_accounts", "params": [["{0}"]], "id": 1}}'.format(identifier)
        with urlopen(get_api_url(currency), data=data.encode('utf-8'), timeout=60) as f:
            # Function split() needed because the balance returned in the following form: "21.340 STEEM"
            # Also we can get the balance in USD. Just set key "sbd_balance" instead "balance"
            return json.loads(f.read().decode('utf-8'))['result'][0]['balance'].split(' ')[0]
    except HTTPError as error:
        print(error)
    except URLError as error:
        print(error)
    except (ValueError, KeyError) as error:
        return error
