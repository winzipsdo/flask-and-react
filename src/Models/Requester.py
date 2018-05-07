import random
import requests
from src.Models.VOs.Subseries import Subseries
from src.Models.GLOBAL import HEADERS, JSON_LAPTOPS, UNDEFINED, DOMAIN
from src.Models.DAO import insert_subseries


class Requester:
    count = 0

    def __init__(self, site, language):
        self.site = site.lower()
        self.language = language.lower()
        self.user_agent = random.choice(HEADERS)
        self.laptops_json = None
        self.products = []

        Requester.count += 1

    def get_laptops_by_json(self):
        if self.site.upper() in JSON_LAPTOPS.keys():
            json_api = JSON_LAPTOPS.get(self.site.upper())
            print('json api got: ' + json_api)  # test line
            laptops_json = requests.get(url=json_api, headers={'Accept-Encoding': ''}).json()
            for series, series_data in laptops_json.items():
                for subseries in series_data:
                    print('got: ' + subseries.get('name'))
                    self.products.append(Subseries(
                        site=self.site,
                        language=self.language,
                        article_number=subseries.get('code'),
                        image_url=subseries.get('imageURL')
                        if DOMAIN in subseries.get('imageURL')
                        else DOMAIN + subseries.get('imageURL'),
                        name=subseries.get('name'),
                        price=subseries.get('value'),
                        url=subseries.get('url'),
                        description=subseries.get('description')
                    ))
        else:
            print('This site is not ready yet, json api is needed.')
            raise Exception


if __name__ == '__main__':
    re = Requester('tw', 'zh')
    re.get_laptops_by_json()
    for subseries in re.products:
        insert_subseries(subseries)
