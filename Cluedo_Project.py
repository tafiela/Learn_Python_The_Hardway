'''
Created on Apr 30, 2017

@author: Me
'''
print "\t****Welcome to Cluedo****"

def players():
    
    print "How many investigators are participating :  "
    player_count=raw_input(">>> ")
    player_count = int(player_count)

    while player_count in range(1,4): 
        
        if player_count == 1:
            pass
        elif player_count == 2:
            pass
        elif player_count == 3:
            pass 
        else:
            break 
    else:
       print "\n\n\n"
       print "\t *** ATTENTION ***"
       print "A maximum number of three players can play this game\n"
       print "\nLets try again : \n"
       players()
       
    

