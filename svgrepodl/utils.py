import os
import time
from .Message import Message
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from progress.bar import IncrementalBar

def downloader(url, path):
  print('going to download into',path)

  options = Options()
  options.set_preference("browser.download.panel.shown", False)
  options.set_preference("browser.download.manager.showWhenStarting", False)
  options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
  options.set_preference("browser.download.folderList", 2)
  options.set_preference("browser.download.dir", path)
  options.add_argument("--headless")

  driver = webdriver.Firefox(options=options)
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
  all_links=driver.execute_script('all_links = []; links = document.querySelectorAll(".style_Node__7ZTBP a"); links.forEach(url => all_links.push(url.href)); return all_links');
  print('found',all_links)
  bar = IncrementalBar('📥 Icons Downloaded', max = len(all_links))
  
  for i, link in  enumerate(all_links):
    print('\n',link)
    driver.execute_script('''window.open("'''+link+'''","_blank");''')
    bar.next()
  print('\n')
  driver.close()
  Message.success('🎉 Download done!')
