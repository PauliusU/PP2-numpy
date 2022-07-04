import config_loader
import scraper
from data_analyzer import analyze_data

if __name__ == '__main__':
    config = config_loader.get_config()
    debt_to_GDP_data = scraper.scrape_site(config)
    analyze_data(debt_to_GDP_data)
