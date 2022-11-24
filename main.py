# # from random import random
# #
# #
# # class Student:
# #     def __init__(self, name):
# #         self.name = name
# #         self.money = 100
# #         self.gladness = 500
# #         self.progress = 0
# #     def go_study(self):
# #         print("Oh!No I will have to pay in the bus")
# #         self.money -= 10
# #         self.gladness -= 20
# #     def go_on_work_in_the_supermarket(self):
# #         print("I`m going to earn some money!!!")
# #         self.gladness += 60
# #         self.money += 100
# #         self.progress += 50
# #     def I_am_not_have_any_good_marks(self):
# #         print("I have to more study.")
# #         self.progress += 10
# #         self.gladness -= 10
# #     def I_am_not_have_enough_money(self):
# #         print("I will have to go on work!!!")
# #         self.progress += 20
# #         self.gladness += -10
# #         self.money += 500
# #     def is_alive(self):
# #         if self.progress < -0.5:
# #             self.alive == False
# #         elif self.gladness <= 0:
# #             print("Depression")
# #             self.alive == False
# #         elif self.money > 0:
# #             self.alive == True
# #
# #     def end_of_day(self):
# #         print(f"Gladness = {self.gladness}")
# #         print(f'Progress = {self.progress}')
# #         print(f'Money = {self.money}')
# #
# #     def live(self, day):
# #         day = "Day" + str(day) + "of" + self.name + "life"
# #         print(f"{day:=^50}")
# #         live_cube = random.randint(1, 4)
# #         if live_cube == 1:
# #             self.go_study()
# #         elif live_cube == 2:
# #             self.go_on_work_in_the_supermarket()
# #         elif live_cube == 3:
# #             self.I_am_not_have_any_good_marks()
# #         elif live_cube == 4:
# #             self.I_am_not_have_enough_money()
# #
# #         self.end_of_day()
# #         self.is_alive()
# # nick = Student(name="Nick")
# #
# # for day in range(366):
# #     if nick.live == False:
# #         break
# #     nick.live(day)
#
# try:
#     class Father:
#     height = 190
#     weight = 90
#     age = 40
#     def __init__(self, father = "Yaroslav"):
#         self.age = 41
#         self.weight = 95
#         self.father = father
# except:
#     class Son(Father):
#     def __init__(self, son = "Nick"):
#         self.son = son
#         super().__init__()
#         self.age -= 25
#         self.weight -= 45
#     def life(self):
#         print(f"{self.father} height = {self.height}")
#         print(f"{self.son} weight and age = {self.weight}, {self.age}")
# nick = Son()
# nick.life()
# import random as random
# class Worker:
#     def __init__(self, name):
#         self.name = name
#         self.progress = 0
#         self.money = 10000
#         self.alive = 0
#
#     def life(self):
#         self.money -= 5000
#         self.progress += 20
#
#     def get_a_job(self):
#         self.money -= 2000
#         self.progress += 50
#
#     def work_for_a_month(self):
#         self.money += 15000
#         self.progress += 100
#
#     def buy_food_every_day(self):
#         self.money -= 5000
#         self.progress += 100
#         print({self.money})
#
#     def is_alive(self):
#         if self.progress < -0.5:
#             self.alive == False
#         elif self.gladness <= 0:
#             print("Depression")
#             self.alive == False
#         elif self.money > 0:
#             self.alive == True
#
#     def end_of_day(self):
#         print(f'Progress = {self.progress}')
#         print(f'Money = {self.money}')
# class Son(Worker):
#     def __init__(self, name = "Nick"):
#         self.name = name
#         super().__init__(name)
#         self.money = 35000
#     def live(self, day):
#         day = "Day" + str(day) + "of" + self.name + "life"
#         print(f"{day:=^50}")
#         live_cube = random.randint(1, 4)
#         if live_cube == 1:
#             self.get_a_job()
#         elif live_cube == 2:
#             self.work_for_a_month()
#         elif live_cube == 3:
#             self.buy_food_every_day()
#         elif live_cube == 4:
#             self.life()
#
#         self.end_of_day()
#         self.is_alive()
# for day in range(366):
#     if nick.live == False:
#         break
#         nick.live(day)
#
# nick = Son(name="Nick")



import cv2

image_path = "cat.png"
image_do = "glasses.png"
cat_face_cascade = cv2.CascadeClassifier("haarcascade_smile.xml")
image = cv2.imread(image_path)
image_one = cv2.imread(image_do)
cat_face = cat_face_cascade.detectMultiScale(image)
mask_face = cat_face.detectMultiScale(image_one)
print(cat_face)
cv2.imshow('Cat', image, image_one)
cv2.waitKey()
