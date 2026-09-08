from utils.test_runner import create_driver
from pages.add_property import AddProperty
from pages.single_tenant import SingleTenant
from pages.login_page import LoginPage
from pages.multiple_tenants import MultipleTenant
import allure
import pytest
from data.multiple_tenant_data import MULTIPLE_TENANT_DATA
from config import LANDLORD_EMAIL, LANDLORD_PASSWORD, ADMIN_EMAIL, ADMIN_PASSWORD, TENANT_EMAIL, COTENANT_EMAIL
import time
from utils.assertions import assert_true


class TestMultipleTenant:
  def setup_method(self):
    self.driver = create_driver()
    self.driver.get("https://app-staging.rentisity.com/")
    self.single_tenant = SingleTenant(self.driver)
    self.add_property = AddProperty(self.driver)
    self.login_page = LoginPage(self.driver)
    self.multiple_tenant = MultipleTenant(self.driver)

  def teardown_method(self):
    self.driver.quit()

  @allure.title("Testing the multiple tenants flow")
  @pytest.mark.parametrize("tenant_data", MULTIPLE_TENANT_DATA)
  def test_multiple_tenants(self, tenant_data):
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
          self.multiple_tenant.apply_for_property(tenant_data["title"], COTENANT_EMAIL)

    with allure.step("Logut from tenant"):
      self.single_tenant.logout()

    with allure.step("Loggin in to the co-tenant's account to accept the invitation"):
      self.login_page.login(COTENANT_EMAIL, LANDLORD_PASSWORD)

    with allure.step("Accepting the invitation from co-tenant's account"):
      self.multiple_tenant.accept_cotenant_invitation()

    with allure.step("Logout from co-tenant account after accepting the invitation"):
      self.single_tenant.logout()

    with allure.step("Login as a landlord"):
      self.login_page.login(LANDLORD_EMAIL, LANDLORD_PASSWORD)

    with allure.step("Accepting the application"):
      if tenant_data["group_creator"] == "landlord":
        self.single_tenant.accept_application(tenant_data["title"], tenant_data["group_creator"])

      else:
        self.multiple_tenant.accept_application(tenant_data["title"])

    with allure.step("Generating the contract"):
      if tenant_data["group_creator"] == "landlord":
        self.multiple_tenant.landlord_group_generate_contract(tenant_data["monthly_rent"], tenant_data["security_deposit"], tenant_data["landlord_address"], tenant_data["bank_name"], tenant_data["account_name"], tenant_data["iban"], tenant_data["bic"], tenant_data["electricity"], tenant_data["gas_oil"], tenant_data["internet"], tenant_data["waste"])

      else:
        self.single_tenant.generate_contract(tenant_data["landlord_address"], tenant_data["bank_name"], tenant_data["account_name"], tenant_data["iban"], tenant_data["bic"], tenant_data["electricity"], tenant_data["gas_oil"], tenant_data["internet"], tenant_data["waste"], tenant_data["payment"], tenant_data["contract_type"], tenant_data["contract_file_path"])

    with allure.step("Logout from landlord"):
      self.single_tenant.logout()

    with allure.step("Login as lead tenant to assign rooms and sign the contract"):
      self.login_page.login(TENANT_EMAIL, LANDLORD_PASSWORD)

    if tenant_data["group_creator"] == "landlord":
      with allure.step("Signing the contract from lead tenant's account"):
        self.single_tenant.signature("tenant")

    else:
      with allure.step("Assigning the rooms"):
        self.multiple_tenant.assign_rooms()

    with allure.step("Logout from lead tenant account after signing the contract"):
      self.single_tenant.logout()

    if tenant_data["contract"] != "lead_tenant":
      with allure.step("Login to co-tenant's account to sign the contract"):
        self.login_page.login(COTENANT_EMAIL, LANDLORD_PASSWORD)
        time.sleep(1)
        self.login_page.click_element(self.login_page.SIGN_IN_BUTTON)

      with allure.step("Signing the contract from co-tenant's account"):
        self.single_tenant.signature("tenant")

      with allure.step("Logout from the co-tenant account"):
        self.single_tenant.logout()

    with allure.step("Login as a Landlord"):
      self.login_page.login(LANDLORD_EMAIL, LANDLORD_PASSWORD)

    with allure.step("Signing the contract from landlord account"):
      self.single_tenant.signature("landlord")

    with allure.step("logout from landlord"):
      self.single_tenant.logout()

    with allure.step("Login as lead tenant"):
      self.login_page.login(TENANT_EMAIL, LANDLORD_PASSWORD)
      time.sleep(1)
      self.login_page.click_element(self.login_page.SIGN_IN_BUTTON)

    with allure.step("paying security deposit"):
      self.single_tenant.security_deposit_payment(tenant_data["security_code"])

    if tenant_data["payment_responsibility"] != "lead":
      with allure.step("Logout from lead tenant's account"):
        self.single_tenant.logout()

      with allure.step("Login to co-tenant account to pay the security deposity"):
        self.login_page.login(COTENANT_EMAIL, LANDLORD_PASSWORD)

      with allure.step("Paying the security deposit and the rent from co-tenant account"):
        self.single_tenant.security_deposit_payment(tenant_data["security_code"])
        self.single_tenant.rent_payment(tenant_data["security_code"])

      with allure.step("Logout from co-tenant after paying security deposit and rent"):
        self.single_tenant.logout()

      with allure.step("Login to the lead tenant's account to pay the rent"):
        self.login_page.login(TENANT_EMAIL, LANDLORD_PASSWORD)


    with allure.step("paying the rent"):
      self.single_tenant.rent_payment(tenant_data["security_code"])

    with allure.step("Logout from tenant"):
      self.single_tenant.logout()

    with allure.step("Login as landlord"):
      self.login_page.login_with_retry(LANDLORD_EMAIL, LANDLORD_PASSWORD)

    with allure.step("Handing over the proeprty"):
      self.single_tenant.handover_property()

    with allure.step("Assertion agains the contract status"):
      assert_true(self.multiple_tenant.is_element_visible(self.single_tenant.UNDER_CONTRACT_STATUS), "The status of the contract is not under contract", f"{tenant_data['title']}", self.multiple_tenant)