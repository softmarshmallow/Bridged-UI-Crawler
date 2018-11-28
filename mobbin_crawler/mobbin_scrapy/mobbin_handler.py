from time import sleep


class MobbinHandle:
    def __init__(self, driver):
        self.driver = driver

    def manual_login(self):
        self.driver.get('http://mobbin.design/')
        input("press enter if login complete...")

    def auto_login(self):
        # LOAD CREDENTIALS
        from credentials.credentials_loader import load_google_credentials
        cred = load_google_credentials()

        # Save main window for handling pop up window
        main_window_handle = None
        while not main_window_handle:
            main_window_handle = self.driver.current_window_handle

        #  Load main page
        self.driver.get('http://mobbin.design/')

        # Click login button
        login_button = self.driver.find_element_by_xpath(
            '//*[@id="root"]/div/div[3]/div/div[3]/div/div[3]/div/div[2]/div[1]/button')
        login_button.click()
        sleep(1)

        # After login options shows up, click google login
        google_login_button = self.driver.find_element_by_xpath(
            '/html/body/div[3]/div/div/div[2]/button[1]')
        google_login_button.click()

        # POP up window for Google sign in will open
        # Get Pop up window
        signin_window_handle = None
        while not signin_window_handle:
            for handle in self.driver.window_handles:
                if handle != main_window_handle:
                    signin_window_handle = handle
                    break

        # Switch to popup window
        self.driver.switch_to.window(signin_window_handle)
        sleep(5)
        #     ON Google Auth page
        emailElem = self.driver.find_element_by_id('identifierId')
        emailElem.send_keys(cred["ID"])
        nextButton = self.driver.find_element_by_id('identifierNext')
        nextButton.click()
        sleep(3)

        passwordElem = self.driver.find_element_by_xpath('//input[@type="password"]')
        passwordElem.send_keys(cred["PW"])
        signinButton = self.driver.find_element_by_id('passwordNext')
        signinButton.click()
        sleep(3)

        self.driver.switch_to.window(main_window_handle) #or driver.switch_to_default_content()

