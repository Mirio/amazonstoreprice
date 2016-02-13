from amazonstoreprice import AmazonStorePrice

url = "http://www.amazon.it/gp/product/0000000"
pricelib = AmazonStorePrice()
pricelib.getpage(pricelib.normalizeurl(url))
