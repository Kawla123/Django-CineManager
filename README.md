# 🎬 Django Movies Project

![Django](https://img.shields.io/badge/Django-5.2.8-green.svg)
![Python](https://img.shields.io/badge/Python-3.12-blue.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Tests](https://img.shields.io/badge/Tests-Pytest-orange.svg)

Une application web moderne de gestion de films construite avec Django, offrant une interface élégante avec Jazzmin Admin et un système complet de tests.

## ✨ Fonctionnalités

- 📝 **CRUD Complet** - Créer, lire, modifier et supprimer des films
- 🖼️ **Upload d'images** - Gestion des affiches de films
- 🔍 **Filtrage dynamique** - Filtre les nouveaux films en temps réel
- 🎨 **Interface Admin moderne** - Grâce à Django Jazzmin
- 🧪 **Suite de tests complète** - Tests unitaires, Selenium, sécurité
- 📊 **Rapports de qualité** - Couverture de code, SonarQube, JMeter
- 🔒 **Tests de sécurité** - Intégration OWASP ZAP
- ⚡ **Tests de performance** - Apache JMeter

## 🚀 Démarrage Rapide

### Prérequis

- Python 3.12+
- pip
- virtualenv (recommandé)

### Installation

1. **Clonez le repository**
```bash
git clone https://github.com/votre-username/TPDjango.git
cd TPDjango
```

2. **Créez et activez l'environnement virtuel**
```bash
# Windows
python -m venv envadmin
envadmin\Scripts\activate

# Linux/Mac
python3 -m venv envadmin
source envadmin/bin/activate
```

3. **Installez les dépendances**
```bash
pip install -r requirements.txt
```

4. **Effectuez les migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Créez un superutilisateur**
```bash
python manage.py createsuperuser
```

6. **Lancez le serveur**
```bash
python manage.py runserver
```

7. **Accédez à l'application**
- Application: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/

## 📁 Structure du Projet

```
movies/
├── manage.py
├── requirements.txt
├── .gitignore
├── README.md
├── moviesproject/              # Configuration Django
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── __init__.py
├── movie_app/                  # Application principale
│   ├── models.py               # Modèle Movie
│   ├── views.py                # Vues CRUD
│   ├── forms.py                # Formulaires
│   ├── admin.py                # Configuration admin
│   ├── urls.py                 # Routes
│   ├── templates/              # Templates HTML
│   │   ├── movie_list.html
│   │   ├── movie_detail.html
│   │   ├── movie_form.html
│   │   └── movie_confirm_delete.html
│   └── migrations/
├── tests/                      # Tests
│   ├── unit_tests/
│   │   └── test_movies.py
│   ├── selenium_tests/
│   │   └── test_selenium.py
│   └── security_tests/
│       └── test_zap_security.py
├── media/                      # Fichiers uploadés
└── reports/                    # Rapports de tests
```

## 🧪 Tests

### Tests Unitaires
```bash
# Django tests
python manage.py test

# Pytest avec couverture
pytest tests/unit_tests/ -v --cov=movie_app --cov-report=html
```

### Tests Selenium
```bash
# Assurez-vous que le serveur Django tourne
python manage.py runserver

# Dans un autre terminal
pytest tests/selenium_tests/ -v -m selenium
```

### Tests de Sécurité (OWASP ZAP)
```bash
# 1. Démarrez ZAP
zap.sh -daemon -port 8080  # Linux/Mac
zap.bat -daemon -port 8080  # Windows

# 2. Démarrez Django
python manage.py runserver

# 3. Lancez les tests
python tests/security_tests/test_zap_security.py
```

### Tests de Performance (JMeter)
```bash
# Mode graphique
jmeter -t jmeter_test_plan.jmx

# Mode CLI avec rapport
jmeter -n -t jmeter_test_plan.jmx -l reports/results.jtl -e -o reports/html_report/
```

### Analyse SonarQube
```bash
sonar-scanner
```

### Script de test complet
```bash
chmod +x run_all_tests.sh
./run_all_tests.sh
```

## 📊 Modèle de Données

### Movie
| Champ | Type | Description |
|-------|------|-------------|
| title | CharField(255) | Titre du film |
| description | TextField | Description complète |
| release_year | IntegerField | Année de sortie |
| image | ImageField | Affiche du film |
| new | BooleanField | Marquer comme nouveau |

## 🛠️ Technologies Utilisées

### Backend
- **Django 5.2.8** - Framework web Python
- **SQLite** - Base de données (développement)
- **Pillow** - Traitement d'images

### Frontend
- **HTML5/CSS3** - Interface utilisateur
- **JavaScript** - Interactivité (filtrage)

### Admin
- **Django Jazzmin** - Interface d'administration moderne

### Tests & Qualité
- **Pytest** - Framework de tests
- **Selenium** - Tests automatisés du navigateur
- **Coverage.py** - Couverture de code
- **OWASP ZAP** - Tests de sécurité
- **Apache JMeter** - Tests de performance
- **SonarQube** - Analyse de qualité de code
- **Flake8** - Linting Python
- **Bandit** - Analyse de sécurité statique

## 🌟 Fonctionnalités Détaillées

### Gestion des Films
- ✅ Listing avec filtrage dynamique
- ✅ Détails complets par film
- ✅ Ajout avec upload d'image
- ✅ Modification
- ✅ Suppression avec confirmation

### Interface Admin
- ✅ Dashboard Jazzmin moderne
- ✅ Recherche et filtres avancés
- ✅ Édition en ligne
- ✅ Actions en masse

### Tests Automatisés
- ✅ Tests unitaires (models, views, forms)
- ✅ Tests d'intégration
- ✅ Tests E2E avec Selenium
- ✅ Tests de sécurité avec ZAP
- ✅ Tests de performance avec JMeter
- ✅ Rapports de couverture détaillés

## 📈 Métriques de Qualité

- **Couverture de code**: Objectif > 90%
- **Tests**: 50+ tests automatisés
- **Performance**: < 200ms pour 90% des requêtes
- **Sécurité**: 0 vulnérabilité critique

## 🚧 Roadmap

- [ ] Authentification utilisateur
- [ ] Système de notes et avis
- [ ] API REST avec Django REST Framework
- [ ] Recherche full-text
- [ ] Recommandations de films
- [ ] Multi-langue
- [ ] Mode sombre
- [ ] Export PDF/Excel

## 🤝 Contribution

Les contributions sont les bienvenues ! Pour contribuer :

1. Forkez le projet
2. Créez votre branche (`git checkout -b feature/AmazingFeature`)
3. Committez vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Pushez vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrez une Pull Request

## 📝 License

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## 👨‍💻 Auteur

**Votre Nom**
- GitHub: [@Kawla123](https://github.com/Kawla123)
- Email: votre.email@example.com

## 🙏 Remerciements

- Django Team pour l'excellent framework
- Jazzmin pour l'interface admin moderne
- La communauté open-source

## 📞 Support

Pour toute question ou problème :
- Ouvrez une [issue](https://github.com/Kawla123/TPDjango/issues)
- Contactez-moi par email

---

⭐ Si ce projet vous a aidé, n'hésitez pas à lui donner une étoile !
# Django-CineManager
