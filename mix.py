import random
stone = ["SI1", "SI2", "SI3", "SI4", "SI5", "SI6", "SI7", "SI8", 
         "SI9", "SI10", "SI11", "SI12", "SI13",
         "MA1", "MA2", "MA3", "MA4", "MA5", "MA6", "MA7", "MA8",
         "MA9", "MA10", "MA11", "MA12", "MA13",
         "KI1", "KI2", "KI3", "KI4", "KI5", "KI6", "KI7", "KI8",
         "KI9", "KI10", "KI11", "KI12", "KI13",
         "SA1", "SA2", "SA3", "SA4", "SA5", "SA6", "SA7", "SA8",
         "SA9", "SA10", "SA11", "SA12", "SA13",
         "SAH1", "SAH2"]
def mix():
    test = random.choice(stone[0:-2])
    joker = test
    if test.endswith("13") is True:
        test = test.replace("13", "1")
    else:
        test = "{}{}".format(test[0:2],
        int(test[2:])+1)
    fakestone = test
    stones = random.sample(stone, len(stone))
    return {"joker":joker, 
            "fakestone":fakestone,
            "stones": stones}

table = mix()

print table