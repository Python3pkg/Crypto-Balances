# -*- coding: utf-8 -*-
from .services.chain_so import pull_request as chain_request
from .services.ethereum import pull_request as eth_request
from .services.doge import pull_request as doge_request


def get_balance(currency, identifier):

    if currency == 'BTC':
        return chain_request(currency, identifier)
    elif currency == 'LTC':
        return chain_request(currency, identifier)
    elif currency == 'ETH':
        return eth_request(identifier)
    elif currency == 'DOGE':
        return doge_request(identifier)
