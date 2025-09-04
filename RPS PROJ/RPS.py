count = 0

# Defeating Strategies for each bot

# Quincy follows a fixed 5-move cycle. We track it and play the winning response

def quincy():

    global count
    q = ['R', 'R', 'P', 'P', 'S']
    counter = {'R': 'P', 'P': 'S', 'S': 'R'}
    index = count % len(q)
    predicted_move = q[index]
    guess = counter[predicted_move]
    return guess

# Abbey uses a simple 2-move Markov chain. We predict her next move based on frequency

def abbey(my_history,play_order =
          [{"RR": 0,
            "RP": 0,
            "RS": 0,
            "PR": 0,
            "PP": 0,
            "PS": 0,
            "SR": 0,
            "SP": 0,
            "SS": 0,
          }]):
    
    counter = {'R': 'P', 'P': 'S', 'S': 'R'}
    last_two = "".join(my_history[-2:])
    if last_two in play_order[0]:
        play_order[0][last_two] += 1

    rm = last_two[-1]
    pot_mov = [
        rm + 'R',
        rm  + 'P',
        rm + 'S'
    ]
    maximum = -1
    key = pot_mov[0]
    for i in pot_mov:
        if play_order[0][i] > maximum:
            maximum = play_order[0][i]
            key = i
    pred = key[-1]
    abguess = counter[pred]
    guess = counter[abguess]
    return guess

# Kris always plays the counter to our previous move. We counter that

def kris(my_history=[]):
    counter = {'R': 'P', 'P': 'S', 'S': 'R'}
    rm = my_history[-1]
    pred = counter[rm]
    guess = counter[pred]
    return guess

# Mrugesh predicts our most frequent move in the last 10 turns. So we counter his counter

def mrugesh(my_history):

    counter = {'R': 'P', 'P': 'S', 'S': 'R'}
    last_ten = my_history[-10:]
    
    pred = max(set(last_ten), key=last_ten.count)
    if pred == '':
       pred = 'S'
       
    mguess = counter[pred]
    guess = counter[mguess]
    return guess


# Main Player Logic

def player(prev_play="", opponent_history=[], bot=[], my_history=[]):
    global count
    opponent_history.append(prev_play)

    guess = "R"

    count = len(opponent_history)

    # Reset all histories after 1000 rounds (of each bot)

    if count == 1001:
      opponent_history.clear()
      opponent_history.append(prev_play)
      bot.clear()
      bot.append('')
      my_history.clear()

    # Identify which bot is being played by testing moves in the first 3 rounds
    
    if count <= 4:

      if count == 1:
        my_history.append("R")
        return "R"
      elif count == 2:
        my_history.append("P")
        return "P"
      elif count == 3:
        my_history.append("S")
        return "S"
      else:              
        o_mov = "".join(opponent_history[-3:])
        poss_op = {"RPP": "quincy", "PPP": "abbey", "PPS": "kris"}
        if o_mov in poss_op:
           op = poss_op[o_mov]
        else:
           op = 'mrugesh'
        bot.append(op)

    if bot[-1] == 'quincy':
       guess = quincy()

    elif bot[-1] == 'abbey':
       guess = abbey(my_history)

    elif bot[-1] == 'kris':
       guess = kris(my_history)

    elif bot[-1] == 'mrugesh':
       guess = mrugesh(my_history)

    my_history.append(guess)
    return guess