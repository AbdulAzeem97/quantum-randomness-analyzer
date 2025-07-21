# Quantum Coin Toss Simulator

This project simulates a fair coin toss using quantum computing principles via the PennyLane library. It demonstrates quantum superposition and measurement, making it suitable for those beginning with quantum computing.

## Project Overview

The simulator uses a single qubit to show how a quantum system can mimic the randomness of a coin toss. The qubit is placed in a superposition state using a Hadamard gate and then measured, collapsing the state into either |0⟩ (Heads) or |1⟩ (Tails).

---

## Quantum Concepts

- **Qubits**: Quantum bits that can be in state |0⟩, |1⟩, or any superposition of both.
- **Hadamard Gate**: Places the qubit into a 50/50 superposition of |0⟩ and |1⟩.
- **Measurement**: Collapses the superposition to one of the basis states (0 or 1), simulating randomness.

---

## Technologies Used

- Python 3.13
- [PennyLane](https://pennylane.ai/) (v0.42.0)
- PennyLane Lightning Simulator (backend)

---

## How to Run

### Prerequisites

- Python 3.13 installed
- PennyLane and its backends installed:
  ```bash
  pip install pennylane pennylane-lightning
  ```

### Execution

Run the following command in your terminal:

```bash
python quantum_coin_toss.py
```

---

## File Structure

```text
quantum_randomness_analyzer/
│
├── quantum_coin_toss.py       # Main script to run the coin toss
├── Quantum_Coin_Toss_Simulator_Report.pdf  # Detailed project report
└── README.md                  # This file
```

---

## Code Explanation

Below is the main part of the code with comments:

```python
import pennylane as qml
import numpy as np

# Define a quantum device with 1 wire (qubit) and 1 shot per execution
dev = qml.device("default.qubit", wires=1, shots=1)

@qml.qnode(dev)
def coin_toss():
    qml.Hadamard(wires=0)  # Apply Hadamard gate to create superposition
    return qml.sample(qml.PauliZ(wires=0))  # Measure the qubit

# Run the coin toss
result = coin_toss()

# Interpret result
print("Heads" if result == 1 else "Tails")
```

---

## Output Example

```text
Heads
```

---

## Potential Improvements

- Simulate multiple tosses
- Add probability analysis
- Visualize outcomes

---

## Author

Developed for educational purposes by Kubix Creative.