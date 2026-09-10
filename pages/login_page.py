from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):
    SIGN_IN_BUTTON = (By.XPATH,"//div[@tabindex='0' and .//div[contains(normalize-space(text()), 'Sign In')]]")
    EMAIL_INPUT = (By.CSS_SELECTOR, 'input[autocomplete="on"][enterkeyhint="next"]')
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    PROFILE_EMAIL = (By.XPATH, "(//div[@dir='auto'][contains(text(), '@')])[1]")

    def login(self, email, password):
        self.wait.until(EC.presence_of_element_located(self.SIGN_IN_BUTTON))
        buttons = self.driver.find_elements(*self.SIGN_IN_BUTTON)
        visible = [b for b in buttons if b.is_displayed()]
        assert len(visible) >= 1, f"No visible 'Contracts' button found (checked {len(buttons)} matches)"
        visible[0].click()
        self.click_element(self.SIGN_IN_BUTTON)
        self.enter_text(self.EMAIL_INPUT, email)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click_element(self.SIGN_IN_BUTTON)


    def login_with_retry(self, email, password, max_attempts=3):
        for attempt in range(max_attempts):
            self.login(email, password)
            time.sleep(2)
            current_url = self.driver.current_url
            if "/login" not in current_url and current_url != "https://app-staging.rentisity.com/":
                return
            print(f"Login bounced back (attempt {attempt+1}/{max_attempts}), URL: {current_url}. Retrying...")
            time.sleep(2)
        raise Exception(f"Login failed for {email} after {max_attempts} attempts — kept bouncing to /login")