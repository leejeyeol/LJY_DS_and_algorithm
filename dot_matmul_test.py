import numpy as np
a = np.array([[1,0,-1],[2,1,-3],[-2,1,1]])
print(a)
cov = a.T.dot(a)/float(a.shape[0])
at = a.T
print(at)
cov2 = a.dot(at)/float(a.shape[0])
print(cov)
print(cov2)
cov3 = a.__matmul__(at)/float(a.shape[0])
print(cov3 )


evt, evl = np.linalg.eig(cov)
print(evt)
print(evl)


