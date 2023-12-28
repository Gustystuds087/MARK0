import config
from selenium import webdriver 
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.headless =True
driver = webdriver.Chrome('C:\\Users\\Anshul\\OneDrive\\Desktop\\MARK0\\spotify_shortcut\\chromedriver.exe')


url ='https://accounts.spotify.com/en/login?continue=https'


def login(Email,Password):
    # load link 
    driver.get(url)
    #username
    driver.find_element(By.XPATH,'//*[@id="login-username"]').send_keys(Email)
    #Password
    driver.find_element(By.XPATH,'//*[@id="login-password"]').send_keys(Password)
    #button
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/div/div[2]/div[3]/div[2]/button/div[1]/p').click()
    

login(config.username,config.password)
