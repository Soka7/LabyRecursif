# 🧩 Résolution de Labyrinthe – Algorithme Récursif & Raylib

## 📌 Présentation

Ce projet implémente un **algorithme récursif de résolution de labyrinthe**, combiné à une **interface graphique interactive** réalisée avec **Raylib**.  
L’objectif est de visualiser pas à pas le cheminement de l’algorithme à travers un labyrinthe, depuis l’entrée jusqu’à la sortie.

Ce projet met l’accent sur :
- la **récursivité**
- le **backtracking**
- la **visualisation graphique des algorithmes**

---

## 🎯 Objectifs pédagogiques

- Comprendre le fonctionnement d’un algorithme récursif
- Manipuler les concepts de **pile d’appels** et de **retour arrière**
- Visualiser l’exploration d’un labyrinthe en temps réel
- Utiliser **Raylib** pour créer une interface graphique simple et efficace

---

## 🧠 Principe de l’algorithme

L’algorithme repose sur une approche **DFS (Depth-First Search)** récursive :

1. On part de la case de départ
2. On marque la case comme visitée
3. On explore récursivement les cases voisines possibles
4. Si une impasse est atteinte, on revient en arrière (*backtracking*)
5. Le processus s’arrête lorsque la sortie est trouvée

Chaque étape est **visualisée graphiquement** :
- cases visitées
- chemins explorés
- chemin final trouvé

<img src="sad-seal.mp4" width="250"/>

---

## 🖥️ Interface graphique (Raylib)

L’interface permet de :
- afficher le labyrinthe sous forme de grille
- visualiser l’exploration récursive en temps réel
- distinguer :
  - les murs
  - les chemins
  - les cases visitées
  - la solution finale

Raylib est utilisé pour sa **simplicité**, sa **légèreté** et ses **performances en temps réel**.

---

## 🛠️ Technologies utilisées

- **Langage** : Python
- **Bibliothèque graphique** : [Raylib](https://www.raylib.com/)
- **Paradigme** : Programmation récursive
- **Algorithme** : Backtracking / DFS

---

## 📁 Structure du projet (exemple)