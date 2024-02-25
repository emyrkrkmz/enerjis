# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class CityItem(scrapy.Item):
    city_name = scrapy.Field()
    precipitation = scrapy.Field()
    air_pressure = scrapy.Field()
    visibility = scrapy.Field()
    clouds = scrapy.Field()
    cloud_base = scrapy.Field()
    wind = scrapy.Field()


turkey_cities_lowercase = [
    "adana",
    "ankara",
    "antalya",
    "bursa",
    "istanbul",
    "izmir",
    "konya",
    "mersin",
    "gaziantep",
    "kayseri",
    "bursa",
    "samsun",
    "edirne",
    "trabzon",
    "eskisehir",
    "diyarbakir",
    "sanliurfa",
    "denizli",
    "mardin",
    "kocaeli",
    "malatya",
    "erzurum",
    "sivas",
    "van",
    "manisa",
    "adiyaman",
    "kutahya",
    "balikesir",
    "sanliurfa",
    "aydin",
    "corum",
    "usak",
    "bolu",
    "afyonkarahisar",
    "tekirdag",
    "giresun",
    "ordu",
    "kirikkale",
    "nevsehir",
    "agri",
    "kars",
    "zonguldak",
    "yalova",
    "canakkale",
    "kirklareli",
    "bolu",
    "sinop",
    "rize",
    "bilecik",
    "bartin",
    "artvin",
    "ardahan",
    "yozgat",
    "karabuk",
    "karaman",
    "kilis",
    "osmaniye",
    "nigde",
    "batman",
    "aksaray",
    "igdir",
    "yalova",
    "duzce",
    "bayburt",
    "kirsehir",
    "cankiri",
    "bingol",
    "erzincan",
    "mus",
    "bitlis",
    "siirt",
    "sirnak",
    "hakkari",
]
