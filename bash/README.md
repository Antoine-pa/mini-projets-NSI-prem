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

#### on commence d'abord par créer un fichier contenant des mots :

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

## c) Afficher le nombre de fichier ou dossier contenue dans un dossier :

## d) Créer une liste de répertoire contenu dans un fichier texte :
