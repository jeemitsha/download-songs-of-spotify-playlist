from selenium import webdriver


def main(name):
    name.replace(' ', '+')

    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    driver = webdriver.Chrome(chrome_options=options)
    driver.get('https://www.youtube.com/results?search_query=' + name)

    site = driver.find_element_by_xpath(
        '/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a')
    site.find_elements_by_xpath("//*[@href]")
    output = (site.get_attribute("href"))
    driver.close()
    return output
