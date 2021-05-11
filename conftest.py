import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def browser():

    driver = webdriver.Chrome(executable_path= 'C:\\Users\\Admin\\Desktop\\gaNIMATION\\Tensor\\chromedriver\\chromedriver.exe')
    yield driver
    driver.quit()


