import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from pyjavaproperties import Properties
from selenium.webdriver.chrome.options import Options

class BaseSetup:
    @pytest.fixture(autouse=True)
    def precondition(self):
        print("Accessing property file")
        pptobj=Properties()
        pptobj.load(open('config.properties'))
        self.xl_path=pptobj['XL_PATH']
        print("XL PATH",self.xl_path)
        
        gridurl=pptobj['GRIDURL']
        print("grid URL",gridurl)
        usergrid=pptobj['USERGRID'].lower()
        print("User Grid",usergrid)
        browser=pptobj['BROWSER'].lower()
        print("browser",browser)
        appurl=pptobj['APPURL']
        print('appurl',appurl)
        
        ito=pptobj['IMPLICIT_TIME_OUT']
        print('ito',ito)
        
        eto=pptobj['EXPLICIT_TIME_OUT']
        print('eto',eto)
        
        if usergrid=='yes':
            print("Executing in remote system")
            if browser=='chrome':
                print("Open chrome browser")
                options = Options()
                self.driver = webdriver.Remote(command_executor=gridurl, options=options)
                
        else:
            if browser=='chrome':
                print("Open chrome browser")
                self.driver=webdriver.Chrome()
                
            elif browser=='firefox':
                print("Open firefox browser")
                self.driver=webdriver.Firefox()
                
            else:
                print("Open edge browser")
                self.driver=webdriver.Edge()
        print("Enter the URL",appurl)   
        self.driver.get(appurl)
        print("maximize the browser")
        self.driver.maximize_window()
        print("Set ito",ito,"seconds")
        self.driver.implicitly_wait(ito)
        print("Set eto",eto,"seconds")
        self.wait=WebDriverWait(self.driver,eto)
        
    
    @pytest.fixture(autouse=True)
    def postcondition(self):
        yield
        print("Close the browser")
        self.driver.quit()