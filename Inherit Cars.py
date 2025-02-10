class User():
    __password = "abc123"
    def __init__(self,name,email,username):
        self.name = name
        self.email = email
        self.username = username

    def getpassword(self):
        return self.__password
    def setpassword(self):
        old_password = input("Enter your old passowrd: ")
        if old_password == self.__password:
            new_password = input("Enter a new password: ")
            self.__password = new_password
        else:
            input("Please enter the correct password: ")

class Car():
    def __init__(self, brand, model, color, fuel):
        self.brand = brand
        self.model = model
        self.color = color
        self.fuel = fuel

    def get_color(self):
        return self.color
    def set_color(self, new_color):
        self.color = new_color
    def show_car(self):
        print("Car-{}-{}, fuel type: {}, color: {}".format(self.brand,self.model,self.fuel,self.color))

class SUV(Car):
    def __init__(self, brand, model, color, fuel, transmission, turbo):
        super().__init__(brand, model, color, fuel)
        self.transmission = transmission
        self.turbo = turbo

    def show_car(self):
        print("Car-{}-{}, fuel type: {}, color: {}, transmission: {}, turbo: {}".format(self.brand, self.model, self.fuel, self.color, self.transmission, self.turbo))

nashwa = User("nashwa","nashwa.zshan@gmail.com","NZ")
print(nashwa.name)
#print(nashwa.__password)
print(nashwa.getpassword())
nashwa.setpassword()

audi = SUV("audi","Q3","white","diesel","automatic","True")
print(audi.get_color())
print(audi.set_color("blue"))
print(audi.show_car())

