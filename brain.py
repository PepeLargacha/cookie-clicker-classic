from selenium import webdriver

upgrades_benefit = {
    'cursor': 0.2,
    'grandma': 0.8,
    'factory': 4,
    'mine': 10,
    'shipment': 20,
    'alchemy lab': 100,
    'portal': 0.2,
    'time machine': 0.2,
}


class TheCookieMaster:

    def __init__(self) -> None:
        self.url = 'http://orteil.dashnet.org/experiments/cookie/'
        self.chromedriver_path = 'C:/Programs/chromedriver/chromedriver'
        self.driver = webdriver.Chrome(self.chromedriver_path)
        self.prices = {
            'cursor': None,
            'grandma': 100,
            'factory': 500,
            'mine': 2000,
            'shipment': 7000,
            'alchemy lab': 50000,
            'portal': 1000000,
            'time machine': 123456789,
        }
        self.best_buy = None
        self.target = None
        self.money = 0

    def get_money(self):
        self.money = int(self.driver.find_element_by_id('money').text.replace(
            ',', ''))
        return self.money

    def update_prices(self):
        prices = {}
        for item in self.driver.find_elements_by_css_selector('div#store div'):
            elem = item.get_attribute('id')[3:]
            if elem.lower() in self.prices:
                price = item.find_element_by_tag_name(
                    'b').text.split(' - ')[1].replace(',', '')
                prices[elem.lower()] = int(price)
        return prices

    def get_best_buy(self):
        best_buy = None
        self.prices = self.update_prices()
        for item in self.prices:
            item = item.lower()
            benefit = upgrades_benefit[item]
            cost_benefit = benefit / self.prices[item]
            if best_buy is None or cost_benefit > best_buy['cost_benefit']:
                best_buy = {
                    'type': item,
                    'price': self.prices[item],
                    'cost_benefit': cost_benefit,
                }
        self.target = int(best_buy['price'])
        return best_buy

    def buy_best_buy(self):
        self.driver.find_element_by_id(
            'buy' + self.best_buy['type'].title()).click()
