from amazonstoreprice import AmazonStorePrice

url = "http://www.amazon.it/Inside-Out-Ronnie-Del-Carmen/dp/B016LMC90O/" \
      "ref=sr_1_1?ie=UTF8&qid=1455389197&sr=8-1&keywords=inside+out"
pricelib = AmazonStorePrice()
print(pricelib.getprice(url, retry_ontemp=True))
