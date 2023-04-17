class client():

    def __init__(self, name, number, qr):
        self.name = name
        self.number = number
        self.qr = qr
        self.coffeCup = 0
        self.freeCoffe = 0

    def coffe_plus(self, quantityCoffe):
        self.coffeCup += quantityCoffe

        while self.coffeCup > 5:
            self.coffeCup -= 5
            self.freeCoffe += 1

    def give_freeCoffe(self):
        self.freeCoffe -= 1
        print("Выдан новый QR-КОД")





if __name__ == "__main__":
    pass
