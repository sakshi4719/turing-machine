# Turing Machine Simulation

This Python script simulates a basic Turing Machine that processes a given string. The Turing Machine operates on a tape represented by a list of characters, performing read, write, and movement operations based on its current state.

## **Purpose**
The Turing Machine is designed to accept or reject a string of characters based on the following rules:
1. It processes a sequence of 'a', 'b', and 'c' characters.
2. It replaces 'a' with 'X', 'b' with 'Y', and 'c' with 'Z' as it traverses the string.
3. The machine accepts the input if it satisfies the conditions encoded in its states and transitions.

## **Components of the Turing Machine**

### **1. Tape**
The tape is represented as a Python list:

- 'B' represents the boundary marker.
- The characters 'a', 'b', and 'c' are the input symbols.
- The machine modifies the tape during processing.

### **2. Pointer**
The pointer (`index`) indicates the current position of the machine on the tape.

### **3. States**
The Turing Machine has several states implemented as Python functions:
- `q1()`: The initial state that begins processing.
- `q2()`: Handles 'a' and transitions based on 'b' or 'Y'.
- `q3()`: Processes 'b' and transitions to handle 'c'.
- `q4()`: Moves left on the tape and returns to `q1` if conditions are met.
- `q5()`: Transitions to the final state upon encountering 'Z'.
- `q6()`: Accepts the input if the boundary 'B' is reached.

### **4. Movement Functions**
- `left()`: Moves the pointer one position to the left.
- `right()`: Moves the pointer one position to the right.

### **5. Utility Function**
- `print_state(state)`: Prints the current state, tape, and pointer position for debugging purposes.



