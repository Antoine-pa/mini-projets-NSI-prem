# *projet bash :*

## a) Crérer 100 répertoires numérotés de 1 à 100 :

#### commande pour créer un dossier :

```sh
mkdir dossier
```
<img src="https://raw.githubusercontent.com/Antoine-pa/mini-projets-NSI/master/mkdir_command.PNG" />

#### l'équivalent du range python en bash :
```
range(1, 6) = seq 1 5
```
<img src="https://raw.githubusercontent.com/Antoine-pa/mini-projets-NSI/master/seq_command.PNG" />

#### commande pour créer les 100 dossiers :

```sh
mkdir `seq 1 100`
```
<img src="https://raw.githubusercontent.com/Antoine-pa/mini-projets-NSI/master/mkdir_100.PNG" />

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

<img src="https://raw.githubusercontent.com/Antoine-pa/mini-projets-NSI/master/texte_txt.PNG" />

#### commande d'affichage d'un contenu de fichier :

```sh
cat texte.txt
```

<img src="https://raw.githubusercontent.com/Antoine-pa/mini-projets-NSI/master/cat_command.PNG" />

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
<image exemple echo "" > fichier\ngrep "" fichier>

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

<img exemple wc>

## c) Afficher le nombre de fichier ou dossier contenue dans un dossier :

## d) Créer une liste de répertoire contenu dans un fichier texte :
