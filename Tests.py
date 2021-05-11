import pytest
from YandexPages import SearchTensor

#Поиск в яндексе
def test_search_word(browser):
    yandex_main = SearchTensor(browser)
    yandex_main.go_to_site()
    yandex_main.enter_word("Тензор")
    yandex_main.check_suggest()
    yandex_main.click_Enter()
    yandex_main.check_resulttable()
    items = yandex_main.check_refs_in_result()
    if "tensor.ru" not in items:
        raise Exception('ссылки "tensor.ru" нет в первых 5 пунктах')

#Картинки в яндексе
def test_search_bild(browser):

    yandex_main = SearchTensor(browser)
    yandex_main.go_to_site()
    yandex_main.find_Bild()
    yandex_main.click_Bild()

    browser.switch_to.window(browser.window_handles[1])
    s = browser.current_url[:browser.current_url.find("?")]
    assert s == "https://yandex.ru/images/", "Не верный URL"

    categiry = yandex_main.click_First_Category()
    namecategory = categiry.get_attribute("data-grid-text")

    yandex_main.Check_Category(namecategory)
    yandex_main.click_First_Picture()

    save_Picture = yandex_main.continue_Open_Picture()
    yandex_main.Next_Picture()
    assert save_Picture != yandex_main.continue_Open_Picture(), "Картинка не изменилась при листании вперед"

    yandex_main.Back_Picture()
    assert save_Picture == yandex_main.continue_Open_Picture(), "Не вернулось к изначальной картинке"

