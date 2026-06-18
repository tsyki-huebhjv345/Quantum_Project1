# Quantum_Project1
My first ever quantum code
# Quantum Probability Simulator

A Qiskit program simulating custom quantum state probabilities using Ry (rotation-Y) gates and the Aer simulator.

## Project Overview
This project uses IBM's Qiskit framework to manipulate the probability of measuring a qubit in the |1> state. It calculates a geometric rotation angle based on a target probability, applies that rotation to two independent qubits, and runs a high-shot simulation to verify the statistical outcomes.

The code defines two paths ("lanes") with different target probabilities:
* **k_lane**: Target probability of 0.05 (5% chance of |1>).
* **l_lane**: Target probability of 0.50 (50% chance of |1>).

---

## How It Works

### 1. Probability to Angle Conversion
The Ry(theta) gate rotates a qubit starting from the |0> state around the Y-axis. The probability of measuring the state |1> is the square of its amplitude:
* P(1) = sin(theta / 2)^2

To find the required angle for a desired probability, the code reverses this equation:
* theta = 2 * arcsin(sqrt(P(1)))

### 2. Quantum Circuit Workflow
1. **Initialization**: Creates a circuit with 2 qubits and 2 classical bits.
2. **State Preparation**: Applies the calculated Ry rotation angles individually to Qubit 0 and Qubit 1.
3. **Measurement**: Measures the quantum states and stores the results in the classical bits.
4. **Simulation**: Executes the circuit 1,000,000 times using AerSimulator to gather precise statistical data.

---

## Prerequisites & Installation

Install the required packages via pip:
```bash
pip install qiskit qiskit-aer
```

---

## How to Run

1. Save the code into a file named `quantum_lanes.py`.
2. Execute the script in your terminal:
```bash
python quantum_lanes.py
```

---

## Expected Output

The simulator outputs a dictionary containing the frequency of each measured binary state. Because measurements are read from right-to-left (Qubit 1 to Qubit 0), the bitstring positions correspond to "{qubit_1}{qubit_0}".

Expect results close to these distributions out of 1,000,000 shots:
* **00** (~47.5%): Both qubits resulted in 0.
* **10** (~47.5%): Qubit 1 (l_lane) is 1, Qubit 0 (k_lane) is 0.
* **01** (~2.5%): Qubit 1 (l_lane) is 0, Qubit 0 (k_lane) is 1.
* **11** (~2.5%): Both qubits resulted in 1.

