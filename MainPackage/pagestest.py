'''
Created on May 21, 2018

@author: aranjan
'''
from ResourcePackage import locaterstest
from ResourcePackage.locaterstest import Locaters
from MainPackage.testtestcase import testcase1
class Manpage(testcase1):
    def dropDown(self):
        elm=driver.find_element(*Locaters.DropDown)