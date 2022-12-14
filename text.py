"""
В классе Text мы храним все тексты которые будем использовать
чтобы не перегружать интерфейс кода в main
"""


class Text():
    start = """ Рады приветствовать вас, юный господин
Тут вы можете создать свою уникальную деревню
с крутыми жителями и будущим развитием"""

    new_village = """ Господин поздравляю вам выделили 10 соток земли

Как назвать вашу деревню?
"""

    def stat(self,data):
        out = ""
        out += str(data["name"]) + "  -  " + str(data["lvl"]) +" уровень\n\n"
        out += "Золото: " + str(data["gold"]) + "\n"
        out += "Население: " + str(data["human"]) + "\n"
        out += "Опыт: " + str(data["exp"]) + "/" + str(data["need_exp"]) + "\n"
        return out

    def taxes(self,data):
        gold = data["human"]*data["tax"]
        out = "Вы собрали налоги: + " + str(gold) + " золота"
        return out