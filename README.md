Réalisé par le groupe 8 
 - FARESSE Yassine
 - OUSSEINI Mansour Mahamadou

FEEDBACK : 

1-Difficultés :

Comprendre et parser les logs avec des expressions régulières.

Manipuler pandas pour grouper et trier les données.

2-Facilités :

Visualiser les résultats avec matplotlib est motivant et intuitif.

Découper le code en fonctions aide à progresser étape par étape.

Le projet est concret et donne du sens à l’apprentissage Python en sécurité.

3-Conclusion :

Projet un peu difficile mais très formateur, idéal pour renforcer ses compétences en Python et cybersécurité. Avec de la patience et de la méthode, il est accessible et valorisant.

LES ETAPES TECHNIQUES : 

1-Chargement et parsing
Lire le fichier log, extraire IP, date, méthode, URL, status, user-agent avec regex, et nettoyer les lignes malformées.

2-Structuration des données
Stocker les données dans un DataFrame pandas, convertir types et filtrer (ex: erreurs 404).

3-Analyse statistique
Grouper par IP, compter occurrences, trier pour identifier les IP suspectes, détecter les bots via user-agent.

4-Visualisation
Créer des graphiques (bar chart) avec matplotlib pour montrer les résultats.

5-Scan réseau
Scanner les ports connus des IP suspectes avec socket, version mono-thread puis multithread, détecter ports ouverts.

6-Interface & export
Ajouter un menu CLI simple, exporter résultats en CSV/JSON/HTML, gérer erreurs et saisies utilisateur.

7-Tests & validation
Vérifier la robustesse du code et la cohérence des résultats.

LES CHOIX TECHNIQUES : 

1-Python pour sa simplicité et ses bibliothèques puissantes.

2-Regex pour extraire précisément les données dans les logs.

3-Pandas pour structurer et analyser facilement les données.

4-Matplotlib pour visualiser les résultats avec des graphiques clairs.

5-Socket pour scanner les ports réseau et tester leur ouverture.

6-Multithreading pour accélérer le scan des ports.

7-Modularisation du code pour une meilleure organisation et maintenance.

8-Interface CLI simple pour faciliter l’utilisation.

9-Gestion des erreurs pour assurer la robustesse.

10-Export CSV/JSON pour partager les résultats.

