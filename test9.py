
import sqlite3


conn = sqlite3.connect ('test3.db')

fileList = ('information.docx','Hello.txt','myImage.png',\
'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_file( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        file_name TEXT \
        )")
    conn.commit()



for file in fileList:
    if (file.endswith('.txt')):
        print(file)
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_file(file_name) VALUES (?)", \
                (file,))
            conn.commit()


