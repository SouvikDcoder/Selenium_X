# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 01:35:42 2023

@author: souvik.dey
"""

"""
TO use this keyword you have to start chrome browser from command prompt (WIN + R) using command given bellow.
>> chrome.exe --remote-debugging-port=9289 --user-data-dir=c:\gcdata 
""" 
from browsermobproxy import Server
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from haralyzer import HarPage


server = Server(r"C:\Users\souvik.dey\Desktop\AutomationCode\browsermob-proxy-2.1.4\bin\browsermob-proxy.bat")
server.start()
print('----here----')
proxy = server.create_proxy()


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--proxy-server={0}".format(proxy.proxy))
driver = webdriver.Chrome(r"D:\Workspace\Automation\chromedriver.exe", chrome_options=chrome_options)

proxy.new_har("my-test")
driver.get("https://www.google.com")


har_page = HarPage("my-test.har")
entries = har_page.entries
for entry in entries:
    if entry.response.status != 200:
        print("Request failed: {0} {1}".format(entry.request.method, entry.request.url))



# =============================================================================
# 
# // start the proxy
# BrowserMobProxy proxy = new BrowserMobProxyServer();
# proxy.start(0);
# 
# // get the Selenium proxy object
# Proxy seleniumProxy = ClientUtil.createSeleniumProxy(proxy);
# 
# // configure it as a desired capability
# # =============================================================================
# # DesiredCapabilities capabilities = new DesiredCapabilities();
# # capabilities.setCapability(CapabilityType.PROXY, seleniumProxy);
# # =============================================================================
# 
# ChromeOptions options = new ChromeOptions();
# options.setCapability("proxy", seleniumProxy);
# 
# // start the browser up
# # =============================================================================
# # WebDriver driver = new FirefoxDriver(capabilities);
# # =============================================================================
# # opt = Options()
# # opt.add_experimental_option("debuggerAddress", "127.0.0.1:9289")
# driver = webdriver.Chrome(executable_path="D:\Workspace\Automation\insync\src\inSyncQA\chromedriver.exe",chrome_options=options)
# 
# // enable more detailed HAR capture, if desired (see CaptureType for the complete list)
# proxy.enableHarCaptureTypes(CaptureType.REQUEST_CONTENT, CaptureType.RESPONSE_CONTENT);
# 
# // create a new HAR with the label "yahoo.com"
# proxy.newHar("yahoo.com");
# 
# // open yahoo.com
# driver.get("http://yahoo.com");
# 
# // get the HAR data
# Har har = proxy.getHar();
# =============================================================================




# =============================================================================
# 
# # Set up the BrowserMob Proxy server:
# # Replace browsermob_path with the path to the BrowserMob Proxy binary.
# def setup_browsermob_proxy(browsermob_path):
#     server = Server(ProxyManager.browsermob_path)
#     server.start()
#     return server
# 
# # Configure Selenium with Chromedriver to use the BrowserMob Proxy:
# # Replace chromedriver_path with the path to the Chromedriver binary. 
# def setup_chromedriver(chromedriver_path, proxy):
#     chrome_options = webdriver.ChromeOptions()
#     chrome_options.add_argument(f"--proxy-server={proxy.proxy}")
# 
#     driver = webdriver.Chrome(executable_path=chromedriver_path, options=chrome_options)
#     return driver
# 
# # Start the proxy server and create a proxy:
# def create_proxy(server):
#     return server.create_proxy()
# 
# # Set up desired capabilities in Selenium to use the proxy:
# def set_proxy_capabilities(proxy, driver):
#     proxy_capabilities = webdriver.DesiredCapabilities.CHROME
#     proxy_capabilities["proxy"] = {
#         "httpProxy": proxy.proxy,
#         "ftpProxy": proxy.proxy,
#         "sslProxy": proxy.proxy,
#         "proxyType": "MANUAL"
#     }
# 
#     driver.start_session(proxy_capabilities)
# 
# # Capture network traffic:
# def start_har_capture(proxy, har_name):
#     proxy.new_har(har_name)
# 
# # Perform web activities:
# def navigate_to_url(driver, url):
#     driver.get(url)
# 
# # Analyze and process the captured network traffic:
# def get_captured_traffic(proxy):
#     return proxy.har
# 
# 
# # Close the proxy server and WebDriver:
# def close_resources(server, driver):
#     driver.quit()
#     server.stop()
# 
# 
# # Now, using these functions in our main code to monitor network traffic using BrowserMob Proxy, Selenium, and Chromedriver:
# 
# def main():
#     browsermob_path = r"C:\Users\souvik.dey\Desktop\AutomationCode\browsermob-proxy-2.1.4\bin\browsermob-proxy.bat"
#     chromedriver_path = r"D:\Workspace\Automation\insync\src\inSyncQA\chromedriver.exe"
#     
#     server = setup_browsermob_proxy(browsermob_path)
#     proxy = create_proxy(server)
#     
#     driver = setup_chromedriver(chromedriver_path, proxy)
#     set_proxy_capabilities(proxy, driver)
#     
#     har_name = "example"
#     start_har_capture(proxy, har_name)
#     
#     url = "https://www.google.com/"
#     navigate_to_url(driver, url)
#     
#     network_traffic = get_captured_traffic(proxy)
#     print(network_traffic)
#     
#     close_resources(server, driver)
# 
# if __name__ == "__main__":
#     main()
#     
# =============================================================================




