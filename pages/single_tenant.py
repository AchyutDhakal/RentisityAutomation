from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC

class SingleTenant(BasePage):
  PROPERTY_BUTTON = (By.XPATH,"//button[@role='button'][.//div[contains(text(), 'Property')]]")
  SEARCH_PROPERTY = (By.XPATH,"//input[@placeholder='Search']")
  PROPERTY = (By.XPATH, "//a[contains(@href,'/property-view/')]")
  INSTANT_APPLY_BUTTON = (By.XPATH, "//div[contains(text(),'Instant Apply')]")
  APPLY_BUTTON = (By.XPATH, "//div[@class='css-146c3p1'][normalize-space()='Apply']")
  PROPERTY_REQUEST_BUTTON = (By.XPATH, "//div[contains(text(),'Property Requests')]")
  # PROPERTY_REQUEST = (By.XPATH, "//div[4]//div[1]//div[1]//div[2]//div[1]//div[1]//div[1]//div[1]//div[1]//div[2]//div[1]//div[1]//div[1]//div[1]//div[1]//div[4]")
  CHECKBOX_1 = (By.XPATH, "(.//div[contains(@style,'width: 28px') and contains(@style,'height: 28px') and contains(@style,'border-radius: 8px')])[1]")
  CHECKBOX_2 = (By.XPATH, "(.//div[contains(@style,'width: 28px') and contains(@style,'height: 28px') and contains(@style,'border-radius: 8px')])[2]")
  PUSH_TO_SHORTLIST_BUTTON = (By.XPATH, "//div[contains(text(),'Push To Shortlist')]")
  CONFIRM_BUTON = (By.XPATH, "//div[contains(text(),'Confirm')]")
  SHORTLIST_BUTTON = (By.XPATH, "//div[@class='css-g5y9jx r-1loqt21 r-1otgn73 r-1awozwy r-o7c05e r-wgabs5 r-13awgt0 r-1mmae3n']//div[@class='css-146c3p1'][normalize-space()='Shortlist']")
  PUSH_TO_VIEWING_BUTTON = (By.XPATH, "//div[contains(text(),'Push To Viewing')]")
  VIEWING_LIST_BUTTON = (By.XPATH, "//div[@class='css-g5y9jx r-1loqt21 r-1otgn73 r-1awozwy r-o7c05e r-wgabs5 r-13awgt0 r-1mmae3n']//div[@class='css-146c3p1'][normalize-space()='Viewing List']")
  APPLICANT = (By.XPATH, "//div[@class='css-g5y9jx']//div[@class='css-g5y9jx']//div[@class='css-g5y9jx']//div[@class='css-g5y9jx']//div[@class='css-g5y9jx']//div[@class='css-146c3p1'][normalize-space()='Viewing List']")
  ACCEPT_APPLICATION_BUTTON = (By.XPATH, "//div[@class='css-g5y9jx r-1loqt21 r-1otgn73 r-1awozwy r-kdyh1x r-15pk7w6 r-13awgt0 r-1777fci r-1mmae3n r-is05cd']")
  YES_BUTTON = (By.XPATH, "//div[contains(text(),'Yes')]")
  REVIEW_AND_COMPLETE_BUTTON = (By.XPATH, "//div[@tabindex='0'][.//div[normalize-space()='Review and Complete']]")
  COMPLETE_BOOKING_BUTTON = (By.XPATH, "//div[normalize-space()='Complete Booking']")
  YES_COMPLETE_BUTTON = (By.XPATH, "//div[contains(text(),'Yes, Complete')]")
  GENERATE_CONTRACT_BUTTON = (By.XPATH, "//div[contains(text(),'Generate Contract')]")
  SYSTEM_GENERATED_CONTRACT = (By.XPATH, "//div[normalize-space()='System Generated']")
  CONTINUE_BUTTON = (By.XPATH, "//div[contains(text(),'Continue')]")
  START_DATE = (By.XPATH, "//div[normalize-space()='Enter Start Date']")
  SET_BUTTON = (By.XPATH,"//div[@class='css-146c3p1'][normalize-space()='Set']")
  END_DATE = (By.XPATH, "//div[normalize-space()='Enter End Date']")
  NEXT_BUTTON = (By.XPATH,"//div[@tabindex='0'][.//div[contains(text(), 'Next')]]")
  RENT_IN_ADVANCE_NO = (By.XPATH, "(//div[normalize-space()='No'])[2]")
  TENANT_ADDRESS_YES = (By.XPATH, "(//div[normalize-space()='Yes'])[4]")
  LANDLORD_MAILING_ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='Enter Details']")
  TENANT_PAYS_PROVIDERS_NO = (By.XPATH,"(//div[normalize-space()='No'])[6]")
  TENANT_PAYS_EQUAL_SHARES_NO = (By.XPATH, "(//div[normalize-space()='No'])[8]")
  DATE_PICKER = (By.XPATH, "//div[@tabindex='0'][.//div[contains(text(),'Enter Date')]]")
  TERMINATION_DURING_FIXED_TERM_NO = (By.XPATH, "(//div[normalize-space()='No'])[10]")
  LANDLORD_BANK_NAME = (By.XPATH, "//input[@placeholder='Bank Name']")
  ACCOUNT_NAME_INPUT = (By.XPATH, "//input[@placeholder='A/c holder name']")
  IBAN_INPUT = (By.XPATH, "//input[@placeholder='IBAN number']")
  BIC_INPUT = (By.XPATH, "//input[@placeholder='BIC']")
  ELECTRICITY_TENANT = (By.XPATH, "(//div[.//div[text()='Electricity']]//div[@tabindex='0'][.//div[contains(text(), 'Tenant')]])[3]")
  GAS_OIL_TENANT = (By.XPATH, "(//div[.//div[text()='Gas/oil']]//div[@tabindex='0'][.//div[contains(text(), 'Tenant')]])[4]")
  INTERNET_TENANT = (By.XPATH, "(//div[.//div[text()='Internet']]//div[@tabindex='0'][.//div[contains(text(), 'Tenant')]])[5]")
  WASTE_TENANT = (By.XPATH, "(//div[.//div[text()='Waste']]//div[@tabindex='0'][.//div[contains(text(), 'Tenant')]])[6]")
  ELECTRICITY_INPUT = (By.XPATH, "(//input[@placeholder='Company Name'])[1]")
  GAS_OIL_INPUT = (By.XPATH, "(//input[@placeholder='Company Name'])[2]")
  INTERNET_INPUT = (By.XPATH, "(//input[@placeholder='Company Name'])[3]")
  WASTE_INPUT = (By.XPATH, "(//input[@placeholder='Company Name'])[4]")
  CONTRACT_BUTTON = (By.XPATH, "//button[@role='button'][.//div[contains(text(), 'Contracts')]]")
  TENANT_CONTRACT = (By.XPATH, "(//div[normalize-space()='Pending Signatures'])[1]")
  LANDLORD_CONTRACT = (By.XPATH, "(//div[normalize-space()='Tenant Signed'])[1]")
  SIGNED_CONTRACT = (By.XPATH, "(//div[normalize-space()='Contract Signed'])[1]")
  SECURITY_DEPOSITED_CONTRACT = (By.XPATH, "(//div[normalize-space()='Security Deposited'])[1]")
  RENTED_CONTRACT = (By.XPATH, "(//div[normalize-space()='Rent Released'])[1]")
  SIGN_CONTRACT_BUTTON = (By.XPATH, "//div[contains(text(),'Sign Contract')]")
  SIGNATURE_CANVAS = (By.TAG_NAME, "canvas")
  UPLOAD_BUTTON = (By.XPATH, "//div[contains(text(),'Upload')]")
  SECURITY_DEPOSIT_BUTTON = (By.XPATH, "(//div[normalize-space()='Security Deposit'])[5]")
  SECURITY_CODE_INPUT = (By.XPATH, "//input[@id='payment-cvcInput']")
  PAY_NOW_BUTTON = (By.XPATH, "(//div[@aria-modal='true']//div[normalize-space()='Pay Now'])[2]")
  RELEASE_RENT_BUTTON = (By.XPATH, "//div[contains(text(),'Release Rent')]")
  PAY_BUTTON = (By.XPATH, "//div[@class='css-146c3p1'][normalize-space()='Pay']")
  YES_PAY_BUTTON = (By.XPATH, "//div[contains(text(),'Yes, Pay')]")
  HANDOVER_PROPERTY_BUTTON = (By.XPATH, "(//div[normalize-space()='Handover Property'])[2]")
  LOGOUT_BUTTON = (By.XPATH, "//div[contains(text(),'Log Out')]")
  CONFIRM_HANDOVER_BUTTON = (By.XPATH, "//div[contains(text(),'Confirm handover to Tenants ?')]")
  ACCEPT_MULTIPLE_BUTTON = (By.XPATH, "//div[normalize-space()='Accept Multiple']")
  REVIEW_AND_COMPLETE_BUTTON_SINGLE = (By.XPATH, "//div[@class='css-g5y9jx r-1loqt21 r-1otgn73 r-1awozwy r-kdyh1x r-15pk7w6 r-13awgt0 r-1777fci r-1mmae3n r-is05cd']//div[@class='css-146c3p1'][normalize-space()='Review and Complete']")
  UNDER_CONTRACT_STATUS = (By.XPATH, "//div[normalize-space()='Under Contract']")
  EXTERNAL_PAYMENT = (By.XPATH, "//div[normalize-space()='External Payment']")
  COFIRM_PAYMENT_MADE_BUTTON = (By.XPATH, "(//div[normalize-space()='Confirm Payment Made'])[3]")
  REVIEW_RECORDED_PAYMENT_BUTTON = (By.XPATH, "(//div[normalize-space()='Review Recorded Payment'])[5]")
  CONFIRM_RECEIPT_BUTTON = (By.XPATH, "(//div[normalize-space()='Confirm Receipt'])[2]")
  UPLOAD_CONTRACT_BUTTON = (By.XPATH, "(//div[normalize-space()='Upload here'])[2]")
  CONTRACT_CONFIRM_CHECKBOX = (By.XPATH, "//div[contains(text(), 'I confirm')]")
  CONTRACT_BUTTON_EXTERNAL_PAYMENT = (By.XPATH, "(//button[@role='button'][.//div[contains(text(), 'Contracts')]])[2]")

  def logout(self):
    self.click_element(self.LOGOUT_BUTTON)
    self.click_element(self.YES_BUTTON)


  def apply_for_property(self, property_title):
    self.click_element(self.PROPERTY_BUTTON)
    self.enter_text(self.SEARCH_PROPERTY, property_title)
    self.click_element(self.PROPERTY)
    self.wait.until(EC.element_to_be_clickable(self.INSTANT_APPLY_BUTTON))
    self.click_element(self.INSTANT_APPLY_BUTTON)
    self.click_element(self.APPLY_BUTTON)
    self.wait.until(EC.invisibility_of_element_located(self.APPLY_BUTTON))

  def accept_application(self, title, group_creator):
    self.click_element(self.PROPERTY_REQUEST_BUTTON)

    PROPERTY_REQUEST = (By.XPATH, f"//div[normalize-space()='{title}']")

    self.wait.until(EC.element_to_be_clickable(PROPERTY_REQUEST))
    self.click_element(PROPERTY_REQUEST)
    # self.click_element(self.APPLICANT)
    self.wait.until(EC.element_to_be_clickable(self.SHORTLIST_BUTTON))

    if group_creator == "landlord":
      self.click_element(self.CHECKBOX_2)

    self.click_element(self.CHECKBOX_1)
    self.click_element(self.PUSH_TO_SHORTLIST_BUTTON)
    self.click_element(self.CONFIRM_BUTON)
    self.click_element(self.SHORTLIST_BUTTON)

    if group_creator == "landlord":
          self.click_element(self.CHECKBOX_2)

    self.click_element(self.CHECKBOX_1)

    if group_creator == "landlord":
      self.click_element(self.ACCEPT_MULTIPLE_BUTTON)
      self.click_element(self.REVIEW_AND_COMPLETE_BUTTON)

    else:
      self.click_element(self.PUSH_TO_VIEWING_BUTTON)
      self.click_element(self.CONFIRM_BUTON)
      self.click_element(self.VIEWING_LIST_BUTTON)
      self.click_element(self.APPLICANT)
      self.wait.until(EC.element_to_be_clickable(self.ACCEPT_APPLICATION_BUTTON))
      self.click_element(self.ACCEPT_APPLICATION_BUTTON)
      self.click_element(self.YES_BUTTON)
      self.click_element(self.REVIEW_AND_COMPLETE_BUTTON_SINGLE)

    self.click_element(self.COMPLETE_BOOKING_BUTTON)
    self.click_element(self.YES_COMPLETE_BUTTON)
    self.wait.until(EC.element_to_be_clickable(self.GENERATE_CONTRACT_BUTTON))


  def generate_contract(self, landlord_address, bank_name, account_name, iban, bic, electricity, gas_oil, internet, waste, payment, contract_type, contract_file_path):
    self.click_element(self.GENERATE_CONTRACT_BUTTON)

    if contract_type == "system":
      self.click_element(self.SYSTEM_GENERATED_CONTRACT)

    self.click_element(self.CONTINUE_BUTTON)
    time.sleep(1)
    self.click_element(self.CONTINUE_BUTTON)
    self.click_element(self.START_DATE)
    self.wait.until(EC.element_to_be_clickable(self.SET_BUTTON))
    self.click_element(self.SET_BUTTON)
    self.click_element(self.END_DATE)
    self.wait.until(EC.element_to_be_clickable(self.SET_BUTTON))
    self.click_element(self.SET_BUTTON)

    if payment == "external":
      self.click_element(self.EXTERNAL_PAYMENT)

    if contract_type == "manual":
      self.upload_property_photo(contract_file_path, self.UPLOAD_CONTRACT_BUTTON)
      self.click_element(self.CONTRACT_CONFIRM_CHECKBOX)

    self.click_element(self.NEXT_BUTTON)
    self.wait.until(EC.invisibility_of_element_located(self.EXTERNAL_PAYMENT))

    if contract_type == "system":
      self.click_element(self.RENT_IN_ADVANCE_NO)
      self.click_element(self.TENANT_ADDRESS_YES)
      self.enter_text(self.LANDLORD_MAILING_ADDRESS_INPUT, landlord_address)
      self.click_element(self.TENANT_PAYS_PROVIDERS_NO)
      self.click_element(self.TENANT_PAYS_EQUAL_SHARES_NO)
      self.click_element(self.DATE_PICKER)
      self.wait.until(EC.element_to_be_clickable(self.SET_BUTTON))
      self.click_element(self.SET_BUTTON)
      self.click_element(self.DATE_PICKER)
      self.wait.until(EC.element_to_be_clickable(self.SET_BUTTON))
      self.click_element(self.SET_BUTTON)
      self.click_element(self.TERMINATION_DURING_FIXED_TERM_NO)
      self.enter_text(self.LANDLORD_BANK_NAME, bank_name)
      self.enter_text(self.ACCOUNT_NAME_INPUT, account_name)
      self.enter_text(self.IBAN_INPUT, iban)
      self.enter_text(self.BIC_INPUT, bic)
      self.click_element(self.ELECTRICITY_TENANT)
      self.click_element(self.GAS_OIL_TENANT)
      self.click_element(self.INTERNET_TENANT)
      self.click_element(self.WASTE_TENANT)
      self.enter_text(self.ELECTRICITY_INPUT, electricity)
      self.enter_text(self.GAS_OIL_INPUT, gas_oil)
      self.enter_text(self.INTERNET_INPUT, internet)
      self.enter_text(self.WASTE_INPUT, waste)
      self.click_element(self.NEXT_BUTTON)
      self.wait.until(EC.element_to_be_clickable(self.TENANT_CONTRACT))


  def signature(self, person):
    self.click_element(self.CONTRACT_BUTTON)
    if person == "tenant":
      self.click_element(self.TENANT_CONTRACT)
    else:
      self.click_element(self.LANDLORD_CONTRACT)

    self.wait.until(EC.element_to_be_clickable(self.SIGN_CONTRACT_BUTTON))
    self.click_element(self.SIGN_CONTRACT_BUTTON)
    self.draw_signature(self.SIGNATURE_CANVAS)
    self.click_element(self.UPLOAD_BUTTON)
    self.wait.until(EC.invisibility_of_element_located(self.UPLOAD_BUTTON))


  def security_deposit_payment(self, security_code):
    self.click_element(self.CONTRACT_BUTTON)
    self.wait.until(EC.element_to_be_clickable(self.SIGNED_CONTRACT))
    self.click_element(self.SIGNED_CONTRACT)
    self.wait.until(EC.element_to_be_clickable(self.SECURITY_DEPOSIT_BUTTON))
    self.click_element(self.SECURITY_DEPOSIT_BUTTON)
    self.click_element(self.CONTINUE_BUTTON)
    self.enter_security_code(security_code, self.SECURITY_CODE_INPUT, self.PAY_NOW_BUTTON)
    self.click_element(self.YES_PAY_BUTTON)
    self.wait.until(EC.invisibility_of_element_located(self.YES_PAY_BUTTON))
    time.sleep(1)
    self.driver.refresh()



  def rent_payment(self, security_code):
    self.wait.until(EC.element_to_be_clickable(self.RELEASE_RENT_BUTTON))
    self.click_element(self.RELEASE_RENT_BUTTON)
    self.click_element(self.CONTINUE_BUTTON)
    self.click_element(self.PAY_BUTTON)
    self.wait.until(EC.element_to_be_clickable(self.PAY_NOW_BUTTON))
    self.enter_security_code(security_code, self.SECURITY_CODE_INPUT, self.PAY_NOW_BUTTON)
    self.click_element(self.YES_PAY_BUTTON)


  def handover_property(self):
    self.wait.until(EC.element_to_be_clickable(self.CONTRACT_BUTTON))
    time.sleep(0.5)
    self.click_element(self.CONTRACT_BUTTON)
    self.wait.until(EC.element_to_be_clickable(self.RENTED_CONTRACT))
    self.click_element(self.RENTED_CONTRACT)
    self.wait.until(EC.element_to_be_clickable(self.HANDOVER_PROPERTY_BUTTON))
    self.click_element(self.HANDOVER_PROPERTY_BUTTON)
    self.click_element(self.CONFIRM_HANDOVER_BUTTON)
    self.wait.until(EC.invisibility_of_element_located(self.HANDOVER_PROPERTY_BUTTON))


  def tenant_confirm_external_payment(self):
    self.wait.until(EC.element_to_be_clickable(self.CONTRACT_BUTTON))
    time.sleep(0.5)
    self.click_element(self.CONTRACT_BUTTON)
    self.wait.until(EC.element_to_be_clickable(self.SIGNED_CONTRACT))
    self.click_element(self.SIGNED_CONTRACT)
    self.wait.until(EC.element_to_be_clickable(self.COFIRM_PAYMENT_MADE_BUTTON))
    self.click_element(self.COFIRM_PAYMENT_MADE_BUTTON)
    # self.wait.until(EC.invisibility_of_element_located(self.COFIRM_PAYMENT_MADE_BUTTON))


  def review_external_payment_and_handover(self):
    self.wait.until(EC.element_to_be_clickable(self.CONTRACT_BUTTON_EXTERNAL_PAYMENT))
    self.click_element(self.CONTRACT_BUTTON_EXTERNAL_PAYMENT)
    self.wait.until(EC.element_to_be_clickable(self.SIGNED_CONTRACT))
    self.click_element(self.SIGNED_CONTRACT)
    self.wait.until(EC.element_to_be_clickable(self.REVIEW_RECORDED_PAYMENT_BUTTON))
    self.click_element(self.REVIEW_RECORDED_PAYMENT_BUTTON)
    self.wait.until(EC.element_to_be_clickable(self.CONFIRM_RECEIPT_BUTTON))
    self.click_element(self.CONFIRM_RECEIPT_BUTTON)
    self.wait.until(EC.element_to_be_clickable(self.HANDOVER_PROPERTY_BUTTON))
    self.click_element(self.HANDOVER_PROPERTY_BUTTON)
    self.click_element(self.CONFIRM_HANDOVER_BUTTON)
    self.wait.until(EC.invisibility_of_element_located(self.HANDOVER_PROPERTY_BUTTON))



  def terminate_contract_tenant(self):
    pass




