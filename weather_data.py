from selenium import webdriver
import time

class Weather:
    def __init__(self,city):
        self.url="https://www.mgm.gov.tr/tahmin/il-ve-ilceler.aspx?il="
        self.browser=webdriver.Chrome()
        self.city=city
        
    def cityWeather(self):
        self.browser.get(self.url + self.city)
        time.sleep(2)
        day = self.browser.find_element_by_xpath("/html/body/div[2]/div[2]/div/section/div[8]/table/tbody/tr[1]/td[1]").text
        weather_info = self.browser.find_element_by_xpath("/html/body/div[2]/div[2]/div/section/div[8]/table/tbody/tr[1]/td[2]/img").get_attribute("title")
        temperature = self.browser.find_element_by_xpath("/html/body/div[2]/div[2]/div/section/div[8]/table/tbody/tr[1]/td[4]").text
        print(f"{day}, {weather_info}, {temperature}")
    
    def townWeather(self):
        town=["Akseki","Aksu","Alanya","Demre","Döşemealtı","Elmalı","Finike","Gazipaşa",
              "Gündoğmuş","İbradı","Kaş","Kemer","Kepez","Konyaaltı","Korkuteli","Kumluca",
              "Manavgat","Muratpaşa","Serik"]
        for i in town:
            self.browser.get(self.url + self.city + "&ilce=" + i)
            time.sleep(2)
            day = self.browser.find_element_by_xpath("/html/body/div[2]/div[2]/div/section/div[8]/table/tbody/tr[1]/td[1]").text
            weather_info = self.browser.find_element_by_xpath("/html/body/div[2]/div[2]/div/section/div[8]/table/tbody/tr[1]/td[2]/img").get_attribute("title")
            temperature = self.browser.find_element_by_xpath("/html/body/div[2]/div[2]/div/section/div[8]/table/tbody/tr[1]/td[4]").text
            print(f"{day} günü {i} ilçesinde, hava {weather_info}, sıcaklık {temperature} derecedir.")
        time.sleep(2)
    
    def close(self):
        self.browser.close()
            
        
if __name__ == '__main__':
    weather=Weather('Antalya')
    weather.cityWeather()
    weather.townWeather()
    weather.close()