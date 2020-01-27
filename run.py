import os
import config
from app.crawler.scrapy import PyCrawler

def main():
    urls = open(config.WEBLIST_PATH, "r")
    for url in urls:
        crawler = PyCrawler(url)     
        crawler.start()


if __name__ == '__main__':
    main()