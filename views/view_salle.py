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