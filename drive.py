from functools import partial
from scipy.stats import norm, norminvgauss
from website import Website

a, b = 0.5, 0.3
n = int(input("Enter the number of users: "))
web = Website(n, partial(norminvgauss.pdf, a=a, b=b), partial(norminvgauss.cdf, a=a, b=b))
web.simulate()
