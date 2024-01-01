from OOP_Python.Flatmates_bill.PDFGenerator import PDFReport
from OOP_Python.Flatmates_bill.flat import Bill, Flatmate


def main():
    a = float(input("Hey User, enter the bill amount: "))
    period = input("What is the bill period? E.g. December 2023: ")
    name = input("What is your name? ")
    days_in_house_1 = int(input(f"How many days did {name} stays in the house during the bill period? "))
    flatmate_name = input("What is your flatmate name? ")
    days_in_house_2 = int(input(f"How many days did {flatmate_name} stays in the house during the bill period? "))

    the_bill = Bill(amount=a, period=period)
    flatmate_1 = Flatmate(name=name, days_in_house=days_in_house_1)
    flatmate_2 = Flatmate(name=flatmate_name, days_in_house=days_in_house_2)

    print(f"{flatmate_1.name} pays: {flatmate_1.pays(bill=the_bill, flatmate2=flatmate_2)}")
    print(f"{flatmate_2.name} pays: {flatmate_2.pays(bill=the_bill, flatmate2=flatmate_1)}")

    pdf_report = PDFReport(filename='Report1.pdf')
    pdf_report.generate(flatmate1=flatmate_1, flatmate2=flatmate_2, bill=the_bill)



if __name__ == '__main__':
    main()