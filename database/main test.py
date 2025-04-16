from database.studente_DAO import getAllStudenti
from database.corso_DAO import getAllCorsi
from database.Iscrizioni_DAO import getAllIscrizioni

studenti = getAllStudenti()
corsi = getAllCorsi()
iscrizioni = getAllIscrizioni()

for i in studenti.keys():
    print(studenti[i])

for corso in corsi.keys():
    print(corsi[corso])

for iscrizione in iscrizioni:
    print(iscrizione)
