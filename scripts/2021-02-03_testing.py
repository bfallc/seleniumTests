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

driver.get("https://bfallc.github.io/seleniumTests/testPages/")
# elem2 = driver.find_element_by_css_selector('a[href*="statement"]')
# driver.execute_script("arguments[0].scrollIntoView();", elem2)

# actions = ActionChains(driver)
# actions.move_to_element(elem2).click().perform()

# #open a website
# driver.get("https://www.amazon.com")

# #check that "python" is in the webpage title
# assert "Amazon" in driver.title

# #find the searchbar (named "q")
# elem = driver.find_element_by_name("field-keywords")
# #clear the text box just in case
# elem.clear()
# #type some stuff
# elem.send_keys("house")
# #hit return
# elem.send_keys(Keys.RETURN)

# time.sleep(5)
# print("waited 3 sec")

#find the second link in search results

# #doesn't work with multiple items with same partial link
# elem2 = driver.find_element_by_css_selector('a[href*="sr=8-2"]')

# #works
# elem2 = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div[2]/div/span[3]/div[2]/div[3]/div/span/div/div/div[2]/div[2]/div/div[1]/h2/a")

# searchResults = driver.find_elements_by_partial_link_text("result")
searchResults = driver.find_elements_by_xpath(".//span")
# searchR = driver.find_elements(By.)
print("elem2")
for r in searchResults:
    print(r.text)

# #scrolling (works)
# driver.execute_script("arguments[0].scrollIntoView();", elem2)
# print("scrolled to element")

# elem2.click()
# print("clicked") 

# #not working yet:
# actions = ActionChains(driver)
# actions.move_to_element(elem2).click().perform()
# print("clicked once")

driver.implicitly_wait(3)
print("waited 3 sec")
#click link with 'sr=8-2' in address (second link)
# driver.find_element_by_css_selector('a[href*="sr=8-1"]').click()




#if assert is true, nothing happens, otherwise assertion error occurs
#if "no results found" is contained in the page source, throw the error "nothing found"
#assert "No results found." not in driver.page_source, "nothing found"

#alternatively, use an if statement:
if "No results found." not in driver.page_source:
    print("results found")

#close the browser window
# driver.quit()

