import time
import os

from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

SNAPSHOT_JS = """
    var ele = document.querySelector('div[_echarts_instance_]');
    var mychart = echarts.getInstanceByDom(ele);
    return mychart.getDataURL({
        type: '%s',
        pixelRatio: %s,
         excludeComponents: ['toolbox']
    });
"""
SNAPSHOT_SVG_JS = """
   var element = document.querySelector('div[_echarts_instance_] div');
   return element.innerHTML;
"""


def make_snapshot(
    html_path: str,
    file_type: str,
    pixel_ratio: int = 2,
    delay: int = 2,
    browser='Chrome'
):
    if delay < 0:
        raise Exception('Time travel is not possible')
    if browser == 'Chrome':
        driver = get_chrome()
    elif browser == 'Safari':
        driver = get_safari()
    else:
        raise Exception('Unknown browser!')
    driver.set_script_timeout(delay + 1)

    if file_type == 'svg':
        snapshot_js = SNAPSHOT_SVG_JS
    else:
        snapshot_js = SNAPSHOT_JS % (file_type, pixel_ratio)

    if not html_path.startswith("http"):
        html_path = 'file://' + os.path.abspath(html_path)
    driver.get(html_path)
    time.sleep(delay)

    try:
        output = driver.execute_script(snapshot_js)
        driver.close()
        return output
    except exceptions.TimeoutException:
        raise Exception("Failed to get snapshot content")


def get_chrome():
    option = webdriver.ChromeOptions()
    option.add_argument("headless")
    capabilities = DesiredCapabilities.CHROME
    capabilities["loggingPrefs"] = {"browser": "ALL"}
    return webdriver.Chrome(
        options=option,
        desired_capabilities=capabilities)


def get_safari():
    return webdriver.Safari(executable_path='/usr/bin/safaridriver')
