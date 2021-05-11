from BaseApp import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest

#список локаторов
class YandexSeacrhLocators:
    LOCATOR_SEARCH_FIELD = (By.ID, "text")
    LOCATOR_SUGGEST = (By.XPATH, "//ul[@class='mini-suggest__popup-content']/li")
    LOCATOR_RESULT_TABLE = (By.XPATH, "//ul[@class='serp-list serp-list_left_yes']/li")
    LOCATOR_LINKS = (By.CSS_SELECTOR, "#search-result > .serp-item a.link > b")


    LOCATOR_BILD = (By.XPATH, "//a[@data-id='images']")
    LOCATOR_FIRST_CATEGORY = (By.XPATH, "//div[@class ='PopularRequestList-Item PopularRequestList-Item_pos_0']")
    LOCATOR_SEARCH_FIELD_BILD = (By.NAME, "text")
    LOCATOR_FIRST_PICTURE = (By.XPATH, "//div[@class='serp-item__preview']")
    LOCATOR_CONTINUE_PICTURE = (By.XPATH, "//img[@class ='MMImage-Origin']")
    LOCATOR_NEXT = (By.XPATH, "//div[@class='MediaViewer-LayoutScene MediaViewer_theme_fiji-LayoutScene']/div[4]/i")
    LOCATOR_BACK = (By.XPATH, "//div[@class='MediaViewer-LayoutScene MediaViewer_theme_fiji-LayoutScene']/div[1]/i")

#методы для работы с элементами страницы
class SearchTensor(BasePage):

# Поиск в яндекс
    def enter_word(self, word):
        search_field = self.find_element(YandexSeacrhLocators.LOCATOR_SEARCH_FIELD)
        search_field.clear()
        search_field.send_keys(word)
        return search_field

    def check_suggest(self):
        return self.find_elements(YandexSeacrhLocators.LOCATOR_SUGGEST)

    def click_Enter(self):
        return self.find_element(YandexSeacrhLocators.LOCATOR_SEARCH_FIELD).send_keys(Keys.ENTER)

    def check_resulttable(self):
        return self.find_elements(YandexSeacrhLocators.LOCATOR_RESULT_TABLE)

    def check_refs_in_result(self):
        links = self.find_elements(YandexSeacrhLocators.LOCATOR_LINKS)
        items = [elem.text.strip() for elem in links[:5]]
        return items


#Картинки в яндекс
    def find_Bild(self):
        return self.find_element(YandexSeacrhLocators.LOCATOR_BILD)

    def click_Bild(self):
        return self.find_element(YandexSeacrhLocators.LOCATOR_BILD).click()

    def click_First_Category(self):
         category = self.find_element(YandexSeacrhLocators.LOCATOR_FIRST_CATEGORY)
         category.click()
         return category

    def Check_Category(self, namecategory):
         Field_Bild = self.find_element(YandexSeacrhLocators.LOCATOR_SEARCH_FIELD_BILD)
         assert Field_Bild.get_attribute('value') == namecategory, "Не верная категория в строке поиска"

    def click_First_Picture(self):
        return self.find_element(YandexSeacrhLocators.LOCATOR_FIRST_PICTURE).click()

    def continue_Open_Picture(self):
        return self.find_element(YandexSeacrhLocators.LOCATOR_CONTINUE_PICTURE).get_attribute("currentSrc")

    def Next_Picture(self):
        self.find_element(YandexSeacrhLocators.LOCATOR_NEXT).click()

    def Back_Picture(self):
        self.find_element(YandexSeacrhLocators.LOCATOR_BACK).click()



