import sqlite3
from datetime import datetime
tday = datetime.now().date()
print(tday, type(tday.__str__()))
test1= "stomer"
None.get_detail()
con = sqlite3.connect("dvd_store_mng.db")
cursor = con.cursor()
query = "SELECT * FROM copies_dvd"
cursor.execute(query)
test = cursor.fetchall()
print(test)
lis1 = [12,"test",None]
print(len(lis1))
#cursor.execute("Insert into copies_dvd values (?,?,?)",lis1)

#con.commit()