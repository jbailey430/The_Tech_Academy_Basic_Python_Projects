

import sqlite3
connection = sqlite3.connect("test_database.db")

c = connection.cursor()
c.execute("INSERT INTO People VALUES('Ron', 'Obvious', 42)")

connection.commit()
connection.close()

with sqlite3.connect("test_database.db") as connection:
    c = connection.cursor()
    c.executescript("""DROP TABLE IF EXISTS People;
                    CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT);
                    INSERT INTO People VALUES('Ron', 'Obvious', '42');
                    """)
peopleValues = (('Luigi', 'Vercotti', 43 ), ('Arthur', 'Belling', 28))
c.executemany("INSERT INTO People VALUES(?, ?, ?)", peopleValues)

# get personal data from user
firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")
age = int(input("Enter your age: "))
personData = (firstName, lastName, age)


# execute insert statement for supplied person data
with sqlite3.connect('test_database.db') as connection:
    c = connection.cursor()
    line = ("INSERT INTO People VALUES (?, ?, ?)", personData)
    
c.execute("UPDATE People SET Age=? WHERE FirstName=? AND LastName=?",
          (45, 'Luigi', 'Vercotti'))
