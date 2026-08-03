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
  SET_BUTTON = (By.XPATH,"(//div[@tabindex='0'][.//div[contains(text(), 'Set')]])[2]")
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



  def navigate_to_add_property(self):
    self.click_element(self.PROPERTY_BUTTON)
    self.click_element(self.ADD_PROPERTY)


  def enter_property_details(self, address, title, area, rent_per_month, file_path):
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
    self.click_element(self.BER_CERTIFICATE)
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
    self.take_screenshot("after_upload")
    self.wait.until(EC.element_to_be_clickable(self.NEXT_BUTTON))
    self.click_element(self.NEXT_BUTTON)


    self.click_element(self.GENERATE_DESCRIPTION_BUTTON)
    self.wait.until(EC.element_to_be_clickable(self.NEXT_BUTTON))
    self.click_element(self.NEXT_BUTTON)
    time.sleep(1)
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




