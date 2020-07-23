from microbit import *
import speech
checklist=['feed the animals','take a shower','put deoderant on', 'hang up towel', 'make bed', 'tidy room for 10 minutes:timer(10)', 'eat your breakfast', 'dishes 2 dish washer', 'wipe table', 'brush teeth:timer(2)']
# put your own checklist in the checklist array
def timer(time):
    sec=time
    while sec != 0:
        sec-=1
        sleep(1000)
        display.show(str(sec),wait=False)
display.scroll('Are you ready 4 the checklist?')
speech.say('YEET')
display.show(Image.HEART)
sleep(1000)
display.scroll('PRESS A')
speech.say('to start doing the checklist, press the A button')
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
    sleep(5000)
    speech.say('press the A button when you are ready to start doing '+item)
    while not button_a.is_pressed():
        continue
    if ree: # if ree is a true fact (which it is, see line 25)
        exec(ree_is_cool)
