from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
class AddProperty(BasePage):
  PROPERTY_BUTTON = (By.XPATH,"//button[@role='button'][.//div[contains(text(), 'Property')]]")
  ADD_PROPERTY = (By.XPATH,"//div[contains(@style,'position: absolute') and contains(@style,'bottom: 40px')]//div[@tabindex='0']")
  SEARCH_ADDRESS_INPUT = (By.XPATH,"//input[@placeholder='Search Address']")
  TITLE_INPUT = (By.XPATH,"//input[@placeholder='Enter Title For this property']")
  AVAILABLE_DATE = (By.XPATH,"(//div[normalize-space()='Availability Date'])[1]")
  SET_BUTTON = (By.XPATH,"//div[@class='css-146c3p1'][normalize-space()='Set']")
  PROPERTY_TYPE = (By.XPATH,"(//div[normalize-space()='Detached'])[1]")
  FURNISHED_TYPE = (By.XPATH,"(//div[normalize-space()='Furnished'])[1]")
  RENTAL_MARKET = (By.XPATH,"(//div[normalize-space()='Professsionals'])[1]")
  BER_CERTIFICATE = (By.XPATH,"(//div[normalize-space()='A1'])[1]")
  AREA_DIV = (By.XPATH,"(//div[normalize-space()='Sq.ft'])[1]")
  AREA_INPUT = (By.XPATH,"//textarea[@placeholder='0']")
  NEXT_BUTTON = (By.XPATH,"//div[@tabindex='0'][.//div[contains(text(), 'Next')]]")
  RENT_PER_MONTH_INPUT = (By.XPATH,"//input[@placeholder='Property Price']")
  FEATURE = (By.XPATH,"//div[contains(text(),'Dry Cleaning Service')]")
  UPLOAD_PHOTO = (By.XPATH, "//div[contains(@style,'font-family: ionicons') and contains(@style,'36px')]")
  GENERATE_DESCRIPTION_BUTTON = (By.XPATH,"//div[contains(text(),'Generate Description')]")
  ADDRESS = (By.XPATH,"(//div[.//input[@placeholder='Search Address']]/following-sibling::div//div[contains(@class,'r-zl2h9q') and contains(@class,'r-ytbthy') and contains(@class,'r-n7gxbd')])[1]")
  SEND_FOR_REVIEW_BUTTON = (By.XPATH,"(//div[normalize-space()='Send for Review'])[3]")
  PROPERTY_MANAGEMENT_BUTTON = (By.XPATH,"//p[normalize-space()='Property Management']")
  SEARCH_PROPERTIES_ADMIN = (By.XPATH, "//input[@placeholder='Search Properties']")
  NOTIFICATIONS_ICON = (By.CSS_SELECTOR, "div.sc-jytpVa")
  NOTIFICATION = (By.XPATH, "//body/div[@id='root']/div[@class='sc-koBvLg kxiJwK']/div[@class='sc-eQwNpu ftPCeT']/div[@class='sc-eknHtZ izJnSZ']/div[2]")
  ACCEPT_PROPERTY_BUTTON = (By.XPATH,"//button[@class='sc-fhHczv dFofPx']")
  ACCEPT_BUTTON = (By.XPATH,"//button[@class='sc-fhHczv WQiWI']")
  SEARCH_PROPERTY_LANDLORD = (By.XPATH,"//input[@placeholder='Search']")
  PROPERTY_STATUS = (By.XPATH,"//div[contains(@style,'padding: 4px 16px') and contains(@style,'border-width: 1px') and contains(@style,'border-radius: 16px')]//div[@dir='auto']")
  ADMIN_EMAIL_INPUT = (By.XPATH, "//input[@placeholder='alma.lawson@example.com']")
  ADMIN_PASSWORD_INPUT = (By.XPATH, "//input[@placeholder='Password']")
  ADMIN_LOGIN_BUTTON = (By.XPATH, "//button[@class='sc-fhHczv eQHLlz']")
  CROSS_BUTTON = (By.XPATH, "//div[contains(@style,'right: 20px') and contains(@style,'top: 20px') and contains(@style,'z-index: 10')]")
  YES_REVIEW_BUTTON = (By.XPATH, "//div[@class='css-g5y9jx r-13awgt0 r-ipm5af']//div[@class='css-g5y9jx']//div[@class='css-g5y9jx']//div[@class='css-g5y9jx']//div[@class='css-g5y9jx']//div[@class='css-g5y9jx']//div[@class='css-g5y9jx r-1loqt21 r-1otgn73']")
  ACCEPT_BUTTON_CONTAINER = (By.XPATH,"//div[@class='sc-eEHciv hKSwDo']")
  PROPERTIES_COUNT_1 = (By.XPATH, "//div[normalize-space()='Properties: 1']")
  MAXIMUM_OCCUPANCY = (By.XPATH, "(//div[contains(., 'Occupancy')]//div[@tabindex='0'][contains(@style,'border-radius: 100px')])[3]")
  MULTIPLE_TENANTS = (By.XPATH, "//div[contains(text(),'Multiple Tenants (e.g., Roommates)')]")
  GROUP_CREATOR_LANDLORD = (By.XPATH, "//div[@class='css-g5y9jx r-1ssbvtb']//div[@class='css-146c3p1'][normalize-space()='Landlord']")
  PAYMENT_RESPONSIBILITY_INDIVIDUAL = (By.XPATH, "//div[@class='css-g5y9jx r-1ssbvtb']//div[@class='css-146c3p1'][normalize-space()='Individual']")
  CONTRACTED_TENANTS_EVERYONE = (By.XPATH, "//div[contains(text(),'Everyone')]")
  CONTRACTED_TENANTS_LEAD_TENANT = (By.XPATH, "//div[contains(text(),'Lead Tenant')]")
  PAYMENT_RESPONSIBILITY_LEAD = (By.XPATH,"//div[@class='css-146c3p1'][normalize-space()='Lead']")
  SINGLE_TENANT = (By.XPATH, "//div[contains(text(),'Single Tenant')]")
  BODY = (By.TAG_NAME, "body")


  def navigate_to_add_property(self):
    self.click_element(self.PROPERTY_BUTTON)
    self.click_element(self.ADD_PROPERTY)


  def enter_property_details(self, address, title, area, rent_per_month, file_path, property_type="single", group_creator = "tenant", payment_responsibility="lead", contracted_tenants="everyone"):
    self.enter_text(self.SEARCH_ADDRESS_INPUT, address)
    self.wait.until(EC.element_to_be_clickable(self.ADDRESS))
    self.click_element(self.ADDRESS)
    self.wait.until(EC.invisibility_of_element_located(self.ADDRESS))
    self.wait.until(EC.element_to_be_clickable(self.NEXT_BUTTON))
    time.sleep(1)

    self.click_element(self.NEXT_BUTTON)
    self.enter_text(self.TITLE_INPUT, title)
    self.click_element(self.AVAILABLE_DATE)
    self.wait.until(EC.element_to_be_clickable(self.SET_BUTTON))
    self.click_element(self.SET_BUTTON)
    self.click_element(self.PROPERTY_TYPE)
    self.click_element(self.FURNISHED_TYPE)
    self.click_element(self.RENTAL_MARKET)

    if property_type != "single":
      self.wait.until(EC.element_to_be_clickable(self.MAXIMUM_OCCUPANCY))
      self.click_element(self.MAXIMUM_OCCUPANCY)

    self.click_element(self.BER_CERTIFICATE)

    self.click_element(self.BODY)
    time.sleep(0.3)

    self.wait.until(EC.element_to_be_clickable(self.AREA_DIV))
    self.click_element(self.AREA_DIV)
    self.enter_text(self.AREA_INPUT, area)
    self.wait.until(EC.element_to_be_clickable(self.SET_BUTTON))
    self.click_element(self.SET_BUTTON)
    self.wait.until(EC.element_to_be_clickable(self.NEXT_BUTTON))
    self.click_element(self.NEXT_BUTTON)
    self.enter_text(self.RENT_PER_MONTH_INPUT, rent_per_month)
    self.wait.until(EC.element_to_be_clickable(self.NEXT_BUTTON))
    self.click_element(self.NEXT_BUTTON)
    self.click_element(self.FEATURE)
    self.wait.until(EC.element_to_be_clickable(self.NEXT_BUTTON))
    self.click_element(self.NEXT_BUTTON)
    self.upload_property_photo(file_path, self.UPLOAD_PHOTO)
    self.wait.until(EC.element_to_be_clickable(self.NEXT_BUTTON))
    self.click_element(self.NEXT_BUTTON)

    self.wait.until(EC.element_to_be_clickable(self.GENERATE_DESCRIPTION_BUTTON))
    self.click_element(self.GENERATE_DESCRIPTION_BUTTON)
    self.wait.until(EC.element_to_be_clickable(self.NEXT_BUTTON))
    self.click_element(self.NEXT_BUTTON)
    time.sleep(1)
    self.click_element(self.NEXT_BUTTON)

    if property_type != "single":
      self.click_element(self.MULTIPLE_TENANTS)

      if group_creator != "tenant":
        self.wait.until(EC.element_to_be_clickable(self.GROUP_CREATOR_LANDLORD))
        self.click_element(self.GROUP_CREATOR_LANDLORD)
        # contracted_tenants = None

      if payment_responsibility != "lead":
        self.click_element(self.PAYMENT_RESPONSIBILITY_INDIVIDUAL)

      else:
        self.click_element(self.PAYMENT_RESPONSIBILITY_LEAD)
        if contracted_tenants == "lead_tenant":
          self.click_element(self.CONTRACTED_TENANTS_LEAD_TENANT)
        elif contracted_tenants == None:
          pass
        else:
          self.click_element(self.CONTRACTED_TENANTS_EVERYONE)

      self.click_element(self.NEXT_BUTTON)

    self.wait.until(EC.visibility_of_element_located(self.CROSS_BUTTON))
    self.click_element(self.CROSS_BUTTON)
    self.wait.until(EC.element_to_be_clickable(self.SEND_FOR_REVIEW_BUTTON))



  def review_property(self, admin_email, admin_password, driver):
    self.click_element(self.SEND_FOR_REVIEW_BUTTON)
    self.click_element(self.YES_REVIEW_BUTTON)
    driver.get("https://admin-staging.rentisity.com/")
    self.enter_text(self.ADMIN_EMAIL_INPUT, admin_email)
    self.enter_text(self.ADMIN_PASSWORD_INPUT, admin_password)
    self.click_element(self.ADMIN_LOGIN_BUTTON)
    self.wait.until(EC.element_to_be_clickable(self.NOTIFICATIONS_ICON))
    self.click_element(self.NOTIFICATIONS_ICON)
    self.click_element(self.NOTIFICATION)
    self.wait.until(EC.element_to_be_clickable(self.ACCEPT_PROPERTY_BUTTON))
    self.click_element(self.ACCEPT_PROPERTY_BUTTON)
    self.wait.until(EC.element_to_be_clickable(self.ACCEPT_BUTTON))
    self.click_element(self.ACCEPT_BUTTON)
    self.wait.until(EC.invisibility_of_element_located(self.ACCEPT_BUTTON_CONTAINER))




