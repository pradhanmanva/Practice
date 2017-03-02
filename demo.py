#Do this programs:
# 1) Pattern Print
# 2) Sum/Average on list
# 3) Class no priogram (like save student details)
# 4) Regular expression to avsej as u know.
# 5) Explain exceptional handling with example
# 6) function ma swap is most famous but recurision na example avi sake.
#these*

class Car:
    color = 5
    def description(self,str=8):
        self.color=str
        print(self.color)
        description_string = "This is a %d car." % self.color    # we'll explain self parameter later in task 4
        return description_string

car1 = Car()
car2 = Car()

Car.color=1
car1.color = 2
print("Car color : ")
print(Car.color)
print("Car1 color : ")
print(car1.color)
car2.color = 3
print("Car color : ")
print(Car.color)
print("Car2 color : ")
print(car2.color)

print(car1.description())
print(car2.description())
