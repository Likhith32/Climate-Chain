Quantum Random Number Generator (QRNG) ⚛️
This project is a Flask-based web server that provides a Quantum Random Number Generator (QRNG) service. It leverages the principles of quantum mechanics to generate truly random numbers, which are then exposed through a simple REST API. To ensure the quality of the randomness, the generated bits are subjected to a series of statistical tests.

Features ✨
Quantum Random Bit Generation: Utilizes Qiskit and its simulator to generate 256 random bits based on the principles of quantum superposition.

Randomness Testing: Performs a suite of statistical tests on the generated bits to validate their randomness:

Entropy Calculation: Measures the uncertainty or randomness in the bits.

Chi-Square Test: Assesses the uniformity of the distribution of 0s and 1s.

Runs Test: Checks for the presence of unusual streaks of 0s or 1s.

REST API: Exposes a simple /qrng endpoint that returns a 256-bit random key in hexadecimal format, along with the results of the randomness tests.

CORS Enabled: The server is configured with CORS to allow cross-origin requests.

How it Works ⚙️
The core of this project lies in its quantum random bit generation function. First, a quantum circuit with 256 qubits is created. A Hadamard gate is then applied to all qubits, which puts them into a state of superposition where they have an equal probability of being a 0 or a 1. Finally, each qubit is measured, causing it to collapse to a definite state of either 0 or 1, providing a string of random bits. These bits are then passed through several statistical tests to ensure their quality.

API Endpoint 📡
GET /qrng
This endpoint returns a JSON object containing a 256-bit quantum random number in hexadecimal format, along with statistics about its randomness. The response includes the hexadecimal key and details from the randomness tests, such as the count of zeros and ones, entropy, chi-square value, p-value, and the observed vs. expected number of runs.
