from selenium import webdriver
driver = webdriver.PhantomJS(executable_path="phantomjs")
driver.get("http://www.baidu.com")
driver.save_screenshot('t.png')