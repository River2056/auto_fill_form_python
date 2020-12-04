from app import driver


def get_by_xpath(path):
    return driver.find_element_by_xpath(path)


def get_by_id(id):
    return driver.find_element_by_id(id)


def get_by_tag_name(tag_name):
    return driver.find_element_by_tag_name(tag_name)


def click(element):
    element.click()


def send_keys(element, keys_to_send):
    element.send_keys(keys_to_send)


def wait(seconds):
    driver.implicitly_wait(seconds)