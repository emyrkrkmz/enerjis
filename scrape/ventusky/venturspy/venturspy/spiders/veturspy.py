import scrapy
from venturspy.items import turkey_cities_lowercase, CityItem
from scrapy_splash import SplashRequest

#https://www.ventusky.com/siirt
#scrapy shell 'http://localhost:8050/render.html?url=http://example.com/page-with-javascript.html&timeout=10&wait=0.5'


class VeturspySpider(scrapy.Spider):
    name = "veturspy"
    
    lua_script='''
        function main(splash, args)
            assert(splash:go(args.url))
            assert(splash:wait(5))
            splash:set_viewport_full()
            return {
              html = splash:html()
            }
        end
    '''
    
    
    def start_requests(self):
        for i in turkey_cities_lowercase:
            yield SplashRequest(url=f"https://ventusky.com/{i}", callback=self.parse, 
                            endpoint='execute', args={'wait' : 1,'lua_source': self.lua_script})


    def parse(self, response):
        city = CityItem()
        
        ##First part
        mid_table = response.css("div#actual > div > div:nth-child(3) > table > tbody")
        
        if mid_table != None:
            city_name = response.css('div.header_background > h1::text').get().strip()

            temperature = response.css('td.temperature::text').get()
            wind = response.css('b.wind_ico::text').get()
            
            if temperature != None:
                city["Temperature"] = temperature.strip()

            if wind != None:
                city['Wind'] = wind.strip()
            
            city["City_name"] = city_name
            
            #midd = mid_table
            trss = len(mid_table.css('tr'))
            for i in range(1 , trss):
                prop = mid_table.css(f'tr:nth-child({i}) > td:nth-child(1)::text').get()
                value = mid_table.css(f'tr:nth-child({i}) > td:nth-child(2) > b::text').get()
                
                
                if prop == None:
                    continue
                
                prop.strip()
                
                
                if "Precipitation" in prop:
                    prop = "Precipitation"
                if "Cloud base" in prop:
                    prop = "Cloud_base"
                if 'Air pressure' in prop:
                    prop = 'Air_pressure'
                if 'Humidity' in prop:
                    prop = 'Humidity'
                if 'Visibility' in prop:
                    prop = 'Visibility'
                if 'Clouds' in prop:
                    prop = 'Clouds'
                

                city[prop] = value.strip()
                
            
        ##Second part
        product = response.css("div.section_grey table")
        
        
                
        


        
        yield city
