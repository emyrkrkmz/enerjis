import scrapy
from  scrape_mgm.items import Bolge, turkey_cities, hafta_gunleri
from scrapy_splash import SplashRequest

#https://www.mgm.gov.tr/?il=Istanbul
#https://www.ventusky.com//?p=39.4;34.1;5&l=temperature-2m

#SCRAPEOPS_API_KEY = "bdedab60-23c0-40b7-b0d8-234dc5d68e63"


class MgmSpySpider(scrapy.Spider):
    name = "mgm_spy"

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
        
        for i in turkey_cities:
            city_url = "https://www.mgm.gov.tr/" + f"?il={i}"
            yield SplashRequest(url=city_url, callback=self.parse, 
                            endpoint='execute', args={'wait' : 1,'lua_source': self.lua_script, 'url' : city_url,}) 
                                                      #'proxy': f'http://scrapeops:{SCRAPEOPS_API_KEY}@proxy.scrapeops.io:5353'})

    def parse(self, response):
        
        c_temp = response.xpath('//ziko[contains(@ng-bind, "sicaklik")]/text()').get()
        bolge_adi = response.xpath('//ziko[contains(@ng-bind, "merkez.il")]/text()').get()
        gun_zaman = response.xpath('//p[contains(@ng-bind, "veriZamani")]/text()').get()
        hava_durumu = response.xpath('//p[contains(@ng-bind, "hadiseAdi")]/text()').get()
        max_temp = "NOT FOUND"
        min_temp = "NOT FOUND"
        basinc = response.xpath('//span[@class="value ng-binding" and not(contains(@ng-bind, "nem"))]/text()').get() 
        ruzgar = response.xpath('//span[contains(@ng-bind, "ruzgarHiz|")]/text()').get()
        nem = response.xpath('//span[@class="value ng-binding" and contains(@ng-bind, "nem")]/text()').get()
        
        ft_name = response.xpath('//div[contains(@ng-bind, "tarihGun1")]/text()').get()
        ft_max_sicaklik = response.xpath('//span[contains(@ng-bind, "enYuksekGun1")]/text()').get()
        ft_min_sicaklik = response.xpath('//span[contains(@ng-bind, "enDusukGun1")]/text()').get()
        ft_ruzgar = response.xpath('//span[contains(@ng-bind, "ruzgarHizGun1")]/text()').get()

        ft_min_nem = response.xpath('//span[contains(@ng-bind, "enDusukNemGun1")]/text()').get()
        ft_max_nem = response.xpath('//span[contains(@ng-bind, "enYuksekNemGun1")]/text()').get()
        
        st_name = response.xpath('//div[contains(@ng-bind, "tarihGun2")]/text()').get()
        st_max_sicaklik = response.xpath('//span[contains(@ng-bind, "enYuksekGun2")]/text()').get()
        st_min_sicaklik = response.xpath('//span[contains(@ng-bind, "enDusukGun2")]/text()').get()
        st_ruzgar = response.xpath('//span[contains(@ng-bind, "ruzgarHizGun2")]/text()').get()
        
        st_min_nem = response.xpath('//span[contains(@ng-bind, "enDusukNemGun2")]/text()').get()
        st_max_nem = response.xpath('//span[contains(@ng-bind, "enYuksekNemGun2")]/text()').get()
        
        for i in range(0,7):
            if str(hafta_gunleri[i]) == str(ft_name):
                gun_adi = hafta_gunleri[i-1]  
                break
            else:
                gun_adi = " "
        
        
        sehir = Bolge()
        
        sehir["bolge_adi"] = bolge_adi
        sehir["gun_adi"] = gun_adi
        sehir["c_sicaklik"] = c_temp
        sehir["tarih"] = gun_zaman
        sehir["hava_durumu"] = hava_durumu
        sehir["max_sicaklik"] = max_temp
        sehir["min_sicaklik"] = min_temp
        sehir["basinc"] = basinc
        sehir["ruzgar"] = ruzgar
        sehir["nem"] = nem
        
        sehir["ft_name"] = ft_name	
        sehir["ft_max_sicaklik"] = ft_max_sicaklik
        sehir["ft_min_sicaklik"] = ft_min_sicaklik
        sehir["ft_ruzgar"] = ft_ruzgar
        sehir["ft_max_nem"] = ft_max_nem
        sehir["ft_min_nem"] = ft_min_nem
        
        sehir["st_name"] = st_name
        sehir["st_max_sicaklik"] = st_max_sicaklik
        sehir["st_min_sicaklik"] = st_min_sicaklik
        sehir["st_ruzgar"] = st_ruzgar
        sehir["st_max_nem"] = st_max_nem
        sehir["st_min_nem"] = st_min_nem

        
        
        yield sehir
            
    # def parse_city(self, response):
    #     print(response.url)
        
        