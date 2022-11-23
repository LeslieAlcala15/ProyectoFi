from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql

app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")


#TIPO PAN
@app.route('/tipopan')
def tipopan():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3' )
    cursor = conn.cursor()
    cursor.execute('select idTipopan, descripcion from tipopan order by idTipopan')
    datos = cursor.fetchall()
    return render_template("tipopan.html", tipopan = datos)

@app.route('/tipopan_editar/<string:id>')
def tipopan_editar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('select idTipopan, descripcion from tipopan where idTipopan = %s', (id))
    dato = cursor.fetchall()
    return render_template("tipopan_edi.html", tipopan=dato[0])

@app.route('/tipopan_fedita/<string:id>',methods=['POST'])
def tipopan_fedita(id):
    if request.method == 'POST':
        desc=request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
        cursor = conn.cursor()
        cursor.execute('update tipopan set descripcion=%s where idTipopan=%s', (desc,id))
        conn.commit()
        return redirect(url_for('tipopan'))

@app.route('/tipopan_borrar/<string:id>')
def tipopan_borrar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('delete from tipopan where idTipopan = {0}'.format(id))
    conn.commit()
    return redirect(url_for('tipopan'))

@app.route('/tipopan_agregar')
def tipopan_agregar():
    return render_template("tipopan_agr.html")

@app.route('/tipopan_fagrega', methods=['POST'])
def tipopan_fagrega():
    if request.method == 'POST':
        desc = request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3' )
        cursor = conn.cursor()
        cursor.execute('insert into tipopan (descripcion) values (%s)',(desc))
        conn.commit()
        return redirect(url_for('tipopan'))

#RELLENO 

@app.route('/relleno')
def relleno():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3' )
    cursor = conn.cursor()
    cursor.execute('select idRelleno, descripcion from relleno order by idRelleno')
    datos = cursor.fetchall()
    return render_template("relleno.html", relleno = datos)

@app.route('/relleno_editar/<string:id>')
def relleno_editar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('select idRelleno, descripcion from relleno where idRelleno = %s', (id))
    dato = cursor.fetchall()
    return render_template("relleno_edi.html", relleno=dato[0])

@app.route('/relleno_fedita/<string:id>',methods=['POST'])
def relleno_fedita(id):
    if request.method == 'POST':
        desc=request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
        cursor = conn.cursor()
        cursor.execute('update relleno set descripcion=%s where idRelleno=%s', (desc,id))
        conn.commit()
        return redirect(url_for('relleno'))

@app.route('/relleno_borrar/<string:id>')
def relleno_borrar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('delete from relleno where idRelleno = {0}'.format(id))
    conn.commit()
    return redirect(url_for('relleno'))

@app.route('/relleno_agregar')
def relleno_agregar():
    return render_template("relleno_agr.html")

@app.route('/relleno_fagrega', methods=['POST'])
def relleno_fagrega():
    if request.method == 'POST':
        desc = request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3' )
        cursor = conn.cursor()
        cursor.execute('insert into relleno (descripcion) values (%s)',(desc))
        conn.commit()
        return redirect(url_for('relleno'))



#Cubierta

@app.route('/cubierta')
def cubierta():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3' )
    cursor = conn.cursor()
    cursor.execute('select idCubierta, descripcion from cubierta order by idCubierta')
    datos = cursor.fetchall()
    return render_template("cubierta.html", cubierta = datos)

@app.route('/cubierta_editar/<string:id>')
def cubierta_editar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('select idCubierta, descripcion from cubierta where idCubierta = %s', (id))
    dato = cursor.fetchall()
    return render_template("cubierta_edi.html", cubierta = dato[0])

@app.route('/cubierta_fedita/<string:id>',methods=['POST'])
def cubierta_fedita(id):
    if request.method == 'POST':
        desc=request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
        cursor = conn.cursor()
        cursor.execute('update cubierta set descripcion=%s where idCubierta=%s', (desc,id))
        conn.commit()
        return redirect(url_for('cubierta'))

@app.route('/cubierta_borrar/<string:id>')
def cubierta_borrar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('delete from cubierta where idCubierta = {0}'.format(id))
    conn.commit()
    return redirect(url_for('cubierta'))

@app.route('/cubierta_agregar')
def cubierta_agregar():
    return render_template("cubierta_agr.html")

@app.route('/cubierta_fagrega', methods=['POST'])
def cubierta_fagrega():
    if request.method == 'POST':
        desc = request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3' )
        cursor = conn.cursor()
        cursor.execute('insert into cubierta (descripcion) values (%s)',(desc))
        conn.commit()
        return redirect(url_for('cubierta'))


#fORMA
@app.route('/forma')
def forma():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3' )
    cursor = conn.cursor()
    cursor.execute('select idForma, descripcion from forma order by idForma')
    datos = cursor.fetchall()
    return render_template("forma.html", forma = datos)

@app.route('/forma_editar/<string:id>')
def forma_editar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('select idForma, descripcion from forma where idForma = %s', (id))
    dato = cursor.fetchall()
    return render_template("forma_edi.html", forma=dato[0])

@app.route('/forma_fedita/<string:id>',methods=['POST'])
def forma_fedita(id):
    if request.method == 'POST':
        desc=request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
        cursor = conn.cursor()
        cursor.execute('update forma set descripcion=%s where idForma=%s', (desc,id))
        conn.commit()
        return redirect(url_for('forma'))

@app.route('/forma_borrar/<string:id>')
def forma_borrar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('delete from forma where idForma = {0}'.format(id))
    conn.commit()
    return redirect(url_for('forma'))

@app.route('/forma_agregar')
def forma_agregar():
    return render_template("forma_agr.html")

@app.route('/forma_fagrega', methods=['POST'])
def forma_fagrega():
    if request.method == 'POST':
        desc = request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3' )
        cursor = conn.cursor()
        cursor.execute('insert into forma (descripcion) values (%s)',(desc))
        conn.commit()
        return redirect(url_for('forma'))


#NIVELES
@app.route('/niveles')
def niveles():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3' )
    cursor = conn.cursor()
    cursor.execute('select idNiveles, descripcion from niveles order by idNiveles')
    datos = cursor.fetchall()
    return render_template("niveles.html", niveles = datos)

@app.route('/niveles_editar/<string:id>')
def niveles_editar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('select idNiveles, descripcion from niveles where idNiveles = %s', (id))
    dato = cursor.fetchall()
    return render_template("niveles_edi.html", niveles=dato[0])

@app.route('/niveles_fedita/<string:id>',methods=['POST'])
def niveles_fedita(id):
    if request.method == 'POST':
        desc=request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
        cursor = conn.cursor()
        cursor.execute('update niveles set descripcion=%s where idNiveles=%s', (desc,id))
        conn.commit()
        return redirect(url_for('niveles'))

@app.route('/niveles_borrar/<string:id>')
def niveles_borrar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('delete from niveles where idNiveles = {0}'.format(id))
    conn.commit()
    return redirect(url_for('niveles'))

@app.route('/niveles_agregar')
def niveles_agregar():
    return render_template("niveles_agr.html")

@app.route('/niveles_fagrega', methods=['POST'])
def niveles_fagrega():
    if request.method == 'POST':
        desc = request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3' )
        cursor = conn.cursor()
        cursor.execute('insert into niveles (descripcion) values (%s)',(desc))
        conn.commit()
        return redirect(url_for('niveles'))


#PRESUPUESTO
@app.route('/presupuesto')
def presupuesto():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3' )
    cursor = conn.cursor()
    cursor.execute('select idPresupuesto, descripcion from presupuesto order by idPresupuesto')
    datos = cursor.fetchall()
    return render_template("presupuesto.html", presupuesto = datos)

@app.route('/presupuesto_editar/<string:id>')
def presupuesto_editar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('select idPresupuesto, descripcion from presupuesto where idPresupuesto = %s', (id))
    dato = cursor.fetchall()
    return render_template("presupuesto_edi.html", presupuesto=dato[0])

@app.route('/presupuesto_fedita/<string:id>',methods=['POST'])
def presupuesto_fedita(id):
    if request.method == 'POST':
        desc=request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
        cursor = conn.cursor()
        cursor.execute('update presupuesto set descripcion=%s where idPresupuesto=%s', (desc,id))
        conn.commit()
        return redirect(url_for('presupuesto'))

@app.route('/presupuesto_borrar/<string:id>')
def presupuesto_borrar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('delete from presupuesto where idPresupuesto = {0}'.format(id))
    conn.commit()
    return redirect(url_for('presupuesto'))

@app.route('/presupuesto_agregar')
def presupuesto_agregar():
    return render_template("presupuesto_agr.html")

@app.route('/presupuesto_fagrega', methods=['POST'])
def presupuesto_fagrega():
    if request.method == 'POST':
        desc = request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3' )
        cursor = conn.cursor()
        cursor.execute('insert into presupuesto (descripcion) values (%s)',(desc))
        conn.commit()
        return redirect(url_for('presupuesto'))


#DECORACIONes
@app.route('/decoraciones')  
def decoraciones():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3' )
    cursor = conn.cursor()
    cursor.execute('select idDecoraciones, descripcion from decoraciones order by idDecoraciones')
    datos = cursor.fetchall()
    return render_template("decoraciones.html", decoraciones = datos)

@app.route('/decoraciones_editar/<string:id>')
def decoraciones_editar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('select idDecoraciones, descripcion from decoraciones where idDecoraciones = %s', (id))
    dato = cursor.fetchall()
    return render_template("decoraciones_edi.html", decoraciones=dato[0])

@app.route('/decoraciones_fedita/<string:id>',methods=['POST'])
def decoraciones_fedita(id):
    if request.method == 'POST':
        desc=request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
        cursor = conn.cursor()
        cursor.execute('update decoraciones set descripcion=%s where idDecoraciones=%s', (desc,id))
        conn.commit()
        return redirect(url_for('decoraciones'))

@app.route('/decoraciones_borrar/<string:id>')
def decoraciones_borrar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('delete from decoraciones where idDecoraciones = {0}'.format(id))
    conn.commit()
    return redirect(url_for('decoraciones'))

@app.route('/decoraciones_agregar')
def decoraciones_agregar():
    return render_template("decoraciones_agr.html")

@app.route('/decoraciones_fagrega', methods=['POST'])
def decoraciones_fagrega():
    if request.method == 'POST':
        desc = request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3' )
        cursor = conn.cursor()
        cursor.execute('insert into decoraciones (descripcion) values (%s)',(desc))
        conn.commit()
        return redirect(url_for('decoraciones'))

#########Pedido-----------------------------------------
@app.route('/pedido')
def encargo():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3' )
    cursor = conn.cursor()
    cursor.execute('select idPedido, nomPedido from pedido order by idPedido')
    datos = cursor.fetchall()
    return render_template("pedido.html", ped=datos, dat=' ', catTipopan=' ', catForma=' ',catCubierta=' ', catNiveles=' ', catRelleno=' ', catDecoraciones=' ', catPresupuesto=' ')

@app.route('/pedido_fdetalle/<string:idP>', methods=['GET'])
def pedido_fdetalle(idP):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('select idPedido, nomPedido from pedido order by idPedido')
    datos = cursor.fetchall()
    cursor.execute('select idPedido,codPedido,idTipopan,nomPedido,tipoevento,fechaentrega,adelanto,numtelefono,nomcliente,identificacion,edad,idForma,idCubierta,idNiveles,idRelleno,quienrecibe,tematica,modoentrega,textopastel,email,numtarjeta,especificaciones from pedido where idPedido = %s', (idP))
    dato = cursor.fetchall()
    cursor.execute('select a.idTipopan, a.descripcion from tipopan a, pedido b where a.idTipopan = b.idTipopan and b.idPedido = %s', (idP))
    datos1 = cursor.fetchall()
    cursor.execute('select a.idForma, a.descripcion from forma a, pedido b where a.idForma = b.idForma and b.idPedido = %s', (idP))
    datos2 = cursor.fetchall()
    cursor.execute('select a.idCubierta, a.descripcion from cubierta a, pedido b where a.idCubierta = b.idCubierta and b.idPedido = %s', (idP))
    datos3 = cursor.fetchall()
    cursor.execute('select a.idNiveles, a.descripcion from niveles a, pedido b where a.idNiveles = b.idNiveles and b.idPedido = %s', (idP))
    datos4 = cursor.fetchall()
    cursor.execute('select a.idRelleno, a.descripcion from relleno a, pedido b where a.idRelleno = b.idRelleno and b.idPedido = %s', (idP))
    datos5 = cursor.fetchall()
    cursor.execute('select a.idPedido, b.idDecoraciones, b.descripcion from pedido a, decoraciones b, pedido_has_decoraciones c where a.idPedido = c.idDecoraciones and b.idDecoraciones = c.idDecoraciones and a.idPedido = %s', (idP))
    datos6 = cursor.fetchall()
    cursor.execute('select a.idPedido, b.idPresupuesto, b.descripcion from pedido a, presupuesto b, pedido_has_presupuesto c where a.idPedido = c.idPedido and b.idPresupuesto = c.idPresupuesto and a.idPedido= %s', (idP))
    datos7 = cursor.fetchall()
    return render_template("pedido.html", ped = datos, dat=dato[0], catTipopan=datos1[0], catForma=datos2[0], catCubierta=datos3[0], catNiveles=datos4[0], catRelleno=datos5[0], catDecoraciones=datos6, catPresupuesto=datos7)

@app.route('/pedido_borrar/<string:idP>')
def pedido_borrar(idP):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('delete from pedido where idPedido = %s',(idP))
    conn.commit()
    cursor.execute('delete from pedido_has_presupuesto where idPedido =%s ', (idP))
    conn.commit()
    cursor.execute('delete from pedido_has_decoraciones where idPedido =%s ', (idP))
    conn.commit()
    return redirect(url_for('pedido'))

@app.route('/pedido_agregar')
def pedido_agregar():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('select idTipopan, descripcion from tipopan ')
    datos1 = cursor.fetchall()
    cursor.execute('select idForma, descripcion from forma ')
    datos2 = cursor.fetchall()
    cursor.execute('select idCubierta, descripcion from cubierta ')
    datos3 = cursor.fetchall()
    cursor.execute('select idNiveles, descripcion from niveles ')
    datos4 = cursor.fetchall()
    cursor.execute('select idRelleno, descripcion from relleno ')
    datos5 = cursor.fetchall()
    cursor.execute('select idDecoraciones, descripcion from decoraciones ')
    datos6 = cursor.fetchall()
    cursor.execute('select idPresupuesto, descripcion from presupuesto ')
    datos7 = cursor.fetchall()
    return render_template("pedido_agr.html", catTipopan=datos1, catForma=datos2, catCubierta=datos3, catNiveles=datos4, catRelleno=datos5, catDecoraciones=datos6, catPresupuesto=datos7)

@app.route('/pedido_fagrega', methods=['POST'])
def pedido_fagrega():
    if request.method == 'POST':
        if 'idTipopan' in request.form:
            idTip = request.form['idTipopan']
        else:
            idTip = '1'
        if 'idForma' in request.form: 
            idFo = request.form['idForma']
        else: 
            idFo = '1'
        if 'idCubierta' in request.form: 
            idCu = request.form['idCubierta']
        else: 
            idCu = '1'
        if 'idNiveles' in request.form: 
            idNi = request.form['idNiveles']
        else: 
            idNi = '1'
        if 'idRelleno' in request.form: 
            idRe = request.form['idRelleno']
        else: 
            idRe = '1'
        codP = request.form['codPedido']
        nomP = request.form['nomPedido']
        tipoeven = request.form['tipoevento']
        fechaent = request.form['fechaentrega']
        adel = request.form['adelanto']
        numte = request.form['numtelefono']
        nomcl = request.form['nomcliente']
        iden = request.form['identificacion']
        eda = request.form['edad']
        idFo = request.form['idForma']
        idCu = request.form['idCubierta']
        idNi = request.form['idNiveles']
        idRe = request.form['idRelleno']
        quienre = request.form['quienrecibe']
        temat = request.form['tematica']
        modoent = request.form['modoentrega']
        textopas = request.form['textopastel']
        emai = request.form['email']
        numta = request.form['numtarjeta']
        espe = request.form['especificaciones']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
        cursor = conn.cursor()
        cursor.execute( 'insert into pedido(codPedido,idTipopan,nomPedido,tipoevento,fechaentrega,adelanto,numtelefono,nomcliente,identificacion,edad,idForma,idCubierta,idNiveles,idRelleno,quienrecibe,tematica,modoentrega,textopastel,email,numtarjeta,especificaciones) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', (codP, idTip, nomP, tipoeven, fechaent, adel, numte, nomcl, iden, eda, idFo, idCu, idNi, idRe, quienre, temat, modoent, textopas, emai, numta, espe))
        conn.commit()
        cursor.execute('select idPedido, nomPedido from pedido where idPedido=(select max(idPedido) from pedido) ')
        dato=cursor.fetchall()
        idPed = dato[0]
        idP = idPed[0]
        cursor.execute('select count(*) from decoraciones ')
        dato = cursor.fetchall()
        ndeco = dato[0]
        nd = ndeco[0] + 1
        
        for d in range(1, nd):
            deco = 'd' + str(d)
            if deco in request.form:
                cursor.execute('insert into pedido_has_decoraciones(idPedido,idDecoraciones) values (%s,%s)', (idP, d))
                conn.commit()
        cursor.execute('select count(*) from presupuesto ')
        dato = cursor.fetchall()
        npres = dato[0]
        np = npres[0] + 1

        for p in range(1, np):
            pres = 'p' + str(p)
            if pres in request.form:
                cursor.execute('insert into pedido_has_presupuesto(idPedido,idPresupuesto) values (%s,%s)', (idP, p))
            conn.commit()
    return redirect(url_for('pedido'))


@app.route('/pedido_editar/<string:idP>')
def pedido_editar(idP):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('select idPedido,codPedido,idTipopan,nomPedido,tipoevento,fechaentrega,adelanto,numtelefono,nomcliente,'
        'identificacion,edad,idForma,idCubierta,idNiveles,idRelleno,quienrecibe,tematica,modoentrega,'
        'textopastel,email,numtarjeta,especificaciones from pedido where idPedido = %s', (idP))
    dato = cursor.fetchall()

    cursor.execute('select idTipopan, descripcion from tipopan ')
    datos1 = cursor.fetchall()

    cursor.execute('select idForma, descripcion from forma ')
    datos2 = cursor.fetchall()

    cursor.execute('select idCubierta, descripcion from cubierta ')
    datos3 = cursor.fetchall()

    cursor.execute('select idNiveles, descripcion from niveles ')
    datos4 = cursor.fetchall()

    cursor.execute('select idRelleno, descripcion from relleno ')
    datos5 = cursor.fetchall()

    cursor.execute('select idDecoraciones, descripcion from decoraciones ')
    datos6 = cursor.fetchall()

    cursor.execute('select idPresupuesto, descripcion from presupuesto ')
    datos7 = cursor.fetchall()

    cursor.execute('select a.idTipopan, a.descripcion from tipopan a, pedido b where a.idTipopan = b.idTipopan and b.idPedido = %s',
                   (idP))
    datos11 = cursor.fetchall()

    cursor.execute(
        'select a.idForma, a.descripcion from forma a, pedido b where a.idForma = b.idForma and b.idPedido = %s',
        (idP))
    datos12 = cursor.fetchall()

    cursor.execute(
        'select a.idCubierta, a.descripcion from cubierta a, pedido b where a.idCubierta = b.idCubierta and b.idPedido = %s',
        (idP))
    datos13 = cursor.fetchall()

    cursor.execute(
        'select a.idNiveles, a.descripcion from niveles a, pedido b where a.idNiveles = b.idNiveles and b.idPedido = %s',
        (idP))
    datos14 = cursor.fetchall()

    cursor.execute(
        'select a.idRelleno, a.descripcion from relleno a, pedido b where a.idRelleno = b.idRelleno and b.idPedido = %s',
        (idP))
    datos15 = cursor.fetchall()

    cursor.execute('select a.idPedido, b.idDecoraciones, b.descripcion from pedido a, decoraciones b, pedido_has_decoraciones c '
                   'where a.idPedido = c.idDecoraciones and b.idDecoraciones = c.idDecoraciones and a.idPedido = %s', (idP))
    datos16 = cursor.fetchall()

    cursor.execute('select a.idPedido, b.idPresupuesto, b.descripcion from pedido a, presupuesto b, pedido_has_presupuesto c '
                   'where a.idPedido = c.idPedido and b.idPresupuesto = c.idPresupuesto and a.idPedido = %s', (idP))
    datos17 = cursor.fetchall()

    return render_template("pedido_edi.html", dat=dato[0], catTipopan=datos1, catForma=datos2, catCubierta=datos3, catNiveles=datos4, catRelleno=datos5, catDecoraciones=datos6, catPresupuesto=datos7, Tipopan=datos11[0], Forma=datos12[0], Cubierta=datos13[0], Niveles=datos14[0], Relleno=datos15[0], Decoraciones=datos16, Presupuesto=datos17)


@app.route('/pedido_fedita/<string:idP>', methods=['POST'])
def pedido_fedita(idP):
    if request.method == 'POST':
        if 'idNiveles' in request.form:
            idNi = request.form['idNiveles']
        else:
            idNi = '1'
        if 'idRelleno' in request.form:
            idRe = request.form['idRelleno']
        else:
            idRe = '1'
        codP = request.form['codPedido']
        idTip = request.form['idTipopan']
        nomP = request.form['nomPedido']
        tipoeven = request.form['tipoevento']
        fechaent = request.form['fechaentrega']
        adel = request.form['adelanto']
        numte = request.form['numtelefono']
        nomcl = request.form['nomcliente']
        iden = request.form['identificacion']
        eda = request.form['edad']
        idFo = request.form['idForma']
        idCu = request.form['idCubierta']
        idNi = request.form['idNiveles']
        idRe = request.form['idRelleno']
        quienre = request.form['quienrecibe']
        temat = request.form['tematica']
        modoent = request.form['modoentrega']
        textopas = request.form['textopastel']
        emai = request.form['email']
        numta = request.form['numtarjeta']
        espe = request.form['especificaciones']

        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
        cursor = conn.cursor()
        cursor.execute('update pedido set codPedido = %s, idTipopan = %s, nomPedido = %s, tipoevento = %s, fechaentrega = %s, adelanto = %s, numtelefono = %s, nomcliente = %s, identificacion = %s, edad = %s, idForma = %s, idCubierta = %s, idNiveles = %s, idRelleno = %s, quienrecibe = %s, ' 'tematica = %s, modoentrega = %s, textopastel = %s, email = %s, numtarjeta = %s, especificaciones = %s where idPedido = %s', (codP, idTip, nomP, tipoeven, fechaent, adel, numte, nomcl, iden, eda, idFo, idCu, idNi, idRe, quienre, temat, modoent, textopas, emai, numta, espe, idP))
        conn.commit()
    return redirect(url_for('pedido'))


####ENCARGO---------------------------------------------------------------------------------------------------------------------------------------

@app.route('/nuevo_encargo')
def nuevo_encargo():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('select idTipopan, descripcion from tipopan ')
    datos1 = cursor.fetchall()
    cursor.execute('select idPedido, nomPedido from pedido ')
    datos2 = cursor.fetchall()
    return render_template("nuevo_encargo.html", catTipopan=datos1, catPedido=datos2)

@app.route('/encargo_fagrega', methods=['POST'])
def enca_fagrega():
    if request.method == 'POST':
        if 'idTipopan' in request.form:idTip = request.form['idTipopan']
    else:
        idTip = '1'
    if 'idPedido' in request.form:idPed = request.form['idPedido']
    else:
        idPed = '1'
    fol = request.form['folio']
    fechape = request.form['fechapedido']
    fechaau = request.form['fechaautorizacion']
    fechaen = request.form['fechaentrega']
    banc = request.form['bancos']
    motEs = request.form['motivoEspecifique']
    tipopa = request.form['tipopago']
    nomSoli = request.form['nomSolicita']
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('insert into encargo(folio, idTipopan, fechapedido, idPedido, nomSolicita, fechaautorizacion, fechaentrega, tipopago, bancos, motivoEspecifique) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(fol, idTip, fechape, idPed, nomSoli, fechaau, fechaen, tipopa, banc, motEs))
    conn.commit()
    return redirect(url_for('index'))

@app.route('/pendientes_autorizacion')
def pendientes_autorizacion():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3' )
    cursor = conn.cursor()
    cursor.execute('select idPedido, nomPedido from pedido order by idPedido')
    datos = cursor.fetchall()
    return render_template("pendientes_autorizacion.html", ped=datos, dat=' ', catTipopan=' ', catForma=' ', catCubierta=' ', catNiveles=' ', catRelleno=' ', catDecoraciones=' ', catPresupuesto=' ')

@app.route('/pendientes_autorizacion_fdetalle/<string:idP>', methods=['GET'])
def pendientes_fdetalle(idP):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('select idPedido, nomPedido from pedido order by idPedido')
    datos = cursor.fetchall()
    cursor.execute('select idPedido, codPedido, idTipopan, nomPedido, tipoevento, fechaentrega, adelanto, numtelefono, nomcliente, identificacion, edad, idForma, idCubierta, idNiveles, idRelleno, quienrecibe, tematica, modoentrega, textopastel, email, numtarjeta, especificaciones from pedido where idPedido = %s', (idP))
    dato = cursor.fetchall()
    cursor.execute('select a.idTipopan, a.descripcion from tipopan a, pedido b where a.idTipopan = b.idTipopan and b.idPedido = %s', (idP))
    datos1 = cursor.fetchall()
    cursor.execute('select a.idForma, a.descripcion from forma a, pedido b where a.idForma = b.idForma and b.idPedido = %s', (idP))
    datos2 = cursor.fetchall()
    cursor.execute('select a.idCubierta, a.descripcion from cubierta a, pedido b where a.idCubierta = b.idCubierta and b.idPedido = %s', (idP))
    datos3 = cursor.fetchall()
    cursor.execute('select a.idNiveles, a.descripcion from niveles a, pedido b where a.idNiveles = b.idNiveles and b.idPedido = %s', (idP))
    datos4 = cursor.fetchall()
    cursor.execute('select a.idRelleno, a.descripcion from relleno a, pedido b where a.idRelleno = b.idRelleno and b.idPedido = %s', (idP))
    datos5 = cursor.fetchall()
    cursor.execute('select a.idPedido, b.idDecoraciones, b.descripcion from pedido a, decoraciones b, pedido_has_decoraciones c where a.idPedido = c.idPedido and b.idDecoraciones = c.idDecoraciones and a.idPedido = %s', (idP))
    datos6 = cursor.fetchall()
    cursor.execute('select a.idPedido, b.idPresupuesto, b.descripcion from pedido a, presupuesto b, pedido_has_presupuesto c where a.idPedido = c.idPedido and b.idPresupuesto = c.idPresupuesto and a.idPedido = %s', (idP))
    datos7 = cursor.fetchall()
    print(datos1)
    print(datos2)
    print(datos3)
    print(datos4)
    print(datos5)
    print(datos6)
    print(datos7)
    return render_template("pendientes_autorizacion.html", ped = datos, dat=dato[0], catTipopan=datos1[0], catForma=datos2[0], catCubierta=datos3[0], catNiveles=datos4[0], catRelleno=datos5[0], catDecoraciones=datos6, catPresupuesto=datos7)


@app.route('/pendientes_autorizacion_borrar/<string:idP>')
def pendientes_borrar(idP):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('delete from pedido where idPedido = %s',(idP))
    conn.commit()
    cursor.execute('delete from pedido_has_presupuesto where idPedido =%s ', (idP))
    conn.commit()
    cursor.execute('delete from pedido_has_decoraciones where idPedido =%s ', (idP))
    conn.commit()
    return redirect(url_for('pendientes_autorizacion')) 
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
@app.route('/autorizadas')
def autorizadas():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3' )
    cursor = conn.cursor()
    cursor.execute('select idPedido, nomPedido from pedido order by idPedido')
    datos = cursor.fetchall()
    return render_template("autorizadas.html", ped=datos, dat=' ', catTipopan=' ', catForma=' ', catCubierta=' ', catNiveles=' ', catRelleno=' ', catDecoraciones=' ', catPresupuesto=' ')

@app.route('/autorizadas_fdetalle/<string:idP>', methods=['GET'])
def autorizadas_fdetalle(idP):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('select idPedido, nomPedido from pedido order by idPedido')
    datos = cursor.fetchall()
    cursor.execute('select idPedido, codPedido, idTipopan, nomPedido, tipoevento, fechaentrega, adelanto, numtelefono, nomcliente, identificacion, edad, idNumpersonas, idForma, idCubierta, idNiveles, idRelleno, quienrecibe, tematica, modoentrega, textopastel, email, numtarjeta, especificaciones from pedido where idPedido = %s', (idP))
    dato = cursor.fetchall()
    cursor.execute('select a.idTipopan, a.descripcion from tipopan a, pedido b where a.idTipopan = b.idTipopan and b.idPedido = %s', (idP))
    datos1 = cursor.fetchall()
    cursor.execute('select a.idForma, a.descripcion from forma a, pedido b where a.idForma = b.idForma and b.idPedido = %s', (idP))
    datos2 = cursor.fetchall()
    cursor.execute('select a.idCubierta, a.descripcion from cubierta a, pedido b where a.idCubierta = b.idCubierta and b.idPedido = %s', (idP))
    datos3 = cursor.fetchall()
    cursor.execute('select a.idNiveles, a.descripcion from niveles a, pedido b where a.idNiveles = b.idNiveles and b.idPedido = %s', (idP))
    datos4 = cursor.fetchall()
    cursor.execute('select a.idRelleno, a.descripcion from relleno a, pedido b where a.idRelleno = b.idRelleno and b.idPedido = %s', (idP))
    datos5 = cursor.fetchall()
    cursor.execute('select a.idPedido, b.idDecoraciones, b.descripcion from pedido a, decoraciones b, pedido_has_decoraciones c where a.idPedido = c.idPedido and b.idDecoraciones = c.idDecoraciones and a.idPedido = %s', (idP))
    datos6 = cursor.fetchall()
    cursor.execute('select a.idPedido, b.idPresupuesto, b.descripcion from pedido a, presupuesto b, pedido_has_presupuesto c where a.idPedido = c.idPedido and b.idPresupuesto = c.idPresupuesto and a.idPedido = %s', (idP))
    datos7 = cursor.fetchall()
    print(datos1)
    print(datos2)
    print(datos3)
    print(datos4)
    print(datos5)
    print(datos6)
    print(datos7)
    return render_template("autorizadas.html", ped = datos, dat=dato[0], catTipopan=datos1[0], catForma=datos2[0], catCubierta=datos3[0], catNiveles=datos4[0], catRelleno=datos5[0], catDecoraciones=datos6, catPresupuesto=datos7)

@app.route('/pendientes_autorizacion_borrar/<string:idE>')
def pendientes_autorizacion_borrar(idE):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('delete from encargo where idEncargo = %s',(idE))
    conn.commit()
    return redirect(url_for('pendientes_autorizacion'))




if __name__ == "__main__":
    app.run(debug=True)
