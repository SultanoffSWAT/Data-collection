import numpy as np

# Matrix Multiplication - Linear Algebra
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
result = np.dot(A, B)

# Matrix Inverse - Linear Algebra
A_inv = np.linalg.inv(A)

# Eigenvalues and Eigenvectors - Linear Algebra
eigenvalues, eigenvectors = np.linalg.eig(A)

# Determinant of a Matrix - Linear Algebra
det_A = np.linalg.det(A)

# Singular Value Decomposition (SVD) - Linear Algebra
U, S, V = np.linalg.svd(A)

# Solving a Linear Equation System - Linear Algebra
b = np.array([1, 2])
x = np.linalg.solve(A, b)

# Matrix Norm - Linear Algebra
norm_A = np.linalg.norm(A)

# Dot Product of Vectors - Linear Algebra
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
dot_product = np.dot(v1, v2)

# Gradient Calculation - Calculus
x = np.linspace(-5, 5, 100)
f_x = x**2
gradient = np.gradient(f_x)

# Numerical Integration (Trapezoidal Rule) - Calculus
area = np.trapz(f_x, x)

# Derivative Approximation (Central Differences) - Calculus
dx = x[1] - x[0]
derivative = (f_x[2:] - f_x[:-2]) / (2 * dx)

# Sum of Elements - Statistics
array = np.array([1, 2, 3, 4])
sum_elements = np.sum(array)

# Mean of Elements - Statistics
mean_array = np.mean(array)

# Standard Deviation - Statistics
std_array = np.std(array)

# Covariance Matrix - Statistics
X = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
cov_matrix = np.cov(X)