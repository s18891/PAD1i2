# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import datetime


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# class definition
class animal():
    def __init__(self, gender="female", genus=""):
        self.gender = gender
        self.genus = genus

    def breed(self, partner):
        check = False
        if self.gender == "female" and partner.gender == "male" and self.genus == partner.genus:
            check = True
        try:
            if check:
                return self
            else:
                raise ValueError
        except ValueError:
            print("attribute not found")


class cat(animal):
    def __init__(self, gender):
        super().__init__(gender, "Felis")

    def purr(self):
        return "purr"


class dog(animal):
    def __init__(self, gender):
        super().__init__(gender, "Canis")

    def woof(self):
        return "woof woof"


###############################################################################################################

class worker():
    iloscm30 = 0
    iloscw30 = 0
    ilosc = 0
    sumaZarobkow = 0
    sumam30 = 0
    sumaw30 = 0

    def __init__(self, Number, Name, Age, Salary):
        self.Number = Number
        self.Name = Name
        self.Age = Age
        self.Salary = Salary
        worker.ilosc += 1
        worker.sumaZarobkow += Salary
        if datetime.date.today().year - self.Age < 30:
            worker.iloscm30+=1
            worker.sumam30+= self.Salary
            #print("IF")

        else:
            worker.iloscw30 += 1
            worker.sumaw30 += self.Salary
            #print("ELSE")

    def Salary(self):
        return self.Salary()

    @staticmethod
    def AvgSalary():
        return worker.sumaZarobkow/worker.ilosc
    @staticmethod
    def AvgSalarym30():
        if worker.iloscm30 == 0:
            return 0
        else:
            return worker.sumam30/worker.iloscm30
    @staticmethod
    def AvgSalaryw30():
        if worker.iloscw30 == 0:
            return 0
        else:
            return worker.sumaw30 / worker.iloscw30

    @staticmethod
    def CompareSalary30():
        if worker.AvgSalaryw30() > worker.AvgSalarym30():
            print("Więcej zarabiają osoby w wieku większym niż 30 lat")
        else:
            print("Więcej zarabiają osoby w wieku mniejszym niż 30 lat")


if __name__ == '__main__':
    print_hi('PyCharm')
    cat1 = cat("male")
    cat2 = cat("female")

    worker1 = worker(1, "Adam", 1983, 1500)
    worker2 = worker(2, "Anna", 1981, 1700)
    worker3 = worker(3, "Błażej", 1990, 1800)
    worker4 = worker(4, "Beata", 1992, 1600)
    worker5 = worker(5, "Czesław", 1980, 2000)
    worker6 = worker(6, "Cecylia", 1983, 2100)
    worker7 = worker(7, "Daniel", 1976, 1900)

    print(worker.AvgSalary())
    print(worker.AvgSalarym30())
    print(worker.AvgSalaryw30())
    worker.CompareSalary30()



    # cat2.breed(cat1)
    # cat1.breed(cat2)
