import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def test_scores_service(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

    driver.get(url)

    score_elements = driver.find_elements_by_id('score')
    if not score_elements:
        driver.quit()
        return False

    score_element = score_elements[0]
    score_text = score_element.text.strip()

    if not score_text.isdigit():
        driver.quit()
        return False

    score = int(score_text)
    is_valid_score = 1 <= score <= 1000

    driver.quit()

    return is_valid_score

def main_function():
    url = "http://127.0.0.1:5000"

    result = test_scores_service(url)

    if result:
        print("Test passed.")
        sys.exit(0)
    else:
        print("Test failed.")
        sys.exit(-1)

if __name__ == "__main__":
    main_function()
