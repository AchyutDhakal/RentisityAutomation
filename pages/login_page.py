from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
  SIGN_IN_BUTTON = (By.XPATH,"//div[@tabindex='0' and .//div[contains(normalize-space(text()), 'Sign In')]]")
  EMAIL_INPUT = (By.CSS_SELECTOR, 'input[autocomplete="on"][enterkeyhint="next"]')
  PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
  PROFILE_EMAIL = (By.XPATH, "(//div[@dir='auto'][contains(text(), '@')])[1]")

  def login(self, email, password):
    self.click_element(self.SIGN_IN_BUTTON)
    self.enter_text(self.EMAIL_INPUT, email)
    self.enter_text(self.PASSWORD_INPUT, password)
    self.click_element(self.SIGN_IN_BUTTON)
