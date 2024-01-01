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

    def pays(self, bill, flatmate2):
        strength = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        total = strength * bill.amount
        return total
