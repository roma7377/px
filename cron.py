import sqlite3
import minimalmodbus

instrument = minimalmodbus.Instrument('COM88', 5)  # port name, slave address (in decimal)

#print(instrument.read_registers(0,1))

print(instrument.read_register(0))

'''
conn = sqlite3.connect('base.db')
c = conn.cursor()


t = ('RHAT',)
c.execute('insert into FROM stocks WHERE symbol=?', t)
print (c.fetchone())

2016/05/24 11:22:23  >>> 05 03 00 00 00 0A C4 49
2016/05/24 11:22:23  < 05 03 14 09 24 15 AE 00 00 00 02 00 46 00 00 00 00 00 00 00 00 00 00 73 B9
'''