from Animal import Animal
class carnivora (Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak,sistem_pencernaan,bentuk):
        super().__init__(name,makanan,hidup,berkembang_biak,)
        self.sistem_pencernaan = sistem_pencernaan
        self.bentuk = bentuk

    def info_carnivora(self):
        super().info_animal()
        print("sistem_pencernaan \t\t\t :", self.sistem_pencernaan,
              "\nBentuk \t\t\t\t :", self.bentuk)

carnivora = carnivora ("Harimau","Daging","Dua Alama","menelan mangsa nya", "panjang dan tida berkaki")
carnivora.info_carnivora()