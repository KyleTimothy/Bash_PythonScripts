from selenium import webdriver
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome("/Users/kylebrooks/Downloads/chromedriver_win32/chromedriver")

driver.get("https://www.cnbc.com/cryptocurrency/")

#whole table, you will grab the id or xpath as the first drill down 
table = driver.find_element_by_xpath("//table[@class='BasicTable-tableBody']")
#column headers from within the table
#header = driver.find_elements_by_tag_name("th")

""" The tbody of the table will be the second drilldown
within the inside of the table but will be passed the 
variable body
 """
body = table.find_element_by_tag_name("tbody")

rows = body.find_elements_by_tag_name("tr")
"""
Will pass the body through rows as row and grab the 
element tr
"""
cells = body.find_elements_by_tag_name("td")
"""
body will pass into data table and pass through the variable 
cells
"""
"""
Enclose len(rows) in the variable length of length variable
name
"""
for headers in cells:
    print(headers.text)

length_Of_Length = len(rows)
""" 


 loop in the length of length to extract the 
 columns and interating rows with (i). and joining through the tag elements of 
 td. Then make another loop inside of the for loop to get the length of columns. 
 Set a condition with columns that will interate the text based on what 
 you may select or pass through the parameter
 and interate the first columns at zero with the click.
 """
for i in range((length_Of_Length)):
    columns = rows[i].find_elements_by_tag_name("td")
    for x in range(len(columns)):
        if columns[x].text == "Bitcoin/USD Coinbase":
            columns[0].click() 