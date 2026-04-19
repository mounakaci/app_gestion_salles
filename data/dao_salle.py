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

    def update_salle(self, salle):
        con = self.get_connection()
        crs = con.cursor()
        crs.execute(
            "UPDATE salle SET description=%s, categorie=%s, capacite=%s WHERE code=%s",
            (salle.description, salle.categorie, salle.capacite, salle.code)
        )
        con.commit()
        crs.close()
        con.close()

    def delete_salle(self, code):
        con = self.get_connection()
        crs = con.cursor()
        crs.execute(
            "DELETE FROM salle WHERE code=%s",
            (code,)
        )
        con.commit()
        crs.close()
        con.close()

    def get_salle(self, code):
        con = self.get_connection()
        crs = con.cursor()
        crs.execute(
            "SELECT * FROM salle WHERE code=%s",
            (code,)
        )
        row = crs.fetchone()
        crs.close()
        con.close()

        return Salle(row[0], row[1], row[2], row[3])

    def get_salles(self):
        con = self.get_connection()
        crs = con.cursor()
        crs.execute("SELECT * FROM salle")
        rows = crs.fetchall()
        crs.close()
        con.close()

        salles = []
        for row in rows:
            salles.append(Salle(row[0], row[1], row[2], row[3]))

        return salles