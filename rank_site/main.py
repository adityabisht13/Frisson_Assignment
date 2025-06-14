from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import pandas as pd

def create_driver():
    options = uc.ChromeOptions()
    options.add_argument('--disable-blink-features=AutomationControlled')
    return uc.Chrome(options=options)

def fetch_page_source(driver, query):
    driver.get(f"https://www.google.com/search?q={query}")
    time.sleep(10)
    return driver.page_source

def parse_results(page_source):
    soup = BeautifulSoup(page_source, "html.parser")
    results = soup.select('div.d8lRkd ')[1:]
    data = []
    seen_sites = set()
    for idx, link in enumerate(results):
        name = link.find('span', class_='OSrXXb')
        if not name:
            continue
        com_name = name.text
        site = link.find('span', class_='x2VHCd')
        if not site:
            continue
        site_1 = site.text
        if site_1 not in seen_sites:
            seen_sites.add(site_1)
            data.append({"Ranking": idx, "Name": com_name, "Site": site_1})
    return data

def save_to_csv(data, filename):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)

def main():
    driver = create_driver()
    query = "web development companies"
    page_source = fetch_page_source(driver, query)
    driver.quit()
    data = parse_results(page_source)
    save_to_csv(data, "frisson_task.csv")

if __name__ == "__main__":
    main()
