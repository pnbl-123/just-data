# import requests
# from bs4 import BeautifulSoup

# def crawl_site(url, depth):
#     if depth == 0:
#         return

#     try:
#         response = requests.get(url)
#         if response.status_code == 200:
#             soup = BeautifulSoup(response.text, 'html.parser')

#             # Extract and print the links
#             for link in soup.find_all('a'):
#                 print(link)

#                 href = link.get('href')

#                 if href and href.startswith('https'):

#                     # Recursively crawl the discovered link with reduced depth
#                     crawl_site(href, depth - 1)
#         else:
#             print(f"Failed to retrieve {url}: Status code {response.status_code}")
#     except Exception as e:
#         print(f"Error crawling {url}: {e}")

# if __name__ == "__main__":
#     starting_url = 'https://help.salesforce.com/s/articleView?id=cc.b2c_getting_started.htm&type=5'  # Replace with the starting URL of the site you want to crawl
#     max_depth = 3  # Specify the maximum depth to crawl

#     crawl_site(starting_url, max_depth)


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def crawl_site_with_selenium(url, depth):
    """
    Crawl a website using Selenium, waiting for content to load.

    Args:
        url (str): The starting URL to crawl.
        depth (int): The maximum depth to crawl.

    Returns:
        None

    This function uses Selenium to crawl a website starting from the provided URL.
    It waits for the page to load completely and extracts links, recursively crawling
    discovered links with reduced depth.
    """
    if depth == 0:
        return

    try:
        # Use the system's Chrome installation
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(options=chrome_options)

        driver.get(url)
        
        # Wait for the page to load completely (you can adjust the timeout)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        # Extract and print the links
        links = driver.find_elements(By.TAG_NAME, 'a')
        for link in links:
            href = link.get_attribute('href')
            if href and href.startswith('http'):
                print(href)

                # Recursively crawl the discovered link with reduced depth
                crawl_site_with_selenium(href, depth - 1)
    except Exception as e:
        print(f"Error crawling {url}: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    starting_url = 'https://trailhead.salesforce.com/help?article=Salesforce-Certified-B2C-Commerce-Architect-Exam-Guide'
    max_depth = 2  # Adjust the maximum depth as needed

    crawl_site_with_selenium(starting_url, max_depth)
