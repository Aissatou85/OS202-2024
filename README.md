# OS202-2024

# Travaux pratiques 1 OS202:

I.Produit matrice-matrice:

1. Temps de calcul du produit matrice-matrice:
   
1023: 1.12735 s;

1024:2.50776 s;

1025:1.12799 s;

Les temps d'exécution obtenu sont absurdes car très différents. On calcule le produit de deux matrices, la façon dont les matrices sont stockées utilisent des tableaux de pointeurs. La matrice est rangée suivant les colonnes(colonne 1, colonne 2...).
Le processeur accède plus facilement aux valeurs de la 2e matrice car les valeurs sont stockées en colonnes donc pour la première matrice on a plutot besoin des données par ligne.
Lorsqu'on effectue des opérations en utilisant la dimension 1024, on ne peit pas réutiliser les valeurs présente dans le cache. Donc on doit les recharger ce qui n'est pas le cas lorsqu'on utilise la dimension 1023. Car les valeurs de la première ligne seront encore dans le cache L3 et le CPU pourra directement y avoir accès.
Le CPU n'accède jamais à la mémoire RAM directement, il transite par les différents caches, il n'a accès qu'au premier cache!

En conclusion, la position d'une variable dans la mémoire impacte considérablement le temps d'exécution d'un programme.

2. Permutons
   temps CPU/MFlops
jik: 1.12735/1899.32
ikj: 1.14361/1872.31
kij:1.12256/1907.43
jki:1.15643/1851.56
kji:1.12651/1895.68

La boucle i est celle qui varie le plus.Lorsque la boucle i et k sont celles qui varient le plus rapidement, on a des meilleurs résultats.
Lorsque j varie le plus vite(dernière boucle) on a les pires résultats.

