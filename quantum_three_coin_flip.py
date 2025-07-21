import pennylane as qml
import matplotlib.pyplot as plt
from collections import Counter
import numpy as np
import os

# Create a 3-qubit quantum device with multiple shots
dev = qml.device("default.qubit", wires=3, shots=1000)

@qml.qnode(dev)
def quantum_coin_flip():
    """Applies Hadamard gates to 3 qubits and returns samples of measurements."""
    for i in range(3):
        qml.Hadamard(wires=i)
    return qml.sample(qml.PauliZ(0)), qml.sample(qml.PauliZ(1)), qml.sample(qml.PauliZ(2))

def convert_to_heads_tails(measurements):
    """Convert -1 (|0⟩) to Tails and +1 (|1⟩) to Heads"""
    binary_flips = [(1 + m) // 2 for m in measurements]
    return ''.join(['H' if b == 1 else 'T' for b in binary_flips])

def run_simulation(num_runs=1000):
    """Run the quantum coin flip simulation and analyze the results."""
    print("Running quantum coin flip simulation...")
    results = quantum_coin_flip()
    flips = [convert_to_heads_tails([results[0][i], results[1][i], results[2][i]]) for i in range(num_runs)]

    counts = Counter(flips)
    print("Simulation complete.")
    for outcome, count in counts.items():
        print(f"{outcome}: {count} times")

    return counts

def plot_results(counts):
    """Plot a histogram of the results."""
    outcomes = list(counts.keys())
    frequencies = list(counts.values())

    plt.figure(figsize=(10, 6))
    bars = plt.bar(outcomes, frequencies, color='purple', edgecolor='black')
    plt.xlabel("Outcome (3 Coin Flips)")
    plt.ylabel("Frequency")
    plt.title("Distribution of 3 Quantum Coin Flips Over 1000 Runs")
    plt.grid(True, axis='y', linestyle='--', alpha=0.7)
    plt.xticks(rotation=0)
    
    # Label bars
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2.0, height, f'{int(height)}',
                 ha='center', va='bottom', fontsize=10)

    os.makedirs("results", exist_ok=True)
    plt.savefig("results/coin_flip_histogram.png")
    plt.show()

if __name__ == "__main__":
    counts = run_simulation(num_runs=1000)
    plot_results(counts)
