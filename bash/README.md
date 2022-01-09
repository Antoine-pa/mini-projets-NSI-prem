# *projet bash :*

## a) Crérer 100 répertoires numérotés de 1 à 100 :

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

## d) Créer une liste de répertoire contenu dans un fichier texte :
