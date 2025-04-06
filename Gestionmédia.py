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
        # Dictionnaires pour stocker les utilisateurs et les médias
        self.__utilisateurs = {}
        self.__medias = {}
        self.__emprunts = {}

    # Créer un média (livre, DVD, CD)
    def ajouter_media(self, type_media, titre, annee_parution, genre, **kwargs):
        identifiant = len(self.__medias) + 1
        if type_media == 'livre':
            media = Livre(identifiant, titre, annee_parution, genre, **kwargs)
        elif type_media == 'dvd':
            media = DVD(identifiant, titre, annee_parution, genre, **kwargs)
        elif type_media == 'cd':
            media = CD(identifiant, titre, annee_parution, genre, **kwargs)
        else:
            print("Type de média inconnu.")
            return None

        self.__medias[identifiant] = media
        print(f"Média '{titre}' ajouté avec succès !")
        return media

    # Rechercher un média par titre
    def rechercher_media(self, titre):
        resultats = [media for media in self.__medias.values() if titre.lower() in media.titre.lower()]
        if resultats:
            print(f"Médias trouvés pour '{titre}':")
            for media in resultats:
                media.afficher_details()
        else:
            print(f"Aucun média trouvé pour '{titre}'.")

    # Emprunter un média
    def emprunter_media(self, utilisateur_id, media_id):
        if utilisateur_id not in self.__utilisateurs:
            print("Utilisateur non trouvé.")
            return

        if media_id not in self.__medias:
            print("Média non trouvé.")
            return

        media = self.__medias[media_id]
        utilisateur = self.__utilisateurs[utilisateur_id]

        if media.emprunte:
            print(f"Le média '{media.titre}' est déjà emprunté.")
            return

        # Calculer la date de retour en fonction du type de média
        if isinstance(media, Livre):
            duree = 21  # Durée de prêt pour les livres
        else:
            duree = 14  # Durée de prêt pour les DVDs et CDs

        date_emprunt = datetime.date.today()
        date_retour = date_emprunt + datetime.timedelta(days=duree)

        # Enregistrer l'emprunt
        utilisateur.ajouter_emprunt(media, str(date_emprunt), str(date_retour))
        media.emprunter(date_emprunt, date_retour)

        print(f"Le média '{media.titre}' a été emprunté par {utilisateur.prenom} {utilisateur.nom}.")
        print(f"Date de retour prévue : {date_retour}.")

    # Retourner un média
    def retourner_media(self, utilisateur_id, media_id):
        if utilisateur_id not in self.__utilisateurs:
            print("Utilisateur non trouvé.")
            return

        if media_id not in self.__medias:
            print("Média non trouvé.")
            return

        media = self.__medias[media_id]
        utilisateur = self.__utilisateurs[utilisateur_id]

        if not media.emprunte:
            print(f"Le média '{media.titre}' n'a pas été emprunté.")
            return

        # Retirer l'emprunt de l'historique
        media.retourner()
        print(f"Le média '{media.titre}' a été retourné par {utilisateur.prenom} {utilisateur.nom}.")

    # Afficher l'historique d'un utilisateur
    def afficher_historique_utilisateur(self, utilisateur_id):
        if utilisateur_id not in self.__utilisateurs:
            print("Utilisateur non trouvé.")
            return
        self.__utilisateurs[utilisateur_id].afficher_historique()

    # Afficher les statistiques de la médiathèque
    def afficher_statistiques(self):
        print("Statistiques de la médiathèque:")
        # Nombre de médias par type
        total_medias = len(self.__medias)
        livres = sum(1 for media in self.__medias.values() if isinstance(media, Livre))
        dvds = sum(1 for media in self.__medias.values() if isinstance(media, DVD))
        cds = sum(1 for media in self.__medias.values() if isinstance(media, CD))

        print(f"Total de médias: {total_medias}")
        print(f"Livres: {livres}")
        print(f"DVDs: {dvds}")
        print(f"CDs: {cds}")

        # Nombre d'utilisateurs
        print(f"Total d'utilisateurs: {len(self.__utilisateurs)}")

        # Nombre d'emprunts et de retours
        emprunts = sum(1 for media in self.__medias.values() if media.emprunte)
        print(f"Nombre d'emprunts en cours: {emprunts}")



        
        
        