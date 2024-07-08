string = ['B','a','a','b','b','c','c','B']

def left():
    global index
    index -= 1
    return index

def right():
    global index
    index += 1
    return index

def print_state(state):
    print(f"State: {state}, String: {string}, Index: {index}")

def q1():
    global index
    print_state('q1')
    if string[index] == 'a':
        string[index] = 'X'
        right()
        q2()
    elif string[index] == 'Y':
        right()
        q5()

def q2():
    global index
    print_state('q2')
    if string[index] == 'a':
        right()
        q2()
    elif string[index] == 'Y':
        right()
        q2()
    elif string[index] == 'b':
        string[index] = 'Y'
        right()
        q3()

def q3():
    global index
    print_state('q3')
    if string[index] == 'Z':
        right()
        q3()
    elif string[index] == 'b':
        right()
        q3()
    elif string[index] == 'c':
        string[index] = 'Z'
        left()
        q4()

def q4():
    global index
    print_state('q4')
    if string[index] == 'Z':
        left()
        q4()
    elif string[index] == 'Y':
        left()
        q4()
    elif string[index] == 'a':
        left()
        q4()
    elif string[index] == 'b':
        left()
        q4()
    elif string[index] == 'X':
        right()
        q1()

def q5():
    global index
    print_state('q5')
    if string[index] == 'Z':
        right()
        q6()

def q6():
    global index
    print_state('q6')
    if string[index] == 'B':
        print("the input is accepted by the turing machine")
        return

if __name__ == "__main__":
    global index
    index = 1  
    q1()
