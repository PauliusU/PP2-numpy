import config_loader
import scraper

if __name__ == '__main__':
    config = config_loader.get_config()
    debt_to_GDP_data = scraper.scrape_site(config)

