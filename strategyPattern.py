TAX_PERCENT = .12

class TaxIN(object):
    def __init__(self,):
        self.country_code = "IN"

    def __call__(self, billamount):
        return billamount * TAX_PERCENT

class TaxUS(object):
    def __init__(self,):
        self.country_code = "US"

    def __call__(self,billamount):
        if billamount < 500:
            return billamount * (TAX_PERCENT//2)
        else:
            return billamount * TAX_PERCENT

class TaxCalculator(object):

    def __init__(self):
        self._impls = [TaxIN(),TaxUS()]

    def __call__(self, country, billamount):
    """select the strategy based on country parameter
    """
        for impl in self._impls:
            if impl.country_code == country:
                return impl(billamount)
        else:
            return None

#tax_cal = TaxCalculator()
#print(tax_cal("IN", 400), tax_cal("IN", 700))
#print(tax_cal("US", 400), tax_cal("US", 700))
