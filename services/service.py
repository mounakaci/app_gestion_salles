from data.dao_salle import DataSalle

class ServiceSalle:
    def __init__(self):
        self.dao_salle = DataSalle()

    def ajouter_salle(self, salle):
        if salle.code and salle.description and salle.categorie and salle.capacite:
            if salle.capacite >= 1:
                self.dao_salle.insert_salle(salle)
                return True, "salle ajoutée avec succès"
            else:
                return False, "capacité invalide"
        else:
            return False, "données invalides"