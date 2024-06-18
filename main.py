from selenium_main import buscar_pisos_fotocasa, buscar_pisos_habitaclia, buscar_pisos_idealista, buscar_pisos_pisoscom, buscar_pisos_yaencontre, start_selenium, selenium_close
import time
from telegram_bot import iniciado, pin, unpin, funcionando, update_funcionando, busqueda_en_curso,msg, resultado_msg
from datetime import datetime
from sql import db_connect, db_disconnect, db_insert, busqueda
import config

enlaces = [config.enlace_fotocasa, config.enlace_idealista, config.enlace_habitaclia, config.enlace_yaencontre, config.enlace_pisoscom]
buscadores = [buscar_pisos_fotocasa, buscar_pisos_idealista, buscar_pisos_habitaclia, buscar_pisos_yaencontre, buscar_pisos_pisoscom]
titulos = ["Fotocasa", "Idealista", "Habitaclia", "YaEncontre", "Pisos.com"]

while True:
    try:
        iniciado()
        unpin()
        funcionando(datetime. now(). strftime("%H:%M"))
        pin()
        db_connect()
        while True:
            busqueda_en_curso()
                
            for a in range(len(enlaces)):
                start_selenium(enlaces[a])

                anuncios = buscadores[a]()
                
                web = titulos[a]

                for item in range(0,len(anuncios),2):
                    titulo = anuncios[item]
                    enlace = anuncios[(item+1)]
                    
                    titulo = titulo.replace("'","")
                    titulo = titulo.replace('"',"")

                    if busqueda(titulo) == []:
                        resultado_msg(titulo,enlace)
                        db_insert(web,titulo,enlace)

                selenium_close()
                time.sleep(10)

            print("\n\nEsperando 10 minutos")        
            update_funcionando(datetime. now(). strftime("%H:%M"))
            time.sleep(600)
    except Exception as e:
        msg(f"Error:\n{e}")
        update_funcionando("Error, se ha roto")

    db_disconnect()

    time.sleep(60)