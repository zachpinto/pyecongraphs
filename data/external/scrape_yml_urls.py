from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Initialize the Selenium web driver (you'll need to have the appropriate driver, e.g., chromedriver.exe, in the PATH)
driver = webdriver.Chrome(ChromeDriverManager().install())

# List to store .yml URLs
yml_urls = []

topics = ["math", "market_power", "growth", "game", "fluctuations", "firm",
          "finance", "exchange", "consumer", "competition", "scarcity"]

for topic in topics:
    # Step 1: Open the main topic page
    driver.get(f"https://www.econgraphs.org/topics/{topic}/")

    # Step 2: Identify and open all graph links
    graph_links = driver.find_elements(By.CSS_SELECTOR, f"a[href*='/graphs/{topic}/']")  # Adjusted the CSS selector
    for link in graph_links:
        graph_url = link.get_attribute("href")

        # Step 3: Modify the graph URL to retrieve the corresponding .yml file
        yml_url = graph_url.replace("/graphs/", "/topics/") + ".yml"
        yml_urls.append(yml_url)

# Closing the browser
driver.close()

# Saving the yml URLs to a file
with open("yml_links.txt", 'w') as f:
    for url in yml_urls:
        f.write(f"{url}\n")

print("All .yml URLs have been saved to yml_links.txt!")
