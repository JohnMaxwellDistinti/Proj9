#Author: John Maxwell Distinti
#Repository Name: Proj9-3.py
#Python version 3.6.8
def readNextCharacter(string):
    if(string.find('Q') < len(string)):
        return string[string.find('Q')+1]
def swapCharacters(direction, string, replace):
    stringAsList = list(string)
    index = stringAsList.index('Q')
    joinedString = ''
    if(index < len(string)):
        if(direction == 'l' and index != 0):
            joinedString = "".join(stringAsList)
            joinedString = joinedString[:index-1] + joinedString[index] + joinedString[index-1] + joinedString[index+1:]
        elif(direction == 'r' and index != len(string)):
            if(replace != ''):
                stringAsList[index+1] = replace
            joinedString = "".join(stringAsList)
            joinedString = joinedString[:index] + joinedString[index+1] + joinedString[index] + joinedString[index+2:]
    return joinedString
def simulate(sigma,start,states,final,s):
    done = False
    #set the start state as the default state
    state = start
    s='Q'+s+' '
    while done == False:
        #Q1
        if(readNextCharacter(s) == '0' and state == 'q1'):
            s = swapCharacters('r',s,' ')
            state = 'q2'
        elif((readNextCharacter(s) == ' ' or readNextCharacter(s) == 'x') and state == 'q1'):
            state = 'q0'
            return "Rejected"
        #Q2
        if(readNextCharacter(s) == 'x' and state == 'q2'):
            s = swapCharacters('r',s,'')
            state = 'q2'
        elif(readNextCharacter(s) == ' ' and state == 'q2'):
            state = 'q6'
            return "Accepted"
        elif(readNextCharacter(s) == '0' and state == 'q2'):
            s = swapCharacters('r',s,'x')
            state = 'q3'
        #Q3
        if(readNextCharacter(s) == 'x' and state == 'q3'):
            s = swapCharacters('r',s,'')
            state = 'q3'
        elif(readNextCharacter(s) == '0' and state == 'q3'):
            s = swapCharacters('r',s,'')
            state = 'q4'
        elif(readNextCharacter(s) == ' ' and state == 'q3'):
            s = swapCharacters('l',s,'')
            state = 'q5'
        #Q4
        if(readNextCharacter(s) == 'x' and state == 'q4'):
            s = swapCharacters('r',s,'')
            state = 'q4'
        elif(readNextCharacter(s) == '0' and state == 'q4'):
            s = swapCharacters('r',s,'x')
            state = 'q3'
        elif(readNextCharacter(s) == ' ' and state == 'q4'):
            s = swapCharacters('l',s,'')
            state = 'q0'
            return "Rejected"
        #Q5
        if(readNextCharacter(s) == 'x' and state == 'q5'):
            s = swapCharacters('l',s,'')
            state = 'q5'
        elif(readNextCharacter(s) == '0' and state == 'q5'):
            s = swapCharacters('l',s,'')
            state = 'q5'
        elif(readNextCharacter(s) == ' ' and state == 'q5'):
            s = swapCharacters('r',s,'')
            state = 'q2'
    if(state in final):
        #determine accept
        return "Accepted"
    else:
        #determine reject
        return "Rejected"

#States of DFA, dictionary determines which states point to which other states based on input values
states = {'q1':{'0':'q2',' ':'q0', 'x':'q0'},'q2':{'x':'q2',' ':'q6', '0':'q3'},'q3':{'x':'q3','0':'q4',' ':'q5'}, 'q4':{'x':'q4',' ':'q0', '0':'q3'},'q5':{'0':'q5','x':'q5',' ':'q2'}, 'q0':{'0':'q0',' ':'q0', 'x':'q0'}, 'q6':{'0':'q6',' ':'q6', 'x':'q6'}}
#Transition functions of DFA
sigma = ['0', ' ', 'x', 'Q']
#Start state of DFA
start = 'q1'
#Accept states of DFA
final = ['q6']
#Entered string
string = ''
while string != 'w':
    #Continually test input for correct input, and accept or reject
    string = input("enter a string, w or CTRL-C to quit : ")
    if(string != 'quit'):
        print(string,"-->",simulate(sigma,start,states,final,string))
