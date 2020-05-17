from pathlib import Path
from selenium import webdriver
import difflib

# edit here
lms_username = '952013011'
lms_password = 'Fuckukhu10times!'
# end edit

driver = webdriver.Chrome()
driver.get('https://lms.khu.ac.ir/login/index.php')
driver.find_element_by_xpath('//*[@id="username"]').send_keys(lms_username)
driver.find_element_by_xpath('//*[@id="password"]').send_keys(lms_password)
driver.find_element_by_xpath('//*[@id="loginbtn"]').click()

coursesUrl = []
nav = driver.find_element_by_xpath('//*[@id="nav-drawer"]').find_elements_by_tag_name('ul li')
for li in nav:
    try:
        link = li.find_element_by_tag_name('a')
        if 'course' in link.get_attribute("href"):
            coursesUrl.append([link.text, link.get_attribute("href")])
    except:
        pass

for link in coursesUrl:
    filename, name, url = "sources/" + link[0] + ".txt", link[0], link[1]
    try:
        driver.get(url)
        source = ""
        for item in driver.find_elements_by_class_name("instancename"):
            source += item.text + "\n"

        file = Path(filename)
        if not file.is_file():
            t = open(filename, "w", encoding="utf-8")
            t.write(source)
            t.close()
            print(name + " اضافه شد")
            continue

        t = open("sources/temp.txt", "w", encoding="utf-8")
        t.write(source)
        t.close()

        f = open(filename, "r", encoding="utf-8")
        prev = f.read()
        f.close()

        diff = difflib.ndiff(open('sources/temp.txt', encoding="utf-8").readlines(), open(filename, encoding="utf-8").readlines())
        changes = [l for l in diff if l.startswith('+ ')]
        print("------"+ "تغییرات " + name + "------")
        for c in changes:
            print(c, end="")
        print()

        t = open(filename, "w", encoding="utf-8")
        t.write(source)
        t.close()

    except Exception as e:
        print(e)

driver.close()