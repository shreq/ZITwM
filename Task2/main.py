import pandas as pd
from utils import *
from sklearn.linear_model import LinearRegression, LogisticRegression
from scipy.stats import chisquare

################# Part 2.1

LBW_THRESHOLD = 2700
ALPHA = 0.05

twins = pd.read_csv('twins.txt')

twins['lbw'] = is_lbw(twins, LBW_THRESHOLD)
twins['one_twin_lbw'] = one_twin_lbw(twins)

twins = twins[twins.one_twin_lbw]

print_mortality('Twin with low body weight', mortality_rate_lbw(twins, lbw=True))
print_mortality('Twin without low body weight', mortality_rate_lbw(twins, lbw=False))
print_mortality('Twins overall', mortality_rate(twins))
print()

singletons = pd.read_csv('singletons.txt')
singletons['lbw'] = is_lbw(singletons, LBW_THRESHOLD)

print_mortality('Singletons with low body weight', mortality_rate_lbw(singletons, lbw=True))
print_mortality('Singletons without low body weight', mortality_rate_lbw(singletons, lbw=False))
print_mortality('Singletons overal', mortality_rate(singletons))

twins_value_counts = twins.mort.value_counts(normalize=True)
singletons_value_counts = singletons.mort.value_counts(normalize=True)

stat, p = chisquare(singletons_value_counts, twins_value_counts)

print()
print('Chi-square statistic: ', stat)
print('P-value: ', p)
print('Hypothesis H0 rejected' if p < ALPHA else 'Cannot reject hypothesis H0')

################# Part 2

x = singletons.dbirwt.values.reshape(-1, 1)
y = singletons.tobacco

linear = LinearRegression().fit(x, y)
logistic = LogisticRegression(solver='liblinear', random_state=0).fit(x, y)

plot_linear_regression(x, y, linear)
plot_logistic_regression(x, y, logistic)
