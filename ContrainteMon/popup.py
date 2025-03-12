import module1
from tkinter import *

def update_text(texte_var):
    texte_var.set(module1.get_event())

def main():
    fenetre = Tk()
    fenetre.title("ContrainteMon - EventManager")
    fenetre.geometry("500x130")  # Définition de la taille de la fenêtre
    
     # Création du cadre principal
    cadre = Frame(fenetre)
    cadre.pack(expand=True, fill=BOTH)

    # Création de la zone de texte
    texte_var = StringVar()
    texte_var.set("Click on the 'Get event' button to start" + "\n" + "Click on the 'Close' button to close ContrainteMon")  # Remplissage avec le texte de module1.get_event()
    zone_texte = Label(cadre, textvariable=texte_var, wraplength=300, padx=10, pady=10)
    zone_texte.pack(expand=True)
    
    # Cadre pour les boutons en bas
    cadre_boutons = Frame(fenetre)
    cadre_boutons.pack(side=BOTTOM, fill=X)

    # Bouton pour mettre à jour le texte
    bouton_update = Button(cadre_boutons, text="Get event", command=lambda: update_text(texte_var))
    bouton_update.pack(fill=X)
    
    # Bouton OK prenant toute la largeur
    bouton_ok = Button(cadre_boutons, text="Close", command=fenetre.quit)
    bouton_ok.pack(fill=X)
    
    fenetre.mainloop()

if __name__ == "__main__":
    main()