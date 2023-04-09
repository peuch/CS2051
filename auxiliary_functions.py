def createState(text):
    all_states = []
    #hex_message = text.encode("utf-8").hex()
    i=0
    finished=False
    while (i<len(text) and not finished):
        #finished filling previous array, still more left to message
        state = [[0 for _ in range(4)] for _ in range(4)]
        for col in range(4):
            for row in range(4):
                if (i+1<=len(text)):
                    #we haven't reached end of string yet
                    state[row][col] = ord(text[i:i+1]) #gives hex value
                    i=i+1
                else:
                    finished=True
                    break
        all_states.append(state)
    return all_states

def createText(allstates):
    text = ""
    for state in allstates:
        for c in range(4):
            for r in range(4):
                text.append(chr(state[r][c]))
    return text