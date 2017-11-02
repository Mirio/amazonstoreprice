## AmazonStorePrice
This module find the price from url given

Compatible with all amazon store

[![Build Status](https://travis-ci.org/Mirio/amazonstoreprice.svg?branch=0.1)](https://travis-ci.org/Mirio/amazonstoreprice)  [![Github All Releases](https://img.shields.io/github/downloads/mirio/amazonstoreprice/total.svg)]() [![Documentation Status](https://readthedocs.org/projects/amazonstoreprice/badge/?version=0.1)](http://amazonstoreprice.readthedocs.org/en/latest/?badge=0.1)
[![Coverage Status](https://coveralls.io/repos/github/Mirio/amazonstoreprice/badge.svg?branch=0.1)](https://coveralls.io/github/Mirio/amazonstoreprice?branch=0.1)


## Link
Documentation: http://amazonstoreprice.readthedocs.org/

Bug Tracker: https://github.com/Mirio/amazonstoreprice/issues

GitHub: https://github.com/Mirio/amazonstoreprice


## Requirement
Python 3.x

Python Library = [ 'requests', 'beautifulsoup4' ]

## How to install
```
pip install amazonstoreprice
```

## Install from source
```
git clone https://github.com/Mirio/amazonstoreprice.git
cd amazonstoreprice
python setup.py install
```

## Getting Started

Example:
```
from amazonstoreprice import AmazonStorePrice

url = "http://www.amazon.it/Inside-Out-Ronnie-Del-Carmen/dp/B016LMC90O/" \
      "ref=sr_1_1?ie=UTF8&qid=1455389197&sr=8-1&keywords=inside+out"
pricelib = AmazonStorePrice()
print(pricelib.getprice(url, retry_ontemp=True))
```

Output:
```
$ python example_getprice.py
15.99
```
