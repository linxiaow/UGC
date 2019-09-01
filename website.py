'''
    Python module for Website class
    One website class can contain several standards alpha.
'''

from random import randint
import numpy as np
from numpy.random import normal
from scipy.optimize import broyden1
from math import exp, sqrt, log, pi
from user import User

def pdf(distribution, v, alpha, user, x):
    def f(x):
        return v * distribution(alpha - x) - user.cost_derivative(x)
    return f

class Website:

    def __init__(self, num, _pdf, _cdf):
        # initialize the attributes of the website
        # initialize the number of users based on "num"
        # Attributes:
        #   - alpha (assume alpha is the same for all badges)
        #   - value of badges
        #   - the number of users participating to win the corresponding badges
        #   - F distribution (standard normal)
        #   - rho (for relative standards mechanisms, fixed number of winners)
        #   - a bunch of users
        self.pdf = _pdf
        self.cdf = _cdf
        self.standard = 1 # float(input("Enter an alpha: ")) # a numerical value to specify the standard
        self.rho = 10 # a fixed number of winners
        self.nUsers = num # number of users
        self.nBadges = 10 # number of badges (questions)
        # the following are the parameters that define the shape of the normal distribution
        self.mean = 5
        self.std = 3

        self.users = []
        for i in range(self.nUsers):
            # self.users.append(User(normal(self.mean, self.std)))
            self.users.append(User(5))
        # end of initializing the users
        
        self.badges = []
        self.participateNum = [0 for i in range(self.nBadges)] # number of users participating in getting the badges
        # index should match the one of badges
        # in the final step, used to calculate the participation rate of each badge
        for i in range(self.nBadges):
            # self.badges.append(randint(1, 10)) # the values of badges range from 1 to 10
            self.badges.append(i + 1 + 5)
        # end of initializing the badges

    def givePayOff(self, user, v):
        # returns the maximum pay-off of a user together with the effort needed for this maximum pay-off given the user's cost funciton, value of a badge, and the corresponding standard of that badge
        # pi(n) = v * p_win - c(n) = v * (1 - F(alpha - n)) - c(n)
        # solving the equation "v * f(alpha - n) - c'(n) = 0" gives you the effort that maximizes the pay-off
        F = pdf(self.pdf, v, self.standard, user, 0)
        effort = broyden1(F, 1)
        # print(effort)
        payOff = v * (1 - self.cdf(self.standard - effort)) - user.cost(effort)
        # print(1 - norm.cdf(self.standard - effort))
        # iprint(payOff)
        return payOff, effort

    def participate_vs_alpha(self):
        alphas = np.linspace(0.1, 5, 500)
        badgeValue = 6
        user = self.users[0]
        participate = []
        for alpha in alphas:
            self.standard = alpha
            payoff, effort = self.givePayOff(user, badgeValue)
            if (user.participate(payoff, badgeValue, effort)):
                participate.append(1)
            else:
                participate.append(0)
        return alphas, np.array(participate)

    def payoff_vs_alpha(self):
        alphas = np.linspace(0.1, 8, 200)
        badgeValue = 6
        user = self.users[0]
        payoffs = []
        for alpha in alphas:
            self.standard = alpha
            payoff, effort = self.givePayOff(user, badgeValue)
            payoffs.append(payoff)
        return alphas, np.array(payoffs)

    def simulate(self):
        # simulate the users' behavior in the website
        # plot the results

        # for each badge
        for i in range(self.nBadges):
            v = self.badges[i] # the value of the badge
            # for each user
            for j in range(self.nUsers):
                user = self.users[j]
                payOff, effort = self.givePayOff(user, v)
                # if the user participates, add 1 to participateNum
                if (user.participate(payOff, v, effort)):
                    self.participateNum[i] += 1
                    user.increment()
            # end of iteration of users
        # end of iteration of badges

        for i in range(self.nBadges):
            print("The current badge value is", self.badges[i], "and the corresponding participation is", self.participateNum[i])

        # TODO: use matplotlib to plot the graphs
