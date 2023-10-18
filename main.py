from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
# Builder.load_file("QuizPage.kv")
# class QuizManager(ScreenManager):
#     pass
#
#
# class QuizPageApp(App):
#     def build(self):
#         return QuizManager()
#
# class LoginManager(ScreenManager):
#     pass
# class Question1Screen(Screen,BoxLayout):
#     def answer_question(self,bool):
#         if bool:
#             self.manager.current="correct"
#         else:
#             self.manager.current="correct"
# class Question2Screen(Screen):
#     def answer_question(self,text):
#         if text == "yes":
#             self.ids.test.text = "correct"
#             self.ids.test.font_size = 50
#         else:
#             self.ids.test.text = "Wrong"
#             self.ids.test.font_size = 50
# class Question3Screen(Screen):
#   pass
# class CorrectScreen(Screen):
#     def advance(self):
#         self.manager.current="question two"
# class IncorrectScreen(Screen):
#     def advance(self):
#         self.manager.current = "question two"
#
# QuizPageApp().run()

Builder.load_file("LoginPage.kv")
class LoginPageApp(App):
    def build(self):
        return LoginManager()
class LoginManager(ScreenManager):
    pass
class LoginScreen(Screen,BoxLayout):
    def welcome(self, username, password):
        if username in user_login and user_login[username] == password:
            self.manager.current = "welcome"
        else:
            self.ids.invalid.text = "INVALID CREDENTIALS"
    def newacc(self):
        self.manager.current = "new account"
class NewAccountScreen(Screen,BoxLayout):
    def register_to_login(self, new_username, new_password, reenter_new_password):
        if new_username in user_login or new_password != reenter_new_password or not self.contain_num(new_password) or not self.special_char(new_password) or not self.lower_case(new_password) or not self.upper_case(new_password):
            self.ids.error.text = "ERROR"
            self.ids.error.font_size = 50
        else:
            user_login[new_username] = new_password
            print(user_login)
            self.manager.current = "login screen"


    def contain_num(self, new_password):
        for char in new_password:
            if char in "0123456789":
                return True
        return False

    def special_char(self, new_password):
        for char in new_password:
            if char in "!@#$%^&*":
                return True
        return False
    def lower_case(self, new_password):
        for char in new_password:
            if char in "abcdefghijklmnopqrstuvwxyz":
                return True
        return False
    def upper_case(self, new_password):
        for char in new_password:
            if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                return True
        return False
class WelcomeScreen(Screen,BoxLayout):
    def advance(self):
        self.manager.current="login screen"


user_login = {"username":"password"}

LoginPageApp().run()
























