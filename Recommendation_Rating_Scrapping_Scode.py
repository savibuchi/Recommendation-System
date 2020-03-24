from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
# WAIT FOR ELEMENTS
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
#CATCH EXCEPTIONS
#from selenium.common.exceptions import TimeoutException,ElementNotVisibleException
import re
import csv

#Configure browser
path_to_chromedriver =  "chromedriver.exe" # change path as needed
browser = webdriver.Chrome(executable_path = path_to_chromedriver)
browser.wait = WebDriverWait(browser, 5)

#Crawl 1st page
path= "reviews_32618_for_1098_users_with_location.csv"
data1 = pd.read_csv(path,encoding='latin')
data1=np.array(data1)
dataurl= data1[:,10]
dataurl=np.unique(dataurl)
with open('c://Users/1/Desktop/project10.csv', 'w') as output:
        output.write(str(dataurl))
lth=len(dataurl)
url.append(dataurl[0])
#browser.get(url[i])
url = 'https://www.tripadvisor.in/Hotel_Review-g189852-d207022-Reviews-Radisson_Blu_Royal_Viking_Hotel_Stockholm-Stockholm.html'
browser.get(url)
url=[]
arr=[]
i=0

for i in range(0,l):
    url.append(dataurl[i])
    try:
        browser.get(url[i])
        browser.wait = WebDriverWait(browser, 5)
        #y1 = browser.wait.until(EC.presence_of_element_located(By.CSS_SELECTOR("#taplc_location_detail_overview_hotel_map_pins_default_0 > div > div.overviewContent > div.ui_columns.is-multiline.is-mobile.reviewsAndDetails > div.ui_column.is-6.reviews > div.rating > span")))
        y2 = browser.find_element_by_css_selector("#taplc_location_detail_overview_hotel_map_pins_default_0 > div > div.overviewContent > div.ui_columns.is-multiline.is-mobile.reviewsAndDetails > div.ui_column.is-6.reviews > div.rating > span")
        arr.append(float(y2.text))
    except :
        arr.append(float(0))
                      
with open('c://Users/1/Desktop/project2.csv', 'w') as output:
        output.write(str(arr))
with open('c://Users/1/Desktop/project3.csv', 'w') as output:
        output.write(str(url))    

