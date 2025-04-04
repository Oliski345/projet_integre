from abc import ABC, abstractmethod


class Empruntable(ABC):
    """ classe empruntable pour implémenter"""
    @abstractmethod
    def emprunter(self):
        pass

    @abstractmethod
    def rendre(self):
        pass


class Media(ABC):
    """ gestion des médias"""
    def __init__(self, identifiants, titre, annee, genre):
        self.__identifiants = identifiants
        self.__titre = titre
        self.__annee = annee
        self.__genre = genre

    @property
    def identifiants(self):
        return self.__identifiants

    @property
    def titre(self):
        return self.__titre

    @prperty
    def annee(self):
        return self.__annee

    @property
    def genre(self):
        return self.__genre

    @abstractmethod
    def afficher_detail(self):
        pass


class Livre(Media, Empruntable):
    """ gestion des livres"""
    def __init__(self, identifiants, titre, annee, genre, auteur, nb_pages):
        super().__init__(identifiants, titre, annee, genre)
        self.__nb_pages = nb_pages
        self.__auteur = auteur
        self.__emprunte = False

    @property
    def auteur(self):
        return self.__auteur

    @property
    def nb_pages(self):
        return self.__nb_pages

    def emprunter(self):
        if not self.__emprunte:
            self.__emprunte = True
            print(f"Le livre {self.__titre} a été emprunté.")
        else:
            print(f"Le livre {self.__titre} est déjà emprunté.")

    def rendre(self):
        if self.__emprunte:
            self.__emprunte = False
            print(f"Le livre {self.__titre} a été rendu.")
        else:
            print(f"Le livre {self.__titre} n'était pas emprunté.")

    def afficher_detail(self):
        return f"{super().afficher_detail()}, Auteur: {self.__auteur}, nb_pages: {self.__nb_pages}"


class DVD(Media, Empruntable):
    """ gestion des DVD"""
    def __init__(self, identifiants, titre, annee, genre, realisateur, duree):
        super().__init__(identifiants, titre, annee, genre)
        self.__realisateur = realisateur
        self.__duree = duree
        self.__emprunte = False

    @property
    def duree(self):
        return self.__duree

    @property
    def realisateur(self):
        return self.__realisateur

    def emprunter(self):
        if not self.__emprunte:
            self.__emprunte = True
            print(f"Le livre {self.__titre} a été emprunté.")
        else:
            print(f"Le livre {self.__titre} est déjà emprunté.")

    def rendre(self):
        if self.__emprunte:
            self.__emprunte = False
            print(f"Le livre {self.__titre} a été rendu.")
        else:
            print(f"Le livre {self.__titre} n'était pas emprunté.")

    def afficher_detail(self):
        return f"{super().afficher_detail()}, Auteur: {self.__auteur}, nb_pages: {self.__nb_pages}"


class CD(Media, Empruntable):
    """ gestion des CD"""
    def __init__(self, identifiants, titre, annee, genre, ariste, nb_piste):
        super().__init__(identifiants, titre, annee, genre)
        self.__nb_piste = nb_piste
        self.__artiste = artiste
        self.__emprunte = False

    @property
    def artiste(self):
        return self.__artiste

    @property
    def nb_piste(self):
        return self.__nb_piste

    def emprunter(self):
        if not self.__emprunte:
            self.__emprunte = True
            print(f"Le livre {self.__titre} a été emprunté.")
        else:
            print(f"Le livre {self.__titre} est déjà emprunté.")

    def rendre(self):
        if self.__emprunte:
            self.__emprunte = False
            print(f"Le livre {self.__titre} a été rendu.")
        else:
            print(f"Le livre {self.__titre} n'était pas emprunté.")

    def afficher_detail(self):
        return f"{super().afficher_detail()}, Auteur: {self.__auteur}, nb_pages: {self.__nb_pages}"



        
        
        