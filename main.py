class Snowball:
    temperature = -7

    coordinates = [1, 2, 3, 4, 5]

    def __init__(self, a):
        if a == 5:
            self.temperature = 0

    def __str__(self):
        return str(self.temperature)

    def __del__(self):
        print("Delete object")

    def __bool__(self):
        return False

    def __len__(self):
        return len(self.coordinates)

    def print_temperature_type(self):
        print(type(self.temperature))

snowball = Snowball(3)

print(snowball)

snowball.print_temperature_type()

if snowball:
    print("True")

print("Hello")

print("I'm snowball")

print("asaafaf")
