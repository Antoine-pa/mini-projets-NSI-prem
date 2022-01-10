# *projet bash :*

## a) Créer 100 répertoires numérotés de 1 à 100 :

#### commande pour créer un dossier :

```sh
mkdir dossier
```
<img src="https://raw.githubusercontent.com/Antoine-pa/mini-projets-NSI/master/bash/images/mkdir_command.png" />

#### l'équivalent du range python en bash :
```
range(1, 6) = seq 1 5
```
<img src="https://raw.githubusercontent.com/Antoine-pa/mini-projets-NSI/master/bash/images/seq_command.png" />

#### commande pour créer les 100 dossiers :

```sh
mkdir `seq 1 100`
```
<img src="https://raw.githubusercontent.com/Antoine-pa/mini-projets-NSI/master/bash/images/mkdir_100.png" />

## b) Afficher le nombre de ligne où apparaît un mot :

#### création d'un fichier contenant des mots :

```sh
echo "nsi
autres mots
blablablansi
encorensi
nsiencore
autre
choses" > texte.txt
```

<img src="https://raw.githubusercontent.com/Antoine-pa/mini-projets-NSI/master/bash/images/texte_txt.png" />

#### commande d'affichage d'un contenu de fichier :

```sh
cat texte.txt
```

<img src="https://raw.githubusercontent.com/Antoine-pa/mini-projets-NSI/master/bash/images/cat_command.png" />

#### commande grep :
La commande grep permet de faire de la recherche de chaine de caractères
L’utilisation générale de la commande grep se fait de la manière suivante :

```sh
grep [options] "recherche" [chaine de caractère ou fichier]
```

avec :
- "recherche" la chaine de caractère à chercher
- [chaine de caractère ou fichier] le document sur lequel portera la rechercher
- [options] des options pour l'utilisation de la commande grep mais on ne l'utilisera pas

exemple :

<img src="https://raw.githubusercontent.com/Antoine-pa/mini-projets-NSI/master/bash/images/grep_command.png" />

#### commande word count (wc) :

la commande wc est une commande qui permet de compter le nombre de lignes, mots et d'autres informations sur un fichier ou une chaine de caractère
L’utilisation générale de la commande wc se fait de la manière suivante :

```sh
wc [options] [chaine de caractère ou fichier]
```

avec :
- [chaine de caractère ou fichier] le document sur lequel portera la commande
- [options] les options pour l'utilisation de la commande wc. One utilisera l'option -l pour compter le nombre de ligne d'un document ou d'une chaine de caractère

exemple :

<img src="https://raw.githubusercontent.com/Antoine-pa/mini-projets-NSI/master/bash/images/wc_command.png" />

#### assemblage des commandes vus avant :

La commande suivante va donc retourner les lignes dans lequelles aparaissent le mot "nsi" dans le fichier texte.txt (grep) et va compter ce nombre de ligne (wc)

```sh
grep "nsi" texte.txt | wc -l
```

<img src="https://raw.githubusercontent.com/Antoine-pa/mini-projets-NSI/master/bash/images/count_nsi.png" />

## c) Afficher le nombre de fichier ou dossier contenue dans un dossier :

#### commande tree :

La commande `tree` permet d'afficher un arbre de l'arborescence d'un dossier.

Pour cette question j'ai créé quelque dossier et fichier qu'on va afficher avec la commande `tree` :

<img src="https://raw.githubusercontent.com/Antoine-pa/mini-projets-NSI/master/bash/images/tree_command.png" />

La solution au problème posé serait de faire comme pour la question précédente et de compter le nombre de ligne de la sortie de la commande `tree `puisque qu'une ligne est égale à une fichier/dossier. Mais la sortie de la commande `tree` possède 3 lignes de trop qui nous sont inutiles. Il faudrait donc soustraire 3 à la sortie de la commande `tree | wc -l`.

Bash est un langage un peu complexe pour l'execution de calculs. La solution pour palier à ce problème est la commande `expr`

#### commande expr :

La commande `expr` est une commande qui permet d'évaluer une expression donc dans notre cas, un calul entre une sortie d'une commande et un nombre (3)

utilisation :

```sh
expr `tree | wc -l` - 3
```

<img src="https://raw.githubusercontent.com/Antoine-pa/mini-projets-NSI/master/bash/images/question_c.png" />

## d) Créer une liste de répertoire contenu dans un fichier texte :

On utilise le même système qu'à la question a mais cette fois en utilisant le contenu d'un fichier. On va réutiliser le fichier texte.txt de la question b :

```sh
mkdir `cat texte.txt`
```

<img src="https://raw.githubusercontent.com/Antoine-pa/mini-projets-NSI/master/bash/images/question_d.png" />
