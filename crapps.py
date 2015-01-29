import random

def _roll():
  min = 1
  max = 6

  r = random.randint(min,max)
  g = random.randint(min,max)

  return (r+g)

def _get_num_bets():
  while True:
      inp = raw_input("Enter number of bets to make: ")
      if inp == "":
          continue
      try:
          val = int(inp)
          break
      except ValueError:
          pass
  return val

def _get_odds(roll_value):

  if(roll_value == 4 or roll_value == 10):
    odds = 3
    payout_ratio = 2 # 2:1 payout
  elif(roll_value == 5 or roll_value == 9):
    odds = 4 # 3:2 payout
    payout_ratio = 3/2
  elif(roll_value == 6 or roll_value == 8):
    odds = 5
    payout_ratio = 6/5 #todo this is returning 1.0 and not 1.2 ... cast as float somehow
  else:
    print("invalid odds calculation")

  return(odds, payout_ratio)

STARTING_CASH = 200
PASSLINE_BET = 5

if __name__ == "__main__":
  cash = STARTING_CASH
  num_bets = _get_num_bets()
  print("starting Cash: " + str(cash))
  #iterate through number of rolls
  for i in range(0, num_bets):
    
    #Comeout Roll
    roll_value = _roll()
    print ("ComeOutRoll: "+str(i+1)+" Dice Value: "+str(roll_value))

    #comeout wins on a 7 or 11
    if (roll_value == 7 or roll_value == 11):
      cash += PASSLINE_BET
      print("+win:  "+str(PASSLINE_BET) + " from passline_bet\n    Total Cash: " +str(cash))
    #comout loses on a 2, 3, or 12
    elif (roll_value == 2 or roll_value == 3 or roll_value == 12):
      cash -= PASSLINE_BET
      print("-lose: "+str(PASSLINE_BET) + " from passline_bet\n    Total Cash: " +str(cash))
      # todo clear the bets on 4,5,6,8,9,10, but not the free odds on those 

    #otherwise the point is on
    else:
      #calculate odds and payout
      (odds, payout_ratio) = _get_odds(roll_value)
      #deduct odds
      free_odds_bet = PASSLINE_BET*odds
      print("bet "+str(free_odds_bet) + " on free odds\n    Total Cash: " +str(cash-free_odds_bet))
      point_roll = roll_value
      done = False
      while(not done):
        roll_value = _roll()
        print ("Roll Value: "+str(roll_value))

        if roll_value == point_roll:
          #passline pays 1:1, free odds pays the ratio
          winnings = PASSLINE_BET+free_odds_bet*payout_ratio
          cash += winnings
          print("+win:  "+str(winnings) + " from point roll - (" + str(PASSLINE_BET) + ")+(" +str(payout_ratio*free_odds_bet)+")\n    Total Cash: " +str(cash))
          done = True;
        elif roll_value == 7:
          losses = PASSLINE_BET+free_odds_bet
          cash -= losses
          print("-lose: "+str(losses) + " from seven out\n    Total Cash: " +str(cash))
          done = True
        else:
          done = False
          #todo add in come bets
