from utils.test_runner import create_driver
from pages.login_page import LoginPage
import pytest
import allure
from config import LANDLORD_EMAIL, LANDLORD_PASSWORD
from utils.assertions import assert_equal

class TestLogin:
  def setup_method(self):
    self.driver = create_driver()
    self.driver.get("https://app-staging.rentisity.com/")
    self.login_page = LoginPage(self.driver)


  def teardown_method(self):
    self.driver.quit()


  @allure.title("Testing the valid login using landlord credentials")
  def test_single_tenant(self):
    with allure.step("Logging in to the application"):
      self.login_page.login(LANDLORD_EMAIL, LANDLORD_PASSWORD)

    with allure.step("Assertion"):
      self.login_page.is_element_visible(self.login_page.PROFILE_EMAIL)
      profile_email = self.login_page.get_element_text(self.login_page.PROFILE_EMAIL)
      assert_equal(profile_email, LANDLORD_EMAIL, "The email in the profile is not matching", "login_test", self.login_page)
