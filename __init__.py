from xperience import Xperience
from orquestator import Orquestator

xperience = Xperience(ini_path="C:/Users/danil/Desktop/noc/noc.ini")
token = xperience.get_authorization_token()

orquestator = Orquestator(ini_path="C:/Users/danil/Desktop/noc/noc.ini")
print(orquestator.get_process_executions())
