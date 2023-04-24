import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from page_object import Locators
from page_object import SearchHelper
from selenium.webdriver.common.by import By
import allure
from allure_commons.types import AttachmentType

exec_path = '/Users/anastasia/Desktop/Graduate_work/chromedriver'


@allure.title('Web tests Zoobazar.by')
class TestPageSearch:
    def setup(self):
        self.driver = webdriver.Chrome(executable_path=exec_path)

    def teardown(self):
        self.driver.quit()


@allure.feature('Header tests')
@allure.title('Card activation')
def test_check_card_activation(browser):
    zoobazar_main_page = SearchHelper(browser)
    zoobazar_main_page.go_to_site()
    zoobazar_main_page.click_element(Locators.LOCATOR_CARD_ACTIVATION)
    time.sleep(4)
    title_activation = zoobazar_main_page.get_text_from_element(Locators.TITLE_CARD_ACTIVATION)
    time.sleep(4)
    with allure.step("Скриншот"):
        allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    assert title_activation == "Активация карты"


@allure.feature('Header tests')
@allure.title('Check cart button')
def test_check_cart_button(browser):
    zoobazar_main_page = SearchHelper(browser)
    zoobazar_main_page.go_to_site()
    zoobazar_main_page.find_element(Locators.LOCATOR_CART_BUTTON)
    time.sleep(3)
    zoobazar_main_page.click_element(Locators.LOCATOR_CART_BUTTON)
    time.sleep(5)
    with allure.step("Скриншот"):
        allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    assert 'Корзина' in browser.title


@allure.feature('Header tests')
@allure.title('Check search button')
def test_zoobazar_search(browser):
    zoobazar_main_page = SearchHelper(browser)
    zoobazar_main_page.go_to_site()
    time.sleep(3)
    zoobazar_main_page.click_element(Locators.LOCATOR_SEARCH_FIELD)
    time.sleep(5)
    with allure.step("Скриншот"):
        allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    zoobazar_main_page.enter_word("Корм")


@allure.feature('Header tests')
@allure.title('Check pick up button')
def test_check_pick_up_button(browser):
    zoobazar_main_page = SearchHelper(browser)
    browser.maximize_window()
    zoobazar_main_page.go_to_site()
    zoobazar_main_page.find_element(Locators.LOCATOR_PICKUP_PIONTS_BUTTON)
    time.sleep(3)
    zoobazar_main_page.click_element(Locators.LOCATOR_PICKUP_PIONTS_BUTTON)
    time.sleep(5)
    with allure.step("Скриншот"):
        allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    assert 'Пункты самовывоза | Zoobazar' in browser.title


@allure.feature('Header tests')
@allure.title('Check payment button')
def test_check_payment_button(browser):
    zoobazar_main_page = SearchHelper(browser)
    zoobazar_main_page.go_to_site()
    zoobazar_main_page.find_element(Locators.LOCATOR_DELIVERY_BUTTON)
    time.sleep(3)
    zoobazar_main_page.click_element(Locators.LOCATOR_DELIVERY_BUTTON)
    time.sleep(5)
    with allure.step("Скриншот"):
        allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    assert 'Доставка и оплата' in browser.title


@allure.feature('Header tests')
@allure.title('Check delivery button')
def test_check_delivery_button(browser):
    zoobazar_main_page = SearchHelper(browser)
    zoobazar_main_page.go_to_site()
    zoobazar_main_page.find_element(Locators.LOCATOR_DELIVERY_BUTTON)
    time.sleep(3)
    zoobazar_main_page.click_element(Locators.LOCATOR_DELIVERY_BUTTON)
    time.sleep(5)
    with allure.step("Скриншот"):
        allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    assert 'Доставка и оплата' in browser.title


@allure.feature('Header tests')
@allure.title('Check favorites button')
def test_check_favorites_button(browser):
    zoobazar_main_page = SearchHelper(browser)
    zoobazar_main_page.go_to_site()
    zoobazar_main_page.find_element(Locators.LOCATOR_FAVORITES_BUTTON)
    time.sleep(3)
    zoobazar_main_page.click_element(Locators.LOCATOR_FAVORITES_BUTTON)
    time.sleep(5)
    with allure.step("Скриншот"):
        allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    assert 'https://zoobazar.by/personal/favorites/' in browser.current_url


@allure.feature('Header tests')
@allure.title('Check login button')
def test_check_login_button(browser):
    zoobazar_main_page = SearchHelper(browser)
    browser.maximize_window()
    zoobazar_main_page.go_to_site()
    time.sleep(4)
    zoobazar_main_page.click_element(Locators.LOCATOR_LOGIN)
    time.sleep(3)
    logg = zoobazar_main_page.get_text_from_element(Locators.LOCATOG_LOGGIN)
    time.sleep(3)
    with allure.step("Скриншот"):
        allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    assert logg == "Авторизация"


@allure.feature('Choose category tests')
@allure.title('Choose category(Cats_page)')
def test_choose_caterogy(browser):
    zoobazar_main_page = SearchHelper(browser)
    zoobazar_main_page.go_to_site()
    zoobazar_main_page.click_element(Locators.LOCATOR_MAIN_MENU_CATS)
    zoobazar_main_page.click_element(Locators.LOCATOR_CATEGORY_BUTTON)
    zoobazar_main_page.click_element(Locators.LOCATOR_CATEGORY_MAX_BENEFITS)
    with allure.step("Скриншот"):
        allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    assert 'https://zoobazar.by/catalog/koshki/?sort=best_sale&order=desc' in browser.current_url
    zoobazar_main_page.click_element(Locators.LOCATOR_CATEGORY_BUTTON)
    zoobazar_main_page.click_element(Locators.LOCATOR_CATEGORY_MIN_PRICE)
    with allure.step("Скриншот"):
        allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    assert 'https://zoobazar.by/catalog/koshki/?sort=price&order=asc' in browser.current_url
    zoobazar_main_page.click_element(Locators.LOCATOR_CATEGORY_BUTTON)
    zoobazar_main_page.click_element(Locators.LOCATOR_CATEGORY_MAX_PRICE)
    with allure.step("Скриншот"):
        allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    assert 'https://zoobazar.by/catalog/koshki/?sort=price&order=desc' in browser.current_url
    zoobazar_main_page.click_element(Locators.LOCATOR_CATEGORY_BUTTON)
    zoobazar_main_page.click_element(Locators.LOCATOR_CATEGORY_POPULAR)
    with allure.step("Скриншот"):
        allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    assert 'https://zoobazar.by/catalog/koshki/?sort=popular&order=desc' in browser.current_url
    zoobazar_main_page.click_element(Locators.LOCATOR_CATEGORY_BUTTON)
    zoobazar_main_page.click_element(Locators.LOCATOR_CATEGORY_MOST_POPULAR)
    with allure.step("Скриншот"):
        allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    assert 'https://zoobazar.by/catalog/koshki/?sort=hit&order=desc' in browser.current_url
    zoobazar_main_page.click_element(Locators.LOCATOR_CATEGORY_BUTTON)
    zoobazar_main_page.click_element(Locators.LOCATOR_CATEGORY_PROMOTIONS)
    with allure.step("Скриншот"):
        allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    assert 'https://zoobazar.by/catalog/koshki/?sort=sale&order=desc' in browser.current_url

@allure.feature('Check filters (Cats page)')

@allure.title('Check_base filters')
def test_check_filters_cats(browser):
    zoobazar_main_page = SearchHelper(browser)
    zoobazar_main_page.go_to_site()
    zoobazar_main_page.click_element(Locators.LOCATOR_MAIN_MENU_CATS)
    browser.execute_script("window.scrollTo(0, 950)")
    zoobazar_main_page.click_element(Locators.LOCATOR_CHECKBOX_BENEFITS)
    zoobazar_main_page.click_element(Locators.LOCATOR_CHECKBOX_ARE_AVAILABLE)
    zoobazar_main_page.click_element(Locators.LOCATOR_CHECKBOX_ONLY_ONLAIN)
    zoobazar_main_page.click_element(Locators.LOCATOR_SEARCHING_RESULT)
    time.sleep(6)
    button_benefits = browser.find_element\
        (By.XPATH, '//button[@aria-label="Акции и скидки"]').text
    button_only_online = browser.find_element\
        (By.XPATH, '//button[@aria-label="% только онлайн"]').text
    button_is_available = browser.find_element\
        (By.XPATH, '//div[@class="filter-rounded-tags__item filter-rounded-tags__item--active"][3]/button').text
    with allure.step("Скриншот"):
        allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    assert button_benefits == "Акции и скидки"
    with allure.step("Скриншот"):
        allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    assert button_only_online == "% только онлайн"
    with allure.step("Скриншот"):
        allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    assert button_is_available == "Есть в наличии"


@allure.feature('Check filters (Cats page)')
@allure.title('Check weight filter')
def test_check_filter_weight(browser):
    zoobazar_main_page = SearchHelper(browser)
    zoobazar_main_page.go_to_site()
    zoobazar_main_page.click_element(Locators.LOCATOR_MAIN_MENU_CATS)
    time.sleep(4)
    zoobazar_main_page.click_element(Locators.LOCATOR_DRY_FOOD)
    browser.execute_script("window.scrollTo(0, 900)")
    zoobazar_main_page.click_element(Locators.LOCATOR_MIN_WEIGHT)
    zoobazar_main_page.click_element(Locators.LOCATOR_MIN_WEIGHT_DIGIT)
    zoobazar_main_page.click_element(Locators.LOCATOR_MAX_WEIGHT)
    time.sleep(3)
    zoobazar_main_page.click_element(Locators.LOCATOR_MAX_WEIGHT_DIGIT)
    time.sleep(4)
    zoobazar_main_page.click_element(Locators.LOCATOR_SHOW_RESULTS)
    time.sleep(3)
    with allure.step("Скриншот"):
        allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    assert 'https://zoobazar.by/catalog/koshki/sukhie_korma/filter/weight-from-0.19-to-0.35/apply/'\
           in browser.current_url


@allure.feature('Check filters (Cats page)')
@allure.title('Check price filter')
def test_check_filter_price(browser):
    zoobazar_main_page = SearchHelper(browser)
    zoobazar_main_page.go_to_site()
    zoobazar_main_page.click_element(Locators.LOCATOR_MAIN_MENU_CATS)
    time.sleep(2)
    zoobazar_main_page.click_element(Locators.LOCATOR_DRY_FOOD)
    browser.execute_script("window.scrollTo(0, 900)")
    time.sleep(2)
    min_price = browser.find_element(By.ID, 'arrFilter_P5_MIN')
    min_price.send_keys('1')
    max_price = browser.find_element(By.ID, 'arrFilter_P5_MAX')
    max_price.send_keys('10')
    zoobazar_main_page.click_element(Locators.LOCATOR_SHOW_RESULTS)
    with allure.step("Скриншот"):
        allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    assert 'https://zoobazar.by/catalog/koshki/sukhie_korma/filter/price-discount_price-from-1-to-10/apply/'\
           in browser.current_url


@allure.feature('Check filters (Cats page)')
@allure.title('Check brands filter')
def test_check_filter_brands(browser):
    zoobazar_main_page = SearchHelper(browser)
    zoobazar_main_page.go_to_site()
    zoobazar_main_page.click_element(Locators.LOCATOR_MAIN_MENU_CATS)
    time.sleep(2)
    zoobazar_main_page.click_element(Locators.LOCATOR_DRY_FOOD)
    zoobazar_main_page.click_element(Locators.LOCATOR_FIRST_CHECKBOX_BRANDS)
    zoobazar_main_page.click_element(Locators.LOCATOR_SHOW_MORE_BRANDS)
    zoobazar_main_page.click_element(Locators.LOCATOR_MEDIUM_CHECKBOX_BRANDS)
    time.sleep(3)
    zoobazar_main_page.click_element(Locators.LOCATOR_SHOW_RESULTS)
    time.sleep(4)
    with allure.step("Скриншот"):
        allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    assert 'https://zoobazar.by/catalog/koshki/sukhie_korma/filter/brand-is-acana-or-chicopee/apply/'\
           in browser.current_url


@allure.feature('Check filters (Cats page)')
@allure.title('Check feed filter')
def test_check_filter_type_of_feed(browser):
    zoobazar_main_page = SearchHelper(browser)
    zoobazar_main_page.go_to_site()
    zoobazar_main_page.click_element(Locators.LOCATOR_MAIN_MENU_CATS)
    time.sleep(2)
    zoobazar_main_page.click_element(Locators.LOCATOR_DRY_FOOD)
    time.sleep(3)
    zoobazar_main_page.click_element(Locators.LOCATOR_TYPE_OF_FEED_BUTTON)
    zoobazar_main_page.click_element(Locators.LOCATOR_DRY_FEED_CHECKBOX)
    zoobazar_main_page.click_element(Locators.LOCATOR_SHOW_RESULTS)
    with allure.step("Скриншот"):
        allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    assert 'https://zoobazar.by/catalog/koshki/sukhie_korma/filter/' \
           'vid_korma-is-1152f3fe-b468-11ea-a4c1-0050568f1acb/apply/' in browser.current_url


@allure.feature('Check filters (Cats page)')
@allure.title('Check special series filter')
def test_check_filter_special_series(browser):
    zoobazar_main_page = SearchHelper(browser)
    zoobazar_main_page.go_to_site()
    browser.maximize_window()
    zoobazar_main_page.click_element(Locators.LOCATOR_MAIN_MENU_CATS)
    time.sleep(3)
    zoobazar_main_page.click_element(Locators.LOCATOR_DRY_FOOD)
    browser.execute_script("window.scrollTo(0, 650)")
    zoobazar_main_page.click_element(Locators.LOCATOR_FILTER_SPEC_SERIES_BUTTON)
    zoobazar_main_page.click_element(Locators.LOCATOR_GLUTEN_FREE_CHECKBOX)
    time.sleep(2)
    zoobazar_main_page.click_element(Locators.LOCATOR_HOLISTIK_CHECKBOX)
    time.sleep(2)
    zoobazar_main_page.click_element(Locators.LOCATOR_SHOW_RESULTS)
    time.sleep(2)
    gluten_free = browser.find_element(By.XPATH, '//button[@aria-label="Безглютеновый"]').text
    holistik = browser.find_element(By.XPATH, '//button[@aria-label="Холистик"]').text
    with allure.step("Скриншот"):
        allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    assert "Безглютеновый" in gluten_free
    with allure.step("Скриншот"):
        allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    assert 'Холистик' in holistik


@allure.feature('Check filters (Cats page)')
@allure.title('Check packing filter')
def test_check_filter_packing(browser):
    zoobazar_main_page = SearchHelper(browser)
    zoobazar_main_page.go_to_site()
    zoobazar_main_page.click_element(Locators.LOCATOR_MAIN_MENU_CATS)
    time.sleep(3)
    zoobazar_main_page.click_element(Locators.LOCATOR_DRY_FOOD)
    browser.execute_script("window.scrollTo(0, 650)")
    zoobazar_main_page.click_element(Locators.LOCATOR_TYPE_OF_PACKING)
    time.sleep(3)
    zoobazar_main_page.click_element(Locators.LOCATOR_TYPE_OF_PACKING_BOX)
    time.sleep(3)
    zoobazar_main_page.click_element(Locators.LOCATOR_TYPE_OF_PACKING_BAG)
    time.sleep(3)
    zoobazar_main_page.click_element(Locators.LOCATOR_SHOW_RESULTS)
    with allure.step("Скриншот"):
        allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    assert "https://zoobazar.by/catalog/koshki/sukhie_korma/filter/" \
           "tip_upakovki-is-9726308d-bf8c-11ea-a4c7-0050568f1acb-or-a010d7c3-f8ee-11ea-a4d7-0050568fefb1/apply/"\
           in browser.current_url


@allure.feature('Add to cart')
def test_add_to_cart(browser):
    zoobazar_main_page = SearchHelper(browser)
    zoobazar_main_page.go_to_site()
    zoobazar_main_page.click_element(Locators.LOCATOR_MAIN_MENU_CATS)
    browser.execute_script("window.scrollTo(0, 650)")
    zoobazar_main_page.click_element(Locators.LOCATOR_CART_ICON1)
    zoobazar_main_page.click_element(Locators.LOCATOR_PICKUP_PIONTS_BUTTON2)
    zoobazar_main_page.click_element(Locators.LOCATOR_CONFIRM_ADDRESS)
    zoobazar_main_page.click_element(Locators.LOCATOR_CLOSE_ADV)
    zoobazar_main_page.click_element(Locators.LOCATOR_CART_ICON2)
    zoobazar_main_page.click_element(Locators.LOCATOR_CART_ICON3)
    zoobazar_main_page.click_element(Locators.LOCATOR_CART_BUTTON)
    goods_in_cart = zoobazar_main_page.get_text_from_element(Locators.LOCATOR_AMOUNT_OF_GOODS)
    with allure.step("Скриншот"):
        allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    assert '3 шт' in goods_in_cart


@allure.feature('Add to favorites')
def test_add_to_favorites(browser):
    zoobazar_main_page = SearchHelper(browser)
    browser.maximize_window()
    zoobazar_main_page.go_to_site()
    zoobazar_main_page.click_element(Locators.LOCATOR_MAIN_MENU_CATS)
    browser.execute_script("window.scrollTo(0, 650)")
    zoobazar_main_page.click_element(Locators.LOCATOR_ADD_TO_FAVORITES1)
    zoobazar_main_page.click_element(Locators.LOCATOR_ADD_TO_FAVORITES2)
    zoobazar_main_page.click_element(Locators.LOCATOR_ADD_TO_FAVORITES3)
    time.sleep(4)
    small_icon_count = browser.find_element(By.XPATH, '//a[@title="Избранное"]/span').text
    with allure.step("Скриншот"):
        allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    assert small_icon_count == '3'
    zoobazar_main_page.click_element(Locators.LOCATOR_FAVORITES_BUTTON)
    items_count = browser.find_element(By.XPATH, '//span[@class="items-count"]').text
    with allure.step("Скриншот"):
        allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    assert items_count == '3'


@allure.feature('Сontact form tests')
@allure.story('Check chat messengers')
@allure.title("Check Live chat")
def test_live_chat_icon(browser):
    zoobazar_main_page = SearchHelper(browser)
    browser.maximize_window()
    zoobazar_main_page.go_to_site()
    zoobazar_main_page.click_element(Locators.LOCATOR_CHAT_ICON)
    time.sleep(4)
    zoobazar_main_page.click_element(Locators.LOCATOR_LIVE_CHAT)
    time.sleep(3)
    tooltip = zoobazar_main_page.get_text_from_element(Locators.LOCATOR_TITLE_LIVE_CHAT)
    with allure.step("Скриншот"):
        allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    assert tooltip == 'Форма обратной связи'


@allure.feature('Сontact form tests')
@allure.story('Check chat messengers')
@allure.title("Check Viber chat")
def test_viber_chat_icon(browser):
    zoobazar_main_page = SearchHelper(browser)
    browser.maximize_window()
    zoobazar_main_page.go_to_site()
    zoobazar_main_page.click_element(Locators.LOCATOR_CHAT_ICON)
    time.sleep(4)
    viber = browser.find_element(By.XPATH, '//a[@href="viber://pa?chatURI=zoobazar"]')
    hover = ActionChains(browser).move_to_element(viber)
    hover.perform()
    viber_tooltip = zoobazar_main_page.get_text_from_element(Locators.LOCATOR_TOOLTIP_VIBER)
    with allure.step("Скриншот"):
        allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    assert viber_tooltip == 'Zoobazar'


@allure.feature('Сontact form tests')
@allure.story('Check chat messengers')
@allure.title("Check TG chat")
def test_telegram_chat_icon(browser):
    zoobazar_main_page = SearchHelper(browser)
    browser.maximize_window()
    zoobazar_main_page.go_to_site()
    zoobazar_main_page.click_element(Locators.LOCATOR_CHAT_ICON)
    time.sleep(4)
    tg = browser.find_element(By.XPATH, '//a[@href="https://t.me/zoobazar_by_feedback_bot"]')
    hover = ActionChains(browser).move_to_element(tg)
    hover.perform()
    tg_tooltip = zoobazar_main_page.get_text_from_element(Locators.LOCATOR_TOOLTIP_TELEGRAM)
    with allure.step("Скриншот"):
        allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    assert tg_tooltip == 'Zoobazar.by: Обратная связь'


@allure.feature('Сontact form tests')
@allure.story('Check chat messengers')
@allure.title("Check VK chat")
def test_vk_chat_icon(browser):
    zoobazar_main_page = SearchHelper(browser)
    browser.maximize_window()
    zoobazar_main_page.go_to_site()
    zoobazar_main_page.click_element(Locators.LOCATOR_CHAT_ICON)
    time.sleep(3)
    vk = browser.find_element(By.XPATH, '//a[@href="https://vk.me/club118986456"]')
    hover = ActionChains(browser).move_to_element(vk)
    hover.perform()
    vk_tooltip = zoobazar_main_page.get_text_from_element(Locators.LOCATOR_TOOLTIP_VK)
    with allure.step("Скриншот"):
        allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    assert vk_tooltip == 'Сеть зоомагазинов Zoobazar — Беларусь'


@allure.feature('Сontact form tests')
@allure.story('Check chat messengers')
@allure.title("Check OK chat")
def test_ok_chat_icon(browser):
    zoobazar_main_page = SearchHelper(browser)
    zoobazar_main_page.go_to_site()
    zoobazar_main_page.click_element(Locators.LOCATOR_CHAT_ICON)
    time.sleep(3)
    ok = browser.find_element(By.XPATH, '//a[@href="https://ok.ru/zoobazar.by"]')
    hover = ActionChains(browser).move_to_element(ok)
    hover.perform()
    ok_tooltip = zoobazar_main_page.get_text_from_element(Locators.LOCATOR_TOOLTIP_OK)
    time.sleep(3)
    with allure.step("Скриншот"):
        allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    assert ok_tooltip == 'Сеть зоомагазинов Zoobazar - Беларусь'


@allure.feature('Footer tests')
@allure.story('Footer menu: Company')
@allure.title('Check vacancies button')
def test_vacancies_button(browser):
    zoobazar_main_page = SearchHelper(browser)
    zoobazar_main_page.go_to_site()
    time.sleep(3)
    browser.execute_script("window.scrollTo(0, 3000)")
    zoobazar_main_page.click_element(Locators.LOCATOR_VACANCIES_BUTTON)
    time.sleep(5)
    with allure.step("Скриншот"):
        allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    assert 'https://zoobazar.by/vacancies/' in browser.current_url


@allure.feature('Footer tests')
@allure.story('Footer menu: Company')
@allure.title('Check about us button')
def test_about_us_button(browser):
    zoobazar_main_page = SearchHelper(browser)
    zoobazar_main_page.go_to_site()
    time.sleep(3)
    browser.execute_script("window.scrollTo(0, 3000)")
    zoobazar_main_page.click_element(Locators.LOCATOR_ABOUT_US_BUTTON)
    time.sleep(3)
    with allure.step("Скриншот"):
        allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    assert 'https://zoobazar.by/about/' in browser.current_url


@allure.feature('Footer tests')
@allure.story('Footer menu: Company')
@allure.title('Check our stories button')
def test_our_stores_button(browser):
    zoobazar_main_page = SearchHelper(browser)
    zoobazar_main_page.go_to_site()
    time.sleep(3)
    browser.execute_script("window.scrollTo(0, 3000)")
    zoobazar_main_page.click_element(Locators.LOCATOR_OUR_STORIES_BUTTON)
    time.sleep(4)
    with allure.step("Скриншот"):
        allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    assert 'https://zoobazar.by/shops/' in browser.current_url


@allure.feature('Footer tests')
@allure.story('Footer menu: Company')
@allure.title('Check pick up button')
def test_pick_up_button(browser):
    zoobazar_main_page = SearchHelper(browser)
    zoobazar_main_page.go_to_site()
    time.sleep(3)
    browser.execute_script("window.scrollTo(0, 3000)")
    zoobazar_main_page.click_element(Locators.LOCATOR_PICKUP_POINTS_BUTTON3)
    time.sleep(4)
    with allure.step("Скриншот"):
        allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    assert 'https://zoobazar.by/pickup/' in browser.current_url


@allure.feature('Footer tests')
@allure.story('Footer menu: Company')
@allure.title('Check delivery map button')
def test_delivery_map_button(browser):
    zoobazar_main_page = SearchHelper(browser)
    zoobazar_main_page.go_to_site()
    time.sleep(3)
    browser.execute_script("window.scrollTo(0, 3000)")
    zoobazar_main_page.click_element(Locators.LOCATOR_DELIVERY_BUTTON)
    time.sleep(4)
    with allure.step("Скриншот"):
        allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    assert 'https://zoobazar.by/pickup/' in browser.current_url


@allure.feature('Footer tests')
@allure.story('Footer menu: Company')
@allure.title('Check lessors button')
def test_lessors_button(browser):
    zoobazar_main_page = SearchHelper(browser)
    zoobazar_main_page.go_to_site()
    time.sleep(3)
    browser.execute_script("window.scrollTo(0, 3000)")
    zoobazar_main_page.click_element(Locators.LOCATOR_LESSORS_BUTTON)
    time.sleep(4)
    with allure.step("Скриншот"):
        allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    assert 'https://zoobazar.by/lessors/' in browser.current_url


@allure.feature('Footer tests')
@allure.story('Footer menu: Company')
@allure.title('Check news button')
def test_news_button(browser):
    zoobazar_main_page = SearchHelper(browser)
    zoobazar_main_page.go_to_site()
    time.sleep(3)
    browser.execute_script("window.scrollTo(0, 3000)")
    zoobazar_main_page.click_element(Locators.LOCATOR_NEWS_BUTTON)
    time.sleep(4)
    with allure.step("Скриншот"):
        allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    assert 'https://zoobazar.by/news/' in browser.current_url


@allure.feature('Footer tests')
@allure.story('Footer menu: Company')
@allure.title('Check Zoobazar guests button')
def test_zooguests_button(browser):
    zoobazar_main_page = SearchHelper(browser)
    zoobazar_main_page.go_to_site()
    time.sleep(3)
    browser.execute_script("window.scrollTo(0, 3000)")
    zoobazar_main_page.click_element(Locators.LOCATOR_ZOOGUESTS_BUTTON)
    time.sleep(4)
    with allure.step("Скриншот"):
        allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    assert 'https://zoobazar.by/visit/' in browser.current_url

@allure.feature('Footer tests')
@allure.story('Footer menu: Company')
@allure.title('Check Zoobazar contacts button')
def test_contacts_button(browser):
    zoobazar_main_page = SearchHelper(browser)
    zoobazar_main_page.go_to_site()
    time.sleep(3)
    browser.execute_script("window.scrollTo(0, 3000)")
    zoobazar_main_page.click_element(Locators.LOCATOR_CONTACTS_BUTTON)
    time.sleep(4)
    with allure.step("Скриншот"):
        allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    assert 'https://zoobazar.by/contacts/' in browser.current_url
