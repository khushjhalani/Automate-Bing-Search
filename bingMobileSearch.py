import random
import json,requests
from time                                           import sleep
from selenium                                       import webdriver
from selenium.webdriver.edge.options                import Options
import argparse as ap

def get_arguments():
    parser = ap.ArgumentParser()
    parser.add_argument('-s', '--searches', help='No of searches', required=True, type=int)
    parser.add_argument('-u', '--username', help=r"Username of your system profile. Can be found in C:\Users\[USERNAME]", required=True, type=str)
    inputs = parser.parse_args()
    # if not inputs.example:
    #    parser.error("[-] Please specify an input")
    return inputs

response = requests.get("https://www.randomlists.com/data/words.json")
wLsample = random.sample((json.loads(response.text)['data']),150)

def randomText():
    base_url = "https://www.bing.com/search?q="
    return base_url + random.choice(wLsample)

def randomBingSearch(driver, times: int = 10):
    for i in range(0, times):
        driver.get(randomText())
        sleep(1)
        # waitForPageLoad()

def get_driver(uname):
    mobile_emulation = {
    "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
    "userAgent": "Mozilla/5.0 (Linux; Android 10; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36",
    }
    edge_options = Options()
    edge_options.add_argument(f"user-data-dir=C:\\Users\\{uname}\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default")
    edge_options.add_experimental_option("mobileEmulation", mobile_emulation)
    driver = webdriver.Edge(options=edge_options)
    return driver

#Driver Code
if __name__=="__main__":
    inp = get_arguments()
    driver = get_driver(inp.username)
    driver.get("https://rewards.bing.com/")
    sleep(3)
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    randomBingSearch(driver, inp.searches)