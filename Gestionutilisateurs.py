class Utilisateur:
    def __init__(self, nom, prenom, email, identifiant):
        self.__nom = nom
        self.__prenom = prenom
        self.__email = email
        self.__identifiant = identifiant

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

    def creer(self):
        nb_utilisateur = 0
        while True:
            while True:
                identifiant = input("Identifiant: ")
                if identifiant in self.__identifiant:
                    print("Identifiant déjà utiliser")
                    continue
                else:
                    identifiant = self.__identifiant
                    break
            self.__nom = nom = input("Votre Nom: ")
            self.__prenom = prenom = input("Votre Prenom: ")
            self.__email = email = input("Votre Email: ")
            nb_utilisateur += 1
            break
        return Utilisateur(nom, prenom, email, identifiant), nb_utilisateur




