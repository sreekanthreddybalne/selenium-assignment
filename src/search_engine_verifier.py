from enum import Enum
from urllib.parse import urlparse

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class SearchEngine(Enum):
    class EngineInfo:
        def __init__(
            self,
            label: str,
            link: str,
            search_input_selector: str,
            first_result_selector: str,
        ):
            self.label = label
            self.link = link
            self.search_input_selector = search_input_selector
            self.first_result_selector = first_result_selector

    google = EngineInfo("Google", "https://www.google.com", "q", "div.g:nth-child(1) a")
    yahoo = EngineInfo("Yahoo", "https://www.yahoo.com", "p", "#web div.compTitle a")
    bing = EngineInfo("Bing", "https://www.bing.com", "q", "#b_results h2 a")


class UnableToFindSearchInputException(Exception):
    """
    Raised when we fail to find the search input element on the search engine's home page.
    """

    def __init__(self, engine: SearchEngine):
        self.message = f"{engine.value.label} - We couldn't find the search input using selector `{engine.value.search_input_selector}`"


class UnableToFindFirstResultException(Exception):
    """
    Raised when we fail to find the first result on the search engine's result page.
    """

    def __init__(self, engine: SearchEngine):
        self.message = f"{engine.value.label} - We couldn't find the first result using selector `{engine.value.first_result_selector}`"


class SearchEngineVerifier:
    """
    Responsible for verifying that a search engine is working as expected.

    Example usage:
    ```
        verifier = SearchEngineVerifier(driver, SearchEngine.yahoo)
        verifier.search_and_open_first_result("amazon.in")
    ```
    """

    def __init__(self, driver: WebDriver, engine: SearchEngine = SearchEngine.google):
        """
        Initializes a SearchEngineVerifier instance.

        Parameters:
        - driver: An instance of the Selenium WebDriver.
        - engine: A SearchEngine Enum instance (default is SearchEngine.google).
        """
        # Open search engine page
        driver.get(engine.value.link)
        self.driver = driver
        self.engine = engine

    def search_and_open_first_result(self, query: str):
        """
        Performs a search using the specified query, opens the first result, and verifies the domain.

        Parameters:
        - query: The search query to be performed.
        """
        try:
            search_box = self.driver.find_element(
                "name", self.engine.value.search_input_selector
            )
        except NoSuchElementException:
            raise UnableToFindSearchInputException(self.engine)

        # Input the search query
        search_box.send_keys(query)

        # Submit the search form
        search_box.submit()

        # Wait for a while to see the results
        self.driver.implicitly_wait(8)

        # Find the first search result link and click it
        try:
            first_result = self.driver.find_element(
                By.CSS_SELECTOR, self.engine.value.first_result_selector
            )
        except NoSuchElementException:
            raise UnableToFindFirstResultException(self.engine)
        first_result.click()

        # Wait for a while to observe the clicked result
        self.driver.implicitly_wait(5)

        # Some search engines open the result in new tab.
        # Switch to the last tab (assuming it's the newly opened one)
        self.driver.switch_to.window(self.driver.window_handles[-1])

        # Parse the current URL and extract the domain name
        current_url = self.driver.current_url
        parsed_url = urlparse(current_url)
        domain = ".".join(parsed_url.netloc.split(".")[-2:])

        return domain
