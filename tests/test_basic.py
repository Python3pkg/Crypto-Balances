# -*- coding: utf-8 -*-
import re
import unittest
from cryptobalances.checker import get_balance
from cryptobalances.config_parser import read_config
from cryptobalances.validator import autodetect_currency


reg_exp = '(^0{1}$)|(^0{1}\.0{1}$)|(^[1-9]{1}[0-9]{0,100}$)|(^[1-9]{1}[0-9]{0,100}\.[0-9]{1,100}$)|(^[0-9]{1}\.[0-9]{1,100}$)'


class TestGetBalance(unittest.TestCase):
    def test_btc(self):
        result = get_balance('BTC', '1KpyvRt5EYumsCTe9SGQ4FeyM4mWcagpnM')
        self.assertRegex(result, reg_exp, 'Function returns: {}'.format(result))

    def test_ltc(self):
        result = get_balance('LTC', 'LLiwS8XkQ7ra4XAg1TybTWrwnqFvMhiRfE')
        self.assertRegex(result, reg_exp, 'Function returns: {}'.format(result))

    def test_eth(self):
        result = get_balance('ETH', '0xfB6916095ca1df60bB79Ce92cE3Ea74c37c5d359')
        self.assertRegex(result, reg_exp, 'Function returns: {}'.format(result))

    def test_doge(self):
        result = get_balance('DOGE', 'DDogepartyxxxxxxxxxxxxxxxxxxw1dfzr')
        self.assertRegex(result, reg_exp, 'Function returns: {}'.format(result))

    def test_xcp(self):
        pass
        # result = get_balance('XCP', '16WhhnUUCZVvszFxsaCG3d6v77Qin1LErQ')
        # self.assertRegex(result, '', 'Function returns: {}'.format(result))


class TestConfigParser(unittest.TestCase):
    def test_read_config(self):
        self.assertIsNotNone(read_config(), 'Reading of config has been failed. The config has not been opened.')


class TestValidator(unittest.TestCase):
    def test_autodetect_eth(self):
        # 0xfB6916095ca1df60bB79Ce92cE3Ea74c37c5d359
        # 1ebacb7844fdc322f805904fbf1962802db1537c
        self.assertEqual(autodetect_currency('0xfB6916095ca1df60bB79Ce92cE3Ea74c37c5d359'),
                         'ETH',
                         'Provided identifier has not been match according regexp.')

    def test_autodetect_ltc(self):
        self.assertEqual(autodetect_currency('LLiwS8XkQ7ra4XAg1TybTWrwnqFvMhiRfE'),
                         'LTC',
                         'Provided identifier has not been match according regexp.')

    def test_autodetect_doge(self):
        self.assertEqual(autodetect_currency('DDogepartyxxxxxxxxxxxxxxxxxxw1dfzr'),
                         'DOGE',
                         'Provided identifier has not been match according regexp.')


if __name__ == '__main__':
    unittest.main()
