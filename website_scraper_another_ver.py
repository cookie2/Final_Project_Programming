# for system, do not edit it
import time
import pathlib
import sys
import ssl
from win32com.client import Dispatch
# if you want to export result by csv, add this line:
import csv
# in that case, this package is used for edit our string
import re
# the package which is uesd for retrieval elements from website
from bs4 import BeautifulSoup
# selenium, is used for simulate a browser
import undetected_chromedriver.v2 as uc

# fake SSL request, do not edit it
ssl._create_default_https_context = ssl._create_unverified_context

# get chrome version, just available in Windows
parser = Dispatch("Scripting.FileSystemObject")
resp = ""
try:
    resp = parser.GetFileVersion(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
except:
    resp = parser.GetFileVersion(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
version = eval(resp.split(".")[0])

# set  up your driver
# undetected_chromedriver cannot set options, but author said it will be available soon.
#chrome_options = uc.ChromeOptions()
#driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=chrome_options)

# 'version_main' should same as your browser, in this case, we get it automatically
driver = uc.Chrome(use_subprocess=True, version_main=version)

# pass the url and get source page
def html_code(url):
    driver.get(url)
    # wait website load it's resource
    time.sleep(10)
    js = "window.scrollTo(0, document.body.scrollHeight/2);"
    time.sleep(10)
    js = "window.scrollTo(0, document.body.scrollHeight);"
    driver.execute_script(js)
    time.sleep(10)
    
    #action you want to do on this website
    #element = driver.find_element(By.XPATH, '//*[@id="reviews-medley-footer"]/div[2]/a')
    #element.click()
    #driver.execute_script("arguments[0].click();", userName)
    #time.sleep(10)
    
    #try to get source
    try:
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        return (soup)
    except:
        print(str(sys.exc_info()))
        return False

# some character may caused problem in csv, we should handle it first
def handle_unacceptable_char(string):
    # delete html tag contain in string
    pattern = re.compile(r'<[^>]+>',re.S)
    resp = pattern.sub('', string)
    # delete newline punctuation
    resp = resp.replace("\n", "")
    resp = resp.replace("\r", "")
    #return data, data type is string
    return resp 

# find the html tag and clear it, edit this section to meet your needs
def cus_resp(soup):
    result = []
    # in this case, i get my target from element's class name, refer to the selenium find functions
    for item in soup.find_all("div", {"data-purpose":"review-comment-content"}):
        data_str = item.text
        # note: because  ',' may contain in review sentence, so we should handle it first or use  special characters as delimiter when you export your result as a csv file
        data_str = handle_unacceptable_char(data_str)
        result.append(data_str)
    return (result)

# export the result to a csv file
def export_to_csv(data):
    recoardfile = '.\\result.csv'
    # open recoardfile, if this file dose not exist then create one
    with open(recoardfile , 'w', encoding="utf-8", newline='') as file:
        mywriter = csv.writer(file, delimiter=',', quotechar='"')
        # write csv colume's header
        mywriter.writerow(["review"])
        for row in data:
            # waring: in this case, 'data' is a string array' so that 'row' is string, you should edit this line according to your data type 
            mywriter.writerow([row])

# declare a variable to store your URL
url = "https://www.udemy.com/course/build-a-web-scraper-with-python/"

if __name__ == "__main__":
    # get website content
    soup = html_code(url)
    # if success then ...
    if not soup == False:
        # handle the content you got
        resp_data = cus_resp(soup)
        # export the result
        export_to_csv(resp_data)
    # remember to close browser
    driver.close();
    driver.service.stop()
