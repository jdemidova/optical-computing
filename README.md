# PART 1: Numerical Implementation of Finite-Range Integral Transforms  
---

## 🎯 Overview
This project implements a **numerical simulation of an integral transform with finite integration limits**.  
The work demonstrates how continuous mathematical operators can be approximated through **discrete numerical integration** — a foundational step toward understanding and implementing the **Fourier transform** in optics.

---

## 🧠 Theoretical Background
An **integral transform** maps a function f(x) into another function F(E) using a kernel K(E, x):

F(E) = ∫ from a to b [ K(E, x) · f(x) · dx ]

In this work, the integral is evaluated **numerically** using the **left rectangle (Riemann sum) method**.
This approach can be extended to complex-valued signals and kernels, allowing matrix-like formulations for computational efficiency.

---

## ⚙️ Task Description

### 🔹 Kernel and Parameters
K(E, x) = x^(αE - 1)

Integration and output domains:
[a, b] = [1, 5],  [p, q] = [0, 3]

---

### 🔹 Task Description

1. **Input Signal:**  
   f(x) = e^(i·β·x) or any simple complex-valued function.

3. **Discretization Parameters:**  
   - Step: Δx = Δt = 1
   - Intervals: n = 1000, ; m = 1000 

4. **Numerical Calculation:**  
   Compute the transform using discrete forms.

5. **Visualization:**  
   - Plot **input signal**: amplitude and phase (two separate graphs).  
   - Plot **transformed signal**: amplitude and phase.  

6. **Parameter Study:**  
   - Vary number of discretization points  
   - Vary integration bounds  
   - Vary function parameter α  

   Analyze how these affect numerical accuracy and the shape of both signals.  
   ⚠️ If your integration domain is non-negative, do not extend it into negative values.


---

## 🧩 Hints
- Test convergence by changing m, n, and bounds [a,b], [p,q].

---

## 📊 Results
- Discretized visualizations of the **original** and **transformed** signals (amplitude + phase).  
- Analysis of numerical errors and how the discretization affects results.
---
# PART 2: Numerical and Analytical Implementation of the Optical Fourier Transform
---

## 🎯 Overview
This part focuses on **implementing and analyzing the optical Fourier transform** using two different approaches:

1. **Numerical Fast Fourier Transform (FFT)**  
2. **Direct numerical integration (finite Fourier transform)**  

The goal is to compare the two methods, verify their equivalence, and explore analytical properties of the transform for specific optical fields.

---

## ⚙️ Task Description

### 🔹 Input Field 
The input optical field is defined as:
f(x) = (4x² − 2) * exp(−x² / 2)
OR Gaussian beam:
f(x) = -s * x^2

---

### 🔹 Task Description

1. **Implement the one-dimensional finite Fourier transform** using the **FFT algorithm**.  

2. **Plot the input Gaussian beam** as amplitude and phase

3. Test the implemented method of step 1 by **inputting a Gaussian beam**. The **output** must also be the **Gaussian beam** of a different scale.

4. **Implement the finite Fourier transform using a standard numerical integration method (e.g., the rectangle method)**. It is necessary to calculate the integral for each discrete value of u to obtain the result as a vector. A Gaussian beam should be input and output again.
5. **Make another input field the input for the transform**. Plot the field itself and the transform result.
6. **Analytically calculate (theorise) the transform result** of the input field and plot the analytical (theorised) and actual results (from step 5) on the same grid. They should match.

---

## 📊 Results
- Amplitude and phase plots of the **Gaussian beam** and **field input** before and after transformation.  
- Comparison between:
  - FFT-based result  
  - Direct integration result  
  - Analytical result using Hermite–Gaussian representation  
Matching all three confirms the correctness of the implementation.
