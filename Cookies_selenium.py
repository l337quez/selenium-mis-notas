# Me he basado en https://github.com/ArturSpirin/YouTube-WebDriver-Tutorials/blob/master/Cookies.py

# Este Scrip funciona siempre y cuando solo se este usando una sola cockie
# ingrese el correo y la clave para poder guardar la contraseña
#debes cambiar el xpat y la ur de la pagina que quieres guardar la cockie

#para guardar las cockies 
#save_cockies.py

import pickle
import pprint
import time
from selenium import webdriver

def save_cookies(driver, location):
    pickle.dump(driver.get_cookies(), open(location, "wb"))

#Es posible que desees eliminar las coockies antes de volver a guardarlas
#driver.delete_all_cookies()

#Guardamos las coockies en un archivo txt en la misma ruta donde colocamos el driver de chrome, bajar el driver
# Path where you want to save/load cookies to/from aka C:\my\fav\directory\cookies.txt
cookies_location = "C:\driver\cookies.txt"

# Initial load of the domain that we want to save cookies for
chrome= webdriver.Chrome(executable_path=r"C:\driver\chromedriver.exe")
chrome.get("https://mastodon.social/about")
    chrome.find_element_by_xpath("//*[@id='login_user_email']").send_keys("corero XXXXXXXXXX")
chrome.find_element_by_xpath("//*[@id='login_user_password']").send_keys("clave XXXXXXXXX")
chrome.find_element_by_xpath("//*[@id='login_new_user']/div[2]/button").click()
time.sleep(5)
save_cookies(chrome, cookies_location)

time.sleep(2)
pprint.pprint(chrome.get_cookies())
print ("=========================\n")
time.sleep(5)
chrome.quit()


#########################################################################################################

#load_cockies.py

import pickle
import pprint
import time
from selenium import webdriver


# Path where you want to save/load cookies to/from aka C:\my\fav\directory\cookies.txt
cookies_location = "C:\driver\cookies.txt"



def load_cookies(driver, location, url):
    cookies = pickle.load(open(location, "rb"))
    #driver.delete_all_cookies()
    # have to be on a page before you can add any cookies, any page - does not matter which
    driver.get("https://mastodon.social/about" if url is None else url)
"""     for cookie in cookies:
        print(cookie)
        if isinstance(cookie.get('expiry'), float):#Checks if the instance expiry a float 
            cookie['expiry'] = int(cookie['expiry'])# it converts expiry cookie to a int  """
        
        #if cookie['name']=="_mastodon_session":
    driver.add_cookie(cookie)
        
        #if cookie['name'] : '_mastodon_session'
        #print(str(driver.add_cookie(cookie[1])))

#chrome.get("https://mastodon.social/about")
chrome = webdriver.Chrome(executable_path=r"C:\driver\chromedriver.exe")
load_cookies(chrome, cookies_location,"https://mastodon.social/about")
