#1-misol
class Odam:
    def __init__(self, ism, yosh):
        self.ism = ism
        self.yosh = yosh

    def salomlashish(self):
        print("Salom", end="")


class Talaba(Odam):
    def salomlashish(self):
        super().salomlashish()
        print(", Men Talaba")


o1 = Odam("Sevinch", 15)
o1.salomlashish()

print()

t1 = Talaba("Dilnura", 15)
t1.salomlashish()
