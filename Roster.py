import sqlite3

connection = sqlite3.connect("Roster.db")
c = connection.cursor()

with sqlite3.connect("Roster.db") as connection:
    c = connection.cursor()
    c.executescript("""DROP TABLE IF EXISTS Roster;
                    CREATE TABLE Roster(Name TEXT, Species TEXT, IQ INT);
                    INSERT INTO Roster VALUES('Jean-Baptiste Zorg','Human','122')('Korben Dallas','Meat Popsicle','100')('Ak'not','Mangalore','-5');
                    """)
connection.commit()
connection.close()
