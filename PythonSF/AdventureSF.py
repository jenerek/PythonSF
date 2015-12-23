import time

#New function for dog encounter
    
def dolores_dog():

    #Arrives at Dolores Park
    print "You find yourself in Dolores Park. It's full of hippies, people drinking on the hill, and lots of dogs. As you glance around you notice a dog run towards you. He drops a ball at your feet."
    
    
    #Pause the time between story
    time.sleep(1)
    
    
    #Ask the user to use the print function to greet the man
    answer_bool = 0
    print "You reach down and pick up the ball. As you pick up the ball a man approaches."
    
    while answer_bool < 3:
        time.sleep (1)
        print "Greet the man using the print function by saying hello. (Time to go? Enter x to exit)"
        answer = raw_input(">>> ").lower()
        #answer = answer.lower()

        if answer == 'x':
            return
        elif ( answer == "print 'hello'") or (answer == 'print "hello"'):
            print "The man extends his hand to you to say hello."
            time.sleep (1)
            break
        else:
            print "Hm, that's not quite right. Try again!"
            answer_bool += 1
    
    if (answer_bool >= 3):
        print "Here's how you write a print statement: print 'hello' or print \"hello\""
    
    
    # gameplay = raw_input("Enter x to exit: ")
    # if gameplay == 'x':
    #     return
    
    time.sleep(1)
    
    #Introduce man to user    
    print "'Hi, my name is John. This is my dog Fido. In order to get him to retrieve the ball you need to assign him to a variable.'"
    time.sleep (1)
   # print "\n" 
   #line above will add large break
    
    print "Here's how you assign Fido to a variable. You'll want to make him a string called dog."
    time.sleep (1)
    
    print "You can simply write: Fido = 'dog' or Fido = \"dog\"."
    time.sleep (1)
    
    print "Just remember that capitalization matters!"
    time.sleep (1)
    
    #Create a counter
    dog_count = 0
    
    #Assign Fido to a variable
    while dog_count < 3:
        time.sleep (1)
        print "Assign Fido to a variable. (Time to go? Enter x to exit)"
        dog_answer = raw_input(">>> ")
    
        if dog_answer == 'x':
            return
        elif ( dog_answer == "Fido = 'dog'") or (dog_answer == 'Fido = "dog"'):
            print "Fido wags his tail at you and barks."
            time.sleep (1)
            break
        else:
            print "Hm, that's not quite right. Try again!"
            dog_count += 1
    
    if (dog_count >= 3):
        print "Here's how you assign Fido to a variable: Fido = 'dog' or Fido = \"dog\" ."
    
    time.sleep(1)
    
    print "You pick up the ball and throw it. Fido races after it and brings it back to you."
    time.sleep(1)
    
dolores_dog()


# New function for rum guy

def dolores_rum ():
    
    print "You say goodbye to leave John and Fido and walk up the hill. On your way you encounter a man selling coconuts filled with rum."
    rum_count = 0
    
    while rum_count < 3:
        time.sleep (1)
        print "Greet the man using the print function by saying hello. (Time to go? Enter x to exit)"
        rum_answer = raw_input(">>> ").lower()
        #rum_answer = rum_answer.lower()

        if rum_answer == 'x':
            return
        elif ( rum_answer == "print 'hello'") or (rum_answer == 'print "hello"'):
            print "The man turns to you and asks if you'd like to buy some rum in a coconut."
            time.sleep (1)
            break
        else:
            print "Hm, that's not quite right. Try again!"
            rum_count += 1
    
    if (rum_count >= 3):
        print "Here's how you write a print statement: print 'hello' or print \"hello\""
        
    time.sleep(1)
    
        
    print "You decide to try and buy a drink. How much do you want to give him? (enter an integer with no $)"
    counting = float (raw_input (">>>"))
        
    def make_a_deal (rum):
        total = counting - rum
        if (counting >= rum):
            print "He looks at you and agrees. You hand him $%.2f and he gives you $%.2f back. You now have a delicious rum and coconut in your hand." %(counting, total)
        else:
            print "He looks at you and says 'Sorry, that's a bit too low for me.' He then turns and walks to the guy lounging on the grass next to you."
            
    make_a_deal(7.50)
    
    time.sleep(1)
                
dolores_rum()


# Head to a taqueria to get dinner

def taqueria ():
    print "At this point lunch is a distant memory and you're hungry. You head to a taqueria to buy a burrito."
    time.sleep(1)
    
    def type_check():
       
        burrito_count = 0
        #print "You arrive at the taqueria and decide to order a burrito."
        
        while burrito_count < 3:
            time.sleep (1)
            print "The burrito cost $7.50, to calculate the cost would you use a float or integer (int)? (Time to go? Enter x to exit)"
            burrito_answer = raw_input(">>> ").lower()
            #burrito_answer = burrito_answer.lower()
            
            if burrito_answer == 'x':
                return
            elif ( burrito_answer == "float"):
                print "Great, you're ready to buy a burrito!"
                time.sleep (1)
                break
            else:
                print "Hm, that's not quite right. Try again!"
                burrito_count += 1
    
            if (burrito_count >= 3):
                print "Since there's a decimal place you'll need to use a float. Integers are whole numbers!"
        
        time.sleep(1)
        
    type_check()
    
    def buy_burrito():
            
        burrito_order = [] 
        maxLengthList = 5
        print "Enter up to 5 ingredients for your burrito. Make sure to hit enter after each item! If you want less then 5 items enter space then return to stop your list."
        while len(burrito_order) < maxLengthList:
            item = str(raw_input(">>> "))
            burrito_order.append(item)
            if item == ' ':
                break
        print "You sit down to enjoy your burrito of: " + ", ".join(burrito_order) + " and think about the amazing day you've had."
            
    buy_burrito()
        
    
taqueria()