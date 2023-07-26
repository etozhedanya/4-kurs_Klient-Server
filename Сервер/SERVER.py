import sqlite3

from flask import Flask, request

app = Flask(__name__)


@app.route("/myfunction", methods=['POST']) #Создаем функцию
def myfunction(): #Описываем
    conn = sqlite3.connect('GOST.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM Clients')
    result = cur.fetchall()
    conn.commit()
    conn.close()

    return {'result': result} # Передаем значение клиенту


@app.route("/myfunction2", methods=['POST'])
def myfunction2():
    conn = sqlite3.connect('GOST.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM Sotrudniki')
    result = cur.fetchall()
    conn.commit()
    conn.close()

    return {'result': result}


@app.route("/myfunction3", methods=['POST'])
def myfunction3():
    conn = sqlite3.connect('GOST.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM Smena')
    result = cur.fetchall()
    conn.commit()
    conn.close()

    return {'result': result}


@app.route("/myfunction4", methods=['POST'])
def myfunction4():
    conn = sqlite3.connect('GOST.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM Nomera')
    result = cur.fetchall()
    conn.commit()
    conn.close()


    return {'result': result}

@app.route("/myfunction5", methods=['POST'])
def myfunction5():
    conn = sqlite3.connect('GOST.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM Zhurnal')
    result = cur.fetchall()
    conn.commit()
    conn.close()

    return {'result': result}

@app.route("/zaprs1", methods=['POST'])
def zaprs1():
    con = sqlite3.connect('GOST.db')
    rest = request.json['text']
    rest = rest.split('-')

    zapr = rest[2]
    cmbx = rest[0]
    cmbx2 = rest[1]

    if cmbx == 'ID Клиента':
        cur = con.cursor()
        sqlquery = f"SELECT * FROM Clients Where IdCl {cmbx2} {zapr}"
        result = cur.execute(sqlquery)
        con.commit()
        itog = cur.fetchall()

    elif cmbx == 'ФИО':
        cur = con.cursor()
        sqlquery = f"SELECT * FROM Clients Where FIO LIKE '{zapr}%'"
        result = cur.execute(sqlquery)
        con.commit()
        itog = cur.fetchall()
        
    elif cmbx == 'Возраст':
        cur = con.cursor()
        sqlquery = f"SELECT * FROM Clients Where Old {cmbx2} {zapr}"
        result = cur.execute(sqlquery)
        con.commit()
        itog = cur.fetchall()
        
    con.close()

    return {'result': itog}


@app.route("/zaprs2", methods=['POST'])
def zaprs2():
    con = sqlite3.connect('GOST.db')
    rest = request.json['text']
    rest = rest.split('-')

    zapr = rest[2]
    cmbx = rest[0]
    cmbx2 = rest[1]

    if cmbx == 'ID Сотрудника':
        cur = con.cursor()
        sqlquery = f"SELECT * FROM Sotrudniki Where IdSotr {cmbx2} {zapr}"
        result = cur.execute(sqlquery)
        con.commit()
        itog = cur.fetchall()

    elif cmbx == 'ФИО':
        cur = con.cursor()
        sqlquery = f"SELECT * FROM Sotrudniki Where FIO LIKE '{zapr}%'"
        result = cur.execute(sqlquery)
        con.commit()
        itog = cur.fetchall()
        
    elif cmbx == 'Возраст':
        cur = con.cursor()
        sqlquery = f"SELECT * FROM Sotrudniki Where Old {cmbx2} {zapr}"
        result = cur.execute(sqlquery)
        con.commit()
        itog = cur.fetchall()

    elif cmbx == 'Должность':
        cur = con.cursor()
        sqlquery = f"SELECT * FROM Sotrudniki Where Dolzhn LIKE '{zapr}%'"
        result = cur.execute(sqlquery)
        con.commit()
        itog = cur.fetchall()
        
    elif cmbx == 'Зарплата':
        cur = con.cursor()
        sqlquery = f"SELECT * FROM Sotrudniki Where Zarplata {cmbx2} {zapr}"
        result = cur.execute(sqlquery)
        con.commit()
        itog = cur.fetchall()
        
    con.close()

    return {'result': itog}

@app.route("/zaprs3", methods=['POST'])
def zaprs3():
    con = sqlite3.connect('GOST.db')
    rest = request.json['text']
    rest = rest.split('-')

    zapr = rest[2]
    cmbx = rest[0]
    cmbx2 = rest[1]

    if cmbx == 'ID Смены':
        cur = con.cursor()
        sqlquery = f"SELECT * FROM Smena Where IdSmen {cmbx2} {zapr}"
        result = cur.execute(sqlquery)
        con.commit()
        itog = cur.fetchall()
        
    elif cmbx == 'ID Сотрудника':
        cur = con.cursor()
        sqlquery = f"SELECT * FROM Smena Where IdSot {cmbx2} {zapr}"
        result = cur.execute(sqlquery)
        con.commit()
        itog = cur.fetchall()
        
    con.close()

    return {'result': itog}

@app.route("/zaprs4", methods=['POST'])
def zaprs4():
    con = sqlite3.connect('GOST.db')
    rest = request.json['text']
    rest = rest.split('-')

    zapr = rest[2]
    cmbx = rest[0]
    cmbx2 = rest[1]

    if cmbx == 'ID Номера':
        cur = con.cursor()
        sqlquery = f"SELECT * FROM Nomera Where IdNom {cmbx2} {zapr}"
        result = cur.execute(sqlquery)
        con.commit()
        itog = cur.fetchall()
        
    elif cmbx == 'Стоимость':
        cur = con.cursor()
        sqlquery = f"SELECT * FROM Nomera Where Price {cmbx2} {zapr}"
        result = cur.execute(sqlquery)
        con.commit()
        itog = cur.fetchall()

    elif cmbx == 'Класс':
        cur = con.cursor()
        sqlquery = f"SELECT * FROM Nomera Where Class LIKE '{zapr}%'"
        result = cur.execute(sqlquery)
        con.commit()
        itog = cur.fetchall()
        
    con.close()

    return {'result': itog}

@app.route("/zaprs5", methods=['POST'])
def zaprs5():
    con = sqlite3.connect('GOST.db')
    rest = request.json['text']
    rest = rest.split('-')

    zapr = rest[2]
    cmbx = rest[0]
    cmbx2 = rest[1]

    if cmbx == 'ID Записи':
        cur = con.cursor()
        sqlquery = f"SELECT * FROM Zhurnal Where IdZap {cmbx2} {zapr}"
        result = cur.execute(sqlquery)
        con.commit()
        itog = cur.fetchall()
        
    elif cmbx == 'ID Клиента':
        cur = con.cursor()
        sqlquery = f"SELECT * FROM Zhurnal Where IdCl {cmbx2} {zapr}"
        result = cur.execute(sqlquery)
        con.commit()
        itog = cur.fetchall()

    elif cmbx == 'ID Номера':
        cur = con.cursor()
        sqlquery = f"SELECT * FROM Zhurnal Where IdNom {cmbx2} {zapr}"
        result = cur.execute(sqlquery)
        con.commit()
        itog = cur.fetchall()

    elif cmbx == 'ID Смены':
        cur = con.cursor()
        sqlquery = f"SELECT * FROM Zhurnal Where IdSmen {cmbx2} {zapr}"
        result = cur.execute(sqlquery)
        con.commit()
        itog = cur.fetchall()

    elif cmbx == 'Дата заезда':
        cur = con.cursor()
        sqlquery = f"SELECT * FROM Zhurnal Where DateZaezd LIKE '{zapr}%'"
        result = cur.execute(sqlquery)
        con.commit()
        itog = cur.fetchall()

    elif cmbx == 'Дата выезда':
        cur = con.cursor()
        sqlquery = f"SELECT * FROM Zhurnal Where DateViezd LIKE '{zapr}%'"
        result = cur.execute(sqlquery)
        con.commit()
        itog = cur.fetchall()
        
    con.close()

    return {'result': itog}

@app.route("/dobavv1", methods=['POST'])
def dobavv1():
    conn = sqlite3.connect('GOST.db')
    cur = conn.cursor()

    rest = request.json['text']
    rest = rest.split('-')

    idcl = rest[0]
    fio = rest[1]
    old = rest[2]
    
    cur.execute(f"INSERT INTO Clients VALUES({idcl},'{fio}', {old})")
    result = cur.fetchall()
    conn.commit()
    conn.close()


    return {'result': result}

@app.route("/ubavv1", methods=['POST'])
def ubavv1():
    conn = sqlite3.connect('GOST.db')
    cur = conn.cursor()

    rest = request.json['text']

    idcl = rest
    
    cur.execute(f"DELETE FROM Clients WHERE IdCl = {idcl}")
    result = cur.fetchall()
    conn.commit()
    conn.close()


    return {'result': result}

@app.route("/izmavv1", methods=['POST'])
def izmavv1():
    conn = sqlite3.connect('GOST.db')
    cur = conn.cursor()

    rest = request.json['text']
    rest = rest.split('-')

    idcl = rest[0]
    cmbx = rest[1]
    upd = rest[2]

    if cmbx == 'ФИО':
        cur.execute(f"UPDATE Clients SET FIO = '{upd}' WHERE IdCl = {idcl}")
    elif cmbx == 'Возраст':
        cur.execute(f"UPDATE Clients SET Old = {upd} WHERE IdCl = {idcl}")
    result = cur.fetchall()
    conn.commit()
    conn.close()


    return {'result': result}


@app.route("/dobavv2", methods=['POST'])
def dobavv2():
    conn = sqlite3.connect('GOST.db')
    cur = conn.cursor()

    rest = request.json['text']
    rest = rest.split('-')

    idnom = rest[0]
    clas = rest[1]
    price = rest[2]
    
    cur.execute(f"INSERT INTO Nomera VALUES({idnom},'{clas}', {price})")
    result = cur.fetchall()
    conn.commit()
    conn.close()


    return {'result': result}

@app.route("/ubavv2", methods=['POST'])
def ubavv2():
    conn = sqlite3.connect('GOST.db')
    cur = conn.cursor()

    rest = request.json['text']

    idnom = rest
    
    cur.execute(f"DELETE FROM Nomera WHERE IdNom = {idnom}")
    result = cur.fetchall()
    conn.commit()
    conn.close()


    return {'result': result}

@app.route("/izmavv2", methods=['POST'])
def izmavv2():
    conn = sqlite3.connect('GOST.db')
    cur = conn.cursor()

    rest = request.json['text']
    rest = rest.split('-')

    idnom = rest[0]
    cmbx = rest[1]
    upd = rest[2]

    if cmbx == 'Класс':
        cur.execute(f"UPDATE Nomera SET Class = '{upd}' WHERE IdNom = {idnom}")
    elif cmbx == 'Стоимость':
        cur.execute(f"UPDATE Nomera SET Price = {upd} WHERE IdNom = {idnom}")
    result = cur.fetchall()
    conn.commit()
    conn.close()


    return {'result': result}

@app.route("/dobavv3", methods=['POST'])
def dobavv3():
    conn = sqlite3.connect('GOST.db')
    cur = conn.cursor()

    rest = request.json['text']
    rest = rest.split('-')

    idnom = rest[0]
    clas = rest[1]
    
    cur.execute(f"INSERT INTO Smena VALUES({idnom},{clas})")
    result = cur.fetchall()
    conn.commit()
    conn.close()


    return {'result': result}

@app.route("/ubavv3", methods=['POST'])
def ubavv3():
    conn = sqlite3.connect('GOST.db')
    cur = conn.cursor()

    rest = request.json['text']
    rest = rest.split('-')

    idnom = rest[0]
    clas = rest[1]
    
    cur.execute(f"DELETE FROM Smena WHERE IdSmen = {idnom} and IdSot = {clas}")
    result = cur.fetchall()
    conn.commit()
    conn.close()


    return {'result': result}

@app.route("/dobavv4", methods=['POST'])
def dobavv4():
    conn = sqlite3.connect('GOST.db')
    cur = conn.cursor()

    rest = request.json['text']
    rest = rest.split('-')
    
    ids = rest[0]
    fio = rest[1]
    gen = rest[2]
    old = rest[3]
    zv = rest[4]
    idot = rest[5]
    
    cur.execute(f"INSERT INTO Zhurnal VALUES({ids},{fio},{gen},{old},'{zv}','{idot}')")
    result = cur.fetchall()
    conn.commit()
    conn.close()


    return {'result': result}

@app.route("/ubavv4", methods=['POST'])
def ubavv4():
    conn = sqlite3.connect('GOST.db')
    cur = conn.cursor()

    rest = request.json['text']

    idnom = rest
    
    cur.execute(f"DELETE FROM Zhurnal WHERE IdZap = {idnom}")
    result = cur.fetchall()
    conn.commit()
    conn.close()


    return {'result': result}

@app.route("/izmavv4", methods=['POST'])
def izmavv4():
    conn = sqlite3.connect('GOST.db')
    cur = conn.cursor()

    rest = request.json['text']
    rest = rest.split('-')

    idnom = rest[0]
    cmbx = rest[1]
    upd = rest[2]

    if cmbx == 'ID Клиента':
        cur.execute(f"UPDATE Zhurnal SET IdCl = {upd} WHERE IdZap = {idnom}")
    elif cmbx == 'ID Номера':
        cur.execute(f"UPDATE Zhurnal SET IdNom = {upd} WHERE IdZap = {idnom}")
    elif cmbx == 'ID Смены':
        cur.execute(f"UPDATE Zhurnal SET IdSmen = {upd} WHERE IdZap = {idnom}")
    elif cmbx == 'Дата заезда':
        cur.execute(f"UPDATE Zhurnal SET DateZaezd = '{upd}' WHERE IdZap = {idnom}")
    elif cmbx == 'Дата выезда':
        cur.execute(f"UPDATE Zhurnal SET DateViezd = '{upd}' WHERE IdZap = {idnom}")
    result = cur.fetchall()
    conn.commit()
    conn.close()


    return {'result': result}

@app.route("/dobavv5", methods=['POST'])
def dobavv5():
    conn = sqlite3.connect('GOST.db')
    cur = conn.cursor()

    rest = request.json['text']
    rest = rest.split('-')
    
    ids = rest[0]
    fio = rest[1]
    gen = rest[2]
    old = rest[3]
    zv = rest[4]
    
    cur.execute(f"INSERT INTO Sotrudniki VALUES({ids},'{fio}',{gen},'{old}',{zv})")
    result = cur.fetchall()
    conn.commit()
    conn.close()


    return {'result': result}

@app.route("/ubavv5", methods=['POST'])
def ubavv5():
    conn = sqlite3.connect('GOST.db')
    cur = conn.cursor()

    rest = request.json['text']

    idnom = rest
    
    cur.execute(f"DELETE FROM Sotrudniki WHERE IdSotr = {idnom}")
    result = cur.fetchall()
    conn.commit()
    conn.close()


    return {'result': result}

@app.route("/izmavv5", methods=['POST'])
def izmavv5():
    conn = sqlite3.connect('GOST.db')
    cur = conn.cursor()

    rest = request.json['text']
    rest = rest.split('-')

    idnom = rest[0]
    cmbx = rest[1]
    upd = rest[2]

    if cmbx == 'ФИО':
        cur.execute(f"UPDATE Sotrudniki SET FIO = '{upd}' WHERE IdSotr = {idnom}")
    elif cmbx == 'Возраст':
        cur.execute(f"UPDATE Sotrudniki SET Old = {upd} WHERE IdSotr = {idnom}")
    elif cmbx == 'Должность':
        cur.execute(f"UPDATE Sotrudniki SET Dolzhn = '{upd}' WHERE IdSotr = {idnom}")
    elif cmbx == 'Зарплата':
        cur.execute(f"UPDATE Sotrudniki SET Zarplata = {upd} WHERE IdSotr = {idnom}")

    result = cur.fetchall()
    conn.commit()
    conn.close()


    return {'result': result}

@app.route("/udal", methods=['POST'])
def udal():
    conn = sqlite3.connect('GOST.db')
    cur = conn.cursor()
    rest = request.json['text'] # Принимаем значение с клиента
    cur.execute('DELETE FROM klient WHERE kod_klienta = ?', (rest,))
    cur.execute('SELECT * FROM klient')
    result = cur.fetchall()
    conn.commit()
    conn.close()

    return {'result': result}


@app.route("/udal2", methods=['POST'])
def udal2():
    conn = sqlite3.connect('fir.db')
    cur = conn.cursor()
    rest = request.json['text']
    cur.execute('DELETE FROM bron WHERE "nomer broni" = ?', (rest,))
    cur.execute('SELECT * FROM bron')
    result = cur.fetchall()
    conn.commit()
    conn.close()

    return {'result': result}


@app.route("/udal3", methods=['POST'])
def udal3():
    conn = sqlite3.connect('fir.db')
    cur = conn.cursor()
    rest = request.json['text']
    cur.execute('DELETE FROM nomer WHERE kod_nomera = ?', (rest,))
    cur.execute('SELECT * FROM nomer')
    result = cur.fetchall()
    conn.commit()
    conn.close()

    return {'result': result}


@app.route("/udal4", methods=['POST'])
def udal4():
    conn = sqlite3.connect('fir.db')
    cur = conn.cursor()
    rest = request.json['text']
    cur.execute('DELETE FROM oplata WHERE kod_klienta = ?', (rest,))
    cur.execute('SELECT * FROM oplata')
    result = cur.fetchall()
    conn.commit()
    conn.close()

    return {'result': result}


@app.route("/dobav", methods=['POST'])
def dobav():
    conn = sqlite3.connect('fir.db')
    cur = conn.cursor()
    rest = request.json['text']
    pp = []

    rest = rest.split(',')
    for i in rest:
        pp.append(i)
    pp = tuple(pp)

    cur.execute(
        'INSERT INTO klient VALUES (?, ?, ?)',
        pp)
    cur.execute('SELECT * FROM klient')
    result = cur.fetchall()
    print(result)
    conn.commit()
    conn.close()
    return {'result': result}


@app.route("/dobav2", methods=['POST'])
def dobav2():
    conn = sqlite3.connect('fir.db')
    cur = conn.cursor()
    rest = request.json['text']
    pp = []

    rest = rest.split(',')
    for i in rest:
        pp.append(i)
    pp = tuple(pp)

    cur.execute(
        'INSERT INTO bron  VALUES (?, ?, ?, ?, ?, ?)',
        pp)
    cur.execute('SELECT * FROM bron')
    result = cur.fetchall()
    print(result)
    conn.commit()
    conn.close()
    return {'result': result}


@app.route("/dobav3", methods=['POST'])
def dobav3():
    conn = sqlite3.connect('fir.db')
    cur = conn.cursor()
    rest = request.json['text']
    pp = []

    rest = rest.split(',')
    for i in rest:
        pp.append(i)
    pp = tuple(pp)

    cur.execute(
        'INSERT INTO nomer  VALUES (?, ?, ?, ?, ?, ?, ?)',
        pp)
    cur.execute('SELECT * FROM nomer')
    result = cur.fetchall()
    print(result)
    conn.commit()
    conn.close()
    return {'result': result}


@app.route("/dobav4", methods=['POST'])
def dobav4():
    conn = sqlite3.connect('fir.db')
    cur = conn.cursor()
    rest = request.json['text']
    pp = []

    rest = rest.split(',')
    for i in rest:
        pp.append(i)
    pp = tuple(pp)

    cur.execute(
        'INSERT INTO oplata (IdRoom, RoomNumber, bedCount) VALUES (?, ?, ?, )',
        pp)
    cur.execute('SELECT * FROM oplata')
    result = cur.fetchall()
    print(result)
    conn.commit()
    conn.close()
    return {'result': result}


@app.route("/zapr", methods=['POST'])
def zapr():
    conn = sqlite3.connect('fir.db')
    cur = conn.cursor()
    print(1)
    cur.execute('SELECT  FIO  FROM klient WHERE kod_klienta  = "11"')
    print(1)
    result = cur.fetchall()
    res = result
    conn.commit()
    conn.close()
    return {'result': result}


@app.route("/zapr2", methods=['POST'])
def zapr2():
    conn = sqlite3.connect('fir.db')
    cur = conn.cursor()
    print(1)
    cur.execute('Select kod_nomera, kod_personala FROM nomer WHERE kod_nomera = "12"')
    print(1)
    result = cur.fetchall()
    res = result
    conn.commit()
    conn.close()
    return {'result': result}


@app.route("/zapr3", methods=['POST'])
def zapr3():
    conn = sqlite3.connect('fir.db')
    cur = conn.cursor()
    print(1)
    cur.execute('Select * FROM Reservation WHERE IdPersonel = "5"')
    print(1)
    result = cur.fetchall()
    res = result
    conn.commit()
    conn.close()
    return {'result': result}


@app.route("/zapr4", methods=['POST'])
def zapr4():
    conn = sqlite3.connect('fir.db')
    cur = conn.cursor()
    print(1)
    cur.execute('Select FIO, IdRoom FROM Personel, Reservation WHERE Personel.IdPersonel = Reservation.IdPersonel and IdRoom = "10"')
    print(1)
    result = cur.fetchall()
    res = result
    conn.commit()
    conn.close()
    return {'result': result}


@app.route("/zapr5", methods=['POST'])
def zapr5():
    conn = sqlite3.connect('fir.db')
    cur = conn.cursor()
    print(1)
    cur.execute(
        'Select FIO From Client Where IdClient = "4"')
    print(1)
    result = cur.fetchall()
    res = result
    conn.commit()
    conn.close()
    return {'result': result}


@app.route("/cor", methods=['POST'])
def cor():
    conn = sqlite3.connect('fir.db')
    cur = conn.cursor()
    pp = []
    vms = request.json['text'].split(',')
    print(vms)
    for i in vms:
        pp.append(i)
    pp = tuple(pp)
    ids = request.json['tes']
    print(ids)
    cur.execute(
        'UPDATE Client SET IdClient = ?, FIO = ? WHERE IdClient = ' + str(
            ids), pp)
    cur.execute('Select * From Client')
    result = cur.fetchall()
    conn.commit()
    conn.close()
    return {'result': result}


@app.route("/cor2", methods=['POST'])
def cor2():
    conn = sqlite3.connect('fir.db')
    cur = conn.cursor()
    pp = []
    vms = request.json['text'].split(',')
    print(vms)
    for i in vms:
        pp.append(i)
    pp = tuple(pp)
    ids = request.json['tes']
    print(ids)
    cur.execute(
        'UPDATE Personel SET  IdPersonel = ?, FIO = ?, Position = ?, beginWork = ?, EndWork = ? WHERE IdPersonel = ' + str(
            ids), pp)
    cur.execute('Select * From Personel')
    result = cur.fetchall()
    conn.commit()
    conn.close()
    return {'result': result}


@app.route("/cor3", methods=['POST'])
def cor3():
    conn = sqlite3.connect('fir.db')
    cur = conn.cursor()
    pp = []
    vms = request.json['text'].split(',')
    print(vms)
    for i in vms:
        pp.append(i)
    pp = tuple(pp)
    ids = request.json['tes']
    print(ids)
    cur.execute(
        'UPDATE Reservation SET IdReserv = ?, PlacesCount = ?, IdClient = ?, ReservDate = ?, LeaveDate = ?, IdRoom = ?,Payment = ?, IdPersonel = ? WHERE IdReserv = ' + str(
            ids), pp)
    cur.execute('Select * From Reservation')
    result = cur.fetchall()
    conn.commit()
    conn.close()
    return {'result': result}


@app.route("/cor4", methods=['POST'])
def cor4():
    conn = sqlite3.connect('fir.db')
    cur = conn.cursor()
    pp = []
    vms = request.json['text'].split(',')
    print(vms)
    for i in vms:
        pp.append(i)
    pp = tuple(pp)
    ids = int(request.json['tes'])
    print(ids)
    cur.execute(
        'UPDATE Room SET IdRoom = ?, RoomNumber = ?, bedCount = ? WHERE IdRoom = ' + str(
            ids), pp)
    cur.execute('Select * From Палата')
    result = cur.fetchall()
    conn.commit()
    conn.close()
    return {'result': result}


if __name__ == '__main__':
    app.run()
