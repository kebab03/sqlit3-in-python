import sqlite3

# Database connection
conn = sqlite3.connect(r'C:\Users\Sharif\Documents\workFinaly\users.db')
cursor = conn.cursor()

# Fetch and print data before deletion
res = cursor.execute("SELECT IDDD, NMA , data FROM EVT")
dat_before = res.fetchall()
print("---------------------dat (before deletion)----------------------------")
print(dat_before)

# Delete rows where IDDD = 4
'''cursor.execute("DELETE FROM EVT WHERE IDDD = 7")

# Commit the changes to the database
conn.commit()

# Fetch and print data after deletion
res = cursor.execute("SELECT IDDD, NMA FROM EVT")
dat_after = res.fetchall()
print("---------------------dat (after deletion)----------------------------")
print(dat_after)
'''

cursor.execute("DELETE FROM EVT WHERE dat = '2023-11-09' AND userId = 'admin'")
conn.commit()

# Fetch and print data after deletion
res = cursor.execute("SELECT IDDD, NMA FROM EVT")
dat_after = res.fetchall()
print("---------------------dat (after deletion)----------------------------")
print(dat_after)