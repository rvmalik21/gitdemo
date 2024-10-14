import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
# For this to work we need to add a command line option and provide the cmdopt through a fixture function:
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )
@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome()
        driver.get("https://rahulshettyacademy.com/angularpractice/")
        driver.maximize_window()
    elif browser_name== "firefox":
        driver= webdriver.Firefox()
        driver.get("https://rahulshettyacademy.com/angularpractice/")
        driver.maximize_window()
    elif browser_name== "edge":
        edge_driver_path = "C:/Users/ravi.malik/Downloads/edgedriver_win64/msedgedriver.exe"
        # Set up Edge options
        edge_options = Options()
        edge_options.add_argument("--start-maximized")  # Optional: Start maximized
        # Initialize the Edge WebDriver
        driver = webdriver.Edge(service=Service(edge_driver_path), options=edge_options)
        # Open a URL
        driver.get("https://rahulshettyacademy.com/angularpractice/")
    request.cls.driver = driver
    #return driver  ----- This line and yield line can not be used together
    yield
    driver.close()

@pytest.fixture(scope="class")
def setupLCCM(self):
    browser_namelccm

