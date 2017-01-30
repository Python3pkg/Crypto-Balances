import re


def autodetect_currency(identifier):
    if re.match('^(0x)?[0-9a-fA-F]{40}$', identifier):
        return 'ETH'
    elif re.match('^L[a-km-zA-HJ-NP-Z1-9]{33}$', identifier):
        return 'LTC'
    elif re.match('^D[a-km-zA-HJ-NP-Z1-9]{33}$', identifier):
        return 'DOGE'
    else:
        return None
