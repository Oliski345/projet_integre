from gestionmédia import Mediatheque, Livre, DVD, CD, Utilisateur
# Olivier Pinard et Juliette Danis
utilisateurs = {}
def ajouter_utilisateur(mediatheque):
    """Ajoute un utilisateur à la médiathèque"""
    nom = input("Entrez le nom de l'utilisateur : ")
    prenom = input("Entrez le prénom de l'utilisateur : ")
    email = input("Entrez l'email de l'utilisateur : ")
    utilisateur = Utilisateur.creer(nom, prenom, email, utilisateurs)  # Utilisation du dictionnaire utilisateurs
    print(f"Utilisateur {nom} {prenom} ajouté avec succès !")


def afficher_utilisateur_details():
    """Affiche les détails d'un utilisateur grâce à son identifiant"""
    utilisateur_id = int(input("Entrez l'identifiant de l'utilisateur : "))
    utilisateur = utilisateurs.get(utilisateur_id)
    if utilisateur:
        utilisateur.afficher_details()
    else:
        print("Utilisateur non trouvé.")




def main():
    """Programme principal interactif"""
    print("Bienvenue dans le programme de gestion de médiathèque")
    print("\n==== MENU PRINCIPAL ====")
    print("1. Ajouter un média")
    print("2. Rechercher des médias")
    print("3. Afficher les détails d'un média")
    print("4. Ajouter un utilisateur")
    print("5. Emprunter un média")
    print("6. Retourner un média")
    print("7. Afficher l'historique d'un utilisateur")
    print("8. Consulter les statistiques de la médiathèque")
    print("0. Quitter")

    # Demande à l'utilisateur de choisir une option
    choix = input("Choisissez une option (0-8): ")

    # Création d'une instance de la médiathèque
    mediatheque = Mediatheque()

    while True:

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
