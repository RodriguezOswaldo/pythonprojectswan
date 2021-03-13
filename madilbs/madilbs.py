#string concatenation (aka how to put strings together)
#suppose we want to create a string that says "subscribe..."

# youtuber = 'Own Rodrig' #some stuff

# #let's try a couple ways
# print('subscribe to ' + youtuber)
# print('subscribe to {}'.format(youtuber))
# print(f'subscribe to {youtuber}')


adj = input('Adjective: ')
verb1 = input('Verb 1: ')
verb2 = input('Verb 2: ')
somebody = input('Add a famous person\'s name: ')

madlib = f"Computer Programming Mola {adj}! It makes me so excited all the time that I want to {verb1} it. Just Drink lots of water and you\'ll {verb2} Like you are {somebody}!"
print(madlib)