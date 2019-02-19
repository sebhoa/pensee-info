# print ou return ? Les deux bien sûr !
**où comment reconcilier tout le monde**
(enfin j'espère)

Cet article tente de donner le point de vue de l'auteur à la  question : **qu'est-ce que la pensée informatique ?** Deux réponses sont faites : une courte, l'autre plus longue illustrée par l'histoire d'un programme informatique qui évolue. Nous profiterons de l'occasion pour revenir sur la polémique : les entrées / sorties font-elles partie de la pensée informatique ?


## L'origine du problème

Quelqu'un, quelque part, dans un bureau, s'est dit : 

> "_supprimons les entrées / sorties, ce n'est pas de la pensée informatique"_ 

Ah ?! Pourtant si on tape dans un moteur de recherche "premier programme java", on obtient dans wikibooks :

```java
public class Exemple {
        public static void main(String[] args) {
                System.out.println("Hello world!");
        }
}
``` 

Ou encore en Python :

Extrait du cours [Python de Openclassroom][1] :

> _"Ajoutez la commande que vous souhaitez exécuter. De mon côté j’y écris  `print("Yo ! T’as pas un 06 ?")`  pour afficher quelque chose sur la console."_

Et vous pouvez continuer à chercher : pratiquement dans **tous** les langages de programmation, le premier programme consiste à afficher par un `print` quelque chose à l'écran.

Alors on se demande mais pourquoi ? Pourquoi avoir supprimé les entrées / sorties des textes officiels de programmation dans l'enseignement ? Je n'ai pas la réponse à cette question. Ce qui est constaté, en classe avec des élèves, pour ma part avec de jeunes étudiants de première année scientifique c'est que quelque soit le langage de programmation la confusion entre les entrées / sorties d'un programme (`input` et `print`) et les entrées / sorties d'une fonction (paramètres d'entrées et le `return`) existe et n'est pas marginale.

Pour autant, je ne crois pas qu'il faille nier l'existence des premières. Nous allons montrer dans la suite qu'avoir une pensée informatique ne concerne pas de savoir si oui ou non les entrées / sorties en font partie.


## Qu'est-ce que la pensée informatique ?

### Réponse courte

> "Pensez-vous qu'on puisse écrire un programme informatique qui...
>
> -- Oui"

Voilà. Si à cette question, _"est-ce qu'on peut..."_ vous répondez oui sans attendre la fin de la question alors c'est que vous avez la pensée informatique. Bien sûr, j'exagère un peu et parfois, la théorie nous dit : "là ce n'est pas possible" (je vous renvoie par exemple à l'[article Wikipédia traitant du problème de l'arrêt][2]). Mais en restreignant les choses, en faisant des hypothèses supplémentaires, le _non_ se tranforme en un _oui_, au moins partiel.

### Réponse longue ou comment mon `print('Hello world')` va (me faire) grandir

Nous l'avons vu en introduction, en général on commence par écrire notre premier programme avec une unique instruction qui est l'appel à la fonction prédéfinie (ie connue du langage de programmation utilisé) qui sert à afficher, imprimer quelque chose à l'écran.

Cette fonction s'appelle `print`, `println`, `printf` suivant le langage utilisé et à ce stade les choses sont assez floues : _c'est quoi une fonction ?_, _'Hello world' ?_ L'intérêt est surtout de voir le mécanisme de rédaction du code source dans un éditeur et l'utilisation du compilateur ou de l'interprèteur pour exécuter ce code source.

Mais avançons un peu. Et plaçons nous dans un apprentissage avec le langage Python. Nous savons donc que `print('Hello world')` est une instruction, que `print` est une fonction prédéfinie, que `'Hello world'` est une chaîne de caractères, que cette chaîne n'a aucun sens pour Python si ce n'est que c'est une suite de caractères. Qu'il faut encadrer cette chaîne avec un délimiteur (ici l'apostrophe). Que Python sait aussi manipuler des nombres : par exemple `print(2+3)` constitue une instruction valide et le programme résultant affiche 5 à l'écran. Bien. Nous progressons drôlement. Mais pouvons-nous dire, par la connaissance de ces quelques concepts de programmation, que nous avons une pensée informatique ? Non, pas encore.

#### Première étape

Au cours de notre apprentissage, on nous demande d'écrire un programme qui affiche un carré 10x10 de 'X' à l'écran (oui les informaticiens sont des gens d'une créativité rare). Nous écrivons donc notre programme dans un fichier, nommons-le `dessin.py` et l'exécution de ce script (programme en mode texte, associé en général à un _truc de geek_) donne le résultat suivant :

```
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
```

Et le contenu de notre `dessin.py` :

```python
print('XXXXXXXXXX')
print('XXXXXXXXXX')
print('XXXXXXXXXX')
print('XXXXXXXXXX')
print('XXXXXXXXXX')
print('XXXXXXXXXX')
print('XXXXXXXXXX')
print('XXXXXXXXXX')
print('XXXXXXXXXX')
print('XXXXXXXXXX')
```

Non ?! Si ! Et si ce code vous choque... il vous choque forcément puisque vous n'êtes pas débutant en programmation, mais mettez-vous dans la peau d'un débutant. S'il continue de vous choquer c'est que, probablement vous avez un début de pensée informatique. Car évidemment on ne _copie-colle_ pas 10 fois la même instruction. Pourquoi ? **Parce que la longueur de notre programme ne peut pas dépendre de la taille de la donnée**. Ce qui, en clair, signifie que s'il fallait, sur le même principe, faire le programme qui affiche un carré 1000x1000 on serait bien embêté. On utilise une boucle. Et si on nous donne cet exercice c'est qu'on veut que nous mettions en oeuvre cette connaissance.

Notre script ressemblera donc plus vraisemblablement à :

```python
for cpt in range(10):
    print('XXXXXXXXXX')
```

Et comme nous avons suivi quand le prof a parlé de chaînes de caractères, de concaténation etc. alors nous écrirons :

```python
for cpt in range(10):
    print('X' * 10)
```

#### Deuxième étape

Nous sommes très fier de notre programme de dessin que nous donnons à Pierre. Qui, tout content, va en parler à Marie, qui vient nous voir : "J'aimerai bien un programme comme celui de Pierre mais je préfèrerais un carré plus petit, disons 6x6, c'est possible ?". Evidemment.

Et là, respectueux de ne pas faire trop attendre Marie, nous nous empressons de _pondre_ le code suivant `dessin_marie.py` :

```python
for cpt in range(6):
    print('X' * 6)
```

Mais quand même nous nous disons : _"hmmm si je pouvais sortir un programme qui s'adapte à la volonté de chaque utilisateur ce serait un gain de temps appréciable"_. Et comme nous avons bien suivi le passage sur la fonction `input` nous pouvons écrire :

```python
size = int(input('Donnez la taille de votre carré : '))
for cpt in range(size):
    print('X' * size)
```

Le passage des cas 10x10 et 6x6 au cas générique c'est de la pensée informatique. 


#### Troisième étape

Notre apprentissage de la programmation avance bien (nous avons pris beaucoup de choses notamment que pour deux nombres entiers a et b, a//b donnait la division entière de a par b) et nous avons un nouvel exercice à résoudre : agrémenter notre dessin carré d'une croix (j'ai remplacé les 'X' par des '.' pour plus de lisibilité). Par exemple pour 5x5 :

```
O...O
.O.O.
..O..
.O.O.
O...O
```

Les choses se compliquent. On voit bien que le dessin d'une ligne dépend du numréo de cette ligne, on voit bien aussi que certaines lignes se retrouvent. 

Notre pensée informatique va nous permettre de manipuler des instances ie des cas particuliers (5x5, 6x6...) du problème pour décortiquer tout ça et essayer d'obtenir une règle générique de construction (valable quelque soit la taille donnée) :

1. une ligne semble comporter : des '.' (éventuellement aucun), puis un 'O', puis des '.' (éventuellement aucun), puis un 'O' et enfin le même nombre de '.' qu'au début.
2. Pour un carré de dimension impaire on voit bien que la ligne centrale est différente mais ce ne sera pas le cas pour un carré de taille paire :
```
O....O
.O..O.
..OO..
..OO..
.O..O.
O....O
```
3. Après la ligne centrale, on répète les lignes précédentes mais dans l'ordre inverse

Occupons nous de la première moitié. Si nous numérotons les lignes de 0 à mid (où, si n est la taille de mon carré, mid vaut n//2). On constate que la ligne 0 possède zéro '.', puis un 'O', puis des '.', puis un 'O' et zéro '.'. De façon similaire la ligne 1 possède un '.', puis un 'O' etc.

Donc la ligne i possède i '.', un 'O', des '.', un 'O' et enfin i '.'. Combien de '.' au milieu ? Ce qui reste de place si la ligne doit faire n caractères... soit n - i - 1 - i - 1 donc n - 2i - 2. Nous tenons notre règle générique, du moins pour la première moitié de notre dessin :

```python
n = int(input('size : '))
mid = n//2
for i in range(mid):
    print('X' * i + 'O' + 'X' * (n - 2*i - 2) + 'O' + 'X' * i)
```

Et l'exécution de ce programme pour n = 5 donne :

```
OXXXO
XOXOX
```

Pour n = 6

```
OXXXXO
XOXXOX
XXOOXX
```

On constate que pour écrire notre règle de construction, il a fallu manipuler des nombres au travers de lettres. C'est le propre même de l'**abstraction**, concept important en informatique comme en mathématiques ! Nous laissons de côté la question qui brûle les lèvres : faut-il être fort en maths pour faire de la programmation ?

Mais notre dessin est incomplet. Nous continuons notre manipulation : si n est un nombre impair il existe une ligne centrale qui se décortique comme ceci : n//2 '.', un seul 'O' et à nouveau n//2 '.'. Si par contre n est pair, cette ligne n'existe pas.

Notre code s'enrichit :

```python
n = int(input('size : '))
mid = n//2
for i in range(mid):
    print('X' * i + 'O' + 'X' * (n - 2*i - 2) + 'O' + 'X' * i)
if n%2 == 1:
    print('X' * mid + 'O' + 'X' * mid)
```

La nouvelle exécution pour n = 5 donne :

```
OXXXO
XOXOX
XXOXX
```

Pour la seconde partie, le raisonnement est similaire, mais la règle générique est plus compliquée à obtenir. Là deux parcours se dessinent : celui qui va insister et finir par trouver le code pour la deuxième partie du dessin, ce qui nous donne le programme complet suivant :

```python
n = int(input('size : '))
mid = n//2
for i in range(mid):
    print('X' * i + 'O' + 'X' * (n - 2*i - 2) + 'O' + 'X' * i)
if n % 2:
    print('X' * (mid) + 'O' + 'X' * (mid))
    mid = n//2 + 1
for i in range(mid, n):
    print('X' * (n - i - 1) + 'O' + 'X' * (2*i - n) + 'O' + 'X' * (n - i - 1))
```

Avec cette petite explication pour l'instruction `mid = n//2 /+ 1` qu'on voit dans le `if` :
Si n est impair, par exemple 5 alors 5//2 = 2 est le numéro de la ligne centrale différente et la deuxième moitié commence à 5//2 + 1. Par contre, si n est pair, par exemple 6, alors 6//2 = 3, la première moitié va de 0 à 2 et la deuxième reprend de 3 jusqu'à 5. 

Mais celui qui a développé encore plus sa pensée informatique va se rebeller : "non c'est trop bête, j'ai déjà construit les lignes qu'il me faut ! Je **veux** pouvoir les réutiliser."

#### Quatrième et dernière étape

Dans notre version précédente du code, ce qui empêche de réutiliser ce qu'on a fait c'est le mélange entre : le traitement des données (la construction de la ligne qui est une chaîne de caractères) et l'utilisation du résultat de ce traitement (le print).

La pensée informatique c'est cela : faire bien attenion de **toujours** séparer les choses et en l'occurence ici :

1. La récupération des données
2. Le traitement de ses données (pour en produire de nouvelles notamment)
3. La valorisation, l'utilisation de ce traitement ou des résultats obtenus

Cette séparation est à l'origine de bien des concepts : programmation modulaire, notion de fonction, modèles de développement comme MVC ([Modèle Vue Contrôleur][4]) et j'en passe.


Nous allons nous servir du concept de fonction informatique. Je ne souhaite pas être trop théorique ici, disons qu'une fonction va être un fragment de code qui, si on lui fournit des données (au travers de paramètres), est capable de nous construire et de nous restituer un résultat.


Nous allons aussi nous servir de liste. La liste va permettre de stocker les premières chaînes de caractères que nous utiliserons une première fois dans un certain ordre pour dessiner la première moitié de la figure et dans l'ordre inverse pour la seconde moitié. 

D'autres concepts très puissants nous servirons, le but ici n'est pas d'en avoir une compréhension précise. Ce que nous en faisons peut être réalisé plus basiquement avec de simples boucles par exemple. Dans le désordre nommons :

1. Le _slicing_
2. la méthode `join` pour passer d'une liste de chaînes de caractères à une unique chaîne.
3. Les chaînes formattées

Un exemple de liste pour le dessin 5x5 serait : 

```python
['OXXXO', 'XOXOX']
```

Avant de vous livrer la fonction moitie, une autre analyse chiffonne : dans la chaîne de caractères 

```python
'X' * i + 'O' + 'X' * (n - 2*i - 2) + 'O' + 'X' * i
```

On constate une répétition des deux portions de fin : le 'O' et le 'X' * i. On aimerait coder une sorte de motif : `'{0}{1}{2}{1}{0}'` où `{0}` c'est `'X' * i`, `{1}` c'est `'O'` et `{2}` c'est `'X' * (n - 2*i - 2)`. Ceci existe en Python, il s'agit des chaînes de caractères formattées : une chaînes de caractères où certaines choses ont une signification, en l'occurence des marqueurs que Python remplace par des valeurs au moment de construire explicitement la chaîne (je vous invite à consulter la doc officielle à propos des [chaînes formattées][3] notamment la section 6.1.3.2 avec les exemples). Et voici notre fonction :

```python
def moitie(n, croix, rond):
    l = []
    for i in range(n//2):
        l.append('{0}{1}{2}{1}{0}'.format(croix * i, rond, croix * (n - 2*i - 2)))
    return l
```

Et oui, nous en avons profité pour que les symboles utilisés pour le dessin soient _configurables_ 

Quelques exemples d'appels :

```python
>>> moitie(5, 'X', 'O')
['OXXXO', 'XOXOX']

>>> moitie(6, '.', '*')
['*....*', '.*..*.', '..**..']
```

Dès lors le dessin va consister à agréger, concaténer une première moitié (la liste fournie par cette fonction) avec la même mais prise à l'envers en y intercalant éventuellement la ligne centrale puis à imprimer toutes ces lignes. 

Et d'abord la fonction qui produit une liste contenant la ligne centrale ou rien :

```python
def milieu(n, croix, rond):
    if n%2:
        return ['{0}{1}{0}'.format(croix * (n//2), rond)]
    else:
        return []
```

Pour la liste inversée, je vous laisse réfléchir à comment vous le feriez. Ici le concept de slicing de python est bien pratique mais n'est pas la seule solution possible. 

```python
>>> l = [1,2,3,4,5]
>>> l[1:3]
[2,3]
>>> l[:]
[1,2,3,4,5]
>>> l[::2]
[1,3,5]
>>> l[::-1]
[5,4,3,2,1]
```

Notre fonction de dessin peut soit retourner une très grande chaîne de caractères (constituée des lignes de notre dessin séparées par des retours à la ligne, des '\n'), soit une liste. Comment nous réalisons cette chaîne de caractères n'est pas le plus important. 

```python
def dessin(n, croix, rond):
    l1 = moitie(n, croix, rond)
    l2 = l1[::-1]
    lm = milieu(n, croix, rond)
    return '\n'.join(l1+lm+l2) 
```

Et notre programme principal, utilisant la fonction dessin :

```python
size = int(input('Dimension du carré : '))
croix = input('Le motif principal : ')
rond = input('Le motif secondaire : ')
print(dessin(size, croix, rond))
```

## Conclusion

Un programme informatique résoud un problème pour un utilisateur, pour des utilisateurs. Nous ne pouvons pas donner à cet utilisateur une fonction en lui disant : _"voilà il suffit de la lancer dans un interprèteur en lui passant les valeurs de ton choix"_. Un programme aboutit, utilisable, possède des entrées et imprime des résultats. C'est une réalité et ma vision de la pensée informatique que j'ai essayé de donner ici n'entre pas en conflit avec cette réalité.

Bien sûr enseigner ces différents concepts n'est pas aisé et il est normal pour un débutant de confondre les entrées / sorties d'un programme et les entrées / sorties d'une fonction. Je ne crois pas que la solution consiste à cacher l'existence d'une des deux notions.




[//]: # (LINKS)

[1]:https://openclassrooms.com/fr/courses/4262331-demarrez-votre-projet-avec-python/4263566-creez-votre-premier-script
[2]:https://fr.wikipedia.org/wiki/Probl%C3%A8me_de_l%27arr%C3%AAt
[3]:https://docs.python.org/fr/3.5/library/string.html#formatstrings
[4]:https://fr.wikipedia.org/wiki/Mod%C3%A8le-vue-contr%C3%B4leur