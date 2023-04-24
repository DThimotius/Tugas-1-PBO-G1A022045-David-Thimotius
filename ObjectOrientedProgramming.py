class Lingkaran:
    def __init__(self, diameter):
        self.diameter = diameter

    def hitung_keliling_lingkaran(self):
        return 3.14 * self.diameter

lingkaran = Lingkaran(28)
keliling = lingkaran.hitung_keliling_lingkaran()
print("Keliling lingkaran adalah", keliling)
