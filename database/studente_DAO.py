# Add whatever it is needed to interface with the DB Table studente

from database.DB_connect import get_connection
from model.studente import Studente

def getAllStudenti():
    con = get_connection()
    cursor = con.cursor()
    query = "SELECT * FROM studente"
    cursor.execute(query)
    results = cursor.fetchall()
    studenti = {}
    for row in results:
        studente = Studente(row[0], row[1], row[2], row[3])
        studenti[row[0]] = studente
    cursor.close()
    con.close()
    return studenti
