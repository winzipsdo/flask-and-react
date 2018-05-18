import datetime
import schedule
import time

from src.Models.Requester import Requester
from src.Models.DAO import insert_subseries


def test():
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


def daily_crawl():
    target_sites = [
        ['tw', 'zh'],
        ['jp', 'ja'],
        ['my', 'en'],
        ['kr', 'ko'],
    ]
    count = 0
    for site in target_sites:
        requester = Requester(site[0], site[1])
        requester.get_laptops_by_json()
        for subseries in requester.products:
            insert_subseries(subseries)
            count += 1
    print(count)


def daily_tasks():
    schedule.every().day.at("8:00").do(daily_crawl)
    while True:
        schedule.run_pending()
        time.sleep(59)


if __name__ == '__main__':
    time_start = time.time()
    daily_crawl()
    time_total = time.time() - time_start
    print(time_total)