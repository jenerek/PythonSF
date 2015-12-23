from __future__ import division
import time
import sys
from helpers import printl as p, compare, printa
import text 
import asciifun
from decimal import Decimal 



#Arriving in SF
print ""
printa(asciifun.gol_gate)
p(text.intro)

#On to Fisherman's Wharf to a tasty Seafood Restaurant, called Merv's Mackrel and More!
printa(asciifun.mervs_place)

p(text.mervs_mack)
#Ask the user to use the print function to greet the server

answer1_bool = 0
print "Howdy folks, I'm Richie! What can I do ya for today? (Time to go? Enter x to exit)"

while answer1_bool < 3:
    time.sleep (2)
    answer1 = raw_input(">>> ")
    #answer = answer.lower()

    if answer1 == 'x':
        sys.exit(0)
    elif compare("print 'Hello richie'", answer1):
        print "Yeehaw, you've got it!"
        time.sleep (1)
        break
    else:
        print "Hm, I didn't quite catch that... Try again!"
        answer1_bool += 1

if (answer1_bool >= 3):
    print "Here's how you write this print statement: print 'Hello Richie' or print \"Hello Richie\" better luck on the next one!"


p(text.after_print)
#Short text defining strings

p(text.learn_float)
#Text for menu, explains floats, and leads to float question below
answer2_bool = 0

while answer2_bool < 4:
    time.sleep(2)
    answer2 = raw_input(">>> ").lower()

    if answer2 == 'x':
        sys.exit(0)
    elif compare("print 'crab, clams, pink'", answer2):
        print "Great job, fast learner!"
        time.sleep (1)
        break
    else:
        print "Hm, not quite, remember they have to be in the order Richie gave you (scroll up for a hint!)"
        answer2_bool += 1

if (answer2_bool >= 4):
    time.sleep(2)
    print "The floats are the items with decimal places! So you would write: print 'crab, clams, pink' or print \"crab, clams, pink\""
    time.sleep(2) 
    
    print "You'll get it next time!"
        
p(text.learn_int)
## Function to learn Integer
answer3_bool = 0

while answer3_bool < 4:
    time.sleep(2)
    answer3 = raw_input(">>> ").lower()

    if answer3 == 'x':
        sys.exit(0)
    elif compare("print 'oyst, mack, sweet'", answer3):
        print "By George, I think you've got it! Let's move on."
        time.sleep (1)
        break
    else:
        print "Hm, not quite, remember they have to be in the order Richie gave you (scroll up for a hint!)"
        answer3_bool += 1

if (answer3_bool >= 4):
    print "The integers are the items which have whole numbers for prices! So you would write: print 'oyst, mack, sweet' or print \"oyst, mack, sweet\""
    time.sleep(2) 
    print "Ok, let's keep going!"

p(text.order_food)
print "What should we get? You can tell me, so no printing or quotes necessary, enter one item at a time!"

food_choices = {"crab": 13.60, "clams": 12.30, "oyst": 15, "mack": 11, "pink": 2.50, "sweet": 3}
order = {}

while len(order.keys()) < 4:
    item = raw_input(">>> ").lower().strip()
    if item in food_choices:
        order[item] = food_choices[item]
    else:
        print("Whoops! Make sure to choose an item from the menu, you only need the nickname!")
        
order_items = ", ".join([str(x) for x in order.keys()])
order_total = float(sum(order.values()))
y = Decimal(order_total)
prop_total = round(y, 2)

time.sleep(1)

def food_bill():    
    p(["Yum, great choices, you! I'm starving so I'll go flag down Richie and give him our order!"])
    p("\n\nRichie here, glad to hear you're ready to eat! I'll give Merv your order of {}, it will be out soon!".format(order_items).split("\n"))
   
    # Money talks
    p(["A couple minutes go by...", "You chat with Py about rising housing prices..."])
    p(asciifun.expense_sf_talk, False)
    
    #Angry Cloud Ascii
    p(["and the unusually angry weather patterns..."])
    p(asciifun.rain_sf_talk, False)
    p(["Until..."])

    #Richie returns
    p(["Richie returns with food! Yay!"])
    p("\n\nHey ya'll! Here's your grub, and here's your check! Today's total will be ${}. Enjoy the rest of your SF Adventure!".format(prop_total).split("\n"))
food_bill()  
   
#Bool lesson
p(text.bool_bill)

tote_cash = raw_input(">>> ")

p(["Second: How much money did we spend? (hint: only enter a float)"])

final_bill = raw_input(">>> ")
remaining_cash = int(tote_cash) - float(final_bill)
percent_tip = float(remaining_cash)/float(final_bill)

if percent_tip >= .018:
    print "Nice tip! Our tip is 18% or more so our Boolean value of our tip is True! Now off to Dolores Park!"
    printa(asciifun.run_away)
else:
    print "OH NO, crappy tippers! We ate too much and our tip is less than 18%, so our Booleaon value is 'False'. Run to Dolores Park!"
    printa(asciifun.run_away)
