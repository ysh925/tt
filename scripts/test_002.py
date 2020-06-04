from tt.common.start_deiver import start_driver
from tt.common.po import go
import tt.pack
import yaml
from time import sleep

def p():
    with open('../Data/data.yml','r',encoding='utf-8')as f:
        a = yaml.load(f,Loader=yaml.FullLoader)
        return a['input']


class Test_001:

    def setup_class(self):
        self.driver = start_driver()
        self.po = go(self.driver).re()

    def teardown_class(self):
        self.driver.quit()

    def test_001(self):
        self.po.click_jia()
        space = p()
        sleep(1)
        self.po.input_text(tt.pack.name,space.get('name'))
        self.po.input_text(tt.pack.tel,space.get('tel'))
        self.po.click_element(tt.pack.re_keys)
        self.driver.keyevent(4)




