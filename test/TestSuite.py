import time
import unittest

from automation.mobile.mobdriver import MobDriver, collect_prerequisites
from automation.mobile.uicomponents import UIComponents
from test.desired_capabilities import get_desired_capabilities

# collect platform and app installation bundle details
dict = collect_prerequisites()


class TestSuite(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        desired_caps = get_desired_capabilities(app_path=dict['app_bundle'], platform=dict['platform'])
        self.driver = MobDriver('http://localhost:4723/wd/hub', desired_caps)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    display_name = 'Test User'
    user_name = 'test.user'
    password = 'test1234'

    invalid_user = 'invalid'
    invalid_pass = 'invalid'

    def test_1_login_invalid_username(self):
        btn_login = self.driver.find_by_name(UIComponents.BUTTON, 'Login')
        btn_login.click()

        result = self.driver.check_alert(msg='Please enter username')
        self.assertTrue(result.result, result.msg)

    def test_2_login_invalid_password(self):
        txt_user = self.driver.find_by_name(UIComponents.TEXTFIELD, 'Username')
        txt_user.set_value(self.invalid_user)
        self.driver.hide_keyboard()

        btn_login = self.driver.find_by_name(UIComponents.BUTTON, 'Login')
        btn_login.click()

        result = self.driver.check_alert(msg='Please enter password')
        self.assertTrue(result.result, result.msg)

    def test_3_login_invalid_credentials(self):
        txt_pwd = self.driver.find_by_name(UIComponents.PWDFIELD, 'Password')
        txt_pwd.set_value(self.invalid_pass)
        self.driver.hide_keyboard()

        btn_login = self.driver.find_by_name(UIComponents.BUTTON, 'Login')
        btn_login.click()

        result = self.driver.check_alert(msg='Invalid username or password')
        self.assertTrue(result.result, result.msg)

    def test_4_register_invalid_displayname(self):
        btn_reg = self.driver.find_by_name(UIComponents.BUTTON, 'Register')
        btn_reg.click()

        time.sleep(5)

        btn_reg = self.driver.find_by_name(UIComponents.BUTTON, 'Register')
        btn_reg.click()

        result = self.driver.check_alert(msg='Please enter display name')
        self.assertTrue(result.result, result.msg)

    def test_5_register_invalid_username(self):
        txt_dn = self.driver.find_by_name(UIComponents.TEXTFIELD, 'Display name')
        txt_dn.set_value(self.display_name)
        self.driver.hide_keyboard()

        btn_reg = self.driver.find_by_name(UIComponents.BUTTON, 'Register')
        btn_reg.click()

        result = self.driver.check_alert(msg='Please enter username')
        self.assertTrue(result.result, result.msg)

    def test_6_register_invalid_password(self):
        txt_user = self.driver.find_by_name(UIComponents.TEXTFIELD, 'Username')
        txt_user.set_value(self.user_name)
        self.driver.hide_keyboard()

        btn_reg = self.driver.find_by_name(UIComponents.BUTTON, 'Register')
        btn_reg.click()

        result = self.driver.check_alert(msg='Please enter password')
        self.assertTrue(result.result, result.msg)

    def test_7_register_valid_registration(self):
        txt_pwd = self.driver.find_by_name(UIComponents.PWDFIELD, 'Password')
        txt_pwd.set_value(self.user_name)
        self.driver.hide_keyboard()

        btn_reg = self.driver.find_by_name(UIComponents.BUTTON, 'Register')
        btn_reg.click()

        result = self.driver.check_alert(msg='Registered successfully')
        self.assertTrue(result.result, result.msg)

    def test_8_login_valid_login(self):
        time.sleep(5)

        txt_pwd = self.driver.find_by_name(UIComponents.TEXTFIELD, 'Username')
        txt_pwd.set_value(self.user_name)
        self.driver.hide_keyboard()

        txt_pwd = self.driver.find_by_name(UIComponents.PWDFIELD, 'Password')
        txt_pwd.set_value(self.user_name)
        self.driver.hide_keyboard()

        btn_login = self.driver.find_by_name(UIComponents.BUTTON, 'Login')
        btn_login.click()

        result = self.driver.check_alert()
        self.assertFalse(result.result, result.msg)

    def test_9_home_valid_welcome_msg(self):
        time.sleep(5)

        welcome_msg = 'Welcome ' + self.display_name + '!'
        txt_welcome = self.driver.find_by_name(UIComponents.LABEL, welcome_msg)
        if txt_welcome is None:
            self.assertTrue(False, 'Label not found with msg - ' + welcome_msg)


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSuite)
    log_file = 'TestSuite_report.txt'
    f = open(log_file, "w")
    unittest.TextTestRunner(stream=f, verbosity=2).run(suite)
