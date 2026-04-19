import json
import mysql.connector
from models.salle import Salle


class DataSalle:
    def get_connection(self):
        with open("./data/config.json", "r", encoding="utf-8") as f:
            config = json.load(f)

        con = mysql.connector.connect(
            host=config["host"],
            user=config["user"],
            password=config["password"],
            database=config["database"]
        )
        return con

    def insert_salle(self, salle):
        con = self.get_connection()
        crs = con.cursor()
        crs.execute(
            "INSERT INTO salle VALUES (%s,%s,%s,%s)",
            (salle.code, salle.description, salle.categorie, salle.capacite)
        )
        con.commit()
        crs.close()
        con.close()

   