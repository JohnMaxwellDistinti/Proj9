#Author: John Maxwell Distinti
#Repository Name: Proj9-2.py
#Python version 3.6.8

#States of DFA, dictionary determines which states point to which other states based on input values
#DFA representation of Regex expression (0*1+), as (0*1+)+ was too complicated.
states = {}
#Transition functions of DFA

#sigma = ['0','1']
sigma = []

#Start state of DFA
start = ''

#Accept states of DFA
final = []

#Entered string
string = ''

def readNextEncoding():
    f = open("proj9-2.txt", "r")
    machine = f.read().replace('\n','').split(';')
    #Remove symbols for clarity
    machine.remove('Q:')
    machine.remove('Σ:')
    machine.remove('S:')
    machine.remove('F:')
    count = 0
    #Read through the file and create our DFA by
    #filling in the turing machine parameters
    for symbol in machine:
        if(symbol != ''):
            if(count <= 4):
                states[symbol]=''
            elif(count > 4 and count <= 6):
                sigma.append(symbol)
            elif(count > 6 and count <= 7):
                start=symbol
            elif(count > 7 and count <= 9):
                final.append(symbol)
            elif(count > 9 and count <= 11):
                if(count==10):
                    states['q1'] = dict({'0':symbol})
                else:
                    states['q1']['1'] = symbol
            elif(count > 11 and count <= 13):
                if(count==12):
                    states['q2'] = dict({'0':symbol})
                else:
                    states['q2']['1'] = symbol
            elif(count > 13 and count <= 15):
                if(count==14):
                    states['q3'] = dict({'0':symbol})
                else:
                    states['q3']['1'] = symbol
            elif(count > 15 and count <= 17):
                if(count==16):
                    states['q4'] = dict({'0':symbol})
                else:
                    states['q4']['1'] = symbol
            elif(count > 17 and count <= 19):
                if(count==18):
                    states['q5'] = dict({'0':symbol})
                else:
                    states['q5']['1'] = symbol
            count=count+1
    f.close()
#Start turing machine construction of DFA
readNextEncoding()
def simulate(sigma,start,states,final,s):
    #set the start state as the default state
    state = start
    for i in s:
        if i in sigma:
            #move to a new state
            state = states[state][i]
        else:
            #go to fail state
            state = 'q5'
    if(state in final):
        #determine accept
        return "Accepted"
    else:
        #determine reject
        return "Rejected"

while string != 'w':
    #Continually test input for correct input, and accept or reject
    string = input("enter a string, w or CTRL-C to quit : ")
    if(string != 'w'):
        print(string,"-->",simulate(sigma,'q1',states,final,string))
