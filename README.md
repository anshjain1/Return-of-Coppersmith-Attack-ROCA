# Return of Coppersmith's Attack (ROCA)

A cryptanalysis project studying the **Return of Coppersmith's Attack (ROCA)** vulnerability in RSA key generation, focusing on structured prime generation, vulnerable-key detection, and lattice-based factorization techniques.

## Overview

ROCA is a vulnerability associated with certain RSA key-generation implementations that generate primes with a particular mathematical structure. This structure introduces exploitable properties into the resulting RSA public keys, potentially enabling an attacker to factor vulnerable RSA moduli.

This project explores the mathematical principles behind the vulnerability and the techniques used to identify and analyze affected RSA keys.

## Objectives

- Understand the mathematical structure behind ROCA-vulnerable RSA primes.
- Analyze how modular constraints can reveal information about RSA public keys.
- Study vulnerable-key detection using modular residue patterns and discrete logarithms.
- Explore Coppersmith–Howgrave-Graham methods and lattice reduction for factoring vulnerable RSA moduli.
- Investigate parameters affecting the efficiency of cryptanalytic experiments.

## Technical Approach

### 1. Structured RSA Prime Generation

Study the prime-generation structure associated with ROCA, in which candidate primes are constrained by powers of a fixed base modulo a primorial-derived modulus.

These constraints introduce patterns that distinguish vulnerable keys from normally generated RSA keys.

### 2. Vulnerable-Key Detection

Analyze public RSA moduli for mathematical properties associated with the vulnerable prime-generation process. Modular residue constraints and discrete-logarithm techniques help identify whether a key exhibits the relevant structure.

### 3. Lattice-Based Cryptanalysis

Explore the Coppersmith–Howgrave-Graham approach to finding sufficiently small roots of polynomial equations modulo an RSA modulus. Lattice construction and the Lenstra–Lenstra–Lovász (LLL) algorithm are studied as components of the factorization approach.

### 4. Parameter Analysis

Investigate how exponent-search strategies, primorial selection, and lattice parameters affect the computational cost and effectiveness of cryptanalytic experiments.

## Technologies and Concepts

- **Language:** Python
- **Mathematical environment:** SageMath
- **Cryptography:** RSA, modular arithmetic, discrete logarithms
- **Number theory:** Prime generation, modular residues, primorials
- **Lattice methods:** Coppersmith's method, Howgrave-Graham technique, LLL reduction

## Key Learnings

- How structural weaknesses in prime generation can compromise RSA security.
- How modular arithmetic and number-theoretic properties can support cryptographic vulnerability detection.
- How discrete logarithms and lattice reduction contribute to cryptanalytic methods.
- Why secure randomness and carefully designed prime-generation procedures are essential for public-key cryptography.

## References

- Nemec, M. et al., *The Return of Coppersmith's Attack: Practical Factorization of Widely Used RSA Moduli* (ROCA research).
- Coppersmith's methods for finding small roots of polynomial equations.
- Howgrave-Graham's work on small-root techniques and lattice-based factorization.
- The LLL lattice-reduction algorithm.


