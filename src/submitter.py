from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random


def submit_fake_credentials(url, credentials):
    options = webdriver.FirefoxOptions()
    options.add_argument(
        "--headless"
    )  # Enable headless mode (comment out for debugging)

    # Specify the path to geckodriver if it's not in your PATH
    driver = webdriver.Firefox(options=options)
    # For debugging purpose, let the driver wait for the elements to load
    driver.implicitly_wait(10)

    for email, password in credentials:
        driver.get(url)
        try:
            print(f"Visiting {url}")
            # Check if the element is inside an iframe
            iframes = driver.find_elements(By.TAG_NAME, "iframe")
            for iframe in iframes:
                driver.switch_to.frame(iframe)
                try:
                    account_name_field = WebDriverWait(driver, 5).until(
                        EC.visibility_of_element_located(
                            (By.ID, "account_name_text_field")
                        )
                    )
                    if account_name_field:
                        break
                except:
                    driver.switch_to.default_content()  # If not found, switch back to the main content

            if not account_name_field:
                # If the element is not inside any iframe, look for it in the main content
                driver.switch_to.default_content()
                account_name_field = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.ID, "account_name_text_field"))
                )

            print("Element 'account_name_text_field' found")
            account_name_field.send_keys(email)
            print(f"Email {email} entered")
            time.sleep(5)
            account_name_field.send_keys(Keys.ENTER)

            # Wait for the password field to become visible
            password_field = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.ID, "password_text_field"))
            )
            print("Password field found")
            password_field.send_keys(password)
            print(f"Password {password} entered")
            time.sleep(5)
            password_field.send_keys(Keys.ENTER)

            # Wait for the error message to appear
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.ID, "errMsg"))
            )
            print("Error message appeared, moving to the next set of credentials")

            # Introduce a random delay between submissions
            delay = random.uniform(1, 5)  # Random delay between 1 and 5 seconds
            print(f"Waiting for {delay:.2f} seconds before the next submission")
            time.sleep(delay)

        except Exception as e:
            print(f"An error occurred: {e}")
            continue

    driver.quit()
