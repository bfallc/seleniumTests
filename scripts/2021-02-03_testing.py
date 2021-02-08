#selenium driver
from selenium import webdriver
from selenium.webdriver.common.by import By

# import Action chains  
from selenium.webdriver import ActionChains
# from selenium.webdriver.common.action_chains import ActionChains 
 
#timing functions
import time

#supports keyboard presses
from selenium.webdriver.common.keys import Keys

# "which geckodriver" into term to find path
driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')

# driver.get("https://bfallc.github.io/seleniumTests/testPages/")
# elem2 = driver.find_element_by_css_selector('a[href*="statement"]')
# driver.execute_script("arguments[0].scrollIntoView();", elem2)

# actions = ActionChains(driver)
# actions.move_to_element(elem2).click().perform()

# #open a website
driver.get("https://www.amazon.com")

# #check that "python" is in the webpage title
assert "Amazon" in driver.title

# #find the searchbar (named "q")
elem = driver.find_element_by_name("field-keywords")

#scroll into view (just in case)
driver.execute_script("arguments[0].scrollIntoView();", elem)

# #clear the text box just in case
elem.clear()

# #type some stuff
elem.send_keys("house")

#optional
time.sleep(3)

#hit return
elem.send_keys(Keys.RETURN)

time.sleep(5)
# print("waited 3 sec")

#find the second link in search results

# this finds the first element with data-index='3' (searching down from root), 
# and then the h2/a element inside it
elem2 = driver.find_element_by_xpath("//*[contains (@data-index, '3')]//h2/a")

#prints the webdriver session id
print("elem2: " + str(elem2))
#prints the text node from inside elem2 (if there is one)
print(elem2.text)

# #scrolling. uses javascript due to a firefox quirk with webdriver
driver.execute_script("arguments[0].scrollIntoView();", elem2)
print("scrolled to element")

#optional
time.sleep(3)

#must be in view to click
elem2.click()
print("clicked") 

#not sure
# driver.implicitly_wait(3)
# print("waited 3 sec if necessary")

#optional
time.sleep(5)

#use javascript to go back one page in history (back button)
driver.execute_script("window.history.go(-1)")

time.sleep(3)

#find next
elem3 = driver.find_element_by_xpath("//*[contains (@data-index, '5')]//h2/a")

#scroll
driver.execute_script("arguments[0].scrollIntoView();", elem3)

#optional
time.sleep(3)

#click
elem3.click()

time.sleep(5)

#go back
driver.execute_script("window.history.go(-1)")

time.sleep(5)

#go back
driver.execute_script("window.history.go(-1)")

## multi-element lists below
##########################

# searchResults = driver.find_elements_by_partial_link_text("result")
# searchResults = driver.find_elements_by_xpath("//span[@class='linktext' and text()='outside']")

# for r in searchResults:
#     print(r.text)



## ActionChains
####################

# #not working yet:
# actions = ActionChains(driver)
# actions.move_to_element(elem2).click().perform()
# print("clicked once")


#alternatively, use an if statement:
# if "No results found." not in driver.page_source:
#     print("results found")

#close the browser window
# driver.quit()

time.sleep(4)
