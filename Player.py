
from doctest import testmod
class Player:

    def __init__(self, nb_bille):
        self.nb_bille = nb_bille
        self.nb_bille_parie = 0

    def get_nb_bille(self):
        return self.nb_bille
    
    def get_nb_bille_parie(self): return self.nb_bille_parie
    
    def parier(self, nb_bille: int):
        assert nb_bille <= self.nb_bille
        self.nb_bille_parie = nb_bille