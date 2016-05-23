import sqlite3

conn = sqlite3.connect('base.db')
c = conn.cursor()


t = ('RHAT',)
c.execute('insert into FROM stocks WHERE symbol=?', t)
print (c.fetchone())