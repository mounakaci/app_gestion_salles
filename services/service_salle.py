from data.dao_salle import DataSalle

class ServiceSalle:
    def __init__(self):
        self.dao_salle = DataSalle()

    def ajouter_salle(self, salle):
        if salle.code and salle.description and salle.categorie and salle.capacite:
            if salle.capacite >= 1:
                self.dao_salle.insert_salle(salle)
                return True
            else:
                return False
        else:
            return False

    def supprimer_salle(self, code):
            self.dao_salle.delete_salle(code)

    def rechercher_salle(self, code):
            return self.dao_salle.get_salle(code)

    def recuperer_salles(self):
            return self.dao_salle.get_salles()

    def modifier_salle(self, salle):
        if salle.code and salle.description and salle.categorie and salle.capacite:
            if salle.capacite >= 1:
                self.dao_salle.update_salle(salle)
                return True
            else:
                return False
        else:
            return False