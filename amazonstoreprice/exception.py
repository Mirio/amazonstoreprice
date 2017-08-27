class UrlNotAmazon(Exception):
    pass


class PageNotFound(Exception):
    pass


class StoreTemporaryUnavailable(Exception):
    pass


class RequestGenericError(Exception):
    pass

class PriceNotFound(Exception):
    pass
