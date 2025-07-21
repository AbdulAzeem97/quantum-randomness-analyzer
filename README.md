# Quantum 3-Coin Flip Simulator (PennyLane)

This project simulates the flipping of **3 quantum coins** using the **PennyLane** quantum computing library. It uses Hadamard gates to create quantum superpositions and measurements to simulate probabilistic outcomes — demonstrating **quantum randomness**.

## 💡 Motivation

Classical coins yield deterministic outcomes based on physical conditions. In contrast, quantum coin flips harness **superposition and measurement** — truly random, rooted in quantum mechanics.

This simulation helps in visualizing and analyzing the statistical nature of quantum randomness using 3 independent qubits.

---

## 🧪 How It Works

1. **Initialize 3 Qubits**: All start in the |0⟩ (Tails) state.
2. **Apply Hadamard Gates**: Each qubit becomes a superposition:  
   \|ψ⟩ = (|0⟩ + |1⟩)/√2
3. **Measure**: Collapse state to either |0⟩ or |1⟩.
4. **Interpretation**:
   - |0⟩ = Tails (T)
   - |1⟩ = Heads (H)

---

## 📊 Example Results from 1000 Simulations

| Outcome | Count |
|---------|-------|
| HHH     | ~125  |
| HHT     | ~122  |
| HTH     | ~130  |
| HTT     | ~115  |
| THH     | ~126  |
| THT     | ~120  |
| TTH     | ~128  |
| TTT     | ~134  |

> 📈 Output is visualized using matplotlib and saved as `results/coin_flip_histogram.png`

---

## 🚀 Run the Project

```bash
pip install -r requirements.txt
python quantum_three_coin_flip.py
