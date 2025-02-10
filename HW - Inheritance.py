class Shoe():
    def __init__(self,brand,size,color,style):
        self.brand = brand
        self.size = size
        self.color = color
        self.style = style

    def get_color(self):
        return self.color
    
    def set_color(self, new_color):
        self.color = new_color

    def show_shoe(self):
        print("Shoe - brand: {}, size: {}, color: {}, style: {}".format(self.brand, self.size, self.color, self.style))

class Sneaker(Shoe):
    def __init__(self, brand, size, color, style, laced,price):
        super().__init__(brand, size, color, style)
        self.laced = laced
        self.price = price
    
    def show_shoe(self):
        print("Shoe - brand: {}, size: {}, color: {}, style: {}, laced: {}, price: {}".format(self.brand, self.size, self.color, self.style, self.laced, self.price)
)
Airforce = Sneaker("Nike", 7, "black", "low", "yes", 100)
print(Airforce.get_color())
print(Airforce.set_color("white"))
print(Airforce.show_shoe())