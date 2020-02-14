import re
import unittest
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver


class TestCaseDemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        # 打开被测网页
        self.driver.get("http://123.56.179.227:28080/bsams/front/login.do")
        # 最大化窗口
        self.driver.maximize_window()

    def tearDown(self):
        # 退出浏览器
        self.driver.quit()

    # 登录按钮文字-测试用例
    def test_submitText(self):
        # 定位到登录按钮文字的input标签，取出文字
        text = self.driver.find_element_by_class_name('dl-button').get_attribute("value")
        # 去除特殊字符
        reg = re.sub(r'\W+', '', text)
        self.assertEqual(reg, "登录")

    # 验证码标签文字-测试用例
    def test_vericodeText(self):
        # 定位到验证码文字的div标签，取出文字
        vertext = self.driver.find_element_by_class_name('label').text
        self.assertEqual(vertext, '验证码')

    # 忘记密码标签文字-测试用例
    def test_forgetpwText(self):
        # 定位到验证码文字的div标签，取出文字
        fptext = self.driver.find_element_by_css_selector('a[class=left]').text
        self.assertIn('忘记密码', fptext)

    # 换一张标签文字-测试用例
    def test_changeVericodeText(self):
        # 定位到验证码文字的div标签，取出文字
        cvtext = self.driver.find_element_by_css_selector('.Log_yzm > a').text
        self.assertIn('换一张', cvtext)


if __name__ == '__main__':
    suites = unittest.TestSuite()
    suites.addTest(TestCaseDemo('test_vericodeText'))
    suites.addTest(TestCaseDemo('test_submitText'))
    suites.addTest(TestCaseDemo('test_forgetpwText'))
    suites.addTest(TestCaseDemo('test_changeVericodeText'))
    # runner = unittest.TextTestRunner()
    with open('report.html', 'wb') as fp:
        runner = HTMLTestRunner(
            stream=fp, title='登录页面文字验证', description='Browser: Chrome 76, System: win10'
        )
        runner.run(suites)


