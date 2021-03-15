from msedge.selenium_tools import Edge, EdgeOptions
import time

options = EdgeOptions()
options.use_chromium = True
driver = Edge(options = options)

time.sleep(3)
driver.quit()