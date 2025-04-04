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
        while True:
            self.__identifiant = input("Identifiant: ")

