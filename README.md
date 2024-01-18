
# Search Engine Verifier with Python and Selenium
The `SearchEngineVerifier` verifies if a search engine is able to return the requested results effectively on the top of their result list.

Configured Search Engines:
- Google
- Yahoo
- Bing

#### Adding a new Search Engine
To add a new search engine, follow these steps:

1. Fetch the following information related to the engine:
   - label: The search engine's label
   - link: The search engine's web page address.
   - search_input_selector: The CSS selector of the search engine's input element on its web page.
   - first_result_selector: The CSS selector for selecting the first result returned by the search engine on its result page.

2. Add the information to the `src/search_engine_verifier.py` file:
    ```python
    class SearchEngine(Enum):
        ...
        bing = EngineInfo("Bing", "https://www.bing.com", "q", "#b_results h2 a")
    ```

3. Add a test case at `tests/test_search_engine_verifier.py`
4. Note that the tests under `tests/test_search_engine_verifier.py` are integration tests. A Search Engine may change its page information in the future, and you should adjust the `search_input_selector` and `first_result_selector` accordingly.


#### Running Tests: 
Make sure you have Python > 3.8 installed on your machine.

1. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```
2. Run the tests:
    ```sh
    python -m unittest 
    ```

#### Using a Virtual Environment
It is recommended to use a virtual environment to manage dependencies and isolate your project's environment from the system-wide Python installation.

1. Create a virtual environment (you can replace venv with your preferred name):
    ```sh
    python -m venv venv
    ```

2. Activate the virtual environment:
    - On Windows:
        ```sh
        .\venv\Scripts\activate
        ```
    - On Unix or MacOS:

        ```sh
        source venv/bin/activate
        ```
3. Install the required dependencies inside the virtual environment:
   ```sh
   pip install -r requirements.txt
   ```
4. Run the tests:

    ```sh
    python -m unittest 
    ```
5. Deactivate the virtual environment when you're done:
    ```sh
    deactivate
    ```