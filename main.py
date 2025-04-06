from gestionmédia import Mediatheque, Livre, DVD, CD, Utilisateur  # Assurez-vous que les classes sont bien importées

# Dictionnaire pour stocker les utilisateurs
utilisateurs = {}

def ajouter_utilisateur(mediatheque):
    """Ajoute un utilisateur à la médiathèque"""
    nom = input("Entrez le nom de l'utilisateur : ")
    prenom = input("Entrez le prénom de l'utilisateur : ")
    email = input("Entrez l'email de l'utilisateur : ")
    utilisateur = Utilisateur.creer(nom, prenom, email, utilisateurs)  # Utilisation du dictionnaire utilisateurs
    print(f"Utilisateur {nom} {prenom} ajouté avec succès !")


def afficher_utilisateur_details():
    """Affiche les détails d'un utilisateur donné par son identifiant"""
    utilisateur_id = int(input("Entrez l'identifiant de l'utilisateur : "))
    utilisateur = utilisateurs.get(utilisateur_id)
    if utilisateur:
        utilisateur.afficher_details()
    else:
        print("Utilisateur non trouvé.")


def main():
    """Programme principal interactif"""
    print("Bienvenue dans le programme de gestion de médiathèque")

    # Création d'une instance de la médiathèque
    mediatheque = Mediatheque()

    while True:
        choix = afficher_menu()

        if choix == '0':
            print("Au revoir")
            break
        elif choix == '1':
            ajouter_media(mediatheque)
        elif choix == '2':
            rechercher_media(mediatheque)
        elif choix == '3':
            afficher_details_media(mediatheque)
        elif choix == '4':
            ajouter_utilisateur(mediatheque)
        elif choix == '5':
            emprunter_media(mediatheque)
        elif choix == '6':
            retourner_media(mediatheque)
        elif choix == '7':
            afficher_utilisateur_details()
        elif choix == '8':
            afficher_statistiques(mediatheque)
        else:
            print("Choix invalide. Essayez de nouveau.")


if __name__ == "__main__":
    main()
