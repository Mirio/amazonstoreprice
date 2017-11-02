# -*- coding: utf-8 -*-
from unittest import TestCase, main
from amazonstoreprice import AmazonStorePrice


class TestAmazonStorePrice(TestCase):
    def setUp(self):
        self.amazonstoreprice = AmazonStorePrice()
        self.urltest = "https://www.amazon.it/gp/product/B01LPSG05O/ref=s9_simh_gw_p74_d0_i6" \
                       "?pf_rd_m=A11IL2PNWYJU7H&pf_rd_s=desktop-1"

    def test_normalizeurl(self):
        self.assertEqual(self.amazonstoreprice.normalizeurl(self.urltest),
                         "https://www.amazon.it/gp/product/B01LPSG05O/")

    def test_normalizeprice(self):
        self.assertEqual(self.amazonstoreprice.normalizeprice("EUR 1,00"), 1.00)
        self.assertEqual(self.amazonstoreprice.normalizeprice("$14.08"), 14.08)
        self.assertEqual(self.amazonstoreprice.normalizeprice("£11.00"), 11.00)

    def test_geturl(self):
        self.assertEqual(self.amazonstoreprice.getpage(self.amazonstoreprice.normalizeurl(self.urltest)).find(
            id="productTitle").contents[0], "Alla ricerca di Dorys")

    def test_getprice(self):
        self.assertIsInstance(self.amazonstoreprice.getprice(self.urltest, retry_ontemp=True), float)

if __name__ == '__main__':
    main(verbosity=3)
