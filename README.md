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

## Limites

- Les murs du labyrinth doivent pouvoir être formé sans avoir a levé le doigt (tout les murs doivent être liés).
- L'éditeur n'est pas très optimisé, meme sur une machine puissante, un labyrinthe de 100 x 100 pourra vous faire atteindre 30 fps.

---

## Commandes (éditeur)

- '+' et '-' (sur un clavier qwerty) pour augmenter ou diminuer la sensibilité de la caméra.
- Ctrl + 'o' pour ouvrir un labyrinth.
- Ctrl + 'z' et Ctrl + 'y' fonctionnent.
- Le scroller de la souris pour zoomer / dezoomer.

---

## Bug 

- La caméra se fera centrer a chaque fois que vous tenterez de la déplacer.
- Si Mazes/dedales.txt est vide, le programme plantera.
- Vous ne pouver pas maintenir une touche pour ajouter ou supprimer un charactère, vous devez appuyer a chaque fois.
- L'éditeur ne montre pas quels object / actions vous être entrain d'effectuer.
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
- **Texture** : PixiEditor

---

## Sources

- Documentation Pyray : https://electronstudio.github.io/raylib-python-cffi/README.html
- Explication de la Camera2D : https://youtu.be/zkjDU3zmk40
- Exemple Camera2D utilisé : https://www.raylib.com/examples/core/loader.html?name=core_2d_camera
- Système de sauvegarde : https://www.w3schools.com/python/python_file_write.asp
- Syntax pour le try & except : https://www.w3schools.com/python/python_try_except.asp
- Syntax pour le default case d'un switch : https://www.datacamp.com/tutorial/python-switch-case

---

## Installer Pyray : 

```
pip3 install raylib==5.5.0.3 --break-system-packages
```
---
## 📁 Structure du projet (exemple)