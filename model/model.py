from database.Iscrizioni_DAO import getAllIscrizioni
from database.studente_DAO import getAllStudenti
from database.corso_DAO import getAllCorsi

class Model:
    def __init__(self):
        self._studenti = getAllStudenti()
        self._corsi = getAllCorsi()
        self._iscrizioni = getAllIscrizioni()

    def cercaIscritti(self, corso):
        output = []
        if corso is None:
            return None
        for iscrizione in self._iscrizioni:
            if iscrizione._codins == corso._codins:
                output.append(iscrizione)
        return output

    def cercaStudente(self, matricola):
        try:
            studente = self._studenti[matricola]
            return studente
        except KeyError:
            return None

    def cercaCorsi(self, matricola):
        output = []
        for iscrizione in self._iscrizioni:
            if iscrizione._matricola == matricola:
                output.append(self._corsi[iscrizione._codins])
        return output
