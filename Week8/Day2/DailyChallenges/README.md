# BaristaBot - Chatbot de commande de café avec LangGraph et Gemini

Ce dossier contient un notebook pédagogique nommé `DailyChallenge_W8_d2.ipynb` qui implémente un assistant de café conversationnel appelé **BaristaBot**.

Le but de ce projet est de montrer comment construire un chatbot capable de :
- comprendre des commandes en langage naturel,
- répondre aux questions sur un menu dynamique,
- ajouter des produits à une commande,
- demander une confirmation avant de finaliser la commande,
- gérer une conversation en état via un graphe d’état.

---

## 1. Ce que fait le chatbot

BaristaBot agit comme un assistant de café. Il peut :
- saluer l’utilisateur,
- présenter le menu,
- aider à choisir une boisson,
- ajouter des articles à la commande,
- confirmer la commande,
- finaliser la commande avec un numéro aléatoire.

Il est construit autour de plusieurs composants :
- un modèle de langage Gemini,
- un graphe de conversation avec LangGraph,
- des outils (tools) pour interagir avec la logique métier,
- un état de conversation pour mémoriser la commande et l’état de la session.

---

## 2. Architecture du notebook

Le notebook suit une progression pédagogique en plusieurs étapes :

### Étape 1 : Installation des dépendances
Le notebook installe les bibliothèques nécessaires :
- `langgraph`
- `langchain-google-genai`
- `google-genai`

### Étape 2 : Configuration de la clé API
Le chatbot utilise l’API Google Gemini. Il faut donc fournir une clé API valide dans la variable `GOOGLE_API_KEY`.

### Étape 3 : Définition de l’état
Un objet `OrderState` est défini pour stocker :
- `messages` : l’historique des messages,
- `order` : la liste des articles commandés,
- `finished` : si la conversation est terminée.

### Étape 4 : Premier chatbot simple
Un premier graphe très simple est créé pour tester la génération d’un message par le modèle.

### Étape 5 : Interaction humaine
Un nœud humain est ajouté afin que l’utilisateur puisse répondre dans la console.

### Étape 6 : Menu dynamique avec outil
Un outil `get_menu()` permet de fournir un menu mis à jour en temps réel au modèle.

### Étape 7 : Gestion des commandes
Des outils supplémentaires sont ajoutés pour :
- `add_to_order()` : ajouter un produit à la commande,
- `confirm_order()` : demander une confirmation,
- `place_order()` : finaliser la commande.

### Étape 8 : Graphe final
Le notebook assemble tous les éléments dans un graphe complet qui peut :
- appeler un outil pour consulter le menu,
- appeler un outil pour gérer la commande,
- revenir vers l’utilisateur pour poursuivre la conversation.

---

## 3. Comment l’essayer

### Prérequis
Avant d’exécuter le notebook, il faut :
1. avoir Python installé,
2. disposer d’une clé API Google Gemini valide,
3. avoir accès à internet pour appeler l’API.

### Étapes
1. Ouvrir le notebook `DailyChallenge_W8_d2.ipynb`.
2. Exécuter les cellules dans l’ordre.
3. Remplacer la valeur de `GOOGLE_API_KEY` par votre vraie clé API.
4. Lancer la cellule finale pour démarrer la conversation.

### Exemple de conversation
Vous pouvez essayer des phrases du type :
- `Bonjour`
- `Quel est le menu ?`
- `Je veux un Latte avec du lait d’avoine`
- `Quels thés avez-vous ?`
- `Confirme ma commande`

Pour quitter, tapez :
- `q`
- `quit`
- `exit`

---

## 4. Exemple de fonctionnement attendu

Le chatbot peut répondre de cette façon :
- il annonce la disponibilité des boissons,
- il ajoute les articles à la commande,
- il demande une confirmation avant de terminer,
- il renvoie un numéro de commande une fois la commande finalisée.

---

## 5. Points importants

- Ce notebook est un exemple pédagogique, pas une application de production complète.
- Le modèle dépend d’une clé API valide.
- Si vous obtenez une erreur liée à l’API, vérifiez :
  - la validité de la clé,
  - l’accès au modèle Gemini,
  - votre connexion réseau.

---

## 6. Résumé rapide

Ce projet montre comment construire un chatbot conversationnel intelligent avec :
- un état de conversation,
- un graphe d’exécution,
- des outils dynamiques,
- une intégration avec Gemini.

C’est un excellent exemple pour comprendre les bases de l’agentic AI avec LangGraph.
