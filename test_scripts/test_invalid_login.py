from generic.base_setup import BaseSetup
from pages.login_page import LoginPage
import pytest
from generic.excel import Excel

class TestInValidLogin(BaseSetup):
    @pytest.mark.run(order=2)
    def test_invalid_login(self):
        un=Excel.get_data(self.xl_path,"TestInValidLogin",2,1)
        pw=Excel.get_data(self.xl_path,"TestInValidLogin",2,2)
    
        #1. Enter Invalid UN
        login_page=LoginPage(self.driver)
        login_page.set_username(un)
        #2. Enter Invalid PW
        login_page.set_password(pw)
        #3. Click on login Button
        login_page.click_loginButton()
        #4.Verify that error message is displayed
        displayed=login_page.verify_err_msg_is_displayed(self.wait)
        assert displayed