# Add whatever it is needed to interface with the DB Table corso

from database.DB_connect import get_connection
from model.Iscrizione import Iscrizione

def getAllIscrizioni():
    con = get_connection()
    cursor = con.cursor()
    query = "SELECT * FROM iscrizione"
    cursor.execute(query)
    results = cursor.fetchall()
    iscrizioni = []
    for row in results:
        iscrizione = Iscrizione(row[0], row[1])
        iscrizioni.append(iscrizione)
    cursor.close()
    con.close()
    return iscrizioni
