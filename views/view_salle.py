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
        ctk.CTkLabel(self.frame_infos, text="Code").pack()
        self.code = ctk.CTkEntry(self.frame_infos)
        self.code.pack()
        ctk.CTkLabel(self.frame_infos, text="Description").pack()
        self.description = ctk.CTkEntry(self.frame_infos)
        self.description.pack()
        ctk.CTkLabel(self.frame_infos, text="Catégorie").pack()
        self.categorie = ctk.CTkEntry(self.frame_infos)
        self.categorie.pack()
        ctk.CTkLabel(self.frame_infos, text="Capacité").pack()
        self.capacite = ctk.CTkEntry(self.frame_infos)
        self.capacite.pack()
        self.frame_actions = ctk.CTkFrame(self)
        self.frame_actions.pack()
        ctk.CTkButton(self.frame_actions, text="Ajouter", command=self.ajouter_salle).pack()
        ctk.CTkButton(self.frame_actions, text="Modifier", command=self.modifier_salle).pack()
        ctk.CTkButton(self.frame_actions, text="Supprimer", command=self.supprimer_salle).pack()
        ctk.CTkButton(self.frame_actions, text="Rechercher", command=self.rechercher_salle).pack()
        self.cadreList = ctk.CTkFrame(self, corner_radius=10, width=400)
        self.cadreList.pack(pady=10, padx=10)
        self.treeList = ttk.Treeview(
            self.cadreList,
            columns=("code", "description", "categorie", "capacite"),
            show="headings"
        )
        self.treeList.heading("code", text="CODE")
        self.treeList.heading("description", text="Description")
        self.treeList.heading("categorie", text="Catégorie")
        self.treeList.heading("capacite", text="Capacité")
        self.treeList.column("code", width=50)
        self.treeList.column("description", width=150)
        self.treeList.column("categorie", width=100)
        self.treeList.column("capacite", width=100)
        self.treeList.pack(expand=True, fill="both", padx=10, pady=10)
        self.lister_salles()

    def ajouter_salle(self):
            salle = Salle(
                self.code.get(),
                self.description.get(),
                self.categorie.get(),
                int(self.capacite.get())
            )
            self.service_salle.ajouter_salle(salle)
            self.lister_salles()

    def supprimer_salle(self):
            self.service_salle.supprimer_salle(self.code.get())
            self.lister_salles()

    def rechercher_salle(self):
            salle = self.service_salle.rechercher_salle(self.code.get())
            self.description.delete(0, "end")
            self.categorie.delete(0, "end")
            self.capacite.delete(0, "end")
            self.description.insert(0, salle.description)
            self.categorie.insert(0, salle.categorie)
            self.capacite.insert(0, salle.capacite)
            
    def modifier_salle(self):
            salle = Salle(
                self.code.get(),
                self.description.get(),
                self.categorie.get(),
                int(self.capacite.get())
            )
            self.service_salle.modifier_salle(salle)
            self.lister_salles()

    def lister_salles(self):
        self.treeList.delete(*self.treeList.get_children())
        liste = self.service_salle.recuperer_salles()
        for s in liste:
            self.treeList.insert("", "end", values=(s.code, s.description, s.categorie, s.capacite))

