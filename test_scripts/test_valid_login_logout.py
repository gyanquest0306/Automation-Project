import pytest

from generic.base_setup import BaseSetup
from pages.login_page import LoginPage
from pages.enter_time_track_page import EnterTimeTrackPage
from generic.excel import Excel

class TestValidLoginLogout(BaseSetup):

    @pytest.mark.run(order=3)
    def test_valid_login(self):
        un=Excel.get_data(self.xl_path,"TestValidLoginLogout",2,1)
        pw=Excel.get_data(self.xl_path,"TestValidLoginLogout",2,2)
        #1. Enter Valid UN
        login_page=LoginPage(self.driver)
        login_page.set_username(un)
        #2. Enter Valid PW
        login_page.set_password(pw)
        #3. Click on login Button
        login_page.click_loginButton()
        # 4. click on logout link
        ett_page = EnterTimeTrackPage(self.driver)
        ett_page.click_logout_link()
        #verify login page is displayed
        displayed=login_page.verify_login_page_is_displayed(self.wait)
        assert displayed

