import random

catMoji =['🐱','🐈','🐈‍⬛','😹','😻','🙀','😿','😸','😺','😾','😼']
emoji = random.choice(catMoji)

def meow():
    print(emoji)

while emoji != catMoji[3]:
    emoji = random.choice(catMoji)
    meow()