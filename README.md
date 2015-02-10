Computational Methods for Astronomy
===================================
by: **Sebastian Bustamante** *2014*

This course is intended for students of Astronomy at the Universidad de Antioquia 
and will cover some numerical methods commonly used in science and specially in 
astronomy. These topics will be addressed from a formal context but also keeping 
a practical and computational approach, illustrating many useful applications in
problems of physics and astronomy.


The practical component will be almost entirely developed in *Python* and 
slightly less in *C* (when computational performance is required). 
However students with knowledge in other programming languages (except
privative languages like MatLab, Mathematica) are also aimed to use them.


In this repository it can be found all the related material of the course, 
including the detailed program, notes and presentations, examples (ipython 
notebooks) and homeworks. (This repository may be subject to changes continuously 
as the course advances).


[**SYLLABUS**](https://github.com/sbustamante/ComputationalMethods/blob/master/syllabus/syllabus.pdf?raw=true):
detailed description of the program of the course, including a brief motivation and presentation, 
topics to be covered, evaluation and bibliography.

Contents
--------

### 1. **Python** *(2 weeks)*
    
**Topics**
- [Overview of python](http://nbviewer.ipython.org/github/sbustamante/ComputationalMethods/blob/master/material/overview-python.ipynb)
- [Basic scripting](http://nbviewer.ipython.org/github/sbustamante/ComputationalMethods/blob/master/material/basic-scripting.ipynb)
- [Implementation of scientific libraries](http://nbviewer.ipython.org/github/sbustamante/ComputationalMethods/blob/master/material/scientific-libraries.ipynb)
- [Plotting with matplotlib](http://nbviewer.ipython.org/github/sbustamante/ComputationalMethods/blob/master/material/matplotlib.ipynb)
- [Ipython notebooks](http://nbviewer.ipython.org/github/sbustamante/ComputationalMethods/blob/master/material/ipython-notebooks.ipynb)

**Tasks**
- *Task01:* Solve the problems in the section [Miscellanea](http://nbviewer.ipython.org/github/sbustamante/ComputationalMethods/blob/master/material/basic-scripting.ipynb#Miscellanea). (*due to:* **Oct 31**) **[GRADES](https://github.com/sbustamante/ComputationalMethods/blob/master/grades/grades_task01.dat)**
- *Task02:* Solve the two activities proposed in [here](http://nbviewer.ipython.org/github/sbustamante/ComputationalMethods/blob/master/activities/halos-catalog.ipynb). (*due to:* **Nov 08**) **[GRADES](https://github.com/sbustamante/ComputationalMethods/blob/master/grades/grades_task02.dat)**
    
### 2. **Mathematical Preliminaries** *(1 week)*
    
**Topics**
- [Computer arithmetics and round-off methods](http://nbviewer.ipython.org/github/sbustamante/ComputationalMethods/blob/master/material/computer-arithmetics.ipynb)
- [Algorithms and convergence](http://nbviewer.ipython.org/github/sbustamante/ComputationalMethods/blob/master/material/algorithms-convergence.ipynb)

**Tasks**
- *Task03:* Solve the two activities proposed in [here](http://nbviewer.ipython.org/github/sbustamante/ComputationalMethods/blob/master/activities/binary-representation.ipynb). (*due to:* **Nov 15**)
    
### 3. **One Variable Equations** *(2 weeks)*
    
**Topics**
- [Bisection method](http://nbviewer.ipython.org/github/sbustamante/ComputationalMethods/blob/master/material/one-variable-equations.ipynb#Bisection-Method)
- [Fixed-point iteration](http://nbviewer.ipython.org/github/sbustamante/ComputationalMethods/blob/master/material/one-variable-equations.ipynb#Fixed-point-Iteration)
- [Newton-Raphson method](http://nbviewer.ipython.org/github/sbustamante/ComputationalMethods/blob/master/material/one-variable-equations.ipynb#Newton-Raphson-Method)
- [Secant method](http://nbviewer.ipython.org/github/sbustamante/ComputationalMethods/blob/master/material/one-variable-equations.ipynb#Secant-Method)

**Tasks**
- *Task04:* Solve the three activities proposed in [here](http://nbviewer.ipython.org/github/sbustamante/ComputationalMethods/blob/master/activities/bisection-performance.ipynb). (*due to:* **Nov 22**).
- *Task05:* Solve the activity discussed [during class](http://nbviewer.ipython.org/github/sbustamante/ComputationalMethods/blob/master/activities/radius-exoplanet.ipynb). (*due to:* **Nov 29**).

### 4. **Interpolation Techniques** *(2 weeks)*
    
**Topics**
- [Linear interpolation](http://nbviewer.ipython.org/github/sbustamante/ComputationalMethods/blob/master/material/interpolation.ipynb#Linear-Interpolation)
- [Lagrange polynomials](http://nbviewer.ipython.org/github/sbustamante/ComputationalMethods/blob/master/material/interpolation.ipynb#Lagrange-Polynomial)
- [Divided differences](http://nbviewer.ipython.org/github/sbustamante/ComputationalMethods/blob/master/material/interpolation.ipynb#Divided-Differences)
- [Hermite interpolation](http://nbviewer.ipython.org/github/sbustamante/ComputationalMethods/blob/master/material/interpolation.ipynb#Hermite-Interpolation)

### **Test 1 (25%)**

This test is divided in two parts. A theoretical part that will be evaluated during class time (50% of the test). And a [computational activity](http://nbviewer.ipython.org/github/sbustamante/ComputationalMethods/blob/master/activities/test1.ipynb) due to *due to:* **Jan 23, Midnight** (50% of the test). **[GRADES](https://github.com/sbustamante/ComputationalMethods/blob/master/grades/grades_test1.dat)**

### 5. **Numerical Calculus** *(2 weeks)*
    
**Topics**
- [Numerical differentiation](http://nbviewer.ipython.org/github/sbustamante/ComputationalMethods/blob/master/material/numerical-calculus.ipynb#Numerical-Differentiation)
- [Numerical integration](http://nbviewer.ipython.org/github/sbustamante/ComputationalMethods/blob/master/material/numerical-calculus.ipynb#Numerical-Integration)
- [Composite numerical integration](http://nbviewer.ipython.org/github/sbustamante/ComputationalMethods/blob/master/material/numerical-calculus.ipynb#Composite-Numerical-Integration)
- [Adaptive quadrature methods](http://nbviewer.ipython.org/github/sbustamante/ComputationalMethods/blob/master/material/numerical-calculus.ipynb#Adaptive-Quadrature-Methods)
- [Improper integrals](http://nbviewer.ipython.org/github/sbustamante/ComputationalMethods/blob/master/material/numerical-calculus.ipynb#Improper-Integrals)

**Tasks**
- *Task06:* Solve the activity proposed in [here](http://nbviewer.ipython.org/github/sbustamante/ComputationalMethods/blob/master/activities/radial-poisson.ipynb). (*due to:* **Feb 1**).
- *Task07:* Solve the activity proposed in [here](http://nbviewer.ipython.org/github/sbustamante/ComputationalMethods/blob/master/activities/ficks-law.ipynb). (*due to:* **Feb 15**).

### 6. **Linear Algebra** *(2 weeks)*
    
**Topics**
- [Linear systems of equations](http://nbviewer.ipython.org/github/sbustamante/ComputationalMethods/blob/master/material/linear-algebra.ipynb#Linear-Systems-of-Equations)
- [Gaussian elimination](http://nbviewer.ipython.org/github/sbustamante/ComputationalMethods/blob/master/material/linear-algebra.ipynb#Gaussian-elimination)

...
