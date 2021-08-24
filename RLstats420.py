#Il faut installer selenium (avec pip par exemple : pip install selenium) et placer chromedriver.exe (je le mettrai sur github) dans le meme dossier que du fichier .py
from selenium.webdriver.chrome.options import Options 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def infosJoueurRL(joueur): # pseudo du joueur en parametre (str), je sais pas comment marche ta base de données pour stocker les pseudos
    chrome_options = Options() 
    chrome_options.add_argument("--headless") # On va lancer le navigateur Chrome en headless, i.e. sans interface graphique
    driver = webdriver.Chrome(options=chrome_options)

    driver.get("https://rocketleague.tracker.network/rocket-league/profile/epic/"+joueur+"/overview") #connexion au site
    wait = WebDriverWait(driver, 5)
    nb_vict = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#app > div.trn-wrapper > div.trn-container > div > main > div.content.no-card-margin > div.site-container.trn-grid.trn-grid--vertical.trn-grid--small > div.trn-grid__sidebar-left > aside > div.overview.card.bordered.header-bordered.responsive > div > div:nth-child(1) > div > div.numbers > span.value")))
    nb_vict_fr=""
    for char in nb_vict.text:
        if char!=',':
            nb_vict_fr=nb_vict_fr+char

    return "Nombre de victoires du joueur: " + nb_vict_fr + "\n hihihiih"

print(infosJoueurRL("Aotrix"))