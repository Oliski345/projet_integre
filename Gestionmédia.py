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
    def __init__(self, identifiants, titre, annee, genre, artiste, nb_piste):
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


class Mediatheque:
    def __init__(self):
        self.__medias = {}
        self.__utilisateurs = {}
        self.__emprunts = set()  # Ensemble pour gérer les emprunts
        self.__historique = []  # Liste pour l'historique des emprunts

    def ajouter_media(self, media):
        self.__medias[media.identifiant] = media

    def ajouter_utilisateur(self, utilisateur):
        self.__utilisateurs[utilisateur.identifiant] = utilisateur

    def emprunter_media(self, media_identifiant, utilisateur_identifiant):
        if media_identifiant in self.__medias and utilisateur_identifiant in self.__utilisateurs:
            media = self.__medias[media_identifiant]
            utilisateur = self.__utilisateurs[utilisateur_identifiant]
            if media_identifiant not in self.__emprunts:
                media.emprunter()
                self.__emprunts.add(media_identifiant)
                self.__historique.append((utilisateur.nom, media.titre, "emprunté"))
            else:
                print(f"Le média '{media.titre}' est déjà emprunté.")
        else:
            print("Média ou utilisateur non trouvé.")

    def rendre_media(self, media_identifiant, utilisateur_identifiant):
        if media_identifiant in self.__medias and utilisateur_identifiant in self.__utilisateurs:
            media = self.__medias[media_identifiant]
            if media_identifiant in self.__emprunts:
                media.rendre()
                self.__emprunts.remove(media_identifiant)
                self.__historique.append((self.__utilisateurs[utilisateur_identifiant].nom, media.titre, "rendu"))
            else:
                print(f"Le média '{media.titre}' n'a pas été emprunté.")
        else:
            print("Média ou utilisateur non trouvé.")

    def afficher_historique(self):
        for entry in self.__historique:
            print(f"Utilisateur: {entry[0]}, Média: {entry[1]}, Action: {entry[2]}")


        
        
        