# -*- coding: utf-8 -*-
import unittest
from cryptobalances.checker import get_balance
from cryptobalances.config import get_api_url
from cryptobalances.validator import autodetect_currency


reg_exp = '(^0{1}$)|(^0{1}\.0{1}$)|(^[1-9]{1}[0-9]{0,100}$)|(^[1-9]{1}[0-9]{0,100}\.[0-9]{1,100}$)|(^[0-9]{1}\.[0-9]{1,100}$)'


class TestGetBalance(unittest.TestCase):
    def test_btc(self):
        result = get_balance('BTC', '1KpyvRt5EYumsCTe9SGQ4FeyM4mWcagpnM')
        self.assertRegex(result, reg_exp, 'Function returns: {}'.format(result))
        print('Function get_balance for BTC returns: {}'.format(result))

    def test_ltc(self):
        result = get_balance('LTC', 'LLiwS8XkQ7ra4XAg1TybTWrwnqFvMhiRfE')
        self.assertRegex(result, reg_exp, 'Function returns: {}'.format(result))
        print('Function get_balance for LTC returns: {}'.format(result))

    def test_eth(self):
        result = get_balance('ETH', '0xfB6916095ca1df60bB79Ce92cE3Ea74c37c5d359')
        self.assertRegex(result, reg_exp, 'Function returns: {}'.format(result))
        print('Function get_balance for ETH returns: {}'.format(result))

    def test_doge(self):
        result = get_balance('DOGE', 'DDogepartyxxxxxxxxxxxxxxxxxxw1dfzr')
        self.assertRegex(result, reg_exp, 'Function returns: {}'.format(result))
        print('Function get_balance for DOGE returns: {}'.format(result))

    def test_xcp(self):
        result = get_balance('XCP', '16WhhnUUCZVvszFxsaCG3d6v77Qin1LErQ')
        self.assertRegex(result['XCP'], reg_exp, 'Function returns: {}'.format(result))
        print('Function get_balance for XCP returns: {}'.format(result['XCP']))

    def test_dash(self):
        result = get_balance('DASH', 'XfgNCeTJxBVHb9CCpn52QyfjfpBmPQUYdA')
        self.assertRegex(result, reg_exp, 'Function returns: {}'.format(result))
        print('Function get_balance for DASH returns: {}'.format(result))

    def test_ppc(self):
        result = get_balance('PPC', 'PGVtF7DJ4KtndgdYZ472skrZQx3MDHNymt')
        self.assertRegex(result, reg_exp, 'Function returns: {}'.format(result))
        print('Function get_balance for PPC returns: {}'.format(result))

    def test_blk(self):
        result = get_balance('BLK', 'B95qcCHpma5XZu4n6hP9pP5APiasCR16Ts')
        self.assertRegex(result, reg_exp, 'Function returns: {}'.format(result))
        print('Function get_balance for BLK returns: {}'.format(result))

    def test_xem(self):
        result = get_balance('XEM', 'NCXIP5-JNP4GC-3JXXBB-U2UHF4-F4JYJ4-4DWFMN-EIMQ')
        self.assertRegex(result, reg_exp, 'Function returns: {}'.format(result))
        print('Function get_balance for XEM returns: {}'.format(result))

    def test_xrp(self):
        result = get_balance('XRP', 'rHb9CJAWyB4rj91VRWn96DkukG4bwdtyTh')
        self.assertRegex(result, reg_exp, 'Function returns: {}'.format(result))
        print('Function get_balance for XRP returns: {}'.format(result))

    def test_oa(self):
        result = get_balance('OA', 'akNgsNMWbjM4svehXchCPkPsLRVAMJU7nrj')
        self.assertRegex(result, reg_exp, 'Function returns: {}'.format(result))
        print('Function get_balance for OA returns: {}'.format(result))

    def test_omni(self):
        result = get_balance('OMNI', '1CRne14GDzTQvKYv1uNuitocTNptF3qKCX')
        self.assertRegex(result, reg_exp, 'Function returns: {}'.format(result))
        print('Function get_balance for OMNI returns: {}'.format(result))

    def test_zcash(self):
        result = get_balance('ZEC', 't1KHa9CJeCy3b9rUX2BhqkFJXSxSSrhM7LJ')
        self.assertRegex(result, reg_exp, 'Function returns: {}'.format(result))
        print('Function get_balance for ZEC returns: {}'.format(result))

    def test_nxt(self):
        result = get_balance('NXT', 'NXT-7LB8-8ZPX-3YR9-3L85B')
        self.assertRegex(result, reg_exp, 'Function returns: {}'.format(result))
        print('Function get_balance for NXT returns: {}'.format(result))

    def test_steem(self):
        result = get_balance('STEEM', 'cryptofunk')
        self.assertRegex(result, reg_exp, 'Function returns: {}'.format(result))
        print('Function get_balance for STEEM returns: {}'.format(result))

    def test_golos(self):
        result = get_balance('GOLOS', 'alex78')
        self.assertRegex(result, reg_exp, 'Function returns: {}'.format(result))
        print('Function get_balance for GOLOS returns: {}'.format(result))


class TestConfig(unittest.TestCase):
    def test_get_api_url(self):
        currencies = ['BTC', 'LTC', 'ETH', 'DOGE', 'XCP',
                      'DASH', 'PPC', 'CPC', 'GRT', 'BLK',
                      'XEM', 'XRP', 'OA', 'OMNI', 'ZEC',
                      'NXT']

        for i in range(0, len(currencies)):
            with self.subTest(i=i):
                api_url = get_api_url(currencies[i])
                self.assertRegex(api_url,
                                 '(^http[:]{1}[/]{2}(?!/).+$)|(^https[:]{1}[/]{2}(?!/).+$)',
                                 'Function returns: {}'.format(api_url))
                print('Function get_api_url for {} returns: {}'.format(currencies[i], api_url))

    def test_get_websocket(self):
        currencies = ['STEEM', 'GOLOS']

        for i in range(0, len(currencies)):
            with self.subTest(i=i):
                api_url = get_api_url(currencies[i])
                self.assertRegex(api_url, '^wss[:]{1}[/]{2}(?!/).+$', 'Function returns: {}'.format(api_url))
                print('Function get_api_url for {} returns: {}'.format(currencies[i], api_url))


class TestValidator(unittest.TestCase):
    def test_autodetect_eth(self):
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

    def test_autodetect_dash(self):
        self.assertEqual(autodetect_currency('XfgNCeTJxBVHb9CCpn52QyfjfpBmPQUYdA'),
                         'DASH',
                         'Provided identifier has not been match according regexp.')

    def test_autodetect_ppc(self):
        self.assertEqual(autodetect_currency('PGVtF7DJ4KtndgdYZ472skrZQx3MDHNymt'),
                         'PPC',
                         'Provided identifier has not been match according regexp.')

    def test_autodetect_blk(self):
        self.assertEqual(autodetect_currency('B95qcCHpma5XZu4n6hP9pP5APiasCR16Ts'),
                         'BLK',
                         'Provided identifier has not been match according regexp.')

    def test_autodetect_xem(self):
        self.assertEqual(autodetect_currency('NCXIP5-JNP4GC-3JXXBB-U2UHF4-F4JYJ4-4DWFMN-EIMQ'),
                         'XEM',
                         'Provided identifier has not been match according regexp.')

    def test_autodetect_xrp(self):
        self.assertEqual(autodetect_currency('rHb9CJAWyB4rj91VRWn96DkukG4bwdtyTh'),
                         'XRP',
                         'Provided identifier has not been match according regexp.')

    def test_autodetect_oa(self):
        self.assertEqual(autodetect_currency('akNgsNMWbjM4svehXchCPkPsLRVAMJU7nrj'),
                         'OA',
                         'Provided identifier has not been match according regexp.')

    def test_autodetect_zec(self):
        self.assertEqual(autodetect_currency('t1KHa9CJeCy3b9rUX2BhqkFJXSxSSrhM7LJ'),
                         'ZEC',
                         'Provided identifier has not been match according regexp.')

    def test_autodetect_nxt(self):
        self.assertEqual(autodetect_currency('NXT-7LB8-8ZPX-3YR9-3L85B'),
                         'NXT',
                         'Provided identifier has not been match according regexp.')

    # def test_autodetect_steem_golos(self):
    #     users = ['cryptofunk', 'alex78', 'catto000']
    #     for i in range(0, len(users)):
    #         with self.subTest(i=i):
    #             self.assertIsInstance(autodetect_currency(i), list,
    #                                   'Provided identifier has not been match according regexp.')

    def test_autodetect_omni(self):
        result = autodetect_currency('1CRne14GDzTQvKYv1uNuitocTNptF3qKCX')
        self.assertIsInstance(result, list)
        self.assertIn('OMNI', result)


if __name__ == '__main__':
    unittest.main()
