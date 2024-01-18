import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from src.search_engine_verifier import SearchEngine, SearchEngineVerifier


class TestSearchEngineVerifier(unittest.TestCase):
    def setUp(self):
        options = Options()
        # options.add_argument("--headless") # Runs Chrome in headless mode.
        options.add_argument("--no-sandbox")  # # Bypass OS security model
        options.add_argument("disable-infobars")
        options.add_argument("--disable-extensions")
        options.add_argument("--start-fullscreen")
        options.add_argument("--disable-gpu")

        # Create a new instance of the browser for each test
        self.driver = webdriver.Firefox()

    def tearDown(self):
        # Close the browser window after each test
        self.driver.quit()

    # def test_google_search_and_open_first_result(self):
    #     verifier = SearchEngineVerifier(self.driver, SearchEngine.google)
    #     query = "amazon.in"
    #     result = verifier.search_and_open_first_result(query)
    #     self.assertEqual(result, query)

    def test_yahoo_search_and_open_first_result(self):
        verifier = SearchEngineVerifier(self.driver, SearchEngine.yahoo)
        query = "amazon.in"
        result = verifier.search_and_open_first_result(query)
        self.assertEqual(result, query)

    # def test_bing_search_and_open_first_result(self):
    #     verifier = SearchEngineVerifier(self.driver, SearchEngine.bing)
    #     query = "amazon.in"
    #     result = verifier.search_and_open_first_result(query)
    #     self.assertEqual(result, query)


if __name__ == "__main__":
    unittest.main()
