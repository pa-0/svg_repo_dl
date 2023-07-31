import os
import time
from .Message import Message
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

def downloader(url, path):
  print('going to download into',path)

  options = Options()
  options.add_argument("--headless")

  driver = webdriver.Firefox(options=options)
  runBrowser(driver, url, path)

# @TODO=use WebDriverWait and find_elements_by_*
def runBrowser(driver, url, path):
  """Run browser and start dowload
  Run browser and start download
  
  Arguments:
    driver {[object]} -- Browser 
    url {[string]} -- URL of SVGREPO Collection
  """
  
  n = 0
  m = 0
  while True:
    n += 1
    
    driver.get(url + '/' + str(n))
    time.sleep(10) # you want to wait longer, if your internet connection is slow
    print('>>>> inspecting',url)
    all_links=driver.execute_script('all_links = []; links = document.querySelectorAll(".style_Node__7ZTBP a img"); links.forEach(img => all_links.push(img.src)); return all_links');
    if len(all_links) == 0:
      print('no more icons to download\n')
      break
      
    for i, link in  enumerate(all_links):
      m += 1
      print('downloading icon #' + str(m),link)
      os.system('wget --quiet ' + link + ' -O ' + path + '/' + link.rsplit('/',1)[1])
  driver.close()
  Message.success('🎉 Download done!')
