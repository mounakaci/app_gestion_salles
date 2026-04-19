import customtkinter as ctk
from tkinter import ttk
from models.salle import Salle
from services.service_salle import ServiceSalle


class ViewSalle(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.service_salle = ServiceSalle()
        self.title("Gestion Salles")
        self.geometry("800x500")
        self.frame_infos = ctk.CTkFrame(self)
        self.frame_infos.pack()
        self.code = ctk.CTkEntry(self.frame_infos)
        self.code.pack()
        self.description = ctk.CTkEntry(self.frame_infos)
        self.description.pack()
        self.categorie = ctk.CTkEntry(self.frame_infos)
        self.categorie.pack()
        self.capacite = ctk.CTkEntry(self.frame_infos)
        self.capacite.pack()