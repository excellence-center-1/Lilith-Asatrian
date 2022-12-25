class Date:
    def __init__(self, year, month, date ):
        self.year = year
        self.month = month
        self.date = date

    def set_year(self, new_year):
        self.year=newyear
    def set_month(self, new_month):
        self.month=new_month
    def set_day(self, new_day):
        self.date=new_day
    def get_year(self):
        return self.year
    def get_month(self):
        return self.month
    def get_day(self):
        return self.date

class AmericanDate(Date):
    def format(self):
        p="{month}.{date}.{year}".format(date=self.date, month=self.month, year=self.year)
        return p
class EuropeanDate(Date):
    def format(self):
        p="{date}.{month}.{year}".format(date=self.date, month=self.month, year=self.year)
        return p

american=AmericanDate(2003, 12, 7)
european=EuropeanDate(2003, 12, 7)

print(american.format())
print(european.format())

