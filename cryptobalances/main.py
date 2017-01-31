# -*- coding: utf-8 -*-
import argparse
from cryptobalances.services import chain_request
from cryptobalances.services import eth_request
from cryptobalances.services import doge_request
from cryptobalances.services import xcp_request
from cryptobalances.services import crypto_request
from cryptobalances.services import xem_request
from cryptobalances.services import xrp_request


def main():
    parser = argparse.ArgumentParser(description='Getting balance of wallet of your crypto currency')
    parser.add_argument('currency', nargs='?', type=str, help='Type of currency')
    parser.add_argument('wallet', nargs='?', type=str, help='Identifier of wallet')
    args = parser.parse_args()
    if (args.currency and args.wallet) is not None:
        if args.currency == 'BTC':
            print(chain_request(args.currency, args.wallet))
        elif args.currency == 'LTC':
            print(chain_request(args.currency, args.wallet))
        elif args.currency == 'ETH':
            print(eth_request(args.currency, args.wallet))
        elif args.currency == 'DOGE':
            print(doge_request(args.currency, args.wallet))
        elif args.currency == 'XCP':
            print(xcp_request(args.currency, args.wallet))
        elif args.currency == 'DASH':
            print(crypto_request(args.currency, args.wallet))
        elif args.currency == 'PPC':
            print(crypto_request(args.currency, args.wallet))
        elif args.currency == 'CPC':
            print(crypto_request(args.currency, args.wallet))
        elif args.currency == 'GRT':
            print(crypto_request(args.currency, args.wallet))
        elif args.currency == 'BLK':
            print(crypto_request(args.currency, args.wallet))
        elif args.currency == 'XEM':
            print(xem_request(args.currency, args.wallet))
        elif args.currency == 'XRP':
            print(xrp_request(args.currency, args.wallet))


if __name__ == "__main__":
    main()
