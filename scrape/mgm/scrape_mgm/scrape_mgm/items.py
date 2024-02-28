# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class Bolge(scrapy.Item):
    bolge_adi = scrapy.Field()
    gun_adi = scrapy.Field()
    tarih = scrapy.Field()
    c_sicaklik = scrapy.Field()
    hava_durumu = scrapy.Field()
    max_sicaklik = scrapy.Field()
    min_sicaklik = scrapy.Field()
    nem = scrapy.Field()
    ruzgar = scrapy.Field()
    basinc = scrapy.Field()
    
    
    
    ft_name = scrapy.Field()
    ft_max_sicaklik = scrapy.Field()
    ft_min_sicaklik = scrapy.Field()
    ft_ruzgar = scrapy.Field()
    ft_min_nem = scrapy.Field()
    ft_max_nem = scrapy.Field()
    
    st_name = scrapy.Field()
    st_max_sicaklik = scrapy.Field()
    st_min_sicaklik = scrapy.Field()
    st_ruzgar = scrapy.Field()
    st_min_nem = scrapy.Field()
    st_max_nem = scrapy.Field()

turkey_cities = [
    "Adana",
    "Adıyaman",
    "Afyonkarahisar",
    "Ağrı",
    "Aksaray",
    "Amasya",
    "Ankara",
    "Antalya",
    "Ardahan",
    "Artvin",
    "Aydın",
    "Balıkesir",
    "Bartın",
    "Batman",
    "Bayburt",
    "Bilecik",
    "Bingöl",
    "Bitlis",
    "Bolu",
    "Burdur",
    "Bursa",
    "Çanakkale",
    "Çankırı",
    "Çorum",
    "Denizli",
    "Diyarbakır",
    "Düzce",
    "Edirne",
    "Elazığ",
    "Erzincan",
    "Erzurum",
    "Eskişehir",
    "Gaziantep",
    "Giresun",
    "Gümüşhane",
    "Hakkari",
    "Hatay",
    "Iğdır",
    "Isparta",
    "İstanbul",
    "İzmir",
    "Kahramanmaraş",
    "Karabük",
    "Karaman",
    "Kars",
    "Kastamonu",
    "Kayseri",
    "Kırıkkale",
    "Kırklareli",
    "Kırşehir",
    "Kilis",
    "Kocaeli",
    "Konya",
    "Kütahya",
    "Malatya",
    "Manisa",
    "Mardin",
    "Mersin",
    "Muğla",
    "Muş",
    "Nevşehir",
    "Niğde",
    "Ordu",
    "Osmaniye",
    "Rize",
    "Sakarya",
    "Samsun",
    "Şanlıurfa",
    "Siirt",
    "Sinop",
    "Şırnak",
    "Sivas",
    "Tekirdağ",
    "Tokat",
    "Trabzon",
    "Tunceli",
    "Uşak",
    "Van",
    "Yalova",
    "Yozgat",
    "Zonguldak"
]


turkey_cities_and_provinces = districts_of_provinces = {
    "Adana": ["Aladag", "Ceyhan", "Cukurova", "Feke", "Imamoglu", "Karaisali", "Karatas", "Kozan", "Pozanti", "Saimbeyli", "Saricam", "Seyhan", "Tufanbeyli", "Yumurtalik", "Yuregir"],
    "Adiyaman": ["Besni", "Celikhan", "Gerger", "Golbasi", "Kahta", "Merkez", "Samsat", "Sincik", "Tut"],
    "Afyonkarahisar": ["Basmakci", "Bayat", "Bolvadin", "Cay", "Cobanlar", "Dazkiri", "Dinar", "Emirdag", "Evciler", "Hocalar", "Ihsaniye", "Iscehisar", "Kiziloren", "Merkez", "Sandikli", "Sinanpasa", "Sultandagi", "Suhut"],
    "Agri": ["Diyadin", "Dogubayazit", "Eleskirt", "Hamur", "Merkez", "Patnos", "Taslicay", "Tutak"],
    "Aksaray": ["Agacoren", "Eskil", "Gulagac", "Guzelyurt", "Merkez", "Ortakoy", "Sariyahsi"],
    "Amasya": ["Goynucek", "Gumushacikoy", "Hamamozu", "Merkez", "Merzifon", "Suluova", "Tasova"],
    "Ankara": ["Akyurt", "Altindag", "Ayas", "Bala", "Beypazari", "Camli dere", "Cankaya", "Cubuk", "Elm adag", "Etimesgut", "Evren", "Golbasi", "Gudul", "Haymana", "Kahramankazan", "Kalecik", "Kecioren", "Kizilcahamam", "Mamak", "Nallihan", "Polatli", "Pursaklar", "Sincan", "Sereflikochisar", "Yenimahalle"],
    "Antalya": ["Akseki", "Aksu", "Alanya", "Demre", "Dosemealti", "Elmali", "Finike", "Gazipasa", "Gundogmus", "Ibradi", "Kale", "Kas", "Kemer", "Kepez", "Konyaalti", "Korkuteli", "Kumluca", "Manavgat", "Muratpasa", "Serik"],
    "Ardahan": ["Cildir", "Damal", "Gole", "Hanak", "Merkez", "Posof"],
    "Artvin": ["Ardanuc", "Arhavi", "Borcka", "Hopa", "Merkez", "Murgul", "Savsat", "Yusufeli"],
    "Aydin": ["Bozdogan", "Buharkent", "Cine", "Didim", "Efeler", "Germencik", "Incirliova", "Karacasu", "Karpuzlu", "Kocarli", "Kosk", "Kusadasi", "Kuyucak", "Nazilli", "Soke", "Sultanhisar", "Yenipazar"],
    "Balikesir": ["Altieylul", "Ayvalik", "Balya", "Bandirma", "Bigadic", "Burhaniye", "Dursunbey", "Edremit", "Erdek", "Gomec", "Gonen", "Havran", "Ivrindi", "Karesi", "Kepsut", "Manyas", "Marmara", "Savastepe", "Sindirgi", "Susurluk"],
    "Bartin": ["Amasra", "Kurucaşile", "Merkez", "Ulus"],
    "Batman": ["Besiri", "Cercus", "Hasankeyf", "Kozluk", "Merkez", "Sason"],
    "Bayburt": ["Aydintepe", "Demirozu", "Merkez"],
    "Bilecik": ["Bozuyuk", "Golpazari", "Inhisar", "Merkez", "Osmaneli", "Pazaryeri", "Sogut", "Yenipazar"],
    "Bingol": ["Adakli", "Genc", "Karliova", "Kigi", "Merkez", "Solhan", "Yayladere", "Yedisu"],
    "Bitlis": ["Adilcevaz", "Ahlat", "Guroymak", "Hizan", "Merkez", "Mutki", "Tatvan"],
    "Bolu": ["Dortdivan", "Gerede", "Goynuk", "Kibriscik", "Mengen", "Merkez", "Mudurnu", "Seben", "Yenicağa"],
    "Burdur": ["Aglasun", "Bucak", "Cavdir", "Celtikci", "Golhisar", "Karamanli", "Kemer", "Merkez", "Tefenni", "Yesilova"],
    "Bursa": ["Buyukorhan", "Gemlik", "Gursu", "Harmancik", "Inegol", "Iznik", "Karacabey", "Keles", "Kestel", "Mudanya", "Mustafakemalpasa", "Nilufer", "Orhaneli", "Orhangazi", "Osmangazi", "Yenisehir", "Yildirim"],
    "Canakkale": ["Ayvacik", "Bayramic", "Biga", "Bozcaada", "Can", "Eceabat", "Ezine", "Gelibolu", "Gokceada", "Lapseki", "Merkez", "Yenice"],
    "Cankiri": ["Atkaracalar", "Bayramoren", "Cerkes", "Eldivan", "Ilgaz", "Kizilirmak", "Korgun", "Merkez", "Orta", "Sabanozu", "Yaprakli"],
    "Corum": ["Alaca", "Bayat", "Bogazkale", "Dodurga", "Iskilip", "Kargi", "Lacin", "Mecitozu", "Merkez", "Oguzlar", "Ortakoy", "Osmancik", "Sungurlu", "Ugurludag"],
    "Denizli": ["Acipayam", "Babadag", "Baklan", "Bekilli", "Beyagac", "Bozkurt", "Buldan", "Cal", "Cameli", "Cardak", "Civril", "Guney", "Honaz", "Kale", "Merkezefendi", "Pamukkale", "Saraykoy", "Serinhisar", "Tavas"],
    "Diyarbakir": ["Baglar", "Bismil", "Cermik", "Cinar", "Cungus", "Dicle", "Egil", "Ergani", "Hani", "Hazro", "Kayapinar", "Kocakoy", "Kulp", "Lice", "Silvan", "Sur", "Yenisehir"],
    "Duzce": ["Akcakoca", "Cumayeri", "Cilimli", "Golyaka", "Gumusova", "Kaynasli", "Merkez", "Yigilca"],
    "Edirne": ["Enez", "Havsa", "Ipsala", "Kesan", "Lalapasa", "Meric", "Merkez", "Suloglu", "Uzunkopru"],
    "Elazig": ["Agin", "Alacakaya", "Aricak", "Baskil", "Karakocan", "Keban", "Kovancilar", "Maden", "Merkez", "Palu", "Sivrice"],
    "Erzincan": ["Cayirli", "Ilic", "Kemah", "Kemaliye", "Merkez", "Otlukbeli", "Refahiye", "Tercan", "Uzumlu"],
    "Erzurum": ["Askale", "Aziziye", "Cat", "Hinis", "Horasan", "Ispir", "Karacoban", "Karayazi", "Koprüköy", "Narman", "Oltu", "Olur", "Palandoken", "Pasinler", "Pazaryolu", "Senkaya", "Tekman", "Tortum", "Uzundere", "Yakutiye"],
    "Eskisehir": ["Alpu", "Beylikova", "Cifteler", "Gunyuzu", "Han", "Inonu", "Mahmudiye", "Mihalgazi", "Mihaliccik", "Odunpazari", "Saricakaya", "Seyitgazi", "Sivrihisar", "Tepebasi"],
    "Gaziantep": ["Araban", "Islahiye", "Karkamis", "Nizip", "Nurdagi", "Oguzeli", "Sahinbey", "Sehitkamil", "Yavuzeli"],
    "Giresun": ["Alucra", "Bulancak", "Camoluk", "Canakci", "Dereli", "Dogankent", "Espiye", "Eynesil", "Gorele", "Guce", "Kesap", "Merkez", "Piraziz", "Sebinkarahisar", "Tirebolu"],
    "Gumushane": ["Kelkit", "Kose", "Kurtun", "Merkez", "Siran", "Torul"],
    "Hakkari": ["Cukurca", "Semdinli", "Yuksekova", "Merkez"],
    "Hatay": ["Altinozu", "Antakya", "Arsuz", "Belen", "Defne", "Dortyol", "Erzin", "Hassa", "Iskenderun", "Kirikhan", "Kumlu", "Payas", "Reyhanli", "Samandag", "Yayladagi"],
    "Igdir": ["Aralik", "Karakoyunlu", "Merkez", "Tuzluca"],
    "Isparta": ["Aksu", "Atabey", "Egirdir", "Gelendost", "Gonen", "Keciborlu", "Merkez", "Senirkent", "Sutculer", "Sarkikaraagac", "Uluborlu", "Yalvac", "Yenisehir"],
    "Istanbul": ["Adalar", "Arnavutkoy", "Atasehir", "Avcilar", "Bagcilar", "Bahcelievler", "Bakirkoy", "Basaksehir", "Bayrampasa", "Besiktas", "Beykoz", "Beylikduzu", "Beyoglu", "Buyukcekmece", "Catalca", "Cekmekoy", "Esenler", "Esenyurt", "Eyupsultan", "Fatih", "Gaziosmanpasa", "Gungoren", "Kadikoy", "Kagithane", "Kartal", "Kucukcekmece", "Maltepe", "Pendik", "Sancaktepe", "Sariyer", "Silivri", "Sultanbeyli", "Sultangazi", "Sile", "Sisli", "Tuzla", "Umraniye", "Uskudar", "Zeytinburnu"],
    "Izmir": ["Aliaga", "Balcova", "Bayindir", "Bayrakli", "Bergama", "Beydag", "Bornova", "Buca", "Cesme", "Cigli", "Dikili", "Foca", "Gaziemir", "Guzelbahce", "Karabaglar", "Karaburun", "Karsiyaka", "Kemalpasa", "Kinik", "Kiraz", "Kinali", "Konak", "Menderes", "Menemen", "Narlidere", "Odemis", "Seferihisar", "Selcuk", "Tire", "Torbalı", "Urla"],
    "Kahramanmaras": ["Afsin", "Andirin", "Caglayancerit", "Dulkadir", "Ekinözu", "Elbistan", "Goksun", "Nurhak", "Onikisubat", "Pazarcik", "Turkoglu"],
    "Karabuk": ["Eflani", "Eskipazar", "Merkez", "Ovacik", "Safranbolu", "Yenice"],
    "Karaman": ["Ayranci", "Basyayla", "Ermenek", "Merkez", "Kazimkarabekir", "Sariveliler"],
    "Kars": ["Arpacay", "Digor", "Kagizman", "Merkez", "Sarikamis", "Selim", "Susuz"],
    "Kastamonu": ["Abana", "Agli", "Arac", "Azdavay", "Bozkurt", "Cide", "Catalzeytin", "Daday", "Devrekani", "Ihsangazi", "Inebolu", "Kure", "Merkez", "Pinarbasi", "Seydiler", "Senpazar", "Taskopru", "Tosya"],
    "Kayseri": ["Akkisla", "Bunyan", "Develi", "Felahiye", "Hacilar", "Incesu", "Kocasinan", "Melikgazi", "Ozvatan", "Pinarbasi", "Sarioglan", "Sariz", "Talas", "Tomarza", "Yahyali", "Yesilhisar"],
    "Kirikkale": ["Bahsili", "Baliseyh", "Celebi", "Delice", "Karakecili", "Keskin", "Merkez", "Sulakyurt", "Yahsihan"],
    "Kirklareli": ["Babaeski", "Demirkoy", "Kofcaz", "Luleburgaz", "Merkez", "Pehlivankoy", "Pinarhisar", "Vize"],
    "Kirsehir": ["Akpinar", "Asikpinar", "Boztepe", "Cicekdagi", "Kaman", "Merkez", "Mucur"],
    "Kilis": ["Elbeyli", "Merkez", "Musabeyli", "Polateli"],
    "Kocaeli": ["Basiskele", "Cayirova", "Darica", "Derince", "Dilovasi", "Gebze", "Golcuk", "Izmit", "Kandira", "Karamursel", "Kartepe", "Korfez"],
    "Konya": ["Ahirl", "Akoren", "Aksehir", "Altinekin", "Beysehir", "Bozkir", "Cihanbeyli", "Celtik", "Cumra", "Derbent", "Derebucak", "Doganhisar", "Eregli", "Guneyyakasi", "Hadim", "Halkapinar", "Huyuk", "Ilg", "Kadinhani", "Karapinar", "Karatay", "Kulu", "Meram", "Sarayonu", "Selcuklu", "Seydisehir", "Taskent", "Tuzlukcu", "Yalihuyuk", "Yunak"],
    "Kutahya": ["Altintas", "Aslanapa", "Cavdarhisar", "Domaniç", "Dumlupinar", "Emet", "Gediz", "Hisarcik", "Merkez", "Pazarlar", "Saphane", "Simav", "Tavsanli"],
    "Malatya": ["Akcadag", "Arapgir", "Arguvan", "Battalgazi", "Darende", "Dogansehir", "Doganyol", "Hekimhan", "Kale", "Kuluncak", "Merkez", "Puturge", "Yazihan", "Yesilyurt"],
    "Manisa": ["Ahmetli", "Akhisar", "Alasehir", "Demirci", "Golmarmara", "Gordes", "Kirkağaç", "Koprubasi", "Kula", "Merkez", "Salihli", "Sarigol", "Saruhanli", "Selendi", "Soma", "Sehzadeler", "Turgutlu", "Yunusemre"],
    "Mardin": ["Artuklu", "Dargeçit", "Derik", "Kiziltepe", "Mazidagi", "Merkez", "Midyat", "Nusaybin", "Omerli", "Savur", "Yesilli"],
    "Mersin": ["Akdeniz", "Anamur", "Aydincik", "Bozyazi", "Camliyayla", "Erdemli", "Gulnar", "Mezitli", "Mut", "Silifke", "Tarsus", "Toroslar", "Yenisehir"],
    "Mugla": ["Bodrum", "Dalaman", "Datca", "Fethiye", "Kavakliyere", "Koycegiz", "Marmaris", "Menteşe", "Milas", "Ortaca", "Seydikemer", "Ula", "Yatagan"],
    "Mus": ["Bulanik", "Haskoy", "Korkut", "Malazgirt", "Merkez", "Varto"],
    "Nevsehir": ["Acigol", "Avanos", "Derinkuyu", "Gulsehir", "Hacibektas", "Kozakli", "Merkez", "Urgup"],
    "Nigde": ["Altunhisar", "Bor", "Camardi", "Ciftlik", "Merkez", "Ulukisla"],
    "Ordu": ["Akkus", "Altinordu", "Aybasti", "Camas", "Catalpinar", "Caybasi", "Fatsa", "Golkoy", "Gulyali", "Gurgentepe", "Ikizce", "Kabaduz", "Kabatas", "Korgan", "Kumru", "Mesudiye", "Persimbe", "Ulubey", "Unye"],
    "Osmaniye": ["Bahce", "Duzici", "Hasanbeyli", "Kadirli", "Merkez", "Sumbas", "Toprakkale"],
    "Rize": ["Ardesen", "Camlihemsin", "Cayeli", "Derepazari", "Findikli", "Guney su", "Hemşin", "Ikizdere", "Iyidere", "Kalkandere", "Merkez", "Pazar"],
    "Sakarya": ["Akyazi", "Arifiye", "Erenler", "Ferizli", "Geyve", "Hendek", "Karapurcek", "Karasu", "Kaynarca", "Kocaali", "Merkez", "Pamukova", "Sapanca", "Serdivan", "Sogutlu", "Tarakli"],
    "Samsun": ["Alacam", "Asarcik", "Atakum", "Ayvacik", "Bafra", "Canik", "Carsamba", "Havza", "Ilkadim", "Kavak", "Ladik", "Ondokuzmayis", "Salipazari", "Tekkekoy", "Terme", "Vezirkopru", "Yakakent"],
    "Siirt": ["Baykan", "Eruh", "Kurtalan", "Merkez", "Pervari", "Sirvan"],
    "Sinop": ["Ayancik", "Boyabat", "Dikmen", "Duragan", "Erfelek", "Gerze", "Merkez", "Sarayduzu", "Turkeli"],
    "Sivas": ["Akincilar", "Altinyayla", "Divrigi", "Doganşar", "Gemerek", "Golova", "Hafik", "Imranli", "Kangal", "Koyulhisar", "Merkez", "Susehri", "Sarkisla", "Ulas", "Yildizeli", "Zara"],
    "Sanliurfa": ["Akçakale", "Birecik", "Bozova", "Ceylanpınar", "Halfeti", "Haliliye", "Harran", "Hilvan", "Karakopru", "Siverek", "Suruç", "Viranşehir"],
    "Sirnak": ["Beytussebap", "Cizre", "Guclukonak", "Idil", "Merkez", "Silopi", "Uludere"],
    "Tekirdag": ["Cerkezkoy", "Corlu", "Ergene", "Hayrabolu", "Kapakli", "Malkara", "Marmara Ereğlisi", "Muratli", "Saray", "Suleymanpasa", "Sarkoy"],
    "Tokat": ["Almus", "Artova", "Basciftlik", "Erbaa", "Merkez", "Niksar", "Pazar", "Resadiye", "Sulusaray", "Turhal", "Yesilyurt", "Zile"],
    "Trabzon": ["Akcaabat", "Arakli", "Arsin", "Besikduzu", "Carsibasi", "Caykara", "Dernekpazari", "Duzkoy", "Hayrat", "Koprubasi", "Macka", "Merkez", "Of", "Surmene", "Salpazari", "Tonya", "Vakfikebir", "Yomra"],
    "Tunceli": ["Cemisgezek", "Hozat", "Mazgirt", "Merkez", "Nazımiye", "Ovacık", "Pertek", "Pul"],
    "Usak": ["Banaz", "Esme", "Karahalli", "Merkez", "Sivasli", "Ulubey"],
    "Van": ["Bahcesaray", "Baskale", "Caldiran", "Catak", "Edremit", "Ercis", "Gevas", "Gurpınar", "Ipekyolu", "Muradiye", "Ozalp", "Saray"],
    "Yalova": ["Altinova", "Armutlu", "Ciftlikkoy", "Cinarcik", "Merkez", "Termal"],
    "Yozgat": ["Akdagmadeni", "Aydincik", "Bogazliyan", "Candir", "Cayiralan", "Cekerek", "Kadişehri", "Merkez", "Saraykent", "Sarikaya", "Sorgun", "Sefaatli", "Yenifakili", "Yerkoy"],
    "Zonguldak": ["Alapli", "Caycuma", "Devrek", "Eregli", "Merkez", "Gokçebey", "Kilimli"]
}

hafta_gunleri = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar"]