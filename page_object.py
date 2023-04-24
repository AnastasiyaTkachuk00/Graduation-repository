from selenium.webdriver.common.by import By
from base_page import BasePage


class Locators:
    title = (By.CSS_SELECTOR, 'head > title')
    LOCATOR_SEARCH_FIELD = (By.CLASS_NAME, "header-search__content")
    LOCATOR_SEARCH_BUTTON = (By.CLASS_NAME, "header-search__icon")
    LOCATOR_SEARCH_FRAME_FIELD = (By.XPATH, '//*[@id="multisearch-search"]/div/form/div/input')
    LOCATOR_CART_BUTTON = (By.CSS_SELECTOR, '[class="button button--clear cart-small"]')
    LOCATOR_FAVORITES_BUTTON = (By.XPATH, '//a[@title="Избранное"]')
    LOCATOR_LOGIN = (By.XPATH, '//div[@class="d-none d-lg-flex header-personal__wrapper header-main__action"]/button')
    LOCATOR_MAIN_PAGE = (By.XPATH, "/html/head/title/text()")
    LOCATOR_AUTH_TITLE = (By.CSS_SELECTOR, '#auth > div > div.popup__heading > div')
    LOCATOR_DELIVERY_BUTTON = (By.XPATH, '//a[@title="Доставка"]')
    LOCATOR_PICKUP_PIONTS_BUTTON = (By.CSS_SELECTOR, '#header > div.d-none.d-lg-block.header-top__wrapper > div > div > div:nth-child(2) > div.header-top-links > a:nth-child(5)')
    LOCATOR_MAIN_MENU_CATS = (By.XPATH, '//div[@class="main-menu__item main-menu__item--1989"]/a[1]')

    LOCATOR_CATEGORY_BUTTON = (By.CLASS_NAME, 'multiselect__tags')
    LOCATOR_CATEGORY_POPULAR = (By.XPATH, '//li[@class="multiselect__element"][1]')
    LOCATOR_CATEGORY_MAX_BENEFITS = (By.XPATH, '//li[@class="multiselect__element"][2]')
    LOCATOR_CATEGORY_MIN_PRICE = (By.XPATH, '//li[@class="multiselect__element"][3]')
    LOCATOR_CATEGORY_MAX_PRICE = (By.XPATH, '//li[@class="multiselect__element"][4]')
    LOCATOR_CATEGORY_PROMOTIONS = (By.XPATH, '//li[@class="multiselect__element"][5]')
    LOCATOR_CATEGORY_MOST_POPULAR = (By.XPATH, '//li[@class="multiselect__element"][6]')

    LOCATOR_CHECKBOX_BENEFITS =  (By.ID, 'arrFilter_2094_3865458834')
    LOCATOR_CHECKBOX_ONLY_ONLAIN = (By.ID, 'arrFilter_2094_1958325001')
    LOCATOR_CHECKBOX_ARE_AVAILABLE = (By.ID, 'arrFilter_617_3233089245')
    LOCATOR_SEARCHING_RESULT = (By.XPATH, '//*[@id="app"]/main/div/div[3]/div/div/div[1]/div[2]/div[2]/form/div[1]/div[5]/a[2]')
    LOCATOR_MIN_WEIGHT = (By.XPATH, '//div[@class="multiselect__tags"][1]')
    LOCATOR_MIN_WEIGHT_DIGIT = (By.XPATH, '//span[@class="multiselect__option multiselect__option--highlight"][1]')
    LOCATOR_MAX_WEIGHT_DIGIT = (By.XPATH, '//*[@id="app"]/main/div/div[3]/div/div/div[1]/div[2]/div[2]/form/div[1]/div[2]/div[10]/div[2]/div/div/div[2]/div/div/div[3]/ul/li[7]/span/span')
    LOCATOR_MAX_WEIGHT = (By.XPATH, '//div[@class="row g-2"]/div[2]/div/div')
    LOCATOR_DRY_FOOD = (By.XPATH,'//*[@id="bx_510680952_2638"]/a/div[2]')
    LOCATOR_PHONE_FIELD = (By.XPATH, '//*[@id="auth-phone"]')
    LOCATOR_SEND_CODE = (By.XPATH, '//*[@id="auth"]/div/div[2]/div[2]/div/button')
    LOCATOR_USER_BUTTON = (By.XPATH, '//*[@id="header"]/div[2]/div/div/div[2]/div[6]/a')
    LOCATOG_LOGGIN = (By.XPATH, '//*[@id="auth"]/div/div[1]')
    Benefits = (By.XPATH, '//*[@id="app"]/main/div/div[3]/div/div/div[2]/div[3]/div[2]/div/div[2]/span')
    LOCATOR_SHOW_RESULTS = (By.XPATH, '//a[@class="button button--primary button--xl smart-filter__button smart-filter__button--show"]')
    LOCATOR_FILTER_MIN_PRICE = (By.ID, 'arrFilter_P5_MIN')
    LOCATOR_FILTER_MAX_PRICE = (By.ID, 'arrFilter_P5_MAX')

    LOCATOR_FIRST_CHECKBOX_BRANDS = (By.ID, 'arrFilter_86_3222927397')
    LOCATOR_MEDIUM_CHECKBOX_BRANDS = (By.ID, 'arrFilter_86_4174463861-popup')
    LOCATOR_SHOW_MORE_BRANDS = (By.CSS_SELECTOR, '#app > main > div > div.content__wrapper > div > div > div.catalog__aside.catalog-mobile-block > div.catalog-mobile-block__content-wrapper > div.catalog-mobile-block__content > form > div.smart-filter__body > div:nth-child(2) > div:nth-child(1) > div.parameters-box__block > div > button')

    LOCATOR_TYPE_OF_FEED_BUTTON = (By.XPATH, '//div[@class="parameters-box"][1]/div[1]/div')
    LOCATOR_DRY_FEED_CHECKBOX = (By.ID, 'arrFilter_303_1763061754')
    LOCATOR_FILTER_SPEC_SERIES_BUTTON = (By.XPATH, '//*[@id="app"]/main/div/div[3]/div/div/div[1]/div[2]/div[2]/form/div[1]/div[2]/div[3]/div[1]')
    LOCATOR_GLUTEN_FREE_CHECKBOX = (By.ID, 'arrFilter_313_591306731')
    LOCATOR_GRAIN_FREE_CHECKBOX = (By.ID, 'arrFilter_313_1413066621')
    LOCATOR_VET_DIET = (By.ID, 'arrFilter_313_591306731')
    LOCATOR_LOW_GRAIN = (By.ID, 'arrFilter_313_3442540231')
    LOCATOR_HOLISTIK_CHECKBOX = (By.ID, 'arrFilter_313_1140397582')

    LOCATOR_TYPE_OF_PACKING = (By.XPATH, '//*[@id="app"]/main/div/div[3]/div/div/div[1]/div[2]/div[2]/form/div[1]/div[2]/div[7]/div[1]/div')
    LOCATOR_TYPE_OF_PACKING_BOX = (By.ID, 'arrFilter_229_2729817228')
    LOCATOR_TYPE_OF_PACKING_BAG = (By.ID, 'arrFilter_229_1210337208')

    LOCATOR_CARD_ACTIVATION = (By.XPATH, '//div[@class="header-top-links"]/a[@title="Активировать карту"]')
    TITLE_CARD_ACTIVATION = (By.ID, 'pagetitle')

    LOCATOR_CART_ICON1 = (By.XPATH, '//*[@id="catalog-list--catalog"]/div/div[1]/div/div/div/div/button')
    LOCATOR_CART_ICON2 = (By.XPATH, '//*[@id="catalog-list--catalog"]/div/div[2]/div/div/div/div/button')
    LOCATOR_CART_ICON3 = (By.XPATH, '//*[@id="catalog-list--catalog"]/div/div[3]/div/div/div/div/button')

    LOCATOR_DELIVERY_BUTTON2 = (By.XPATH, '//*[@id="location-select"]/div/div[2]/div/div[2]/button[1]')
    LOCATOR_PICKUP_PIONTS_BUTTON2 = (By.XPATH, '//*[@id="location-select"]/div/div[2]/div/div[2]/button[2]')
    LOCATOR_CONFIRM_ADDRESS = (By.XPATH, '//*[@id="location-select"]/div/div[2]/div[3]/button')
    LOCATOR_CLOSE_ADV = (By.XPATH, '//*[@id="sale-popup"]/button')
    LOCATOR_AMOUNT_OF_GOODS = (By.XPATH, '//*[@id="app"]/main/div/div[3]/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]')

    LOCATOR_ADD_TO_FAVORITES1 = (By.XPATH, '//*[@id="catalog-list--catalog"]/div/div[1]/div/a/button')
    LOCATOR_ADD_TO_FAVORITES2 = (By.XPATH, '//*[@id="catalog-list--catalog"]/div/div[2]/div/a/button')
    LOCATOR_ADD_TO_FAVORITES3 = (By.XPATH, '//*[@id="catalog-list--catalog"]/div/div[3]/div/a/button')

    LOCATOR_CHAT_ICON = (By.XPATH, '//div[@class="b24-widget-button-inner-item b24-widget-button-icon-animation"]')
    LOCATOR_LIVE_CHAT = (By.XPATH, '//a[@class="b24-widget-button-social-item b24-widget-button-crmform"]')
    LOCATOR_TITLE_LIVE_CHAT = (By.XPATH, '//div[@class="feedback__title"]')
    LOCATOR_TOOLTIP_VIBER = (By.XPATH, '//a[@href="viber://pa?chatURI=zoobazar"]/span')
    LOCATOR_TOOLTIP_TELEGRAM = (By.XPATH, '//a[@href="https://t.me/zoobazar_by_feedback_bot"]/span')
    LOCATOR_TOOLTIP_VK = (By.XPATH, '//a[@href="https://vk.me/club118986456"]/span')
    LOCATOR_TOOLTIP_OK = (By.XPATH, '//a[@href="https://ok.ru/zoobazar.by"]/span')
    LOCATOR_VACANCIES_BUTTON = (By.XPATH, "//li[@class='footer-menu__item']/a[@title='Вакансии']")
    LOCATOR_ABOUT_US_BUTTON = (By.XPATH, "//li[@class='footer-menu__item']/a[@title='О нас']")
    LOCATOR_OUR_STORIES_BUTTON = (By.XPATH, "//li[@class='footer-menu__item']/a[@title='Наши магазины']")
    LOCATOR_PICKUP_POINTS_BUTTON3 = (By.XPATH, "//li[@class='footer-menu__item']/a[@title='Пункты самовывоза']")
    LOCATOR_DELIVERY_MAP_BUTTON = (By.XPATH, "//li[@class='footer-menu__item']/a[@title='Зоны доставки']")
    LOCATOR_LESSORS_BUTTON = (By.XPATH, "//li[@class='footer-menu__item']/a[@title='Аренда помещений']")
    LOCATOR_NEWS_BUTTON = (By.XPATH, "//li[@class='footer-menu__item']/a[@title='Публикации']")
    LOCATOR_ZOOGUESTS_BUTTON = (By.XPATH, "//li[@class='footer-menu__item']/a[@title='Zoobazar гости']")
    LOCATOR_CONTACTS_BUTTON = (By.XPATH, "//li[@class='footer-menu__item']/a[@title='Контакты и реквизиты']")


class SearchHelper(BasePage):

    def enter_word(self, word):
        search_field = self.find_element(Locators.LOCATOR_SEARCH_FRAME_FIELD)
        search_field.send_keys(word)
        return search_field

    def click_on_the_favorites_button(self):
        return self.find_element(Locators.LOCATOR_FAVORITES_BUTTON, time=2).click()

    def click_on_the_search_field(self):
        return self.find_element(Locators.LOCATOR_SEARCH_FIELD, time=2).click()
