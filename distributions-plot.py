from scipy.stats import norm, norminvgauss
from matplotlib import pyplot as plt
import numpy as np

fig, ax = plt.subplots(1, 1)

a, b = 0.33, 0
x = np.linspace(norminvgauss.ppf(0.01, a, b), norminvgauss.ppf(0.99, a, b), 100)
ax.plot(x, norm.pdf(x), 'r-', lw=2, alpha=0.6, label='norm pdf')
ax.plot(x, norminvgauss.pdf(x, a, b), 'b-', lw=2, alpha=0.6, label='norminvgauss pdf')

ax.legend(loc='best', frameon=False)
ax.set_title("Distribution functions used for epsilon")
plt.grid()
plt.show()
