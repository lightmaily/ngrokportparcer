from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import time

a = 0
while a <= 3:
    time.sleep(1)
    print('''
Перед тем как начать использовать данное приложение. 
Убедитесь в том что в папке, где вы открывайте данное приложение, 
есть ChromeDriver или ChromeDriver.exe 
Скачать можно по этой ссылке:
https://chromedriver.chromium.org/home
    \n
    ''')

    a += 1

driver = webdriver.Chrome()
try:
    driver.get("http://127.0.0.1:4040/inspect/http")
except:
    driver.get("http://127.0.0.1:4041/inspect/http")

elems = driver.find_elements(by=By.XPATH, value="//a[@href]")

elemList = []
for elem in elems:
    elemList.append(elem.get_attribute("href"))

sortedList = re.findall(r'tcp://[1-9].tcp.eu.ngrok.io:[1-9]*', elemList[4])
sortedList2 = re.findall(r'tcp://[1-9].tcp.eu.ngrok.io:(\w[1-9]+)?', elemList[4])
without = sortedList2[0]
print(sortedList2)
with open("ServerConfig.txt", mode='w', encoding='utf-8') as e:
    e.write('''general {

    ##########################################################################################################
    # generalconfig
    #--------------------------------------------------------------------------------------------------------#
    # This is the general config of ModularVoiceChat
    ##########################################################################################################

    generalconfig {
        # This field is optionnal, but may correct some issue with connecting to voice-server!
        # By providing an given hostname you are assured that all players use the same.
        S:forcedHostname=

        # The vocal-server port
        I:port=%s

        # Define if the micro on the speaking-players will be rendered.
        B:showWhoSpeak=false

        ##########################################################################################################
        # dispatcher
        #--------------------------------------------------------------------------------------------------------#
        # The used voice-dispatcher
        ##########################################################################################################

        dispatcher {
            # The DispatchType
            #  - "distanced" for a distance-based voice-dispatch
            #  - "global" for a global, to all players, voice-dispatch
            S:dispatchType=distanced
            B:fadeOut=true
            I:maxDistance=15
        }

    }

}
''' % (without))
