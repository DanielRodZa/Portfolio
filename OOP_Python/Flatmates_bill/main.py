class Bill:
    """
    Object that contains data about a bill, such as total amount and period of the bill
    """
    def __init__(self, amount, period):
        self.period = period
        self.amount = amount

class Flatmate:
    """

    """
    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill):
        pass

class PDFReport:
    """

    """
    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pass