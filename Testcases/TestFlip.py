
import pytest
from Pages.GoToPriceList import GoToPriceList
from Pages.GoToPriceList import GetLowPriceInPage
from Testdata.Td import Td


#setTimeout(()=>{debugger;},3000)


@pytest.mark.usefixtures("setup")
class TestFlip():


    def test_child(self):
        g = GoToPriceList(self.driver,self.wait,self.actions)
        td=Td()
        self.fashion_xpath = td.fashion_xpath
        g.load_page(self.fashion_xpath)
        g.repeat_process(self.driver)





