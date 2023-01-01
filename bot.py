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
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.base_url = 'https://www.instagram.com/'
		self.bot = webdriver.Chrome(ChromeDriverManager().install())

	def login(self):
		self.bot.get(self.base_url)
		self.bot.implicitly_wait(10)
		
		# Cookie popup
		self.bot.find_element(By.XPATH,
							'/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]').click()

		# Enter username and password on website
		enter_username = WebDriverWait(self.bot, 20).until(
			expected_conditions.presence_of_element_located((By.NAME, 'username')))
		enter_username.send_keys(self.username)

		enter_password = WebDriverWait(self.bot, 20).until(
			expected_conditions.presence_of_element_located((By.NAME, 'password')))
		enter_password.send_keys(self.password)
		enter_password.send_keys(Keys.RETURN)

		
		# Save password popup
		self.bot.find_element(By.XPATH,
							'/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/section/div/button').click()
		self.bot.implicitly_wait(10)

		# Notifications popup
		self.bot.find_element(By.XPATH,
							'/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]').click()
		self.bot.implicitly_wait(20)
		
		# Direct messages button
		self.bot.find_element(By.XPATH,
							'/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[4]/div/a/div').click()
		self.bot.implicitly_wait(20)

		# Pencil button
		self.bot.find_element(By.XPATH,
							'/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[1]/div[1]/div/div[3]').click()
		self.bot.implicitly_wait(20)
		
	def message(self, username, message):
		# Enter username
		self.bot.find_element(By.XPATH,
							'/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[2]/input').send_keys(username)
		self.bot.implicitly_wait(20)
		
		# Select username
		self.bot.find_element(By.XPATH,
							'/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[2]/div[1]/div/div[2]/div/div').click()
		self.bot.implicitly_wait(20)

		# Next button
		self.bot.find_element(By.XPATH,
							'/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[3]/div/button/div').click()
		self.bot.implicitly_wait(20)
		
		# Click on message area
		send = self.bot.find_element(By.XPATH,
									'/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
		self.bot.implicitly_wait(20)
		
		# Type message
		send.send_keys(message)
		time.sleep(0.5)
		"""
		# Send message
		send.send_keys(Keys.RETURN)
		self.bot.implicitly_wait(20)
		"""
		# Write to next user
		self.bot.find_element(By.XPATH,
							'/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[1]/div[1]/div/div[3]').click()
		time.sleep(2)

