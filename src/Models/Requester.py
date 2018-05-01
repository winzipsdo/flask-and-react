import random
import requests

from src.Models.GLOBAL import HEADERS, JSON_LAPTOPS


class Requester:
    count = 0

    def __init__(self,site,language):
        self.site = site.upper()
        self.language = language.upper()
        self.user_agent = random.choice(HEADERS)
        self.laptops_json = None

    def get_laptops_by_json(self):
        if self.site in JSON_LAPTOPS.keys():
            json_api = JSON_LAPTOPS.get(self.site)
            print('json api got: ' + json_api)  # test line
            self.laptops_json = requests.get(url=json_api)
            print(self.laptops_json.json())
        else:
            print('This site is not ready yet, json api is needed.')
            raise Exception



if __name__ == '__main__':
    re = Requester('jp','ja')
    re.get_laptops_by_json()