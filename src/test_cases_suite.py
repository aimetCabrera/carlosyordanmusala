import json
import unittest
import time
import pytesseract
import cv2
import HtmlTestRunner
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from configTest import browser


class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = browser.__class__
        self.driver.maximize_window()
        time.sleep(1)

    def test_case_1(self):
        with open("emails.json") as json_file:
            data = json.load(json_file)

            for e in data["wrong_emails"]:
                self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
                cookies_accept = self.driver.find_element(By.ID, "wt-cli-accept-all-btn")
                cookies_accept.click()
                contact_btn = self.driver.find_element(By.CLASS_NAME, "contact-label btn btn-1b")
                contact_btn.click()
                name = self.driver.find_element(By.ID, "cf-1")
                name.send_keys("NameTest1")
                mobile = self.driver.find_element(By.ID, "cf-3")
                mobile.send_keys("+5352647185")
                subject = self.driver.find_element(By.ID, "cf-4")
                subject.send_keys("SubjectTest1")
                message = self.driver.find_element(By.ID, "cf-5")
                message.send_keys("Message Test 1")
                email = self.driver.find_element(By.ID, "cf-2")
                email.send_keys(e["email"])
                captcha = self.driver.find_element(By.ID, "siwp_captcha_image_0")
                image = cv2.imread(captcha)
                pytesseract.pytesseract.tesseract_cmd = "\\tools\\tesseract.exe"
                text = pytesseract.image_to_string(image)
                code = self.driver.find_element(By.ID, "siwp_captcha_value_0")
                code.send_keys(text)
                send_btn = self.driver.find_element(By.CLASS_NAME,
                                                    "wpcf7-form-control has-spinner wpcf7-submit btn-cf-submit")
                send_btn.click()
                error_msg = self.driver.find_element(By.CLASS_NAME, "wpcf7-not-valid-tip")
                self.assertEqual(error_msg.text, "The e-mail address entered is invalid.")
                self._case_2_test()
                self._case_3_test()
                self._joinus_page_test()
                self._case_4_test()

    def _case_2_test(self):
        time.sleep(1)
        cookies_accept = self.driver.find_element(By.ID, "wt-cli-accept-all-btn")
        cookies_accept.click()
        company_btn = self.driver.find_element(By.XPATH,
                                               "/html[1]/body[1]/header[1]/nav[2]/div[1]/div[1]/ul[1]/li[1]/a[1]")
        company_btn.click()
        company_url = self.driver.current_url
        self.assertEqual(company_url, "http://www.musala.com/company/")
        self.assertTrue(self.driver.find_element(By.CLASS_NAME, "company-members"))
        leader = self.driver.find_element(By.XPATH,
                                          "/html[1]/body[1]/main[1]/div[1]/div[1]/div[2]/section[3]/div[1]/h2[1]")
        self.assertEqual(leader.text, "Leadership")
        facebook_btn = self.driver.find_element(By.XPATH, "/html[1]/body[1]/footer[1]/div[1]/div[1]/a[4]/span[1]")
        facebook_btn.click()
        facebook_url = self.driver.current_url
        self.assertEqual(facebook_url, "http://www.facebook.com/MusalaSoft?fref=ts")
        profile_image = self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div["
                                                           "1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div["
                                                           "1]/div[1]/div[1]/div[1]/div[1]/a[1]")
        self.assertTrue(profile_image)

    def _case_3_test(self):
        time.sleep(1)
        cookies_accept = self.driver.find_element(By.ID, "wt-cli-accept-all-btn")
        cookies_accept.click()
        careers_btn = self.driver.find_element(By.XPATH, "/html[1]/body[1]/header[1]/nav[2]/div[1]/div[1]/ul[1]/li["
                                                         "5]/a[1]")
        careers_btn.click()
        posit_btn = self.driver.find_element(By.XPATH,
                                             "/html[1]/body[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div["
                                             "1]/section[1]/div[1]/a[1]/button[1]/span[1]")
        posit_btn.click()
        careers_url = self.driver.current_url
        self.assertEqual(careers_url, "http://www.musala.com/careers/join-us/")
        locations_dd = Select(self.driver.find_element(By.ID, "get_location"))
        locations_dd.select_by_value("Anywhere")
        qa_engineer = self.driver.find_element(By.XPATH, "/html[1]/body[1]/main[1]/div[1]/div[1]/section[1]/div["
                                                         "2]/article[6]/div[1]/a[1]/div[1]/div[2]/img[1]")
        qa_engineer.click()
        self.assertTrue(self.driver.find_element(By.XPATH, "/html[1]/body[1]/main[1]/div[1]/div[1]/section[1]/article["
                                                           "1]/div[1]/div[2]/div[1]/div[1]"))
        sec1 = self.driver.find_element(By.XPATH, "/html[1]/body[1]/main[1]/div[1]/div[1]/section[1]/article[1]/div["
                                                  "1]/div[2]/div[1]/div[1]/div[1]/div[2]/h2[1]")
        self.assertEqual(sec1.text, "General description")
        sec2 = self.driver.find_element(By.XPATH, "/html[1]/body[1]/main[1]/div[1]/div[1]/section[1]/article[1]/div["
                                                  "1]/div[2]/div[1]/div[1]/div[2]/div[2]/h2")
        self.assertEqual(sec2.text, "Requirements")
        sec3 = self.driver.find_element(By.XPATH, "/html[1]/body[1]/main[1]/div[1]/div[1]/section[1]/article[1]/div["
                                                  "1]/div[2]/div[1]/div[2]/div[1]/div[2]/h2")
        self.assertEqual(sec3.text, "Responsibilities")
        sec4 = self.driver.find_element(By.XPATH, "/html[1]/body[1]/main[1]/div[1]/div[1]/section[1]/article[1]/div["
                                                  "1]/div[2]/div[1]/div[2]/div[2]/div[2]/h2")
        self.assertEqual(sec4.text, "What we offer")
        apply_btn = self.driver.find_element(By.CLASS_NAME, "wpcf7-form-control wpcf7-submit btn-join-us btn-apply")
        self.assertTrue(apply_btn)
        apply_btn.click()
        with open("negative_data.json") as json_file:
            data = json.load(json_file)
            for d in data["wrong_emails"]:
                name = self.driver.find_element(By.ID, "cf-1")
                name.send_keys(d["name"])
                email = self.driver.find_element(By.ID, "cf-2")
                email.send_keys(d["email"])
                mobile = self.driver.find_element(By.ID, "cf-3")
                mobile.send_keys(d["mobile"])
                linkedin = self.driver.find_element(By.ID, "cf-5")
                linkedin.send_keys(d["linkedin"])
                message = self.driver.find_element(By.ID, "cf-6")
                message.send_keys(d["message"])
                up_cv = self.driver.find_element(By.ID, "uploadtextfield")
                up_cv.send_keys("\\tools\\myCV.pdf")
                time.sleep(5)
                check = self.driver.find_element(By.ID, "adConsentChx")
                if check.is_selected() is False:
                    check.click()
                else:
                    send_btn = self.driver.find_element(By.CLASS_NAME, "wpcf7-form-control has-spinner wpcf7-submit "
                                                                       "btn-cf-submit")
                    send_btn.click()
                if d["email"] == "invalid email" is True:
                    error_btn = self.driver.find_element(By.CLASS_NAME, "close-form")
                    error_btn.click()
                    error_msg = self.driver.find_element(By.CLASS_NAME, "/html[1]/body[1]/div[8]/div[1]/div[9]/div["
                                                                        "1]/div[1]/div[1]/form[1]/p[3]/span[1]/span["
                                                                        "2]")
                    self.assertEqual(error_msg.text, "The e-mail address entered is invalid.")
                if d["name"] == "" is True:
                    error_btn = self.driver.find_element(By.CLASS_NAME, "close-form")
                    error_btn.click()
                    error_msg = self.driver.find_element(By.CLASS_NAME, "/html[1]/body[1]/div[8]/div[1]/div[9]/div["
                                                                        "1]/div[1]/div[1]/form[1]/p[2]/span[1]/span[2]")
                    self.assertEqual(error_msg.text, "The field is required.")
                if d["mobile"] == "fffff" is True:
                    error_btn = self.driver.find_element(By.CLASS_NAME, "close-form")
                    error_btn.click()
                    error_msg = self.driver.find_element(By.CLASS_NAME, "/html[1]/body[1]/div[8]/div[1]/div[9]/div["
                                                                        "1]/div[1]/div[1]/form[1]/p[4]/span[1]/span[2]")
                    self.assertEqual(error_msg.text, "The telephone number is invalid.")

    def _case_4_test(self):
        time.sleep(1)
        cookies_accept = self.driver.find_element(By.ID, "wt-cli-accept-all-btn")
        cookies_accept.click()
        careers_btn = self.driver.find_element(By.XPATH, "/html[1]/body[1]/header[1]/nav[2]/div[1]/div[1]/ul[1]/li["
                                                         "5]/a[1]")
        careers_btn.click()
        posit_btn = self.driver.find_element(By.XPATH,
                                             "/html[1]/body[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div["
                                             "1]/section[1]/div[1]/a[1]/button[1]/span[1]")
        posit_btn.click()
        locations_dd = Select(self.driver.find_element(By.ID, "get_location"))
        locations_dd.select_by_value("Sofia")
        sofia_positions = self.driver.find_elements(By.CLASS_NAME, "card-jobsHot")
        print("Sofia")
        for sp in sofia_positions:
            pos = sp.find_element(By.CLASS_NAME, "card-jobsHot__title").text
            print("Position: " + pos)
            link = sp.find_element(By.CLASS_NAME, "card-jobsHot__link").get_dom_attribute("href")
            print("More info: " + link)

        locations_dd = Select(self.driver.find_element(By.ID, "get_location"))
        locations_dd.select_by_value("Skopje")
        sofia_positions = self.driver.find_elements(By.CLASS_NAME, "card-jobsHot")
        print("Skopje")
        for sp in sofia_positions:
            pos = sp.find_element(By.CLASS_NAME, "card-jobsHot__title").text
            print("Position: " + pos)
            link = sp.find_element(By.CLASS_NAME, "card-jobsHot__link").get_dom_attribute("href")
            print("More info: " + link)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output='\\reports'))
