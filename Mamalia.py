from Animal import Animal
from Amphibi import Amphibi

class mamalia (Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak,bernafas,ukuran_tubuh,jenis_kulit):
        super().__init__(name, makanan, hidup, berkembang_biak,)
        self.bernafas = bernafas
        self.ukuran_tubuh = ukuran_tubuh
        self.jenis_kulit = jenis_kulit

    def info_mamalia(self):
        super().info_animal()
        print("ukuran_tubuh \t\t\t : ", self.ukuran_tubuh,
              "\njenis_kulit \t\t\t : ", self.jenis_kulit, "\nbernafas \t\t\t :", self.bernafas)
        
mamalia  = mamalia("sapi", "rumput", "darat", "melahirkan", "Paru-paru","Besar","Kelenjar susu")
mamalia.info_mamalia()

print ("===============================")