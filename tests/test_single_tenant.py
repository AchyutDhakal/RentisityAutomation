from utils.test_runner import create_driver
from pages.single_tenant import SingleTenant
from pages.add_property import AddProperty
from pages.login_page import LoginPage
from config import LANDLORD_EMAIL, LANDLORD_PASSWORD, ADMIN_EMAIL, ADMIN_PASSWORD, TENANT_EMAIL
import allure
import pytest
from data.single_tenant_data import SINGLE_TENANT_DATA
import time
from utils.assertions import assert_true
from selenium.webdriver.support import expected_conditions as EC

class TestSingleTenant:
  def setup_method(self):
    self.driver = create_driver()
    self.driver.get("https://app-staging.rentisity.com/")
    self.single_tenant = SingleTenant(self.driver)
    self.add_property = AddProperty(self.driver)
    self.login_page = LoginPage(self.driver)

  def teardown_method(self):
    self.driver.quit()


  @allure.title("Testing the Single Tenant Flow")
  @pytest.mark.parametrize("tenant_data", SINGLE_TENANT_DATA)
  def test_single_tenant(self, tenant_data):
    with allure.step("Login as a landlord"):
      self.login_page.login(LANDLORD_EMAIL, LANDLORD_PASSWORD)

    with allure.step("Adding property"):
      self.add_property.navigate_to_add_property()
      self.add_property.enter_property_details(tenant_data["address"], tenant_data["title"], tenant_data["area"], tenant_data["rent_per_month"], tenant_data["file_path"], tenant_data["property_type"] , tenant_data["group_creator"], tenant_data["payment_responsibility"], tenant_data["contract"])

    with allure.step("Reviewing the property from the admin panel"):
      self.add_property.review_property(ADMIN_EMAIL, ADMIN_PASSWORD, self.driver)

    with allure.step("Logging in to the landlord's account"):
      self.driver.get("https://app-staging.rentisity.com/")

    with allure.step("logout from the landlord"):
      self.single_tenant.logout()

    with allure.step("Login as a tenant"):
      self.login_page.login(TENANT_EMAIL, LANDLORD_PASSWORD)

    with allure.step("Applying for the property"):
      self.single_tenant.apply_for_property(tenant_data["title"])

    with allure.step("Logut from tenant"):
      self.single_tenant.logout()

    with allure.step("Login as a landlord"):
      self.login_page.login(LANDLORD_EMAIL, LANDLORD_PASSWORD)

    with allure.step("Accepting the application"):
      self.single_tenant.accept_application(tenant_data["title"], tenant_data["group_creator"])

    with allure.step("Generating the contract"):
      self.single_tenant.generate_contract(tenant_data["landlord_address"], tenant_data["bank_name"], tenant_data["account_name"], tenant_data["iban"], tenant_data["bic"], tenant_data["electricity"], tenant_data["gas_oil"], tenant_data["internet"], tenant_data["waste"], tenant_data["payment"], tenant_data["contract_type"], tenant_data["contract_file_path"])

    with allure.step("Logout from landlord"):
      self.single_tenant.logout()

    with allure.step("Login as a tenant"):
      self.login_page.login(TENANT_EMAIL, LANDLORD_PASSWORD)


    if tenant_data["contract_type"] == "system":
      with allure.step("Signing the contract from tenant account"):
        self.single_tenant.signature("tenant")

      with allure.step("Logout from tenant"):
        self.single_tenant.logout()

      with allure.step("Login as a Landlord"):
        self.login_page.login(LANDLORD_EMAIL, LANDLORD_PASSWORD)

      with allure.step("Signing the contract from landlord account"):
        self.single_tenant.signature("landlord")

      with allure.step("logout from landlord"):
        self.single_tenant.logout()

      with allure.step("Login as tenant"):
        self.login_page.login(TENANT_EMAIL, LANDLORD_PASSWORD)
        time.sleep(1)
        self.login_page.click_element(self.login_page.SIGN_IN_BUTTON)

    if tenant_data["payment"]=="external":
      self.single_tenant.tenant_confirm_external_payment()

    else:
      with allure.step("paying security deposit"):
        self.single_tenant.security_deposit_payment(tenant_data["security_code"])

      with allure.step("paying the rent"):
        self.single_tenant.rent_payment(tenant_data["security_code"])

    with allure.step("Logout from tenant"):
      self.single_tenant.logout()

    with allure.step("Login as landlord"):
      self.login_page.login_with_retry(LANDLORD_EMAIL, LANDLORD_PASSWORD)

    if tenant_data["payment"] == "external":
      self.single_tenant.review_external_payment_and_handover()
    else:
      with allure.step("Handing over the proeprty"):
        self.single_tenant.handover_property()

    with allure.step("Assertion agains the contract status"):
      assert_true(self.single_tenant.is_element_visible(self.single_tenant.UNDER_CONTRACT_STATUS), "The status of the contract is not under contract", f"{tenant_data['title']}", self.single_tenant)


