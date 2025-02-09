import pytest

from PageObjects.LoginPage import LoginClass
from Utilities import ExcelMethods
from Utilities.Logger import LoggenClass
from Utilities.ReadConfigFile import ReadConfig


@pytest.mark.usefixtures
class Test_UserLogin:
    log = LoggenClass.log_generator()
    Excel_File_Path = "C:\\Users\\91992\\PycharmProjects\\OHRM_101\\Testcases\\TestData\\Test_Data_01.xlsx"

    # username = ReadConfig.GetUsername()
    # password = ReadConfig.GetPassword()

    def test_VerifyUrl_001(self, setup):
        self.log.info("We have started executing testcase test_VerifyUrl_001.")
        self.driver = setup

        if self.driver.title == "OrangeHRM":
            self.log.info("we have verified url by page title.")
            assert True
        else:
            assert False

    def test_Login_002(self, setup):
        self.driver = setup
        self.lp = LoginClass(self.driver)
        self.rows = ExcelMethods.numRow(self.Excel_File_Path, 'LoginData')

        Status_List = []

        for r in range(2, self.rows + 1):
            self.username = ExcelMethods.readData(self.Excel_File_Path, 'LoginData', r, 2)
            self.password = ExcelMethods.readData(self.Excel_File_Path, 'LoginData', r, 3)
            self.Expected_Result = ExcelMethods.readData(self.Excel_File_Path, 'LoginData', r, 4)

            self.lp.Enter_Username(self.username)
            self.lp.Enter_Password(self.password)
            self.lp.Click_LoginBtn()

            if self.lp.VerifyLogin_Status() == "Login Pass":
                ExcelMethods.writeData(self.Excel_File_Path, 'LoginData', r, 5, "Pass")
                if self.Expected_Result == "Pass":
                    Status_List.append("Pass")
                else:
                    Status_List.append("Fail")
                self.lp.Click_LogoutOptionBtn()
                self.lp.Click_LogoutBtn()
            else:
                ExcelMethods.writeData(self.Excel_File_Path, 'LoginData', r, 5, "Fail")
                if self.Expected_Result == "Fail":
                    ExcelMethods.writeData(self.Excel_File_Path, 'LoginData', r, 6, "TestCase Pass")
                    Status_List.append("Pass")
                else:
                    ExcelMethods.writeData(self.Excel_File_Path, 'LoginData', r, 6, "TestCase Fail")
                    Status_List.append("Fail")

        if "Fail" in Status_List:
            assert False
        else:
            assert True
