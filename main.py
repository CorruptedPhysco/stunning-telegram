from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def scrape_specific_link():
    # Set up Selenium WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run in headless mode
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # Open the target URL
    url = "https://bingotingo.com/best-social-media-platforms/"
    driver.get(url)

    # Locate the specific <a> tag using attributes
    try:
        link_element = driver.find_element(By.CSS_SELECTOR, "a#tool")  # Target by ID
        link_href = link_element.get_attribute("href")
    except Exception as e:
        link_href = None
        print(f"Error: {e}")

    driver.quit()
    return link_href

if __name__ == "__main__":
    scraped_link = scrape_specific_link()
    print(f"Scraped Link: {scraped_link}")
  
