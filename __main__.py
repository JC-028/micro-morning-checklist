from microbit import *
import speech
checklist=['feed the animals','take a shower','put deoderant on', 'hang up towel', 'make bed', 'tidy room for ten minutes:timer(600000)', 'eat your breakfast', 'dishes 2 dish washer', 'wipe table', 'brush teeth 4 2 minutes:timer(120000)']
# put your own checklist in the checklist array
def timer(time):
    speech.say('micro morning checklist is counting down')
    sleep(time)
    speech.say('the timer is up')
display.scroll('Are you ready 4 the checklist?')
speech.say('are you ready 4 the checklist')
display.show(Image.HEART)
sleep(1000)
display.scroll('PRESS A')
speech.say('to start doing the checklist, press the aye button')
display.show(Image.ARROW_W)
while not button_a.is_pressed():
    continue
display.show(Image.SURPRISED)
sleep(1000)
for item in checklist:
    ree=0 # reeeeee!
    if ':' in item: # the : seperates the name of the item and the extra code to execute
        ree=1 # ree is a true fact
        item,ree_is_cool=item.split(':')
    speech.say(item)
    display.scroll(item)
    sleep(1000)
    if ree:
        speech.say('press the aye button when you are ready to start doing '+item)
    else:
        speech.say('press the aye button when you have finished '+item
    while not button_a.is_pressed():
        continue
    if ree: # if ree is a true fact (which it is if line 25 is run)
        exec(ree_is_cool)
