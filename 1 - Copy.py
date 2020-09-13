import numpy as np
import matplotlib.pyplot as plt 
A = np.array([[6,2],
              [2,3]])
u_0 = np.array([[1],
                [1]])
landa = 0
e = 0.0001
eigh = []
count = 0 

while True:
    u_1 = np.dot(A,u_0)
    u_mx = np.amax(u_1)
    u_2 = u_1/u_mx
    if abs(landa - u_mx) < e :
        break
    else:
        u_0 = u_2
        landa = u_mx
        count += 1 # += means : count = count + 1
        eigh.append(landa)
       
print(eigh)        
print("the dominant eigh value is: ",eigh)
print(u_2)
print("the number of iteration is:  " , count)

plt.plot(range(count),eigh,'r') # r is related to color of graph ## y = yellow,...

plt.xlabel("iteraion")
plt.ylabel("landa")
plt.show()

