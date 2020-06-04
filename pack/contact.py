from tt.common.Base import Base
import tt.pack

class A(Base):

    def __init__(self,driver):
        Base.__init__(self,driver)

    def click_jia(self):
        self.click_element(tt.pack.jia)