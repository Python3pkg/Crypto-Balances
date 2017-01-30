# -*- coding: utf-8 -*-
from cryptobalances.validator import autodetect_currency
from cryptobalances.services.chain_so import pull_request as chain_request
from cryptobalances.services.ethereum import pull_request as eth_request
from cryptobalances.services.doge import pull_request as doge_request
from cryptobalances.services.counterparty import pull_request as xcp_request
from cryptobalances.services.chain_cryptoid import pull_request as crypto_request


def get_balance(currency, identifier):

    auto_currency = autodetect_currency(identifier)

    if auto_currency:
        currency = auto_currency

    if currency == 'BTC':
        return chain_request(currency, identifier)
    elif currency == 'LTC':
        return chain_request(currency, identifier)
    elif currency == 'ETH':
        return eth_request(currency, identifier)
    elif currency == 'DOGE':
        return doge_request(currency, identifier)
    elif currency == 'XCP':
        return xcp_request(currency, identifier)
    elif currency == 'DASH':
        return crypto_request(currency, identifier)
    elif currency == 'PPC':
        return crypto_request(currency, identifier)
    elif currency == 'CPC':
        return crypto_request(currency, identifier)
    elif currency == 'GRT':
        return crypto_request(currency, identifier)
    elif currency == 'BLK':
        return crypto_request(currency, identifier)
