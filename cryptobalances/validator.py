import re


def autodetect_currency(identifier):
    if re.match('^(0x)?[0-9a-fA-F]{40}$', identifier):
        return 'ETH'
    elif re.match('^L[a-km-zA-HJ-NP-Z1-9]{33}$', identifier):
        return 'LTC'
    elif re.match('^D[a-km-zA-HJ-NP-Z1-9]{33}$', identifier):
        return 'DOGE'
    elif re.match('^X[a-km-zA-HJ-NP-Z1-9]{33}$', identifier):
        return 'DASH'
    elif re.match('^P[a-km-zA-HJ-NP-Z1-9]{33}$', identifier):
        return 'PPC'
    elif re.match('^C[a-km-zA-HJ-NP-Z1-9]{33}$', identifier):
        return 'CPC'
    elif re.match('^G[a-km-zA-HJ-NP-Z1-9]{33}$', identifier):
        return 'GRT'
    elif re.match('^B[a-km-zA-HJ-NP-Z1-9]{33}$', identifier):
        return 'BLK'
    else:
        return None
