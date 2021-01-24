# ROS-project

## Challenge 1

Tout d'abord, il faut lancer la simulation du challenge 1 dans le package larmm dans un webshell et rviz dans un autre webshell

roslaunch larm challenge-1.launch

rosrun rviz rviz

Le launch file à exécuter dans un troisième webshell est navigation.launch dans le package student_pkg.

roslaunch student_pkg navigation.launch

(ce launch file lance les launch files scan_map.launch et path_planning.launch)

Désormais, il suffit de donner au robot une destination via l'outil 2D Nav Goal de l'interface graphique rviz.

Le robot arrive bien à atteindre son objectif en évitant les obstacles lorsqu'il connait la map. S'il ne connait pas encore toute la map, il va choisir le meilleur chemin pour arriver au niveau du point le plus proche de la destination dasn la map qu'il connait déja, puis il va mettre à jour son itinéraire en fonction de ce qu'il a réussi à charger de la map.


## Challenge 2

Tout d'abord, il faut lancer la simulation du challenge 2 dans le package larmm dans un webshell et rviz dans un autre webshell

roslaunch larm challenge-2.launch

rosrun rviz rviz

Le launch file à exécuter est mapping.launch dans le package student_pkg.

roslaunch mapping.launch student_pkg

(ce launch file lance les launch files navigation.launch et detection.launch. navigation.launch est le launch file du challenge 1 et detection.launch est le launch file qui gère lance la détection de la canette et la publication de sa position)

Les scripts detection et detection_copy utilisent des methodes de détection que nous n'avons pas réussi à faire fonctionner de manière suffisamment efficace (parfois le mur était considéré comme une cannette en fonction des ombres). Respectivement, ces méthodes sont celles des key points et de la binarisation de l'image. L'image coca-cola.png sert pour la méthode des key points
Dans le script detection_qui_marche, on utilise un masque rouge puisque dans la simulation du challenge 2, les seuls éléments rouges sont les cannettes. Cette méthode fonctionne très bien.

En revanche, nous ne sommes pas arrivés à aller au bout de la publication des positions des cannettes dans le topic /bottle : rien n'est publié dans le topic et nous ne savons pas d'où vient le problème.


## Challenge 3

Tout d'abord, il faut lancer la simulation du challenge 3 dans le package larmm dans un webshell et rviz dans un autre webshell

roslaunch larm challenge-3.launch

rosrun rviz rviz

Le launch file à exécuter est exploration.launch dans le package student_pkg.

roslaunch exploration.launch student_pkg

(ce launch file lance les launch files navigation.launch, detection.launch et bottle_goals.launch)

Le launch file bottle_goals.launch lance l'exécution du script python bottle_goals.py, qui donne au robot les positions successives à atteindre afin d'explorer efficacement la map.