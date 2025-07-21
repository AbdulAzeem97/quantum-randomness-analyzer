import pennylane as qml
import matplotlib.pyplot as plt

dev = qml.device("default.qubit", wires=1, shots=200)

@qml.qnode(dev)
def quantum_random_bit():
    qml.Hadamard(wires=0)
    return qml.sample(qml.PauliZ(0))

results = quantum_random_bit()

# Convert: +1 → 0, -1 → 1
bits = [0 if x == 1 else 1 for x in results]



from pennylane import numpy as np
import matplotlib.pyplot as plt

# Step 1: Set up the quantum device with 1 wire and 1000 shots
dev = qml.device("default.qubit", wires=1, shots=1000)

# Step 2: Define quantum circuit simulating a quantum coin toss
@qml.qnode(dev)
def quantum_coin_toss():
    qml.Hadamard(wires=0)  # Apply Hadamard to create superposition (quantum heads or tails)
    return qml.sample(qml.PauliZ(0))  # Measure in Z-basis (result will be +1 or -1)

# Step 3: Run the experiment
samples = quantum_coin_toss()

# Step 4: Convert measurements to classical coin terms
# +1 → Heads, -1 → Tails
head_count = np.count_nonzero(samples == 1)
tail_count = np.count_nonzero(samples == -1)

# Step 5: Display results
print(f"Heads: {head_count}")
print(f"Tails: {tail_count}")

# Step 6: Plot the results using matplotlib
labels = ['Heads', 'Tails']
values = [head_count, tail_count]

plt.figure(figsize=(6, 6))
plt.bar(labels, values, color=['skyblue', 'lightcoral'])
plt.title('Quantum Coin Toss Results (1000 shots)')
plt.xlabel('Outcome')
plt.ylabel('Count')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Plot   
#
plt.figure(figsize=(8, 5))
plt.hist(bits, bins=2, rwidth=0.6, color='purple')
plt.xticks([0, 1])
plt.xlabel("Random Bit")
plt.ylabel("Frequency")
plt.title("Quantum Random Bit Generator")
plt.show()
