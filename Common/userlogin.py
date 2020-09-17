from time import sleep


class Loginuser():
    def login(self, driver):
        url = "http://192.168.3.11/system/login"
        driver.get(url)
        driver.maximize_window()
        driver.find_element_by_xpath("//input[@placeholder='请输入账号']").send_keys("admin001")
        driver.find_element_by_xpath("//input[@placeholder='请输入密码']").send_keys("a888888")
        driver.find_element_by_xpath("//span[contains(text(),'登录')]").click()
        sleep(2)



