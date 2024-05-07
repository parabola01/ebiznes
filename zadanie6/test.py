import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class ProgramizTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_home_page(self):
        driver = self.driver
        driver.get("https://pythonforthelab.com/")
        self.assertIn("Python for scientific instrument control | Python For The Lab", self.driver.title)
        driver.quit()

    def test_blog_page(self):
        driver = self.driver
        driver.get("https://pythonforthelab.com/blog/")
        self.assertIn("Python for experimental scientists | Python For The Lab", self.driver.title)
        driver.quit()

    def test_footer_presence(self):
        driver = self.driver
        driver.get("https://pythonforthelab.com/")
        footer = self.driver.find_element(By.TAG_NAME, 'footer')
        self.assertTrue(footer.is_displayed())
        driver.quit()

    def test_footer_links(self):
        footer_links = self.driver.find_elements(By.CSS_SELECTOR, 'footer a')
        for link in footer_links:
            url = link.get_attribute('href')
            self.driver.get(url)
            self.assertNotIn("404", self.driver.title)
            self.assertNotIn("Error", self.driver.title)
            self.driver.get("https://pythonforthelab.com/")

    def test_hire_me_button(self):
        self.driver.get("https://pythonforthelab.com/")
        hire_me_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Hire Me"))
        )
        hire_me_button.click()
        new_url = self.driver.current_url
        self.assertEqual(new_url, "https://pythonforthelab.com/hire-me/")

    def test_forum_button(self):
        self.driver.get("https://pythonforthelab.com/")
        forum_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Forum"))
        )
        forum_button.click()
        new_url = self.driver.current_url
        self.assertEqual(new_url, "https://github.com/PFTL/pftl_discussions/discussions")

    def test_courses_button(self):
        self.driver.get("https://pythonforthelab.com/")
        courses_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Courses"))
        )
        courses_button.click()
        new_url = self.driver.current_url
        self.assertEqual(new_url, "https://pythonforthelab.com/courses/")

    def test_books_button(self):
        self.driver.get("https://pythonforthelab.com/")
        books_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Books"))
        )
        books_button.click()
        new_url = self.driver.current_url
        self.assertEqual(new_url, "https://pythonforthelab.com/books/")

    def test_about_button(self):
        self.driver.get("https://pythonforthelab.com/")
        about_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "About"))
        )
        about_button.click()
        new_url = self.driver.current_url
        self.assertEqual(new_url, "https://pythonforthelab.com/about/")

    def test_all_the_articles_button(self):
        self.driver.get("https://pythonforthelab.com/")
        all_the_articles_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "All the articles"))
        )
        all_the_articles_button.click()
        new_url = self.driver.current_url
        self.assertEqual(new_url, "https://pythonforthelab.com/blog/")

    def test_responsiveness(self):
        self.driver.get("https://pythonforthelab.com/")
        self.driver.set_window_size(350, 450)
        navigation = self.driver.find_element(By.ID, 'menu-button')
        self.assertTrue(navigation.is_displayed())

    def test_navigation(self):
        self.driver.get("https://pythonforthelab.com/")
        about_us_link = self.driver.find_element(By.LINK_TEXT, 'About Us')
        about_us_link.click()
        self.assertIn("About Aquiles Carattino from Python for the Lab | Python For The Lab", self.driver.title)

    def test_newsletter_presence(self):
        driver = self.driver
        self.driver.get("https://pythonforthelab.com/")
        newsletter_input = driver.find_element(By.NAME, "EMAIL")
        self.assertTrue(newsletter_input.is_displayed())
        driver.quit()

    def test_newsletter_button_presence(self):
        driver = self.driver
        self.driver.get("https://pythonforthelab.com/")
        subscribe_button = driver.find_element(By.ID, "mc-embedded-subscribe")
        self.assertTrue(subscribe_button.is_displayed())

    def test_pagination_links(self):
        self.driver.get("https://pythonforthelab.com/blog/")
        pages = self.driver.find_elements(By.XPATH, "//nav[@aria-label='Pagination']/a[@aria-current='page']")

        self.assertGreaterEqual(len(pages), 5)
        expected_urls = [
            "https://pythonforthelab.com/blog/",
            "https://pythonforthelab.com/blog/index2",
            "https://pythonforthelab.com/blog/index3",
            "https://pythonforthelab.com/blog/index4",
            "https://pythonforthelab.com/blog/index5"
        ]
        actual_urls = [page.get_attribute('href') for page in pages]

        self.assertEqual(expected_urls, actual_urls, "The URLs of the pagination links are not correct.")

    def test_invalid_email_submission(self):
        self.driver.get(
            "https://us21.list-manage.com/contact-form?u=f0d9bfa6188cdcc67890a07f6&form_id=23280542e88944b2a32bed276c724d1e")

        email_input = self.driver.find_element(By.NAME, "fields.1425")
        subject_input = self.driver.find_element(By.NAME, "fields.1426")
        message_input = self.driver.find_element(By.NAME, "fields.1427")
        subscribe_checkbox = self.driver.find_element(By.NAME, "subscribe")
        submit_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")

        email_input.send_keys("johnexample.com")
        subject_input.send_keys("Test subject")
        message_input.send_keys("Test message")
        subscribe_checkbox.click()
        submit_button.click()

        error_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@role='alert']/div/strong")))
        self.assertIn("There were some errors with your submission.", error_message.text)

    def test_invalid_subscription(self):
        self.driver.get("https://pythonforthelab.us21.list-manage.com/subscribe/post?u=f0d9bfa6188cdcc67890a07f6&id=8a0ca536e8&f_id=00dfebe6f0")

        email_input = self.driver.find_element(By.ID, "MERGE0")
        submit_button = self.driver.find_element(By.NAME, "submit")

        email_input.send_keys("johnexample.com")
        submit_button.click()

        error_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".feedback.error")))
        self.assertIn("Please enter a value", error_message.text)

    def test_subscription_redirect(self):
        self.driver.get("https://pythonforthelab.com")

        subscribe_button = self.driver.find_element(By.ID, "mc-embedded-subscribe")
        subscribe_button.click()

        WebDriverWait(self.driver, 10).until(EC.url_to_be(
            "https://pythonforthelab.us21.list-manage.com/subscribe/post?u=f0d9bfa6188cdcc67890a07f6&id=8a0ca536e8&f_id=00dfebe6f0"))
        current_url = self.driver.current_url
        expected_url = "https://pythonforthelab.us21.list-manage.com/subscribe/post?u=f0d9bfa6188cdcc67890a07f6&id=8a0ca536e8&f_id=00dfebe6f0"
        self.assertEqual(current_url, expected_url)

    def test_course_cards(self):
        self.driver.get("https://pythonforthelab.com/courses/")
        course_cards = self.driver.find_elements(By.XPATH, "//*[starts-with(@class, 'bg-gradient-to-br')]")
        self.assertGreater(len(course_cards), 0)

    def test_contact_button_redirect(self):
        self.driver.get("https://pythonforthelab.com/courses/")
        contact_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(@href, 'contact-form')]"))
        )
        contact_button.click()
        new_url = self.driver.current_url
        self.assertNotEqual(new_url, "https://pythonforthelab.com/courses/")


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
