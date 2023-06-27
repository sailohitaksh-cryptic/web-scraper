# Web Crawler - Email Scraper

This is a Python script that scrapes email addresses from a given website. It uses a web crawler to explore the website and extract email addresses found in its pages. The script is built using the following libraries:

- re: Used for regular expression matching to find email addresses.
- pandas: Used for creating a dataframe to store the scraped email addresses.
- requests: Used for making HTTP requests to retrieve web pages.
- BeautifulSoup: Used for parsing HTML and XML documents.
- urllib.parse: Used for joining URLs and constructing absolute URLs.
- streamlit: Used for creating a simple web interface.
- requests_html: Used for rendering JavaScript content on web pages.
- tqdm: Used for displaying a progress bar during the scraping process.

## Usage

To use the web crawler and scrape email addresses from a website, follow these steps:

1. Install the required libraries by running `pip install -r requirements.txt`.
2. Run the script by executing `streamlit run crawler.py` in your command-line interface.
3. Access the web interface by opening the displayed URL in your web browser.
4. Enter the website URL in the provided input field.
5. Specify the number of email addresses you want to scrape.
6. Click the "Scrape Emails" button to start the scraping process.
7. The scraped email addresses will be displayed in a table on the web page.
8. You can download the scraped email addresses as a CSV file by clicking the "Download CSV" button.

Please note that this script assumes the website has a sitemap.xml file that contains URLs to all the pages you want to scrape. It retrieves the sitemap.xml file and extracts the URLs from it to crawl the website. Make sure the website you want to scrape has a valid sitemap.xml file.

## Limitations

- The script relies on the assumption that the website has a sitemap.xml file. If the website does not have a sitemap.xml file, the script may not work properly.
- The email scraping process relies on regular expressions and may not capture all possible email formats. The provided regular expression pattern is a commonly used one but might not cover all variations.
- The script may take some time to scrape the specified number of email addresses, depending on the size of the website and the number of pages to crawl.

## Disclaimer

Please ensure that you have the necessary permissions and comply with applicable laws and regulations before scraping any website. Respect the website's terms of service and privacy policy. Scraping websites without permission may violate their terms of service or legal restrictions. Use this script responsibly and at your own risk.

---

Feel free to modify and enhance the code according to your specific requirements.
