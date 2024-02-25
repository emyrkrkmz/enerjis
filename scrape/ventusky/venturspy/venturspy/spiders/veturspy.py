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
        yield SplashRequest(url="https://ventusky.com/istanbul", callback=self.parse, 
                            endpoint='execute', args={'wait' : 1,'lua_source': self.lua_script, 'url' : "https://ventusky.com/istanbul"})


    def parse(self, response):
        istanbul = CityItem()
        all_tables = response.xpath('//table')
        
        mini_table = all_tables[1]
        
        
        #istanbul["precipitation"] = mini_table.xpath('.//tr[1]/td[2]/b/text()').get()
        #istanbul["air_pressure"] = mini_table.xpath('.//tr[2]/td[2]/b/text()').get()
        #istanbul["visibility"] = mini_table.xpath('.//tr[3]/td[2]/b/text()').get()
        #istanbul['clouds'] = mini_table.xpath('.//tr[4]/td[2]/b/text()').get()
        #istanbul['cloud_base'] = mini_table.xpath('.//tr[5]/td[2]/b/text()').get()
        #istanbul['wind_speed'] = mini_table.xpath('.//tr[6]/td[2]/b/text()').get()
        Humidity = mini_table.xpath('.//tr[1]/td[2]/b/text()').get()
        print(Humidity)
        yield {
            'Humidity': mini_table.xpath('.//tr[1]/td[2]/b/text()').get(),
            'Clouds': mini_table.xpath('.//tr[2]/td[2]/b/text()').get(),
            'Cloud base': mini_table.xpath('.//tr[3]/td[2]/b/text()').get(),
        }

