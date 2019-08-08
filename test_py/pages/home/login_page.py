from base.basepage import BasePage
import utilities.custom_logger as cl
import logging
from selenium.webdriver.common.action_chains import ActionChains
import time
import re
class LoginPage(BasePage):
    log = cl.customLogger(logging.DEBUG)
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver
    #locators
    _popup="/html/body/div[2]/div/div/button"
    _electronics="//*[@id='container']/div/div[2]/div/ul/li[1]/span"
    _Pixel="Pixel 3a | 3a XL"#text
    _fristphone= "(//div/img[@class='_1Nyybr  _30XEf0'])[1]"
    _cart="//*[@id='container']/div/div[3]/div[2]/div[1]/div[1]/div[2]/div/ul/li[1]/button"
    _price="//div[@class='hJYgKM']/span"
    _plus="//*[@id='container']/div/div[2]/div[2]/div/div[1]/div/div[2]/div/div[2]/div[1]/div/button[2]"

    #assignment2
    _search="twotabsearchtextbox"#id
    _searchtext="iPhone 7 32 gb(black)"
    _searchbtn="nav-input"#class
    _matchingphone="Apple iPhone 7 (32GB) - Black"#link
    _priceofiphone="priceblock_ourprice"#gettext
    _flipkartsearch="//*[@id='container']/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input"
    _clicksearchonflpkrt="//*[@id='container']/div/div[1]/div[1]/div[2]/div[2]/form/div/button"
    _matchingphone2="//div[contains(text(),'Apple iPhone 7 (Black, 32 GB)')]"
    _priceinflipkart="//*[@id='container']/div/div[3]/div[2]/div[1]/div[2]/div[2]/div/div[4]/div[1]/div/div[1]"#gettext

    def clickpopup(self):
        self.elementClick(locator=self._popup,locatorType="xpath")
    def movetoele(self):
        element1=self.getElement(locator=self._electronics,locatorType="xpath")
        action = ActionChains(self.driver)
        action.move_to_element(element1).perform()
        time.sleep(5)
    def clickpixel(self):
        self.elementClick(self._Pixel,locatorType="link")
    def clickfirstphone(self):
        self.elementClick(self._fristphone,locatorType="xpath")
    def addtocart(self):
        self.elementClick(self._cart,locatorType="xpath")
    def getprice(self):
        price=self.getText(self._price,locatorType="xpath")
        print(price)
        return price
    def clickplus(self):
        self.elementClick(self._plus,locatorType="xpath")

    #assignemnt2
    def searchforphone(self):
        self.sendKeys(data=self._searchtext,locator=self._search,locatorType="id")
    def clicksearch(self):
        self.elementClick(locator=self._searchbtn,locatorType="class")
    def clickmatchingphone(self):
        self.elementClick(locator=self._matchingphone,locatorType="link")
    def getpriceamazn(self):
        pamzn=self.getText(locator=self._priceofiphone,locatorType="id")
        v = pamzn.replace('₹', '')

        j = v.replace(',', '')
        k=j.replace(' ','')
        return int(float(k))

    def serchforphoneinflpkat(self):
        self.sendKeys(data=self._searchtext,locator=self._flipkartsearch,locatorType="xpath")
    def clicksearchinflp(self):
        self.elementClick(locator=self._clicksearchonflpkrt,locatorType="xpath")
    def clickonphone(self):
        self.elementClick(locator=self._matchingphone2,locatorType="xpath")
    def priceonflpkart(self):
        pfpkt=self.getText(locator=self._priceinflipkart,locatorType="xpath")
        n = pfpkt.replace('₹', '')
        m = n.replace(',', '')
        return int(m)
    def login(self):
        time.sleep(5)
        self.clickpopup()
        time.sleep(2)
        self.movetoele()
        time.sleep(2)
        self.clickpixel()
        self.clickfirstphone()
        time.sleep(2)
        self.switchtonewwindow()
        self.addtocart()
        time.sleep(2)
        result=self.getprice()
        self.clickplus()
        print("Assignment 1 completed")
        self.driver.get("https://amazon.in/")
        self.searchforphone()
        self.clicksearch()
        self.clickmatchingphone()
        self.switchtonewwindow()
        priceofamazon=self.getpriceamazn()


        print(priceofamazon)
        self.driver.get("https://flipkart.com/")
        self.clickpopup()
        self.serchforphoneinflpkat()
        self.clicksearchinflp()
        self.clickonphone()
        self.switchtonewwindow()
        priceofflipkar=self.priceonflpkart()

        if priceofflipkar > priceofamazon:
            print("amazon cheap")
        elif priceofflipkar < priceofamazon:
            print("flpkart cheap")
        else:
            print("both are same")
