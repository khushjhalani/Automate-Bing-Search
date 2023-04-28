import random
import json,requests
from time                                           import sleep
from selenium                                       import webdriver
# from selenium.webdriver.edge.options                import Options
# from selenium.webdriver.edge.service                import Service
import argparse as ap


# #TO OPEN MY DEFAULT EDGE PROFILE AND NOT OPEN A NEW BOT PROFILE
# edge_driver_path = "C:\Program Files (x86)\edgedriver_win64"
# edge_options = Options()
# edge_options.add_argument("user-data-dir=C:\Users\[USERNAME]\AppData\Local\Microsoft\Edge\User Data\Default")
# driver = webdriver.Edge(service=Service(executable_path=edge_driver_path), options=edge_options)


def get_arguments():
    parser = ap.ArgumentParser()
    parser.add_argument('-s', '--searches', help='No of searches', required=True, type=int)
    inputs = parser.parse_args()
    # if not inputs.example:
    #    parser.error("[-] Please specify an input")
    return inputs

response = requests.get("https://www.randomlists.com/data/words.json")
wLsample = random.sample((json.loads(response.text)['data']),150)

def randomText():
    base_url = "https://www.bing.com/search?q="
    # return f"{base_url}{random.choice(wLsample)}+{random.choice(wLsample)}+{random.choice(wLsample)}"
    return base_url + random.choice(wLsample)


# def waitForPageLoad():
# while driver.execute_script("return document.readyState") != ("complete" or 'interactive'):
#     sleep(0.5)

def randomBingSearch(times: int = 10):
    for i in range(0, times):
        driver.get(randomText())
        sleep(1)
        # waitForPageLoad()


#Driver Code
if __name__ == "__main__":
    inp = get_arguments()
    driver = webdriver.Edge()
    driver.get("https://rewards.bing.com/")
    sleep(3)
    #Open a new tab
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    randomBingSearch(inp.searches)
    driver.close()
