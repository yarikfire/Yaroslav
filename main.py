import requests

res_parse_list = []
response = requests.get("https://coinmarketcap.com/")
response_text = response.text
response_parse = response_text.split('<span>')
for parse_elem_1 in response_parse:
    if parse_elem_1.startswith("$"):
        for parse_elem_2 in parse_elem_1.split("</span>"):
            if parse_elem_2.startswith("$") and parse_elem_2[1].isdigit():
                res_parse_list.append(parse_elem_2)
tether_exchange_rate = res_parse_list[2]
print(tether_exchange_rate)
print("I have done it")

# import logging
#
# try:
#     class Worker:
#         progress = 0
#         money = 100000
#
#         def __init__(self, name="Yura"):
#             self.name = name
#
#         def life(self):
#             self.money -= 50000
#             self.progress += 100
#
#         def go_on_work(self):
#             self.progress += 150
#             self.money += 15000
#
#
#     class Son(Worker):
#         def __init__(self, names="Nick"):
#             self.names = names
#             super().__init__()
#             self.progress += 20
#             self.money -= 3000
#             if self.progress > self.money:
#                 raise("Sorry this can`t be True!")
#
#         def life(self):
#             print(f"{self.names} money = {self.money}")
#             print(f"{self.names} progress = {self.progress}")
#
# except:
#     print(10/0)
# logging.error("print if we have an error")
#
# nick = Son()
# nick.life()