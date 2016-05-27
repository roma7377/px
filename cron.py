import sqlite3
import minimalmodbus
import db_create

db = sqlite3.connect('base.db')
c = db.cursor()

#получаем список слейвов


c.execute('''INSERT INTO devices_list(slave_id,SerialNumber)
                  VALUES(?,?)''', (5,'12345'))
db.commit()

c.execute('''INSERT INTO devices_list(slave_id,SerialNumber)
                  VALUES(?,?)''', (1, '67890'))
db.commit()

c.execute('''SELECT slave_id FROM devices_list''')

slaves_list = c.fetchall()
print(slaves_list)

for i in slaves_list:
    instrument = minimalmodbus.Instrument('/dev/ttyUSB0', i[0])  # port name, slave address (in decimal)
    #print(instrument.read_registers(0,1))
    try:
        d = instrument.read_registers(0,10)
    except:
        print('read slave #'+str(i[0])+' error')

    data = [(5,'temperature', d[0]/100),
            (5, 'humidity', d[1]/100),
            (5, 'speed_fun', d[2])]




    c.executemany('''INSERT INTO data(slave_id, data_type,data)
                      VALUES(?,?,?)''', data)
    db.commit()



db.close()

def slave_read_info(port,id):
    instrument = minimalmodbus.Instrument(port, id)
    n = instrument.read_register(0)
    serial_number = instrument.read_string(1,5)
    sw_version = instrument.read_string(6, 2)
    n = instrument.read_registers(21,2*n)
