# Cinéma Film WebApp

## Description

Cinéma Film WebApp est une application web Flask qui affiche une liste de films actuellement en salle au cinéma. Les utilisateurs peuvent cliquer sur un film pour afficher plus de détails.

## Fonctionnalités

- Affichage de la liste des films actuellement en salle au cinéma.
- Affichage des détails d'un film sélectionné.
- Prise en charge de plusieurs langues.
- Intégration avec l'API TMDb pour récupérer les données sur les films.

## Installation

1. Clonez ce dépôt :
   ```bash
   git clone https://github.com/adialloo/cinemafilm.git
   ```
2. Accédez au répertoire du projet :
   ```bash
   cd cinemafilm
   ```
3. Installez les dépendances Python :
   ```bash
   pip install -r requirements.txt
   ```
4. Créez un fichier .env à la racine du projet et ajoutez votre clé d'API TMDb :
   ```
   API_KEY=YOUR_API_KEY_HERE
   ```

## Utilisation

1. Lancez l'application :
   ```bash
   python app.py
   ```
2. Accédez à l'application dans votre navigateur Web à l'adresse http://localhost:5000.

## Tests

Pour exécuter les tests, assurez-vous d'avoir installé les dépendances de développement, puis exécutez pytest :

```bash
pip install pytest
pytest
```

## Technologies utilisées

- Python
- Flask
- HTML/CSS
- Docker

## Auteur

[Alexis - Aly](https://github.com/votre-utilisateur)
