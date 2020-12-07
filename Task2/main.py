import pandas as pd
from utils import *
from sklearn.linear_model import LinearRegression


################# Part 2.1

LBW_THRESHOLD = 2700

twins = pd.read_csv('twins.txt')

twins['lbw'] = is_lbw(twins, LBW_THRESHOLD)
twins['one_twin_lbw'] = one_twin_lbw(twins)

twins = twins[twins.one_twin_lbw]

print_mortality('Twin with low body weight', mortality_rate_lbw(twins, lbw=True))
print_mortality('Twin without low body weight', mortality_rate_lbw(twins, lbw=False))

print()

singletons = pd.read_csv('singletons.txt')

print_mortality('Twins', mortality_rate(twins))
print_mortality('Singletons', mortality_rate(singletons))

################# Part 2

x = singletons.dbirwt.values.reshape(-1, 1)
y = singletons.tobacco.values.reshape(-1, 1)

model = LinearRegression().fit(x, y)

plot_linear_regression(x, y, model)