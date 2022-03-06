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
        user_element = driver.find_element_by_xpath("//input[@name='username']")
        user_element.clear()
        user_element.send_keys(self.username)

        time.sleep(2)
        password_element = driver.find_element_by_xpath("//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)

        time.sleep(3)
        password_element.send_keys(Keys.RETURN)

        time.sleep(5)
        agora_nao = driver.find_element_by_class_name("cmbtv")
        agora_nao.click()
        time.sleep(3)

        driver.find_element_by_xpath("//span[@class='_2dbep qNELH']").click()
        time.sleep(3)

        driver.get("https://www.instagram.com/wellington_rxz/saved/")
        time.sleep(5)

        for i in range(1, 3): driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

        driver.find_element_by_xpath("//div[@class='v1Nh3 kIKUG  _bz0w']").click()
        time.sleep(5)

        self.comente_nas_fotos_com_a_hashtag()

    @staticmethod
    def type_like_a_person(sentence, single_input_field):
        """ Este código irá basicamente permitir que você simule a digitação como uma pessoa """
        print("Digitando comentario...")
        for letter in sentence:
            single_input_field.send_keys(letter)
            time.sleep(random.randint(1,5)/30)

    def comente_nas_fotos_com_a_hashtag(self):
        a = 0
        tempo = 0
        while (1):
            ''' Aqui você coloca uma variável e atribui no valor o link do post da promoção. Por exemplo:
            # sorteio_cozinha = "https://www.instagram.com/ ......"'''
            '''sorteio_1 = "https://www.instagram.com/p/CZPKpcOta5i/"
            sorteio_2 = "https://www.instagram.com/p/CZkLAdDJwDh/"
            sorteio_3 = "https://www.instagram.com/p/CYt4VNZLUR_/"
            ##Nessa lista de sorteios, você insere todos as variáveis que você criou acima.

            sorteios = [
                ## INSIRA AQUI A VARIÁVEL COM A URL do sorteio
                sorteio_2,
                sorteio_2,
                sorteio_2
            ]
            '''
            '''
            Este random existe para que a cada execução ele pegue um sorteio diferente. 
            Para minimizar a sensação que é um robô comentando
            '''
            if tempo >= 20:
                time.sleep(400)
                print('Pausa')
                tempo = 0

            #sorteio_da_vez = random.choice(sorteios)

            driver = self.driver
            time.sleep(random.randint(4,6))
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                '''
                Dentro dessa lista comments, você insere diversos @, para que a cada comentário ele sorteie algum e nunca repita o comentário.
                Dica: Se você for em algum video do youtube que fale sobre comentar em sorteio, nos comentários terão várias pessoas dizendo: "Pode me marcar, eu não me importo"
                Pegue o @ delas e coloque nessa lista, igual o exemplo abaixo.
                Coloque bastante @, tipo uns 30, 40, 50!!
                '''
                comments = [
                    "@ingridbrito1", "@phaela_marques", "@ingrindmascena",
                    "@dressa_o", "@franciellelys", "@sasahandrade",
                    "@nataliafernandaz", "@euthaynafialho ", "@florpratu",
                    "@jessicasantos0098", "@euviiviane", "@mylly_lorenzo",
                    "@myllena_loppez", "@eumyllysouza", "@dindydantas",
                    "@Carolina_grey11", "@k.jeyci", "@nutrievanlene",
                    "@jessicayuriyamanaka", "@biannaty", "@Micaelle_azevedoo",
                    "@Dudah4328", "@isabergamasco_", "@meelmkt", "@deiseiddd5",
                    "@sandrasanttos.11", "@carlacristianemachado", "@lari__.martins",
                    "@luanaffagundes", "@paolazanerato", "@esmgpti21", "@esmgpmi",
                    "@ap_.s2", "@bell.medeiros15", "@brulayyy", "@bea.trizsantos_",
                    "@andrielly_silvaa0", "@evy__ctorres", "@morenamoratto",
                    "@gueixa97", "@planetpinkconfeccoes",
                    "@eloizasilva19", "@lariluana_", "@me_raissasilva",
                    "@_ni.andradee", "@joycevalente12", "@tomscardoso",
                    "@olliverzx"
                ]
                '''Isto é o que comentei acima. Se for o sorteio da cozinha por exemplo, então comente utilizando a variável marcar_2_pessoas'''
                '''if sorteio_da_vez == sorteio_1:
                    for i in range(3, 5):
                        driver.find_element_by_class_name("Ypffh").click()
                        comment_input_box = driver.find_element_by_class_name("Ypffh")
                        time.sleep(random.randint(1, 3))
                        if 1:
                            pessoa_1 = random.choice(comments)
                            pessoa_2 = random.choice(comments)
                            marcar_2_pessoas = pessoa_1 + " " + pessoa_2    
                        self.type_like_a_person(marcar_2_pessoas, comment_input_box)
                        print("Comentei: ", marcar_2_pessoas, " no post: ", sorteio_da_vez, "Pix 150")
                        tempo += 1
                        time.sleep(random.randint(2, 4))
                        driver.find_element_by_xpath(
                            "//button[contains(text(), 'Publicar')]"
                        ).click()
                        time.sleep(14)
                        a += 1'''
                for i in range(5, 10):
                    driver.find_element_by_class_name("Ypffh").click()
                    comment_input_box = driver.find_element_by_class_name("Ypffh")
                    time.sleep(random.randint(3, 5))
                    if 1:
                        pessoa_1 = random.choice(comments)
                        marcar_1_pessoa = pessoa_1
                    self.type_like_a_person((marcar_1_pessoa + " 💙"), comment_input_box)
                    tempo += 1
                    time.sleep(random.randint(2, 4))
                    driver.find_element_by_xpath(
                        "//button[contains(text(), 'Publicar')]"
                    ).click()
                    time.sleep(10)
                    print("Comentei: ", marcar_1_pessoa, " no post: Iphone")
                    a += 1
                '''Aqui ele te informará quantas vezes já comentou o todo, desde o momento do start do script'''
                print('Vezes comentadas: ')
                print(a)
                #A linha abaixo foi colocada a partir de uma sugestão no Youtube. Ela pode ser removida, caso você queira.
                for i in range(1, 3): driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(random.randint(50, 120)) 
                #Sugestão: Mude o trecho acima para time.sleep(60) para fazer um comentário a cada minuto e diminuir a possibilidade de ser bloqueado. 
            except Exception as e:
                print(e)
                time.sleep(5)

# Entre com o usuário e senha aqui
'''Insira abaixo seu usuário e senha do instagram
Dica amiga: Crie um instagram só para concorrer a sorteios... '''
OliverBot = InstagramBot("username", "password")
OliverBot.login()