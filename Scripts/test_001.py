import allure,pytest



class Test_01:
    @allure.step(title="这是一个登陆方法")
    def test_login(self):
        allure.attach("输入用户名","zhuyuxing1993")
        allure.attach("输入密码", "19931117q")
        print("-->test_001")
        assert 1

    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    @allure.step(title="这是一个订单方法")
    def test_order(self):
        print("-->test_order")
        assert 0
    @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    @allure.step(title="这是一个支付方法")
    def test_payfor(self):
        print("-->test_order")
        assert 0
    def test_quit(self):
        assert 0