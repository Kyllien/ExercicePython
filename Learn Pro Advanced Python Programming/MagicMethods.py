class TShirt:
    def __init__(self, color, inventory_count):
        self.color = color
        self.inventory_count = inventory_count

    def __str__(self):
        return "tShirt de couleur {0} avec un count de {1}".format(self.color, self.inventory_count)

    def __add__(self, other):
        return self.inventory_count + other.inventory_count


black = TShirt("black", 14)
blue = TShirt("blue", 10)

print(blue)
print(black)
