# 🧮 PART 1: Numerical Implementation of Finite-Range Integral Transforms  
---

## 🎯 Overview
This project implements a **numerical simulation of an integral transform with finite integration limits**.  
The work demonstrates how continuous mathematical operators can be approximated through **discrete numerical integration** — a foundational step toward understanding and implementing the **Fourier transform** in optics.

---

## 🧠 Theoretical Background
An **integral transform** maps a function \( f(x) \) into another function \( F(E) \) using a kernel \( K(E, x) \):

\[
F(E) = \int_a^b K(E, x)\, f(x)\, dx
\]

In this work, the integral is evaluated **numerically** using the **left rectangle (Riemann sum) method**.
This approach can be extended to complex-valued signals and kernels, allowing matrix-like formulations for computational efficiency.

---

## ⚙️ Task Description

### 🔹 Kernel and Parameters
\[
K(E, x) = x^{\alpha E - 1}
\]

Integration and output domains:

\[
[a, b] = [1, 5], \quad [p, q] = [0, 3]
\]

---

### 🔹 Implementation Requirements

1. **Input Signal:**  
   \( f(x) = e^{i \beta x} \) or any simple complex-valued function.

3. **Discretization Parameters:**  
   - Step: \( \Delta x = \Delta t = 1 \)  
   - Intervals: \( n = 1000, \; m = 1000 \)

4. **Numerical Calculation:**  
   Compute the transform using discrete forms.

5. **Visualization:**  
   - Plot **input signal**: amplitude and phase (two separate graphs).  
   - Plot **transformed signal**: amplitude and phase.  

6. **Parameter Study:**  
   - Vary number of discretization points  
   - Vary integration bounds  
   - Vary function parameter /alpha  

   Analyze how these affect numerical accuracy and the shape of both signals.  
   ⚠️ If your integration domain is non-negative, do not extend it into negative values.


---

## 🧩 Hints
- Test convergence by changing \( m \), \( n \), and bounds \([a,b]\), \([p,q]\).

---

## 📊 Expected Results
- Discretized visualizations of the **original** and **transformed** signals (amplitude + phase).  
- Analysis of numerical errors and how the discretization affects results.
