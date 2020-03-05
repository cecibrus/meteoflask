from flask import Flask, render_template
from scrap import temperaturas
from scrap import velocidades
from scrap import direcciones
from scrap import lis_ciudades

app= Flask(__name__) #instancia la clase flask y crea el objeto flask

@app.route('/') #este es el index
def indice():
    return render_template('inicio.html') #esta es la respuesta del servidor

if __name__ == "__main__":
    app.run()

@app.route('/datos_asuncion')
def datos_asuncion():
    datos_asu={
        'temperatura':temperaturas[0],'velocidad':velocidades[0],'direccion':direcciones[0],'ciudad':lis_ciudades[0]
    }
    return render_template('datos.html', data=datos_asu)

@app.route('/datos_concepcion')
def datos_concepcion():
    datos_con={
        'temperatura':temperaturas[1],'velocidad':velocidades[1],'direccion':direcciones[1],'ciudad':lis_ciudades[1]
    }
    return render_template('datos.html', data=datos_con)

@app.route('/datos_sanpedro')
def datos_sanpedro():
    datos_sp={
        'temperatura':temperaturas[2],'velocidad':velocidades[2],'direccion':direcciones[2],'ciudad':lis_ciudades[2]
    }
    return render_template('datos.html', data=datos_sp)

@app.route('/datos_caacupe')
def datos_caacupe():
    datos_caac={
        'temperatura':temperaturas[3],'velocidad':velocidades[3],'direccion':direcciones[3],'ciudad':lis_ciudades[3]
    }
    return render_template('datos.html', data=datos_caac)

@app.route('/datos_villarrica')
def datos_villarrica():
    datos_vr={
        'temperatura':temperaturas[4],'velocidad':velocidades[4],'direccion':direcciones[4],'ciudad':lis_ciudades[4]
    }
    return render_template('datos.html', data=datos_vr)

@app.route('/datos_cneloviedo')
def datos_cneloviedo():
    datos_co={
        'temperatura':temperaturas[5],'velocidad':velocidades[5],'direccion':direcciones[5],'ciudad':lis_ciudades[5]
    }
    return render_template('datos.html', data=datos_co)

@app.route('/datos_caazapa')
def datos_caazapa():
    datos_caaz={
        'temperatura':temperaturas[6],'velocidad':velocidades[6],'direccion':direcciones[6],'ciudad':lis_ciudades[6]
    }
    return render_template('datos.html', data=datos_caaz)

@app.route('/datos_encarnacion')
def datos_encarnacion():
    datos_enc={
        'temperatura':temperaturas[7],'velocidad':velocidades[7],'direccion':direcciones[7],'ciudad':lis_ciudades[7]
    }
    return render_template('datos.html', data=datos_enc)

@app.route('/datos_sanjuan')
def datos_sanjuan():
    datos_sj={
        'temperatura':temperaturas[8],'velocidad':velocidades[8],'direccion':direcciones[8],'ciudad':lis_ciudades[8]
    }
    return render_template('datos.html', data=datos_sj)

@app.route('/datos_paraguari')
def datos_paraguari():
    datos_par={
        'temperatura':temperaturas[9],'velocidad':velocidades[9],'direccion':direcciones[9],'ciudad':lis_ciudades[9]
    }
    return render_template('datos.html', data=datos_par)

@app.route('/datos_cdeleste')
def datos_cdelestde():
    datos_cde={
        'temperatura':temperaturas[10],'velocidad':velocidades[10],'direccion':direcciones[10],'ciudad':lis_ciudades[10]
    }
    return render_template('datos.html', data=datos_cde)

@app.route('/datos_aregua')
def datos_aregua():
    datos_ar={
        'temperatura':temperaturas[11],'velocidad':velocidades[11],'direccion':direcciones[11],'ciudad':lis_ciudades[11]
    }
    return render_template('datos.html', data=datos_ar)

@app.route('/datos_pilar')
def datos_pilar():
    datos_pi={
        'temperatura':temperaturas[12],'velocidad':velocidades[12],'direccion':direcciones[12],'ciudad':lis_ciudades[12]
    }
    return render_template('datos.html', data=datos_pi)

@app.route('/datos_pjuanc')
def datos_pjuanc():
    datos_pjc={
        'temperatura':temperaturas[13],'velocidad':velocidades[13],'direccion':direcciones[13],'ciudad':lis_ciudades[13]
    }
    return render_template('datos.html', data=datos_pjc)

@app.route('/datos_saltos')
def datos_saltos():
    datos_sdg={
        'temperatura':temperaturas[14],'velocidad':velocidades[14],'direccion':direcciones[14],'ciudad':lis_ciudades[14]
    }
    return render_template('datos.html', data=datos_sdg)

@app.route('/datos_villahayes')
def datos_villahayes():
    datos_vh={
        'temperatura':temperaturas[15],'velocidad':velocidades[15],'direccion':direcciones[15],'ciudad':lis_ciudades[15]
        }
    return render_template('datos.html', data=datos_vh)

@app.route('/datos_filadelfia')
def datos_filadelfia():
    datos_fil={
        'temperatura':temperaturas[16],'velocidad':velocidades[16],'direccion':direcciones[16],'ciudad':lis_ciudades[16]
    }
    return render_template('datos.html', data=datos_fil)

@app.route('/datos_fuerteolimpo')
def datos_fuerteolimpo():
    datos_fo={
        'temperatura':temperaturas[17],'velocidad':velocidades[17],'direccion':direcciones[17],'ciudad':lis_ciudades[17]
    }
    return render_template('datos.html', data=datos_fo)

if __name__ == "__main__":
    app.run()