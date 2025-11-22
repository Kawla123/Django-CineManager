# 📖 Guide du Projet Django Movies

## 🎯 À propos du Projet

Ce projet est une application web de gestion de films développée avec Django. Elle permet de créer, consulter, modifier et supprimer des films avec leurs informations et images.

## 🌟 Fonctionnalités Principales

### 1. Gestion des Films
- **Liste des films** : Affichage de tous les films avec leurs informations
- **Détails d'un film** : Page détaillée pour chaque film
- **Ajout de film** : Formulaire pour ajouter un nouveau film avec image
- **Modification** : Éditer les informations d'un film existant
- **Suppression** : Supprimer un film avec confirmation

### 2. Filtrage Dynamique
- Filtre pour afficher uniquement les nouveaux films
- Mise à jour automatique sans rechargement de page
- Case à cocher pour activer/désactiver le filtre

### 3. Gestion des Images
- Upload d'images pour les affiches de films
- Stockage dans le dossier `media/movies/`
- Affichage responsive des images

### 4. Interface d'Administration
- Interface admin moderne avec **Django Jazzmin**
- Dashboard élégant et intuitif
- Gestion complète des films
- Recherche et filtres avancés
- Édition en ligne du champ "Nouveau"

## 🗂️ Structure du Projet

```
movies/
├── manage.py                   # Commandes Django
├── requirements.txt            # Dépendances Python
├── .gitignore                  # Fichiers à ignorer par Git
├── README.md                   # Documentation principale
├── db.sqlite3                  # Base de données
│
├── moviesproject/              # Configuration du projet
│   ├── settings.py            # Paramètres Django
│   ├── urls.py                # URLs principales
│   ├── wsgi.py                # Configuration WSGI
│   └── __init__.py
│
├── movie_app/                  # Application des films
│   ├── models.py              # Modèle Movie
│   ├── views.py               # Vues (list, detail, create, update, delete)
│   ├── forms.py               # Formulaire MovieForm
│   ├── admin.py               # Configuration admin
│   ├── urls.py                # Routes de l'app
│   │
│   ├── templates/             # Templates HTML
│   │   ├── movie_list.html        # Liste des films
│   │   ├── movie_detail.html      # Détails d'un film
│   │   ├── movie_form.html        # Formulaire ajout/modification
│   │   └── movie_confirm_delete.html  # Confirmation suppression
│   │
│   └── migrations/            # Migrations de base de données
│
└── media/                     # Fichiers uploadés
    └── movies/                # Images des films
```

## 🎨 Modèle de Données

### Movie
Le modèle principal qui représente un film :

| Champ | Type | Description |
|-------|------|-------------|
| **title** | CharField(255) | Titre du film (obligatoire) |
| **description** | TextField | Description complète du film |
| **release_year** | IntegerField | Année de sortie |
| **image** | ImageField | Affiche du film (upload) |
| **new** | BooleanField | Marquer comme nouveau film (par défaut: False) |

## 🚀 Installation et Utilisation

### 1. Cloner le projet
```bash
git clone https://github.com/Kawla123/TPDjango.git
cd TPDjango
```

### 2. Créer l'environnement virtuel
```bash
# Windows
python -m venv envadmin
envadmin\Scripts\activate

# Linux/Mac
python3 -m venv envadmin
source envadmin/bin/activate
```

### 3. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 4. Configurer la base de données
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Créer un administrateur
```bash
python manage.py createsuperuser
```

### 6. Lancer le serveur
```bash
python manage.py runserver
```

### 7. Accéder à l'application
- **Application** : http://127.0.0.1:8000/
- **Admin** : http://127.0.0.1:8000/admin/

## 📱 Pages Disponibles

### Page d'Accueil (Liste)
- **URL** : `/`
- **Description** : Affiche tous les films sous forme de grille
- **Fonctionnalités** :
  - Vue en grille responsive
  - Filtre "Nouveaux films"
  - Badge "Nouveau" sur les films récents
  - Bouton "Voir détails" pour chaque film
  - Bouton "Ajouter un film"

### Page Détails
- **URL** : `/movie/<id>/`
- **Description** : Affiche les informations complètes d'un film
- **Fonctionnalités** :
  - Affichage de l'image en grand
  - Toutes les informations du film
  - Boutons Modifier et Supprimer
  - Bouton retour à la liste

### Page Ajout/Modification
- **URL** : 
  - Ajout : `/add/`
  - Modification : `/edit/<id>/`
- **Description** : Formulaire pour créer ou modifier un film
- **Champs** :
  - Titre (obligatoire)
  - Description (obligatoire)
  - Année de sortie (obligatoire)
  - Image
  - Case "Nouveau film"

### Page Suppression
- **URL** : `/delete/<id>/`
- **Description** : Page de confirmation avant suppression
- **Fonctionnalités** :
  - Affichage des informations du film
  - Avertissement
  - Boutons Confirmer/Annuler

### Interface Admin
- **URL** : `/admin/`
- **Description** : Interface d'administration Django avec Jazzmin
- **Fonctionnalités** :
  - Dashboard moderne
  - Gestion complète des films
  - Recherche par titre/description
  - Filtres par année et statut "nouveau"
  - Édition en ligne
  - Actions en masse

## 🛠️ Technologies Utilisées

### Backend
- **Django 5.2.8** - Framework web Python
- **Python 3.12** - Langage de programmation
- **SQLite** - Base de données

### Frontend
- **HTML5** - Structure des pages
- **CSS3** - Styles et design
- **JavaScript** - Interactivité (filtrage)

### Packages Python
- **Pillow** - Traitement et gestion des images
- **Django Jazzmin** - Interface admin moderne et élégante

## 🎨 Personnalisation

### Modifier les couleurs
Les couleurs principales sont définies dans les templates HTML :
- Bleu : `#3498db`
- Vert : `#27ae60`
- Rouge : `#e74c3c`
- Gris : `#95a5a6`

### Ajouter des champs au modèle
1. Modifier `movie_app/models.py`
2. Ajouter le champ au formulaire dans `movie_app/forms.py`
3. Créer et appliquer les migrations
4. Mettre à jour les templates si nécessaire

### Changer le thème admin
Modifier les paramètres Jazzmin dans `moviesproject/settings.py`

## 📝 Commandes Utiles

```bash
# Créer un nouveau superuser
python manage.py createsuperuser

# Créer des migrations
python manage.py makemigrations

# Appliquer les migrations
python manage.py migrate

# Lancer le serveur
python manage.py runserver

# Lancer le serveur sur un port spécifique
python manage.py runserver 8080

# Accéder au shell Django
python manage.py shell

# Collecter les fichiers statiques
python manage.py collectstatic
```

## 🔒 Sécurité

### En Développement
- `DEBUG = True` dans settings.py
- Secret key visible dans le code
- SQLite comme base de données

### En Production (Recommandations)
- Changer `DEBUG = False`
- Utiliser une secret key sécurisée (variables d'environnement)
- Utiliser PostgreSQL ou MySQL
- Configurer ALLOWED_HOSTS
- Servir les fichiers static/media via un serveur web (Nginx)
- Utiliser HTTPS
- Configurer CSRF et sécurité Django

## 🌐 Déploiement

### Préparer pour la production
1. Mettre à jour `settings.py` :
   ```python
   DEBUG = False
   ALLOWED_HOSTS = ['votre-domaine.com']
   ```

2. Utiliser des variables d'environnement pour les secrets

3. Configurer une vraie base de données (PostgreSQL)

4. Collecter les fichiers statiques :
   ```bash
   python manage.py collectstatic
   ```

### Options de déploiement
- **Heroku** - Simple et rapide
- **PythonAnywhere** - Gratuit pour petits projets
- **DigitalOcean** - VPS avec contrôle total
- **AWS / Azure / GCP** - Solutions cloud professionnelles

## 💡 Conseils

1. **Sauvegardez régulièrement** votre base de données
2. **Utilisez Git** pour versionner votre code
3. **Testez** avant de déployer en production
4. **Documentez** vos modifications
5. **Commentez** votre code pour faciliter la maintenance

## 🔄 Workflow de Développement

1. Créer une branche pour une nouvelle fonctionnalité
2. Développer et tester localement
3. Commiter les changements
4. Pousser vers GitHub
5. Créer une Pull Request
6. Review et merge

## 📞 Support

Pour toute question :
- Consulter la [documentation Django](https://docs.djangoproject.com/)
- Vérifier les issues GitHub
- Contacter le mainteneur du projet

## 🎓 Apprentissage

Ce projet est idéal pour apprendre :
- Les bases de Django (models, views, templates)
- Le système de formulaires Django
- La gestion des fichiers uploadés
- L'interface d'administration
- Les relations entre URLs, vues et templates
- Le pattern MVT (Model-View-Template)

---

**Version** : 1.0.0  
**Dernière mise à jour** : Novembre 2025  
**Auteur** : Kawla123