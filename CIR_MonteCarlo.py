import numpy as np
from matplotlib import pyplot as plt
from numpy import random as rn

a = -0.00163921
b = 0.009709917
σ = 0.024776989

r0 = 0.0514  # as of May 1, 2023
T = 1
N = 12
δt = T/N
print(f"Time interval: δt={δt} years")
M = int(5*1e4)
print(f"Simulation path M={M}")
dz = rn.randn(M,N)
r = r0*np.ones((M,N+1))
for i in range(0,N):
    r[:,i+1] = r[:,i] + a*(b-r[:,i])*δt + σ*np.sqrt(r[:,i])*dz[:,i]*np.sqrt(δt)
plt.show()

a = [ rn.randint(0,M) for j in range(1,60)]

for runer in a:
    plt.plot(np.arange(0,T+δt,δt),r[runer])
plt.show()
V = (r[:,-1])
print("The expected value for the interest rate is:","{:.3%}".format(np.mean(V)))
print("The standard error of sample mean is:", "{:.4%}".format(np.std(V)/np.sqrt(M)))
from scipy.stats import norm
def normsinv(x):
    x = norm.ppf(x)
    return (x)

z = normsinv(0.975)
μ = np.mean(V)
SE = np.std(V)/np.sqrt(M)

print("Lower 95% is:","{:.3%}".format( (μ-z*SE) ))
print("Upper 95% is:","{:.3%}".format( (μ+z*SE) ))
