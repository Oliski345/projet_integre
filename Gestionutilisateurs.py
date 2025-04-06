class Utilisateur:
    def __init__(self, nom, prenom, email, identifiant):
        self.__nom = nom
        self.__prenom = prenom
        self.__email = email
        self.__identifiant = identifiant
        self.__historique_emprunt = []

    @property
    def nom(self):
        return self.__nom

    @property
    def prenom(self):
        return self.__prenom

    def email(self):
        return self.__email

    @property
    def identifiant(self):
        return self.__identifiant
    @property
    def historique_emprunt(self):
        return self.__historique_emprunt

    def ajouter_emprunt(self, media, date_emprunt, date_retour):
        emprunt = (media, date_emprunt, date_retour)
        self.__historique_emprunts.append(emprunt)

    if not self.__historique_emprunts:
        def afficher_historique(self):
            print(f"Aucun emprunt effectué par {self.__prenom} {self.__nom}.")
            return
        print(f"Historique des emprunts de {self.__prenom} {self.__nom}:")
        for media, date_emprunt, date_retour in self.__historique_emprunts:
            print(f"  Média: {media.titre}, Date d'emprunt: {date_emprunt}, Date de retour prévue: {date_retour}")

    def afficher_details(self):
        print(f"Utilisateur: {self.__prenom} {self.__nom}")
        print(f"Email: {self.__email}")
        print(f"ID Utilisateur: {self.__identifiant}")
        self.afficher_historique()

    @classmethod
    def creer(cls, nom, prenom, email, identifiant):
        """Création d'un utilisateur"""
        identifiant = len(utilisateurs) + 1
        utilisateur = cls(nom, prenom, email, identifiant)
        utilisateurs[identifiant] = utilisateur
        return utilisateur



