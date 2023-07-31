import os
import time
from .Message import Message
from selenium import webdriver
from progress.bar import IncrementalBar

def downloader(url, path):
	driver = webdriver.Firefox()
	runBrowser(driver, url)

# @TODO=use WebDriverWait and find_elements_by_*
def runBrowser(driver, url):
	"""Run browser and start dowload
	Run browser and start download with progress bar
	
	Arguments:
		driver {[object]} -- Browser 
		url {[string]} -- URL of SVGREPO Collection
	"""
	driver.get(url)
	time.sleep(3) #REACT app need to sleep and wait app load.
	print('got',url)
	
	all_links=driver.execute_script('all_links = []; links = document.querySelectorAll(".style-module--action--1Avvt>a"); links.forEach(url => all_links.push(url.href)); return all_links');
	print('found the following links which have to be downloaded:\n',all_links)
	
	bar = IncrementalBar('📥 Icons Downloaded', max = len(all_links))
	for i, link in  enumerate(all_links):
		print('downloading',link,'\n')
		driver.execute_script('''window.open("'''+link+'''","_blank");''')
		bar.next()
	print('\n')
	driver.close()
	Message.success('🎉 Download done!')
