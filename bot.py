from selenium import webdriver
import os
import time
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

class Bot:
	def __init__(self, username, password, driver):
		self.username = username
		self.password = password
		self.base_url = 'https://www.instagram.com/'
		self.bot = driver	
		self.login()



	def login(self):
		self.bot.get(self.base_url)
		self.bot.implicitly_wait(10)
		# cookie popup
		self.bot.find_element(By.XPATH,
							'/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]').click()

		enter_username = WebDriverWait(self.bot, 20).until(
			expected_conditions.presence_of_element_located((By.NAME, 'username')))
		enter_username.send_keys(self.username)

		enter_password = WebDriverWait(self.bot, 20).until(
			expected_conditions.presence_of_element_located((By.NAME, 'password')))
		enter_password.send_keys(self.password)
		enter_password.send_keys(Keys.RETURN)

		
		# save password popup
		self.bot.implicitly_wait(10)
		self.bot.find_element(By.XPATH,
							'/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/section/div/button').click()
		
		self.bot.implicitly_wait(20)
		# 2nd pop-up
		self.bot.find_element(By.XPATH,
							'/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]').click()
		
		self.bot.implicitly_wait(20)
		# direct button
		self.bot.find_element(By.XPATH,
							'/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[4]/div/a/div').click()

		self.bot.implicitly_wait(20)
		# clicks on pencil icon
		self.bot.find_element(By.XPATH,
							'/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[1]/div[1]/div/div[3]').click()
		self.bot.implicitly_wait(20)

	def message(self, recipient):
		# enter the username
		self.bot.find_element(By.XPATH,
							'/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[2]/input').send_keys(recipient)
		
		self.bot.implicitly_wait(20)
		# click on the username
		self.bot.find_element(By.XPATH,
							'/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[2]/div[1]/div/div[2]/div/div').click()


		# next button
		self.bot.implicitly_wait(20)
		self.bot.find_element(By.XPATH,
							'/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[3]/div/button/div').click()
		# click on message area
		self.bot.implicitly_wait(20)
		send = self.bot.find_element(By.XPATH,
									'/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
		"""
		# types message
		self.bot.implicitly_wait(20)
		send.send_keys("Happy new year!")
	
		# send message
		self.bot.implicitly_wait(20)
		send.send_keys(Keys.RETURN)
		"""
		# clicks on direct option or pencil icon
		self.bot.implicitly_wait(50)
		self.bot.find_element(By.XPATH,
							'/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[1]/div[1]/div/div[3]').click()


