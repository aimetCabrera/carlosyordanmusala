import json
import pytest
import selenium.webdriver


@pytest.fixture(scope="session")
def config():
    with open('config.json') as config_file:
        config = json.load(config_file)

    assert config['browser'] in ['Firefox', 'Chrome']
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit wait'] > 0

    return config


@pytest.fixture
def browser(config):
    if config['browser'] == 'Firefox':
        brw = selenium.webdriver.Firefox(executable_path="drivers/geckodriver.exe")
    elif config['browser'] == 'Chrome':
        brw = selenium.webdriver.Chrome(executable_path="drivers/chromedriver.exe")
    else:
        raise Exception('Browser not supported')

    brw.get("http://www.musala.com/")
    brw.implicitly_wait(config['implicit_wait'])
    yield brw
