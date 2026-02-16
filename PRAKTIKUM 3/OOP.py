class Device:
    def __init__(self, name, seri, warna ):
        self.name = name
        self.seri = seri
        self.warna = warna

    def greet(self):
     print("Device ku adalah" + self.name)

    def serial(self):
     print("serinya adalah" + self.seri)

p1 = Device("vivo", "y20", "biru" )
p2 = Device("lenovo", "v14", "hitam")
p3 = Device("samsung", "j2", "putih")



p1.greet()
p2.serial()

print(p1.name)
