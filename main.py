from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
import difflib
import datetime
import os

# edit here
lms_username = '1234'
lms_password = '1234'


# end edit

def write(path, method, content):
    t = open(path, method, encoding="utf-8")
    t.write(content)
    t.close()


def read(path):
    t = open(path, "r", encoding="utf-8")
    content = t.read()
    t.close()
    return content


def main():
    driver = webdriver.Chrome()
    driver.get('https://lms.khu.ac.ir/login/index.php')
    driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(lms_username)
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(lms_password)
    driver.find_element(By.XPATH, '//*[@id="loginbtn"]').click()

    courses = []
    nav = driver.find_element(By.XPATH, '//*[@id="nav-drawer"]').find_elements(By.TAG_NAME, 'ul li')
    for li in nav:
        try:
            link = li.find_element(By.TAG_NAME, 'a')
            if 'course' in link.get_attribute("href"):
                courses.append((link.get_attribute('innerText').strip(), link.get_attribute("href")))
        except:
            pass

    now = str(datetime.datetime.now())
    whats_new = '''
    <html>
    <head>
    <meta charset="utf-8">
    <style>.new{color:red;}</style>
    </head>
    <body>

    <h1>lms notifier</h1>
    <h3>------ ''' + now + ''' ------</h3>
    <p>
    '''
    report = "------ " + now + " ------\n"
    for course in courses:
        filename, name, url = "sources/" + course[0] + ".txt", course[0], course[1]
        try:
            driver.get(url)
            source = ""
            for item in driver.find_elements(By.CLASS_NAME, "instancename"):
                source += item.text + "\n"

            file = Path(filename)
            if not file.is_file():
                write(filename, "w", source)
                print(name + " added")
                continue

            write("sources/temp.txt", "w", source)

            diff = difflib.ndiff(open('sources/temp.txt', encoding="utf-8").readlines(),
                                 open(filename, encoding="utf-8").readlines())
            changes = [c for c in diff if c.startswith("- ")]
            report += "تغییرات " + name + " =>\n"

            whats_new += " تغییرات " + name + " =><br><span class='new'>"
            for c in changes:
                whats_new += c + "<br>"
                report += c + "\n"
            whats_new += "</span><br><br>"
            report += "\n\n"

            write("report.txt", "a", report)
            report = ""

            write(filename, "w", source)

        except Exception as e:
            print(e)

    whats_new += "</p><br><i>by junior</i></body></html>"
    write("whats_new.html", "w", whats_new)
    driver.close()
    print("done")
    os.startfile('whats_new.html')


if __name__ == "__main__":
    main()
