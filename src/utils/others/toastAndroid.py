def run():
    toastMsg = wait.until(lambda x:x.find_element_by_xpath("//android.widget.Toast[1]"))
    print(toastMsg.get_attribute("name"))