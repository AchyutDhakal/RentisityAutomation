from pages.add_property import AddProperty
import pytest
import allure
from utils.test_runner import create_driver
from data.property_data import PROPERTY_DATA
from pages.login_page import LoginPage
from config import LANDLORD_EMAIL, LANDLORD_PASSWORD, ADMIN_EMAIL, ADMIN_PASSWORD
from utils.assertions import assert_equal
import time
from selenium.webdriver.support import expected_conditions as EC

class TestAddProperty:
  def setup_method(self):
    self.driver = create_driver()
    self.driver.get("https://app-staging.rentisity.com/")
    self.add_property = AddProperty(self.driver)
    self.login_page = LoginPage(self.driver)

  def teardown_method(self):
    self.driver.quit()

  @allure.title("Testing the single tenant flow")
  @pytest.mark.parametrize("property_data", PROPERTY_DATA)
  def test_add_property(self, property_data):
    with allure.step("Logging in to the landlord account"):
      self.login_page.login(LANDLORD_EMAIL, LANDLORD_PASSWORD)

    with allure.step("Adding a single tenant property"):
      self.add_property.navigate_to_add_property()
      self.add_property.enter_property_details(property_data["address"], property_data["title"], property_data["area"], property_data["rent_per_month"], property_data["file_path"])

    with allure.step("Reviewing the property from the admin panel"):
      self.add_property.review_property(ADMIN_EMAIL, ADMIN_PASSWORD, self.driver)

    with allure.step("Logging in to the landlord's account"):
      self.driver.get("https://app-staging.rentisity.com/")

    with allure.step("Searching for the property"):
      self.add_property.click_element(self.add_property.PROPERTY_BUTTON)
      self.add_property.enter_text(self.add_property.SEARCH_PROPERTY_LANDLORD, property_data['title'])

    with allure.step("Asserting the status of the property"):
      self.add_property.wait.until(EC.visibility_of_element_located(self.add_property.PROPERTIES_COUNT_1))
      property_status = self.add_property.get_element_text(self.add_property.PROPERTY_STATUS)
      assert_equal(property_status, "Active", "The status of the property is not active", "single_tenant", self.add_property)


