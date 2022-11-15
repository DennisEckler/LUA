import sqlite3
import csv

def importTable(artikelnummer, bezeichnung, anzahl, kategorie, lieferant, ekpreis, vkpreis, storage_id):
    try:
        sqliteConnection = sqlite3.connect('db.sqlite3')
        cursor = sqliteConnection.cursor()
        print("Connected to SQlite")
        data = (artikelnummer, bezeichnung, anzahl, kategorie, lieferant, ekpreis, vkpreis, storage_id)
        cursor.execute("""Insert INTO LagerApp_Article (artikelnummer, bezeichnung, anzahl, kategorie, lieferant, ekpreis, vkpreis, storage_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?);""", data)
        sqliteConnection.commit()
        print('Insert Sucsessfull')

    except sqlite3.Error as error:
        print("Failed to insert", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("SQLite Connection closed")

def initalimport():
    with open('Artikel.csv', newline='') as file:
        reader = csv.reader(file, delimiter=';', quotechar='|')
        for row in reader:
            importTable(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])

initalimport()
