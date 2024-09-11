import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
@pytest.mark.usefixtures("setup")
class BaseClass:
    @property
    def getLogger(self):
        loggerName =inspect.stack()[1][3]
        logger =logging.getLogger(loggerName)
        fileHandler =logging.FileHandler('C:/Users/ravi.malik/PycharmProjects/pythonProject1/Scripts/tests/logfile.log')
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : % message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler) #fileHandler object
        logger.setLevel(logging.DEBUG)
        # logger.debug("A debug statement is here")
        # logger.info("A informtation  statement is here")
        # logger.warning("A warning statement is here")
        # logger.error("Something went wrong here")
        # logger.critical("A critical statement PLEASE BE attendtion")
        return logger
    def verifyPresence(self, text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,text)))
    def selectOptionbyText(self,locater, text):
        dropdown = Select(locater)
        dropdown.select_by_visible_text(text)
