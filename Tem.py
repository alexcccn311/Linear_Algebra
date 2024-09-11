import numpy as np
from calculate_adjugate_matrix import adjugate_matrix
from calculate_inverse_matrix import inverse_matrix
from calculate_determinant import quick_calculate_determinant_value

A = np.array([
    [2, -1, 0],
    [1, 3, 4],
    [0, -2, 5],
])

B = np.array([
    [1, 2, 3, 4, 5, 6],
    [7, 8, 9, 10, 11, 12],
    [13, 14, 15, 16, 17, 18],
    [20, 22, 24, 26, 28, 30],
    [25, 26, 27, 28, 29, 30],
    [31, 32, 33, 34, 35, 36],
    [37, 38, 39, 40, 41, 42]
])


n = A.shape[0]

if np.allclose(np.linalg.inv(adjugate_matrix(A)), adjugate_matrix((adjugate_matrix(A)))/(np.linalg.det(adjugate_matrix(A)))) and np.allclose(adjugate_matrix((adjugate_matrix(A)))/(np.linalg.det(A))**(n-1),adjugate_matrix((adjugate_matrix(A)))/(np.linalg.det(adjugate_matrix(A)))):
    print('1')
else:
    print('-1')
if np.allclose(adjugate_matrix((np.linalg.inv(A))),  adjugate_matrix((adjugate_matrix(A)/(np.linalg.det(A))))) and np.allclose(adjugate_matrix((adjugate_matrix(A)))/(np.linalg.det(A))**(n-1), adjugate_matrix((adjugate_matrix(A)))/(np.linalg.det(adjugate_matrix(A)))):
    print('2')
else:
    print('-2')
if np.allclose(A/(np.linalg.det(A)), adjugate_matrix((adjugate_matrix(A)))/(np.linalg.det(A))**(n-1)):
    print('3')
else:
    print('-3')
if np.allclose(adjugate_matrix((np.linalg.inv(A))), np.linalg.inv((adjugate_matrix(A)))):
    print('4')
else:
    print('-4')