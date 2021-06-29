# Projet12
Ce projet consiste à créer un CRM + API qui permettra d'organiser et suivre des evenements pour des clients.


# Documentation API
Veuillez trouver la documentation de l'api sur le lien suivant [API-REST](https://documenter.getpostman.com/view/14846551/TzefBPft)
# Execution du code
 1. Cloner ce dépôt de code à l'aide de la commande: <code>$ git clone https://github.com/Nyankoye/Projet12 </code>
 2. Créez un environnement virtuel dans le projet en utilisant la commande: <code> $ python -m venv env </code>
 3. Activez l'environnement virtuel en utilisant la commande: <code>$ source env/Scripts/activate </code>
 4. Installer les paquets Python répertoriés dans le fichier requirements.txt en utilisant la commande : <code>$ pip install -r requirements.txt </code>
 5. Installer [Postgresql](https://www.postgresql.org/) et créer une une base de données
 6. Modifier le fichier settings.py qui se trouve dans le dossier projet_CRM en renseignant les informations de votre configuration de Postgresql comme suit:
 ```
 DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql', # on utilise l'adaptateur postgresql
        'NAME': 'disquaire', # le nom de votre base de donnees creee precedemment
        'USER': 'celinems', # attention : remplacez par votre nom d'utilisateur
        'PASSWORD': '',
        'HOST': '',
        'PORT': '5432',
    }
}
```
 7. Déplacez-vous dans le fichier projet_CRM en utilisant la commande : <code>$ cd projet_CRM </code>
 8. Charger le contenu de la base de données en utilisant la commande : <code>$ python manage.py migrate </code>
 9. Créer un supper utilisateur avec la commande: <code>$ python manage.py createsuperuser</code>
 10. Créer les Equipes: Equipe Gestion, Equipe Support et Equipe Vente dans la table Equipe.
 11. Lancer le serveur en utilisant la commande : <code>$ python manage.py runserver </code>
 12. Vous pouvez maintenant utiliser l'API en utilisant [postman desktop agent](https://www.postman.com/downloads/) et en suivant les intructions dans la [documentation](https://documenter.getpostman.com/view/14846551/TzefBPft) ou utilisé l'application CRM.