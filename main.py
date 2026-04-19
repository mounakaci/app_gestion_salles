from data.dao_salle import DataSalle
from models.salle import Salle

data = DataSalle()

con = data.get_connection()
print("connexion réussie")
con.close()

s1 = Salle("s1", "bibliothique", "ecole", 64)
data.insert_salle(s1)

s1.capacite = 40
data.update_salle(s1)

salle = data.get_salle("S1")
salle.afficher_infos()

salles = data.get_salles()
for s in salles:
    s.afficher_infos()

data.delete_salle("S1")