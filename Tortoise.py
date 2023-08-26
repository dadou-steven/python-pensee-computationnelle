class Tortoise:
    def __init__(self):
        self.position = 0

    def forward(self):
        self.position += 1


pokey = Tortoise()
pokey.forward()
print(pokey.position)
