# -*- coding: utf-8 -*-
import json
from urllib.request import urlopen
from urllib.error import URLError, HTTPError


def get_rates_poloniex_btc(pair):
    try:
        with urlopen('https://poloniex.com/public?command=returnTicker', timeout=60) as f:
            return json.loads(f.read().decode('utf-8')).get(pair).get('last')
    except HTTPError as error:
        return error
    except URLError as error:
        return error.reason
    except (ValueError, KeyError) as error:
        return error


def foo(currency):
    return 'None'

MAP = {'BTC_BTC': foo, 'BTC_ETH': get_rates_poloniex_btc,
       'BTC_LTC': get_rates_poloniex_btc, 'BTC_DOGE': get_rates_poloniex_btc,
       'BTC_XCP': get_rates_poloniex_btc, 'BTC_DASH': get_rates_poloniex_btc,
       'BTC_PPC': get_rates_poloniex_btc, 'BTC_CPC': foo,
       'BTC_GRT': foo, 'BTC_BLK': get_rates_poloniex_btc,
       'BTC_XEM': get_rates_poloniex_btc, 'BTC_XRP': get_rates_poloniex_btc,
       'BTC_OA': foo, 'BTC_OMNI': get_rates_poloniex_btc,
       'BTC_ZEC': get_rates_poloniex_btc, 'BTC_NXT': get_rates_poloniex_btc,
       'BTC_STEEM': get_rates_poloniex_btc, 'BTC_GOLOS': foo}
