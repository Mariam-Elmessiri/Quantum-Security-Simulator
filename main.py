import numpy as np

h_gate = (1 / np.sqrt(2)) * np.array([[1,1],
                                      [1,-1]])

def send_qubit(state_type):
    if state_type == 0:
        return np.array([1,0])
    else:
        return np.array([0,1])
    
def apply_superposition(qubit):
    return np.dot(h_gate, qubit)

def hacker_intercepts(qubit):
    probabilities = np.abs(qubit)**2
    intercepted_result = np.random.choice([0,1], p=probabilities)
    return intercepted_result

def alert_system(oridinal_stat, received_result):
    if received_result == -1:
        print("ALERT: Communication link is broken.")
    elif received_result != oridinal_stat:
        print("SECURITY ALERT: Unauthorized interception detected!")
    else:
        print("Status: Connection secure. Data integrity verified.")

my_qubit = send_qubit(0)
print(f"My_Qubit: {my_qubit}")

qubit_in_superposition = apply_superposition(my_qubit)
print(f"Qubit in superposition: {qubit_in_superposition}")

hacker_view = hacker_intercepts(qubit_in_superposition)
print(f"Hacker view: {hacker_view}")

probabilities = np.abs(qubit_in_superposition)**2
final_result = np.random.choice([0,1], p=probabilities)
print(f"Final_result: {final_result}")

alert_system(0,final_result)
