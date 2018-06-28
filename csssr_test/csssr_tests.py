import os
import unittest
import urllib.request
import re
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup



class csssrTests(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(executable_path=r"C:\webdrivers\chromedriver.exe")
		self.url = "https://csssr.github.io/qa-engineer"
		self.driver.implicitly_wait(20)

# 	def test_percent_5_0(self):
# 		driver=self.driver
# 		driver.get("https://csssr.github.io/qa-engineer")

# # Click tabs
# 		driver.find_element_by_partial_link_text("НАХОДИТЬ НЕСОВЕРШЕНСТВА").click()
# 		sleep(3)
# 		driver.find_element_by_partial_link_text("СОПРОВОЖДАТЬ ПРОЕКТЫ").click()
# 		sleep(3)
# 		driver.find_element_by_partial_link_text("РАБОТАТЬ С ФАЙЛАМИ ПРОЕКТОВ").click()
# 		sleep(3)
# 		driver.find_element_by_partial_link_text("ВНИКАТЬ В ДЕТАЛИ ПРОЕКТОВ").click()
# 		sleep(3)

	def test_link_8_0(self):

# Click tabs
		url_list0 = []
		html_page = urllib.request.urlopen(self.url)
		soup = BeautifulSoup(html_page, "lxml")
		# for id_1 in soup.find_all("a"):
		

		# for tag in soup.find_all(re.compile("http[s]?^")):
		# 	print(tag.name)

		link=soup.find("input",id="soft")

		print(link.find_next('a', 'href'))

		# for link1 in link.find_next_siblings("a"):
		# 	  if "app" in link1["href"]:
		# 	  	print('found a url with national-park in the link')

		# print(link.find_next("a"))
		 	# print(id_1["data-id"])
		 	# url_list0.append(id_1["href"])
		 	# print("bala: "+id_1["type"])
		 	# print(id_1.find_next_siblings("a"))
		 	# print(id_1.p['a'])

# print the first elemnt id 
		# print("bala: "+url_list0[0]) 

    
	def tear_down(self):
		self.driver.quit()
 
if __name__ == "__main__":
	unittest.main()
