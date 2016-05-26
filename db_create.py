import sqlite3

db = sqlite3.connect('base.db')
c = db.cursor()


c.execute('''
    DROP TABLE IF EXISTS devices_list
''')

c.execute('''
    DROP TABLE IF EXISTS data
''')
db.commit()


data_types = [(0,'temperature'), (1, 'humidity'), (2, 'speed_fun'), (3,'mode'), (4,'threshold')]

c.execute('''
    CREATE TABLE IF NOT EXISTS data_types(id INTEGER PRIMARY KEY, name TEXT unique)
''')
c.executemany('''INSERT INTO data_types(id, name) VALUES(?,?)''', data_types)

c.execute('''
    CREATE TABLE IF NOT EXISTS devices_list(id INTEGER PRIMARY KEY, slave_id INTEGER unique, SerialNumber text)
''')

c.execute('''
    CREATE TABLE IF NOT EXISTS data(id INTEGER PRIMARY KEY, slave_id INTEGER, data_type TEXT,
                       data TEXT, datetime NOT NULL DEFAULT CURRENT_TIMESTAMP)
''')

db.commit()