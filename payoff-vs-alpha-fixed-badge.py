from matplotlib import pyplot as plt
from scipy.stats import norm, norminvgauss
from functools import partial
from website import Website

webNorm = Website(1, norm.pdf, norm.cdf)
x, participationNorm = webNorm.payoff_vs_alpha()

a, b = 0.33, 0
webGauss = Website(1, partial(norminvgauss.pdf, a=a, b=b), partial(norminvgauss.cdf, a=a, b=b))
x, participationGauss = webGauss.payoff_vs_alpha()

fig, ax = plt.subplots(1, 1)
ax.plot(x, participationNorm, "r-", lw=2, alpha=0.6, label="norm")
ax.plot(x, participationGauss, "b-", lw=2, alpha=0.6, label="norminvgauss")
ax.legend(loc="best", frameon=False)
ax.set_title("Optimal Payoff vs. Standard Alpha")
ax.set_xlabel("alpha")
ax.set_ylabel("optimal payoff")
plt.grid()
plt.show()
