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


if __name__ == "__main__":
    main()

