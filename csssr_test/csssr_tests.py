import os
import unittest
import urllib.request
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup



class csssrTests(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(executable_path=r"C:\webdrivers\chromedriver.exe")
		self.url = "https://csssr.github.io/qa-engineer"
		self.driver.implicitly_wait(20)

	def test_percent_5_0(self):
		driver=self.driver
		driver.get("https://csssr.github.io/qa-engineer")

# Click tabs
		driver.find_element_by_partial_link_text("НАХОДИТЬ НЕСОВЕРШЕНСТВА").click()
		sleep(3)
		driver.find_element_by_partial_link_text("СОПРОВОЖДАТЬ ПРОЕКТЫ").click()
		sleep(3)
		driver.find_element_by_partial_link_text("РАБОТАТЬ С ФАЙЛАМИ ПРОЕКТОВ").click()
		sleep(3)
		driver.find_element_by_partial_link_text("ВНИКАТЬ В ДЕТАЛИ ПРОЕКТОВ").click()
		sleep(3)

	def test_link_8_0(self):
		url_list0 = []
		html_page = urllib.request.urlopen(self.url)
		soup = BeautifulSoup(html_page, "lxml")

# We're searching link
		link=soup.find("input",id="soft").find_next("a")

# We're printing a current link
		print("_______8_0 Test link_______ ")
		print("It's link: "+link["href"])

# And print test result if link searched
		if "http://monosnap.com/" in link["href"]:
			print('Pass!')
		else:
		  	print('Fail! It is not this link: http://monosnap.com/' )
   
	def tear_down(self):
		self.driver.quit()
		driver.guit()
 
if __name__ == "__main__":
	unittest.main()
