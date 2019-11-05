# https://store.playstation.com/en-us/home/games
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def GamePriceCheck(driver):
    try:
        gameTitleName = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.grid-cell__title')))
        mainPageTitles = []
        for title in gameTitleName:
            mainPageTitles.append(title.text)

        mainPagePrice = []
        gameMainPagePrice = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.price-display__price')))
        for price in gameMainPagePrice:
            mainPagePrice.append(price.text)

        # there is 12 thumbnails; however, only 8 games, the other 4 are add-on. I'll write another script to validate those
        # for k in range(0, 7):
        for k in range(len(gameTitleName)):
            # Get list of title names, links, Price on the home page:
            divLinks = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.grid-cell')))
            driver.implicitly_wait(30)
            divLinks[k].click()

            secondPageGameTitle = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.pdp__title')))[0].text
            secondPageGamePrice = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.price-display__price')))[0].text

            titleCheck = mainPageTitles[k] == secondPageGameTitle
            priceCheck = mainPagePrice[k] == secondPageGamePrice

            print(str(k+1) + ' : ' + mainPageTitles[k] + ' Title Check: ' + str(titleCheck))
            print(str(k+1) + ' : ' + mainPagePrice[k] + ' Price Check: ' + str(priceCheck))

            driver.back()

    finally:
        driver.quit()
        print('done')


browser = webdriver.Firefox(executable_path='./geckodriver')
wait = WebDriverWait(browser, 5)
browser.get('https://store.playstation.com/en-us/home/games')

GamePriceCheck(browser)

