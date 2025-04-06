from gestionmédia import Médiateque
from gestionmédia import CD



def afficher_menu():
    """Fonction pour afficher le menu"""
    print("\n====MENU PRINCIPAL====")
    print("1. Ajouter un média")
    print("2. Rechercher des médias")
    print("3. Afficher les détails d'un média")
    print("4. Ajouter un utilisateur")
    print("5. Emprunter un média")
    print("6. Retourner un média")
    print("7. Afficher l'historique d'un utilisateur")
    print("8. Consulter les statistiques de la médiatèque")
    print("0. Quitter")
    return input("Choississez une option")


def main():
    """Programme principale interactif"""
    print("Bienvenue dans le programme de système de gestion médiatèque")

    while True:
        choix = afficher_menu()
        if choix == '0':
            print("Au revoir")
            break
        elif choix == '1':
            while True:
                media = input("Rentrez un livre l'identifiant, titre, annee, genre, auteur et nb_pages ou"
                              "un DVD l'identifiant, titre, annee, genre, réalisateur et durée ou"
                              "un CD l'identifiant, titre, annee, genre, artiste et nombre de piste :")
                mediatheque.ajouter_media(media)


if __name__ == "__main__":
    main()
