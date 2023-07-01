from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
print("All Modules are loaded")


driver = webdriver.Remote(
    command_executor="http://chrome.radu.ovh:4444/ui",
    desired_capabilities=DesiredCapabilities.CHROME
    )

URL = "https://www.rd.com/jokes/"
driver.get(url=URL)
print(driver.page_source)

from tiktok_uploader.upload import upload_video, upload_videos
from tiktok_uploader.auth import AuthBackend

# single video
upload_video('tiktokvideo.mp4', 
            description='this is my description', 
            cookies='cookies.txt')