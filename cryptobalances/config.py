# -*- coding: utf-8 -*-


def get_api_url(currency):
    api_urls = {"BTC": "https://chain.so/api/v2/get_address_balance/{network}/{identifier}",
                "LTC": "https://chain.so/api/v2/get_address_balance/{network}/{identifier}",
                "ETH": "http://api.etherscan.io/api?module=account&action=balance&address={identifier}&tag=latest",
                "DOGE": "http://dogechain.info/api/v1/address/balance/{identifier}",
                "XCP": "http://xcp.blockscan.com/api2?module=address&action=balance&btc_address={identifier}",
                "DASH": "http://chainz.cryptoid.info/dash/api.dws?q=getbalance&a={identifier}",
                "PPC": "http://chainz.cryptoid.info/ppc/api.dws?q=getbalance&a={identifier}",
                "CPC": "http://chainz.cryptoid.info/cpc/api.dws?q=getbalance&a={identifier}",
                "GRT": "http://chainz.cryptoid.info/grt/api.dws?q=getbalance&a={identifier}",
                "BLK": "http://chainz.cryptoid.info/blk/api.dws?q=getbalance&a={identifier}",
                "XEM": "http://bigalice3.nem.ninja:7890/account/get?address={identifier}",
                "XRP": "https://data.ripple.com/v2/accounts/{identifier}/balances"
                }
    return api_urls[currency]
