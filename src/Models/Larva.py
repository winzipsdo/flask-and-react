import re,datetime
from src.Models.GLOBAL import UNDEFINED, DOMAIN
from src.Models.DAO import insert_subseries
from src.Models.VOs.Subseries import Subseries

if __name__ == '__main__':
    subseries = Subseries(
        site='jp',
        language='ja',
        article_number="22TP2TBL38020M7",
        image_url="/medias/lenovo-laptop-thinkpad-l380-yoga-series-front.png?context=bWFzdGVyfHJvb3R8MjU1MDN8aW1hZ2UvcG5nfGgyYS9oZDIvOTYzMzMzMTkwNDU0Mi5wbmd8OTAxOTVlM2ExNjdmMzUyZjkzNzRkOTBhYjE3ZGFmNjMwNGFjZjgzODBhODE2YTM5YWMyMGM0NzM4ZjRmYjU1NQ",
        name="ThinkPad L380 Yoga",
        price=108540.0,
        url="/notebooks/thinkpad/l-series/ThinkPad-L380-Yoga/p/22TP2TBL38020M7",
    )
    insert_subseries(subseries)
