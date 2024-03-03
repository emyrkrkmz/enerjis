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
    def turkce_upper(self, metin):
        turkce_buyuk = {"i": "İ", "ı": "I"}
        return "".join(turkce_buyuk.get(harf, harf.upper()) for harf in metin)

    def start_requests(self):
        yield SplashRequest(url="https://www.mgm.gov.tr/tahmin/gunluk-tahmin.aspx", callback=self.parse_gunluk, 
                            endpoint='execute', args={'wait' : 1,'lua_source': self.lua_script})
        
    def parse_gunluk(self, response):
        df = pd.read_csv("data.csv")
        
        for i in df.index:
            a_city = df.loc[i, "bolge_adi"]
            if a_city == "Afyonkarahisar":
                a_city = "A.KARAHİSAR"
            else:
                a_city = self.turkce_upper(a_city)
            
            print(a_city)
            for i in len(response.xpath('//h4')):
                pass
            city = response.xpath('//h4'.format(a_city))
            if city != None:
                max_temp = city.css("span.renkMin::text").get()
                min_temp = city.css('span.renkMax::text').get() 
                df.loc[df['bolge_adi'] ==a_city, 'max_sicaklik'] = max_temp
                df.loc[df['bolge_adi'] ==a_city, 'min_sicaklik'] = min_temp
                
            yield {
            'name' : a_city,
            'max_temp' : max_temp,
            'min_temp' : min_temp,
            }
                
        
        
        
    


            
