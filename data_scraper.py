from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
wait = WebDriverWait(driver, 20, 1)
filter_locator = ('xpath', '//th[contains(text(), "Субьект выдвижения")]')
party_locator = ('xpath', '//td[contains(text(), "НОВЫЕ")]')
district = ('xpath', '//h1[@class="report-title"]')

with open('links_St_Petersburg.txt', 'r', encoding='utf-8') as links:
    with open('output.txt', 'a+', encoding='utf-8') as out:
        full = links.readlines()
        last_link = open('last_link.txt', 'w+', encoding='utf-8')
        last_link_num = int(last_link.readline())
        for i in range(last_link_num, len(full)):
            f = open('last_link.txt.txt', 'w')
            f.write(f'{i}')  # записываем текущие координаты, чтобы при перезапуске не выставлять их вручную
            f.close()
            print(f'Progress: {i + 1} / {len(full)} COMPLETE')
            driver.get(full[i])
            wait.until(EC.visibility_of_element_located(district))  # Ждём пока появится название выборной кампании
            # после введения капчи
            table = ('xpath', '//table[@id="candidates-220-2"]')
            rows = ('xpath', '//table[@id="candidates-220-2"]//tr')
            cols = ('xpath', '//table[@id="candidates-220-2"]//tr[3]/td')
            rows_num = int(len(driver.find_elements(*rows)))
            cols_num = int(len(driver.find_elements(*cols)))
            for r in range(1, rows_num - 1):
                out.write(f'{driver.find_element(*district).text}$')
                for c in range(1, cols_num + 1):
                    value = driver.find_element('xpath', f'//table[@id="candidates-220-2"]//tr[{r}]/td[{c}]').text
                    out.write(f'{value}$')
                out.write('\n')
