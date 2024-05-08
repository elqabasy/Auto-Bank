import num2words

class NumberScrapping:
    def numberToEgyptionCurrency(number):
        return str(num2words.num2words(number, False, lang='ar', to="currency", currency="EGP"))