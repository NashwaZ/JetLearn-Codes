
class Fruit():
    def __init__(self, color, taste, shape, preference):
        self.color = color
        self.taste = taste
        self.shape = shape
        self.preference = preference

    def get_shape(self):
        return self.shape
    def set_shape(self, new_shape):
        self.shape = new_shape
    def increase_preference(self):
        self.preference = self.preference +1
    def show_fruit(self):
        print("Hello! I'm a Fruit! with {} {} {} {}".format(self.color, self.shape, self.taste, self.preference))
    
apple = Fruit("red","sour","round",1)
apple.show_fruit()
apple.increase_preference()
print(apple.get_shape())
apple.set_shape("sphere")
apple.show_fruit()

banana = Fruit("yellow","sweet","round",2)
banana.show_fruit()
banana.increase_preference()
print(banana.get_shape())
banana.set_shape("cylindrical")
banana.show_fruit()





