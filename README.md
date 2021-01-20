# ROS-project

## Challenge 1

Le launch file à exécuter est navigation.launch dans le package student_pkg.

Il suffit ensuite de donner au robot une destination via rviz.

Le robot arrive bien à atteindre son objectif en évitant dles obstacles lorsqu'il connait la map. Rien à redire de ce côté.

Cependant, s'il ne connait pas la map, il va aller jusqu'au point "qu'il connait" le plus proche de la destination, puis aller en ligne droite jusqu'à la destination. Le problème c'est qu'il ne recalcule pas son parcours si au cours de son scan il rencontre des obstacles qu'il n'avait pas anticipés. C'est donc la local costmap qui ne fonctionne pas. Nous avons essayer de résoudre le problème, puis de le contourner, sans succès.


## Challenge 2

Le launch file à exécuter est detection.launch dans le package student_pkg.

On peut alors déplacer le robot en utilisant le clavier. (roslaunch turtlebot_teleop keyboard_teleop.launch)

Le robot détecte bien les canettes mais il a besoin d'être proche des canettes pour que ça marche, et face au logo. Par ailleurs, nous n'avons pas encore réussi à trouver de condition à partir de laquelle on considère bien qu'une cannette est détectée, ni à trouver comment déterminer sa position.
