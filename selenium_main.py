from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
import time

opciones = Options()
scroll_distance = 1000

anuncios_enviados = []

opciones.headless = True
opciones.add_argument("--incognito")
opciones.add_argument('log-level=3')
opciones.add_argument('--window-size=1920,1080')

def start_selenium(url):
    global navegador
    navegador = webdriver.Chrome(options=opciones) 
    navegador.implicitly_wait(2)
    navegador.get(url)
    time.sleep(2)

def scroll():
    navegador.execute_script(f"window.scrollBy(0,1000)")

def buscar_pisos_fotocasa():
    try:
        navegador.find_element(By.XPATH, '//*[@id="App"]/div[4]/div/div/div/footer/div/button[2]').click() # Aceptamos las cookies
    except:
        pass

    time.sleep(5)

    for a in range(2):
        scroll()
        time.sleep(2)
    print("\n")
    tiempo_publicacion = navegador.find_elements(By.CLASS_NAME, "re-CardTimeAgo")
    anuncio = navegador.find_elements(By.CLASS_NAME, "re-CardPackMinimal-info-container")
    anuncios = []

    try:
        for a in range(len(tiempo_publicacion)):
            
            titulo = anuncio[a].get_attribute("title")

            if tiempo_publicacion[a].text == "Novedad":
                
                enlace = anuncio[a].get_attribute("href")
                
                anuncios.append(titulo)
                anuncios.append(enlace)
    except:
        pass

    return anuncios

def buscar_pisos_idealista():
    for a in range(2):
        scroll()
        time.sleep(2)

    print("\n")

    tiempo_publicacion = navegador.find_elements(By.CLASS_NAME, "txt-highlight-red")
    anuncio = navegador.find_elements(By.CLASS_NAME, "item-info-container")
    anuncios = []

    for a in range(len(tiempo_publicacion)):

        titulo = anuncio[a].get_attribute("title")
        enlace = anuncio[a].get_attribute("href")
        
        anuncios.append(titulo)
        anuncios.append(enlace)

    return anuncios

def buscar_pisos_habitaclia():
    navegador.find_element(By.XPATH, '//*[@id="legalCookies"]/div/div/div/footer/div/button[2]').click() # Aceptamos las cookies
    
    time.sleep(5)

    for a in range(2):
        scroll()
        time.sleep(2)

    print("\n")

    enlaces = []
    tiempo_publicacion = navegador.find_elements(By.CLASS_NAME, "list-item-date")
    titulos = navegador.find_elements(By.CLASS_NAME, "list-item-title")
    anuncios = []

    for a in range(len(titulos)):
        enlaces.append(titulos[a].find_element(By.TAG_NAME,"a"))

    for a in range(len(tiempo_publicacion)):
        
        titulo = titulos[a].text
        enlace = enlaces[a].get_attribute("href")
        
        if (tiempo_publicacion[a].text.find("minutos") > -1 or tiempo_publicacion[a].text.find("horas") > -1):
            
            anuncios.append(titulo)
            anuncios.append(enlace)
    
    return anuncios

def buscar_pisos_yaencontre():
    try:
        navegador.find_element(By.XPATH, '//*[@id="didomi-notice-agree-button"]').click() # Aceptamos las cookies
    except:
        pass

    time.sleep(5)

    for a in range(2):
        scroll()
        time.sleep(2)
    print("\n")

    titulos = navegador.find_elements(By.CLASS_NAME, "title")
    enlaces = []
    anuncios = []
    
    for a in range(len(titulos)):
        enlaces.append(titulos[a].find_element(By.TAG_NAME,"a"))
    
    for a in range(6):
        titulo = enlaces[a].get_attribute("title")
        enlace = enlaces[a].get_attribute("href")

        anuncios.append(titulo)
        anuncios.append(enlace)
    
    return anuncios

def buscar_pisos_pisoscom():
    try:
        navegador.find_element(By.XPATH, '//*[@id="didomi-notice-agree-button"]').click() # Aceptamos las cookies
    except:
        pass

    time.sleep(5)

    for a in range(2):
        scroll()
        time.sleep(2)

    print("\n")

    titulos = navegador.find_elements(By.CLASS_NAME, "ad-preview__title")
    tiempo_publicacion = navegador.find_elements(By.CLASS_NAME,"ad-preview__product-tag--date")

    for a in range(len(titulos)):
        titulo = titulos[a].text
        enlace = titulos[a].get_attribute("href")
        anuncios = []

        if tiempo_publicacion[a].text.find("minutos") > -1:
            anuncios.append(titulo)
            anuncios.append(enlace)
            
    return anuncios

def selenium_close():
    navegador.close() # Cerramos el navegador de selenium