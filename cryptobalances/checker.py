# -*- coding: utf-8 -*-
import json
import argparse
from urllib.request import urlopen
from urllib.error import URLError, HTTPError


def get_balance(currency, identifier):
    api_url = {'ETH': 'http://api.etherscan.io/api?module=account&action=balance&address={identifier}&tag=latest',
               'BTC': 'https://chain.so/api/v2/get_address_balance/{network}/{identifier}',
               'LTC': 'https://chain.so/api/v2/get_address_balance/{network}/{identifier}',
               'DOGE': 'http://dogechain.info/api/v1/address/balance/{identifier}',
               'XCP': 'http://xcp.blockscan.com/api2?module=address&action=balance&btc_address={identifier}'}
    try:
        with urlopen(api_url[currency].format(network=currency, identifier=identifier), timeout=60) as f:
            return json.loads(f.read().decode('utf-8'))['data']['confirmed_balance']
    except HTTPError as error:
        response = json.loads(error.read().decode('utf-8'))
        print("{}. {}".format(response['data']['network'], response['data']['address']))
    except URLError as error:
        print(error.reason)
    except (ValueError, KeyError) as error:
        print(error)


def main():
    parser = argparse.ArgumentParser(description='Getting balance of wallet of your crypto currency')
    parser.add_argument('currency', nargs='?', type=str, help='Type of currency')
    parser.add_argument('wallet', nargs='?', type=str, help='Identifier of wallet')
    args = parser.parse_args()
    if (args.currency and args.wallet) is not None:
        print(get_balance(args.currency, args.wallet))


if __name__ == "__main__":
    main()
