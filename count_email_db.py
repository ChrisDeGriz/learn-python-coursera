import sqlite3
import re

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if line.startswith('From: '):
        email_org = re.findall('.+@(.+\..+)', line)[0]
        cur.execute('SELECT count FROM Counts WHERE org = ? ', (email_org,))
        row = cur.fetchone()
        if row is None:
            cur.execute('''INSERT INTO Counts (org, count)
                    VALUES (?, 1)''', (email_org,))
        else:
            cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                        (email_org,))
        conn.commit()

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
