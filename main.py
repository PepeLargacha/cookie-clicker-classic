from time import time, sleep
from brain import TheCookieMaster

cm = TheCookieMaster()

timeout = time() + 5
five_min = time() + 300

cm.driver.get(cm.url)
cm.best_buy = cm.get_best_buy()

while True:
    if cm.get_money() < cm.target:
        for n in range(100):
            cm.driver.find_element_by_id('cookie').click()
    else:
        cm.buy_best_buy()
        sleep(0.03)
        cm.best_buy = None
        cm.target = None
        cm.best_buy = cm.get_best_buy()

    if time() > five_min:
        break

print(cm.driver.find_element_by_id('cps').text)
