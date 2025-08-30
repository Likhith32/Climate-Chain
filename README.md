🌍 ClimateChain: A Quantum-Secured, Verifiable Climate Data Platform
Problem Statement Title

Cryptographic Proof Over Institutional Trust

Theme: Quantum Technologies for a Sustainable Future
Category: Software
Team ID: C-17937@238T1A0581

📌 Project Overview

ClimateChain is a real-time, quantum-secured climate data collection and visualization platform. It empowers farmers, scientists, and community admins with actionable insights on climate conditions by combining:

Quantum Random Number Generation (QRNG) ⚛️ for data security

Blockchain-inspired ledger ⛓️ for data integrity

AI-based predictions 🤖 for risk assessment

React-based frontend ⚛️ for seamless user experience

The MVP demonstrates the core value proposition in under 5 minutes, making it ideal for hackathon demos.

🔑 Features ✨
🔐 Backend & Security

Quantum-Secured Encryption: Keys generated using Qiskit-based QRNG.

Randomness Testing: Entropy, Chi-Square, and Runs Test applied to generated bits.

Flask REST API: Provides /qrng endpoint and climate data services.

Ledger Integrity: Blockchain-inspired system ensures tamper-proof data storage.

⚛️ Quantum Random Number Generator (QRNG)

256-bit random keys generated from quantum superposition.

Exposed via Flask API with CORS support.

Statistical validation for randomness quality.

📊 Frontend (React + Next.js + Tailwind)

React-based Dashboard: Built with Next.js 14 + TypeScript.

Tailwind CSS + Shadcn/UI: For modern, responsive design.

Framer Motion: Smooth animations for better UX.

Recharts: Climate data visualization with interactive charts.

User Authentication: Farmers, scientists, and admins get role-based dashboards.

Mobile Responsive: Fully optimized for phones, tablets, and desktops.

🤖 AI & Insights

Lightweight ML model for drought-risk and extreme condition predictions.

Real-time updates with animated graphs and charts.

🏆 Hackathon MVP Flow

Preloaded demo sensors for offline use.

3–5 minute demo-ready presentation.

Error handling, loading spinners, and accessibility support.

⚙️ How It Works
QRNG Service

A quantum circuit with 256 qubits is created using Qiskit.

Each qubit goes through a Hadamard gate, creating equal probability of 0 or 1.

Measurement collapses states → Produces a random bitstring.

Bits are tested using entropy, chi-square, and runs tests.

Flask exposes results via /qrng endpoint.

ClimateChain Flow

Frontend (React/Next.js): User signs up and logs in.

Backend (Flask): Collects climate data from IoT sensors and OpenWeatherMap API.

QRNG Security: Encrypts data using Qiskit QRNG keys.

Ledger Logging: Hashes stored in blockchain-inspired ledger.

Frontend Dashboard: Displays encrypted climate data, risk predictions, and visual charts.


🌱 Impact & Benefits

Farmers & Communities: Real-time drought-risk predictions → Better crop planning.

Scientists & Policymakers: Transparent and tamper-proof climate data.

Economic: Improves credibility in carbon markets & conservation funding.

Social: Restores public trust in environmental science.

Environmental: Creates a global standard for trusted climate data.


Blockchain for Environmental Data Integrity

OpenWeatherMap API
