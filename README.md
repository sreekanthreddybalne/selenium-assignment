
# Selenium Page Object Model with Python 

`BasePage` class include basic functionality and driver initialization


`MainPage` is derived from the `BasePage class, it contains methods related to this page, which will be used to create test steps.

`Note`
When you want to write tests, you should derive your test class from `BaseTest` which holds basic functionality for your tests. Then you can call  page and related methods in accordance with the steps in the test cases

#### If you want to run all tests, you should type: 
```sh
python -m unittest 
```
#### If you want to run just a class, you should type: 
```sh
python -m unittest tests.test_sign_in_page.TestSignInPage
```
#### If you want to run just a test method, you should type: 
```sh
python -m unittest tests.test_sign_in_page.TestSignInPage.test_page_load
```