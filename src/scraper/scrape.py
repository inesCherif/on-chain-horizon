from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
from bs4 import BeautifulSoup
from config.settings import SBR_WEBDRIVER

class WebScraper:
    @staticmethod
    def scrape_website(website):
        print("Connecting to Scraping Browser...")
        sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, "goog", "chrome")
        with Remote(sbr_connection, options=ChromeOptions()) as driver:
            driver.get(website)
            print("Waiting for captcha to solve...")
            solve_res = driver.execute(
                "executeCdpCommand",
                {
                    "cmd": "Captcha.waitForSolve",
                    "params": {"detectTimeout": 10000},
                },
            )
            print("Captcha solve status:", solve_res["value"]["status"])
            print("Navigated! Scraping page content...")
            return driver.page_source

    @staticmethod
    def extract_body_content(html_content):
        soup = BeautifulSoup(html_content, "html.parser")
        body_content = soup.body
        return str(body_content) if body_content else ""

    @staticmethod
    def clean_body_content(body_content):
        soup = BeautifulSoup(body_content, "html.parser")
        for script_or_style in soup(["script", "style"]):
            script_or_style.extract()
        cleaned_content = soup.get_text(separator="\n")
        return "\n".join(
            line.strip() for line in cleaned_content.splitlines() if line.strip()
        )