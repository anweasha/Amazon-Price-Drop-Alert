# importing all the necessary libraries

import smtplib
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import warnings
warnings.filterwarnings("ignore")



URL = ''
fromEmail = ''
# Generate app password (mail) for 2-step verification enabled accounts. 
# For others, disable secure login from Account Settings->Security.
pwd = ''
toEmail = ''
updateAfter = 0
price = 0.0
name = ''
contact = ''



def main():
    global url
    url = input()
    global fromEmail
    fromEmail = input()
    global pwd
    pwd = input()
    global toEmail
    toEmail = input()
    global contact
    contact = input()
    global updateAfter
    updateAfter = int(input())
    global price
    driver = webdriver.Chrome('/opt/homebrew/bin/chromedriver')
    driver.get(url)
    
    global name
    name = driver.find_element_by_xpath('//*[@id="productTitle"]').text
    
    global price
    # get the price when the program runs for the first time
    price = driver.find_element_by_xpath('//*[contains(@class,"PriceToPay")]').text
    price = float(price[1:].replace(',', ''))
                  
    time.sleep(10)
    # start monitoring
    if(updateAfter!=0):
        while(True):
            priceVariationCheck()
            time.sleep(60*60*updateAfter)
    else:
        priceVariationCheck()

        

# to update the price of the product to the current price

def updateprice():
    driver = webdriver.Chrome('/opt/homebrew/bin/chromedriver')
    driver.get(url)

    priceNow = driver.find_element_by_xpath('//*[contains(@class,"PriceToPay")]').text
    priceNow = float(priceNow[1:].replace(',', ''))

    return priceNow



# to check if there is any variation between the original price and the current price of the product

def priceVariationCheck():
    newPrice = updateprice()
    global price
    if(newPrice < price):
        price = newPrice
        send_msg(newPrice)
        send_mail(newPrice)
        


# to send a WhatsApp message to the user-accepted number once the price decreases        
        
def send_msg(currentPrice):
    
    url1=f'https://web.whatsapp.com/send?phone={contact}&text&app_absent=0'
    option=Options()
    option.add_argument(r'user-data-dir=/Users/anweashasaha/Desktop/whatsapp_profile')
    
    driver = webdriver.Chrome('/opt/homebrew/bin/chromedriver',options=option)
    driver.get(url1)
    
    time.sleep(40)
    chatbox = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')

    chatbox.send_keys(f'ALERT: Price Went Down!\nCheck the Amazon link: {url}\nPrice Reduced By: Rs.{price-currentPrice}\nCurrent Price: Rs.{currentPrice}')
    time.sleep(5)
    chatbox.send_keys(Keys.RETURN) 
    time.sleep(0.1)
    chatbox.send_keys(Keys.RETURN) 
    time.sleep(0.1)
    chatbox.send_keys(Keys.RETURN) 
    time.sleep(0.1)
    chatbox.send_keys(Keys.RETURN)
    time.sleep(3)
    
    print("Hey, WhatsApp message has been sent!")
    driver.quit()
    
    
    
# to send a mail to the user-accepted email address once the price decreases

def send_mail(currentPrice):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login(fromEmail, pwd)
    
    subject = f'ALERT: Price Went Down for Your Favourite Item!'
    body = f'Check the Amazon link: \n{url}\nPrice Reduced By: Rs.{price-currentPrice}\nCurrent Price: Rs.{currentPrice}'
    msg = f'Subject: {subject}\n\n{body}'
    
    server.sendmail(fromEmail, toEmail, msg)
    
    print("Hey, email has been sent!")
    server.quit()
  

    
if __name__ == "__main__":
    main()