import logging
import os
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def scrape_site(config) -> list:
    """ Scrapes website using provided settings """
    try:
        logging.info(f'Loading scraping configuration (URL, selectors, etc.)')
        base_url = config['scraping']['base_url']
        page_title_text = config['scraping']['page_title_text']
        page_title_selector = config['scraping']['page_title_selector']
        selector_price = config['scraping']['selector_price']

        project_root = Path(__file__).parent.parent.parent
        driver_path = os.path.join(project_root, 'drivers',
                                   config['scraping']['driver_path'])

        prices = []

        logging.info('Setting up webdriver')
        service = ChromeService(driver_path)
        options = webdriver.ChromeOptions()

        with webdriver.Chrome(service=service, options=options) as driver:
            logging.info(f'Getting {base_url}')
            driver.get(base_url)

            logging.info(f'Waiting for the page to load')
            logging.info(driver.title)

            delay = 20
            WebDriverWait(driver, delay).until(
                expected_conditions.text_to_be_present_in_element(
                    (By.CSS_SELECTOR, page_title_selector),
                    page_title_text
                )
            )

            elements_with_prices = driver.find_elements(By.CSS_SELECTOR,
                                                        selector_price)

            for i in range(0, len(elements_with_prices)):
                price = elements_with_prices[i].text
                price = price.replace("%", "")  # Remove percent signs
                price = int(price)  # Convert to integers

                prices.append(price)

        return prices
    except Exception as err:
        logging.error(f'Scrapping error {err}')
