import datetime
import re
from src.Models.GLOBAL import UNDEFINED, DOMAIN
detail_index = 0
url_index = 1


class Subseries:
    count = 0

    def __init__(self,
                 site,
                 language,
                 article_number,  # code
                 name,  # name
                 price,  # value
                 url,  # url
                 image_url,  # imageURL
                 description
                 ):
        self.site = site
        self.language = language
        self.article_number = article_number
        self.name = name
        self.price = price
        self.image_url = DOMAIN + image_url if image_url[0] is '/' else image_url
        self.url = DOMAIN + '/' + site + '/' + language + url if url[0] is '/' else url

        details = self.decipher_url(self.url)
        self.spliter = details.get('spliter')
        self.brand = details.get('brand')
        self.series = details.get('series')

        self.date = self.get_date()
        self.description = description

        Subseries.count += 1

    @staticmethod
    def decipher_url(url):
        pattern = re.compile(
            '(https:\/\/www3.lenovo.com\/[\w]{2}\/\w{2}){0,1}\/([\w%-]*)\/{0,1}([\w%-]*)\/([\w%-]*)\/([\w%-]*)\/p\/([\w%-]*)')
        res = pattern.match(url)
        res_formatted = {
            # 'domain': res[1] if res[1] else DOMAIN,
            # 'spliter': res[2] if res[2] else UNDEFINED,
            # 'brand': res[3] if res[3] else UNDEFINED,
            # 'series': res[4] if res[4] else UNDEFINED,
            # 'name': res[5] if res[5] else UNDEFINED,
            # 'article_number': res[6] if res[6] else UNDEFINED
            'domain': res[1] if res else DOMAIN,
            'spliter': res[2] if res else UNDEFINED,
            'brand': res[3] if res else UNDEFINED,
            'series': res[4] if res else UNDEFINED,
            'name': res[5] if res else UNDEFINED,
            'article_number': res if res else UNDEFINED
        }
        return res_formatted

    @staticmethod
    def get_date():
        return str(datetime.datetime.now().year) + \
               '-' + \
               str(datetime.datetime.now().month) + \
               '-' + \
               str(datetime.datetime.now().day)

    def dictify(self):
        return {
            'site': self.site,
            'language': self.language,
            'article_number': self.article_number,
            'name': self.name,
            'price': self.price,
            'image_url': self.image_url,
            'url': self.url,
            'spliter': self.spliter,
            'brand': self.brand,
            'series': self.series,
            'date': self.date
        }


if __name__ == '__main__':
    sub = Subseries(
        site='jp',
        language='ja',
        article_number="22TP2TBL38020M7",
        image_url="/medias/lenovo-laptop-thinkpad-l380-yoga-series-front.png?context=bWFzdGVyfHJvb3R8MjU1MDN8aW1hZ2UvcG5nfGgyYS9oZDIvOTYzMzMzMTkwNDU0Mi5wbmd8OTAxOTVlM2ExNjdmMzUyZjkzNzRkOTBhYjE3ZGFmNjMwNGFjZjgzODBhODE2YTM5YWMyMGM0NzM4ZjRmYjU1NQ",
        name="ThinkPad L380 Yoga",
        price=108540.0,
        url="/notebooks/thinkpad/l-series/ThinkPad-L380-Yoga/p/22TP2TBL38020M7"
    )
    print(sub)
