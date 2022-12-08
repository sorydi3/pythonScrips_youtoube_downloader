
from requests_html import AsyncHTMLSession
from selenium import webdriver
import traceback
import pandas as pd
import asyncio

# Specify the URL of the website you want to scrape
url = "www.google.com"

print("scrip is running!!!!")

# Set up a cache to store the results of previous requests

# Use Selenium to automate a headless web browser
options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)


async def scrape_website(url):
    try:
        # Check the cache to see if we have already visited this URL

        # Use Selenium to visit the website
        driver.get(url)

        # Wait for the page to load, then retrieve the HTML
        html = driver.page_source

        # Use requests-html to parse the HTML
        session = AsyncHTMLSession()
        re = await session.get(url)
        re.html.render()

        # Extract the data you want from the HTML using a combination of CSS class and tag names
        regex = r"/^[a-zA-Z]+$/"
        data = re.html.search(regex)

        # Use regular expressions to extract specific patterns of text from the HTML
        pattern = re.compile(regex)
        extracted_data = [pattern.search(
            str(datum)).group(0) for datum in data]

        # Use pandas to organize and manipulate the data
        df = pd.DataFrame({"Extracted Data": extracted_data})
        df.to_csv("extracted_data.csv", index=False)

        # Print the data
        print(df)

        # Add the result to the cache

    except Exception as e:
        print(f"An error occurred: {e}")
        traceback.print_exc()
    finally:
        driver.close()

# Scrape the website asynchronously
asyncio.run_until_complete(scrape_website(url))

print("hellow world!!!")
