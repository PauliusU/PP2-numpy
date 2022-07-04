import config_loader
import scraper

if __name__ == '__main__':
    config = config_loader.get_config()
    share_price_data = scraper.scrape_site(config)

