'''
@FileName:商城价格修改

@Author：毛向官

@Create date:2018-7-19

@description：数量太多，重复操作，脚本操作

@version：蛆蛆帆1.0
'''


from selenium import webdriver
from time import sleep
import config


class Instantiation():
    def __init__(self):
        # 实行登录操作
        self.Boswer = webdriver.Chrome()
        self.Boswer.set_window_size(1920,1000)
        self.Boswer.get("http://yxadmin.hoshiibuy.com/admin/")
        username = self.Boswer.find_element_by_name("account")
        pwd = self.Boswer.find_element_by_name("password")
        username.send_keys("18558728101")
        pwd.send_keys("zhuni123456")
        login = self.Boswer.find_element_by_class_name("m-b")
        login.click()
        self.change_price()

    # 进入商品列表
    def change_price(self):
        for everyCommodity in config.Array[1:]:
            sleep(1)
            self.Boswer.get("http://yxadmin.hoshiibuy.com/admin/product/go/list-product")
            search_info = self.Boswer.find_element_by_name("serial")
            Commodity_coding, ori_price, price, Taxation, profit, senior, Blue, red = everyCommodity
            search_info.clear()
            search_info.send_keys(Commodity_coding)
            sleep(2)  #网页反应不过来，设置2S间隔
            search_btn = self.Boswer.find_element_by_class_name("glyphicon-search")
            search_btn.click()
            table = self.Boswer.find_element_by_id("tables")
            table_rows = table.find_elements_by_tag_name("tr")
            print(len(table_rows))
            table_cols = table_rows[0].find_elements_by_tag_name('th')
            print("总列数:", len(table_cols))
            btn2 = table.find_element_by_xpath("//*[@id='tables']/tbody/tr/td[13]/button[1]")
            # 供应商推荐奖修改
            self.change_supplier(senior, Blue, red)
            # print(btn2.get_attribute("data-url"))
            # 获取商品ID，直接访问页面
            # http://yxadmin.hoshiibuy.com/admin/product/go/edit-product?id=3423
            # "//*[@id="submitForm"]/div/div[2]/div[40]/div/button[1]"
            # 进行商品页面信息修改
            url = "http://yxadmin.hoshiibuy.com/" + btn2.get_attribute("data-url")
            self.change_info(url, ori_price, price, profit, Taxation)

    def change_supplier(self, seniors, Blues, reds):
        btn4 = self.Boswer.find_element_by_xpath("//*[@id='tables']/tbody/tr/td[13]/button[8]")
        btn4.click()
        senior = self.Boswer.find_element_by_xpath("//*[@id='add-supplier-modal']/div/div/div[1]/div[4]/div/input")
        Blue = self.Boswer.find_element_by_xpath("//*[@id='add-supplier-modal']/div/div/div[1]/div[5]/div/input")
        red = self.Boswer.find_element_by_xpath("//*[@id='add-supplier-modal']/div/div/div[1]/div[6]/div/input")
        purple = self.Boswer.find_element_by_xpath("//*[@id='add-supplier-modal']/div/div/div[1]/div[7]/div/input")
        black = self.Boswer.find_element_by_xpath("//*[@id='add-supplier-modal']/div/div/div[1]/div[8]/div/input")
        # 清楚输入框信息
        senior.clear()
        Blue.clear()
        red.clear()
        purple.clear()
        black.clear()
        # 输入供应商推荐奖
        senior.send_keys(seniors)
        Blue.send_keys(Blues)
        red.send_keys(reds)
        purple.send_keys(reds)
        black.send_keys(reds)
        # 保存操作
        save_btn = self.Boswer.find_element_by_xpath("//*[@id='add-product-submit-btn']")
        save_btn.click()

    def change_info(self, url, ori_prices, price, profit, Taxation):
        self.Boswer.get(url)
        sleep(1)
        # 划线价
        ori_price = self.Boswer.find_element_by_xpath("//*[@id='submitForm']/div/div[2]/div[6]/div[2]/input")
        ori_price.clear()
        ori_price.send_keys(ori_prices)
        # 销售价
        sale_price = self.Boswer.find_element_by_xpath("//*[@id='submitForm']/div/div[2]/div[8]/div[1]/input")
        sale_price.clear()
        sale_price.send_keys(price)
        # 税费
        rateFee = self.Boswer.find_element_by_xpath("//*[@id='submitForm']/div/div[2]/div[10]/div/input")
        rateFee.clear()
        rateFee.send_keys(Taxation)
        # 利润
        profits = self.Boswer.find_element_by_xpath("//*[@id='submitForm']/div/div[2]/div[8]/div[2]/input")
        profits.clear()
        profits.send_keys(profit)
        # 保存操作
        btn3 = self.Boswer.find_element_by_xpath("//*[@id='submitForm']/div/div[2]/div[40]/div/button[1]")
        btn3.click()
        sleep(1)


if __name__ == "__main__":
    Instantiation()
