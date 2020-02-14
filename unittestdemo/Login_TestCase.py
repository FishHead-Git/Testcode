import unittest
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from ddt import ddt, data, unpack


@ddt
class LoginTestCaseDemo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        # 打开被测网页
        cls.driver.get("http://123.56.179.227:28080/bsams/front/login.do")
        # 最大化窗口
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        driver = self.driver
        driver.find_element_by_id('taskId').clear()
        driver.find_element_by_id('loginName').clear()
        driver.find_element_by_id('password').clear()
        driver.find_element_by_id('vericode').clear()

    @data(
        ('', 'zcgl', 'zcgl', 'asdf', '请输入任务ID'),
        ('6', '', '', 'asdf', '请输入用户名'),
        ('6', 'zcgl', '', 'asdf', '请输入密码'),
        ('6', 'zcgl', 'zcgl', '', '请输入验证码！')
    )
    @unpack
    def test_loginfunc(self, taskId, loginName, password, vericode, msg):
        driver = self.driver
        driver.find_element_by_id('taskId').send_keys(taskId)
        driver.find_element_by_id('loginName').send_keys(loginName)
        driver.find_element_by_id('password').send_keys(password)
        driver.find_element_by_id('vericode').send_keys(vericode)
        driver.find_element_by_class_name('dl-button').click()
        error_msg = driver.find_element_by_id('error_msg').text
        self.assertEqual(error_msg, msg, msg)


if __name__ == '__main__':
    cases = unittest.TestLoader().loadTestsFromTestCase(LoginTestCaseDemo)
    suites = unittest.TestSuite([cases])
    with open('Login_report.html', 'wb') as fp:
        runner = HTMLTestRunner(
            stream=fp, title='登录功能验证', description='Browser: Chrome 76, System: win10'
        )
        runner.run(suites)
    # runner = unittest.TextTestRunner()
    # runner.run(suites)
    # unittest.main(verbosity=2)

