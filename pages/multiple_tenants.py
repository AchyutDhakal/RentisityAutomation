from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class MultipleTenant(BasePage):
  PROPERTY_BUTTON = (By.XPATH,"//button[@role='button'][.//div[contains(text(), 'Property')]]")
  SEARCH_PROPERTY = (By.XPATH,"//input[@placeholder='Search']")
  PROPERTY = (By.XPATH, "//a[contains(@href,'/property-view/')]")
  INSTANT_APPLY_BUTTON = (By.XPATH, "//div[contains(text(),'Instant Apply')]")
  ADD_BUTTON = (By.XPATH, "//div[normalize-space()='Add']")
  CO_TENANT_SEARCH_INPUT = (By.XPATH, "(//input[@placeholder='Search'])[2]")
  DONE_BUTTON = (By.XPATH, "//div[contains(text(),'Done')]")
  NOTIFICATIONS_ICON = (By.XPATH, "(//div[normalize-space()='9+'])[2]")
  NOTIFICATION_ITEM = (By.XPATH, "(//div[@tabindex='0'][contains(@style,'background-color: rgb(236, 236, 236)')][.//div[contains(text(), 'You are invited to submit')]])[1]")
  ACCEPT_BUTTON = (By.XPATH, "//div[contains(text(),'Accept')]")
  YES_ACCEPT_BUTTON = (By.XPATH, "(//div[normalize-space()='Yes, Accept'])[2]")
  APPLY_BUTTON = (By.XPATH, "//div[@class='css-146c3p1'][normalize-space()='Apply']")
  APPLICANTS = (By.XPATH, "//div[normalize-space()='2 tenants']")
  PROPERTY_REQUEST_BUTTON = (By.XPATH, "//div[contains(text(),'Property Requests')]")
  SHORTLIST_BUTTON = (By.XPATH, "//div[@class='css-g5y9jx r-1loqt21 r-1otgn73 r-1awozwy r-o7c05e r-wgabs5 r-13awgt0 r-1mmae3n']//div[@class='css-146c3p1'][normalize-space()='Shortlist']")
  ACCEPT_GROUP_BUTTON = (By.XPATH, "(//div[contains(text(),'Accept')])[3]")
  REVIEW_AND_COMPLETE_BUTTON = (By.XPATH, "//div[normalize-space()='Review and Complete']")
  COMPLETE_BOOKING_BUTTON = (By.XPATH, "//div[normalize-space()='Complete Booking']")
  YES_COMPLETE_BUTTON = (By.XPATH, "//div[contains(text(),'Yes, Complete')]")
  GENERATE_CONTRACT_BUTTON = (By.XPATH, "//div[contains(text(),'Generate Contract')]")
  CONTRACT_BUTTON = (By.XPATH, "//div[@class='css-146c3p1 r-dnmrzs r-1udh08x r-1udbk01 r-3s2u2q r-1iln25a r-9iso6'][normalize-space()='Contracts']")
  TENANT_CONTRACT = (By.XPATH, "(//div[normalize-space()='Pending Signatures'])[1]")
  LANDLORD_CONTRACT = (By.XPATH, "(//div[normalize-space()='Tenant Signed'])[1]")
  SIGNED_CONTRACT = (By.XPATH, "(//div[normalize-space()='Contract Signed'])[1]")
  SECURITY_DEPOSITED_CONTRACT = (By.XPATH, "(//div[normalize-space()='Security Deposited'])[1]")
  RENTED_CONTRACT = (By.XPATH, "(//div[normalize-space()='Rent Released'])[1]")
  SIGN_CONTRACT_BUTTON = (By.XPATH, "//div[contains(text(),'Sign Contract')]")
  ASSIGN_ROOMS_BUTTON = (By.XPATH, "//div[contains(text(),'Assign Rooms')]")
  SHARE_RENT_EQUALLY_BUTTON = (By.XPATH, "//div[contains(text(),'Share Rent Equally')]")
  ADD_ROOM_BUTTON = (By.XPATH, "(//div[normalize-space()='+ Add unit to this tenant'])[2]")
  ROOM_NUMBER_BUTTON = (By.XPATH, "//div[@class='css-g5y9jx r-1loqt21 r-1otgn73']//div[@class='css-146c3p1'][normalize-space()='Room - 1']")
  COMPLETE_BUTTON = (By.XPATH, "//div[contains(text(),'Complete')]")
  SIGN_CONTRACT_BUTTON = (By.XPATH, "//div[contains(text(),'Sign Contract')]")
  SIGNATURE_CANVAS = (By.TAG_NAME, "canvas")
  UPLOAD_BUTTON = (By.XPATH, "//div[contains(text(),'Upload')]")
  SHARE_DEPOSIT_EQUALLY_BUTTON = (By.XPATH, "(//div[normalize-space()='Share Deposit Equally'])[2]")


  def apply_for_property(self, property_title, co_tenant_email):
    CO_TENANT = (By.XPATH, f"(//div[@tabindex='0'][.//div[contains(text(), '{co_tenant_email}')]])[2]")
    self.click_element(self.PROPERTY_BUTTON)
    self.enter_text(self.SEARCH_PROPERTY, property_title)
    self.click_element(self.PROPERTY)
    self.wait.until(EC.element_to_be_clickable(self.INSTANT_APPLY_BUTTON))
    self.click_element(self.INSTANT_APPLY_BUTTON)
    self.click_element(self.ADD_BUTTON)
    self.enter_text(self.CO_TENANT_SEARCH_INPUT, co_tenant_email)
    self.wait.until(EC.visibility_of_any_elements_located(CO_TENANT))
    self.click_element(CO_TENANT)
    self.click_element(self.APPLY_BUTTON)
    self.wait.until(EC.invisibility_of_element_located(self.APPLY_BUTTON))

  def accept_cotenant_invitation(self):
    self.wait.until(EC.element_to_be_clickable(self.NOTIFICATIONS_ICON))
    self.click_element(self.NOTIFICATIONS_ICON)
    self.click_element(self.NOTIFICATION_ITEM)
    self.wait.until(EC.element_to_be_clickable(self.ACCEPT_BUTTON))
    self.click_element(self.ACCEPT_BUTTON)
    self.click_element(self.YES_ACCEPT_BUTTON)
    self.wait.until(EC.invisibility_of_element_located(self.ACCEPT_BUTTON))


  def accept_application(self, title):
    self.click_element(self.PROPERTY_REQUEST_BUTTON)

    PROPERTY_REQUEST = (By.XPATH, f"//div[normalize-space()='{title}']")

    self.wait.until(EC.element_to_be_clickable(PROPERTY_REQUEST))
    self.click_element(PROPERTY_REQUEST)
    self.wait.until(EC.element_to_be_clickable(self.SHORTLIST_BUTTON))
    self.click_element(self.APPLICANTS)
    self.click_element(self.ACCEPT_BUTTON)
    time.sleep(0.5)
    self.click_element(self.ACCEPT_GROUP_BUTTON)
    self.wait.until(EC.element_to_be_clickable(self.REVIEW_AND_COMPLETE_BUTTON))
    self.click_element(self.REVIEW_AND_COMPLETE_BUTTON)
    self.click_element(self.COMPLETE_BOOKING_BUTTON)
    self.click_element(self.YES_COMPLETE_BUTTON)
    self.wait.until(EC.element_to_be_clickable(self.GENERATE_CONTRACT_BUTTON))


  def assign_rooms(self, deposit):
    self.wait.until(EC.element_to_be_clickable(self.CONTRACT_BUTTON))
    self.click_element(self.CONTRACT_BUTTON)
    self.wait.until(EC.element_to_be_clickable(self.TENANT_CONTRACT))
    self.click_element(self.TENANT_CONTRACT)
    self.click_element(self.ASSIGN_ROOMS_BUTTON)
    self.click_element(self.SHARE_RENT_EQUALLY_BUTTON)

    if deposit == "everyone":
      self.click_element(self.SHARE_DEPOSIT_EQUALLY_BUTTON)
      
    self.click_element(self.ADD_ROOM_BUTTON)
    self.click_element(self.ROOM_NUMBER_BUTTON)
    time.sleep(1)
    self.click_element(self.ADD_ROOM_BUTTON)
    self.click_element(self.ROOM_NUMBER_BUTTON)
    self.click_element(self.COMPLETE_BUTTON)
    self.wait.until(EC.element_to_be_clickable(self.SIGN_CONTRACT_BUTTON))
    self.click_element(self.SIGN_CONTRACT_BUTTON)
    self.draw_signature(self.SIGNATURE_CANVAS)
    self.click_element(self.UPLOAD_BUTTON)
    self.wait.until(EC.invisibility_of_element_located(self.UPLOAD_BUTTON))