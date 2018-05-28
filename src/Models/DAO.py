# -*- coding:utf-8 -*-
from sqlalchemy import create_engine, Column, String, Float, Integer, Date, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from flask import jsonify

engine = create_engine("mysql+pymysql://root:123@localhost:3306/lenovo",
                       echo=False,  # 打印数据库操作
                       connect_args={'charset': 'utf8'})
Base = declarative_base()
DBSession = sessionmaker(bind=engine)


class SubseriesModel(Base):
    __tablename__ = 'subseries'
    id = Column(Integer, primary_key=True, autoincrement=True)
    site = Column(String(10))
    language = Column(String(10))
    article_number = Column(String(30))
    name = Column(String(50))
    price = Column(Float)
    image_url = Column(String(500))
    url = Column(String(500))
    spliter = Column(String(50))
    brand = Column(String(50))
    series = Column(String(50))
    date = Column(Date)
    description = Column(Text)

    def __init__(self,
                 site,
                 language,
                 article_number,  # code
                 name,  # name
                 price,  # value
                 image_url,  # imageURL
                 url,  # url
                 spliter,
                 brand,
                 series,
                 date,
                 description
                 ):
        self.site = site
        self.language = language
        self.article_number = article_number
        self.name = name
        self.price = price
        self.image_url = image_url
        self.url = url
        self.spliter = spliter
        self.brand = brand
        self.series = series
        self.date = date
        self.description = description

    def dictify(self):
        return {
            'id': self.id,
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
            'date': self.date,
            'description': self.description,
        }


def insert_subseries(subseries):
    session = DBSession()
    query = session.query(SubseriesModel).filter(
        SubseriesModel.date == subseries.date,
        SubseriesModel.article_number == subseries.article_number,
        SubseriesModel.site == subseries.site
    ).all()
    if len(query) == 0:
        session.add(SubseriesModel(
            site=subseries.site,
            language=subseries.language,
            article_number=subseries.article_number,
            name=subseries.name,
            price=subseries.price,
            image_url=subseries.image_url,
            url=subseries.url,
            spliter=subseries.spliter,
            brand=subseries.brand,
            series=subseries.series,
            date=subseries.date,
            description=subseries.description
        ))
        session.commit()
        print(subseries.article_number + " insert successfully.")
    else:
        print(subseries.article_number + " is already exist.")
    session.close()


def get_subseries_by_site_date(site,date):
    session = DBSession()
    ResultSet = session.query(SubseriesModel).filter(
        SubseriesModel.site == site,
        SubseriesModel.date == date,
    ).all()
    data = []
    for item in ResultSet:
        data.append(item.dictify())
    return data


if __name__ == '__main__':
    print(get_subseries_by_site_date('jp','2018-5-27'))

