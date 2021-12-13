class Classe:
    def __init__(self, dict_eleve, devoirs):
        self.dict_eleve = dict_eleve
        self.list_devoir = devoirs


    def __repr__(self):
        return str(self.dict_eleve)

    def add(self, name):
        self.dict_eleve[name] = Eleve(name)
        for devoir in self.list_devoir:
            self.list_devoir.append({self.name : None})

    def delete(self, name):
        del self.dict_eleve[name]

    def search(self, name):
        return self.dict_eleve.get(name, None)

    def moyenne(self, trim = None, eleve = None, devoir = None):
        moyenne = 0
        div = 0
        for dev in self.list_devoir:
            for eleve_note in dev.dict_eleve_note.items():
                if devoir is None or dev.index == devoir:
                    if trim is None or dev.trim == trim:
                        if eleve is None or eleve_note[0] == eleve:
                            if eleve_note[1] is not None:
                                moyenne += eleve_note[1]
                                div += 1

        if div != 0:
            return moyenne / div
        return None

    def liste_resultats(self):
        l_note = []
        for eleve in self.dict_eleve.items():
            l_note.append(self.moyenne(eleve=eleve[0]))
        return(sorted(l_note))

    def liste_resultats_inv(self):
        return self.liste_resultats()[::-1]


class Eleve:
    def __init__(self, name):
        self.name = name
        self.age = 254

    def __repr__(self):
        return str({"nom" : self.name})

    def print_age(self):
        print(self.age)

    def other(self):
        self.print_age()



class Devoir:
    def __init__(self, index, trim, dict_eleve_note):
        self.index = index
        self.trim = trim
        self.dict_eleve_note = dict_eleve_note

    def __repr__(self):
        return str({"trimestre" : self.trim, "eleve : note" : self.dict_eleve_note})

dev = Devoir(0, 1, {"henri" : 12, "mich" : 17})
classe = Classe({"henri" : Eleve("henri"), "mich" : Eleve("mich")}, [dev, Devoir(1, 1, {"henri" : 15, "mich" : 19})])
