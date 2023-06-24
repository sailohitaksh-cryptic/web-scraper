import re
import pandas as pd
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import streamlit as st
from requests_html import HTMLSession
from tqdm import tqdm

st.title("Email Scraper")
st.write("Enter the website URL and specify the number of email addresses to scrape.")

url = st.text_input("Website URL")
num_emails = st.number_input("Number of Emails", min_value=1, step=1, value=10)
submit = st.button("Scrape Emails")

EMAIL_REGEX = r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""

def get_sitemap_url(base_url):
    if base_url.endswith('/'):
        base_url = base_url[:-1]
    return urljoin(base_url, 'sitemap.xml')

def get_urls_of_xml(xml_url):
    r = requests.get(xml_url)
    xml = r.text
    soup = BeautifulSoup(xml, 'html.parser')

    links_arr = []
    for link in soup.findAll('loc'):
        linkstr = link.getText('', True)
        links_arr.append(linkstr)

    return links_arr

def scrape_emails(url, max_emails):
    session = HTMLSession()
    email = set()
    sitemap_url = get_sitemap_url(url)
    links_data_arr = get_urls_of_xml(sitemap_url)

    for i in tqdm(links_data_arr):
        r = session.get(i)
        for re_match in re.finditer(EMAIL_REGEX, r.html.raw_html.decode()):
            email.add(((re_match.group())).replace("-", ""))
        if len(email) >= max_emails:
            break

    return email

if submit:
    if url:
        st.write("Scraping emails...")
        emails = scrape_emails(url, num_emails)
        df = pd.DataFrame(emails, columns=["Email"])
        st.write(df)
        csv = df.to_csv(index=False)
        st.download_button(
            label="Download CSV",
            data=csv,
            file_name="Emails.csv",
            mime="text/csv"
        )
    else:
        st.warning("Please enter a valid website URL.")
