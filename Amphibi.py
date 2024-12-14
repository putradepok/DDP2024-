from Animal import Animal

class Amphibi (Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak,habitat,bernafas):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.habitat = habitat
        self.bernafas = bernafas

    def info_amphibi(self):
        super().info_animal(),
        print("Habitat \t\t\t :", self.habitat,
        "\nbernafas \t\t\t :", self.bernafas)

Amphibi = Amphibi("Buaya", "Daging", "di air", "Mengeluarkan telur","Dua Alam","Paru-paru")
Amphibi.info_amphibi()

print("======================================")