from qiskit import QuantumCircuit
from qiskit_aer import Aer
from flask import Flask, jsonify
from flask_cors import CORS
import math
from scipy.stats import chisquare

app = Flask(__name__)
CORS(app)

# -----------------------------
# Quantum Random Bit Generator
# -----------------------------
def quantum_random_bits(n_bits=256):
    backend = Aer.get_backend("qasm_simulator")

    # One circuit with n_bits qubits
    qc = QuantumCircuit(n_bits, n_bits)
    qc.h(range(n_bits))        # Apply Hadamard to all qubits
    qc.measure(range(n_bits), range(n_bits))

    # Run once with 1 shot
    job = backend.run(qc, shots=1)
    counts = job.result().get_counts()

    # Get the single measurement result (binary string)
    result_bits = list(counts.keys())[0]

    return result_bits[::-1]  # reverse, since Qiskit returns little-endian


# -----------------------------
# Randomness Tests
# -----------------------------
def test_randomness(bits):
    zeros = bits.count("0")
    ones = bits.count("1")
    total = len(bits)

    # 1. Entropy
    p0 = zeros / total
    p1 = ones / total
    entropy = -(p0*math.log2(p0) + p1*math.log2(p1)) if p0 > 0 and p1 > 0 else 0

    # 2. Chi-Square Test (uniformity of 0s and 1s)
    chi, p_val = chisquare([zeros, ones])

    # 3. Runs Test (checks streaks of 0s and 1s)
    runs, expected_runs = runs_test(bits)

    return {
        "zeros": zeros,
        "ones": ones,
        "entropy": entropy,
        "chi_square": chi,
        "p_value": p_val,
        "runs_observed": runs,
        "runs_expected": expected_runs
    }


def runs_test(bits):
    """Simple Wald–Wolfowitz runs test implementation."""
    n = len(bits)
    runs = 1  # first bit counts as a run
    for i in range(1, n):
        if bits[i] != bits[i - 1]:
            runs += 1

    n0 = bits.count("0")
    n1 = bits.count("1")

    # Expected runs formula
    expected_runs = ((2 * n0 * n1) / (n0 + n1)) + 1 if (n0 + n1) > 0 else 0

    return runs, expected_runs


# -----------------------------
# Flask Route
# -----------------------------
@app.route("/qrng")
def get_qrng_key():
    bits = quantum_random_bits(256)
    hex_key = hex(int(bits, 2))[2:].upper()
    stats = test_randomness(bits)
    return jsonify({
        "qrng_key": hex_key,
        "randomness_stats": stats
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
