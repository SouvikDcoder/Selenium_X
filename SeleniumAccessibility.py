from selenium import webdriver
from axe_selenium_python import Axe


def test_accessibility(url):
    # Initialize the webdriver (replace 'path/to/chromedriver' with the actual path to your chromedriver)
    driver = webdriver.Chrome('path/to/chromedriver')
    driver.get(url)

    # Initialize Axe for the webdriver
    axe = Axe(driver)
    axe.inject()  # Injects the Axe library into the webpage

    # Run accessibility tests
    results = axe.run()

    # Write results to a JSON file
    axe.write_results(results, 'accessibility_report.json')

    # Close the webdriver
    driver.quit()

    # Raise an exception if there are accessibility violations
    assert len(results['violations']) == 0, f"Accessibility violations found: {results['violations']}"


if __name__ == "__main__":
    test_accessibility('https://www.example.com')


'''
pip install selenium
pip install axe-selenium-python

'''