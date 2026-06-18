import math
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

def prob_to_angle(probability_of_one):
    return 2 * math.asin(math.sqrt(probability_of_one))

circuit = QuantumCircuit(2, 2)

k_lane = prob_to_angle(0.05)#!
circuit.ry(k_lane, 0)

l_lane = prob_to_angle(0.50)
circuit.ry(l_lane, 1)

circuit.measure(0, 0)
circuit.measure(1, 1)

simulator = AerSimulator()
result = simulator.run(circuit, shots = 1000000).result()#-!

counts = result.get_counts()
print(f"Quantum Results: {counts}")