# Amazon Price Drop Alert

A Python program to check the price of an Amazon product and send  a mail and a WhatsApp message if price falls down below the last checked price.


### Input:

1. Product URL
2. Email address from which the notification is to be sent
3. An app password for above email
4. Destination email
5. WhatsApp number 
6. The number of hours after which it should check again

<br>

## Clone Project
```
https://github.com/anweasha/Amazon-Price-Drop-Alert.git
```
<br>

## Instructions to Run:

> To send a mail
- For safety, preferably generate an app password for the sender gmail account in case it has 2-step verification enabled.
- Otherwise, you need to change a setting in the Gmail account to ensure you can send a mail. 
- Head to this website: https://myaccount.google.com/lesssecureapps
- Make sure the setting is turned ON. If not, Python cannot log into your Gmail account.

<br>

> To send a WhatsApp message
- While running the send_msg() function, a Chrome browser while pop up and you should see a screen that asks you to scan a QR code to log into WhatsApp. It means you need to manually use your phone to scan it before the program can access your WhatsApp profile.
- To fix this, create a folder called “whatsapp_profile” in the current working directory. You can choose any location and any folder name. 
- In the pricecheck.py file, you'll notice I have already created this file and mentioned the path as 'user-data-dir=/Users/anweashasaha/Desktop/whatsapp_profile'. Replace '/Users/anweashasaha/Desktop/whatsapp_profile' with the path of your "whatsapp_profile" folder.
- After making these changes and running the code, you’ll get a bunch of files populated in the “whatsapp_profile” folder. 
- A Chrome browser should open up with the WhatsApp page. Go ahead and use your phone to scan the QR code to log in. After logging in, you can close the browser and Selenium. 
- Try re-running the code, this time you should land on a WhatsApp page that’s already logged in. But this time use the following code
```
option=Options()
driver = webdriver.Chrome('/opt/homebrew/bin/chromedriver',options=option)
driver.get(url1)
```
instead of
```
option=Options()
option.add_argument(r'user-data-dir=/Users/anweashasaha/Desktop/whatsapp_profile')
driver = webdriver.Chrome('/opt/homebrew/bin/chromedriver',options=option)
driver.get(url1)
```
otherwise you'll get an error.

<br>

## Tech Stack Used
- Python
- Selenium
- ChromeDriver
- email
- smtplib
