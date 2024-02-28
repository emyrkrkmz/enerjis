import scrapy
from scrapy_splash import SplashRequest
import pandas as pd

class LittleMgmSpySpider(scrapy.Spider):
    name = "little_mgm_spy"
    
    lua_script='''
    function main(splash, args)
        assert(splash:go(args.url))
        assert(splash:wait(1))
        splash:set_viewport_full()
        
        
        return {
          html = splash:html()
        }
    end
    '''

    def start_requests(self):
        yield SplashRequest(url="https://www.mgm.gov.tr/tahmin/gunluk-tahmin.aspx", callback=self.parse_gunluk, 
                            endpoint='execute', args={'wait' : 1,'lua_source': self.lua_script})
        
    def parse_gunluk(self, response):
        df = pd.read_csv("data.csv")
        
        
        for i in df.index:
            a_city = df.loc[i, "bolge_adi"]
            if a_city == "Ankara":
                a_city = ""
            city = response.xpath(f'//h4[contains(text(), "{a_city}")]/span')
            if city != None:
                max_temp = city.css("span.renkMin::text").get()
                min_temp = city.css('span.renkMax::text').get() 
                df.loc[df['bolge_adi'] ==a_city, 'max_sicaklik'] = max_temp
                df.loc[df['bolge_adi'] ==a_city, 'min_sicaklik'] = min_temp
                
        df.to_csv("data.csv")

            
