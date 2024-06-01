import random

woman = ["a queen", "a girl", "a scientist", "a fairy"]
man = ["A police officer", "A plamber", "An engineer"]
place = ["a castle", "on Pluto"]
time = ["Once upon a time", "A million years ago", "Long time ago"]
sheWore = ["scuba diving gear", "fairy wings"]
heWore = ["a purple suit", "a shark costume", "a beach towel"]
womanSays = ["Who are you?", "Who is that?", "How many beans make five?"]
manSays = ["Its me!", "I do not know."]
consequence = ["world peace.", "chaos.", "she called police.", "they married and lived happily ever after."]
worldSaid =["Nonsense.", "Cheese is trending now!"]
print()
while True:
    print("Here is a random story:\n")
    txt = random.choice(time) + " there was " + random.choice(woman) +"."
    txt += " She lived in " + random.choice(place) +", and she wore " + random.choice(sheWore) + '.'
    print(txt)
    print()
    txt = random.choice(man) + " came to her house. He was in " + random.choice(heWore) +". He knocked up."
    print(txt)
    print()
    txt = "She said: " + random.choice(womanSays)
    print(txt)
    txt = "He said: " + random.choice(manSays)
    print(txt)
    print()
    txt = "The consequence was " + random.choice(consequence)
    print(txt)
    print()

    txt = "The moral of the story: " + random.choice(worldSaid)
    print(txt)
    print()
    input("\nPress Enter to generate a random story again")
    print()

