#selenium driver
from selenium import webdriver

#supports keyboard presses
from selenium.webdriver.common.keys import Keys

# "which geckodriver" into term to find path
driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')

#open a website
driver.get("http://www.python.org")

#check that "python" is in the webpage title
assert "Python" in driver.title

#find the searchbar (named "q")
elem = driver.find_element_by_name("q")
#clear the text box just in case
elem.clear()
#type some stuff
elem.send_keys("pyth333n")
#hit return
elem.send_keys(Keys.RETURN)

#if assert is true, nothing happens, otherwise assertion error occurs
#if "no results found" is contained in the page source, throw the error "nothing found"
#assert "No results found." not in driver.page_source, "nothing found"

#alternatively, use an if statement:
if "No results found." not in driver.page_source:
    print("no results found")

#close the browser window
# driver.quit()

