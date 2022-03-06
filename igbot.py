from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        firefoxProfile = webdriver.FirefoxProfile()
        firefoxProfile.set_preference("intl.accept_languages", "pt,pt-BR")
        firefoxProfile.set_preference("dom.webnotifications.enabled", False)
        self.driver = webdriver.Firefox(
            firefox_profile=firefoxProfile, executable_path='C:\\Users\\55859\\Downloads\\geckodriver.exe'
        )


    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")       

        time.sleep(5)
        campo_user = driver.find_element_by_xpath("//input[@name='username']")
        campo_user.click()
        campo_user.clear()
        campo_user.send_keys(self.username)
        campo_pass = driver.find_element_by_xpath("//input[@name='password']")
        campo_pass.click()
        campo_pass.clear()
        campo_pass.send_keys(self.password)
        campo_pass.send_keys(Keys.RETURN)
        time.sleep(4)
        agora_nao = driver.find_element_by_class_name("cmbtv")
        agora_nao.click()
        time.sleep(2)
        self.comente_nas_fotos_com_a_hashtag('tumblr')

    @staticmethod
    def type_like_a_person(sentence, single_input_field):
        """ Este código irá basicamente permitir que você simule a digitação como uma pessoa """
        print("Comentando...")
        for letter in sentence:
            single_input_field.send_keys(letter)
            time.sleep(random.randint(1, 5) / 30)

    def comente_nas_fotos_com_a_hashtag(self, hashtag):
        links_de_posts = []
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(5)

        # Altere o segundo valor aqui para que ele desça a quantidade de páginas que você quiser: quer que ele desça 5 páginas então você deve alterar de range(1,3) para range(1,5)
        for i in range(1, 3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
        
        hrefs = driver.find_elements_by_tag_name("a")
        pic_hrefs = [elem.get_attribute("href") for elem in hrefs]
        print(hashtag + " fotos: " + str(len(pic_hrefs)))
        
        for link in pic_hrefs:
            try:
                if link.index("/p/") != -1:
                    links_de_posts.append(link)
            except:
                pass

        for pic_href in links_de_posts:
            driver.get(pic_href)
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            try:
                comments = [
                    "Massa!!", "Curti!!😉", "Foda!😎",
                    "Bacana!!😉", "😎"
                ]  # Remova esses comentários e insira os seus comentários aqui

                driver.find_element_by_class_name("Ypffh").click()
                comment_input_box = driver.find_element_by_class_name("Ypffh")
                time.sleep(random.randint(2, 5))
                self.type_like_a_person(random.choice(comments), comment_input_box)
                time.sleep(random.randint(3, 5))

                driver.find_element_by_xpath("//button[contains(text(), 'Publicar')]").click()
                time.sleep(random.randint(30, 100))

            except Exception as e:
                print(e)
                time.sleep(5)

oliverBot = InstagramBot("username", "password")
oliverBot.login()