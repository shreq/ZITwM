import matplotlib.pyplot as plt
import numpy as np
import math


def mortality_rate(df):
    return df.mort.value_counts(normalize=True)[1] * 100


def mortality_rate_lbw(df, lbw):
    return mortality_rate(df[df.lbw == lbw])


def is_lbw(df, threshold):
    return df.dbirwt < threshold


def one_twin_lbw(df):
    twin_groups = df.groupby(df.pair_id)

    one_twin_lbw_dict = {}
    for id, group in twin_groups:
        lbw = group.lbw.values
        one_twin_lbw_dict[id] = lbw[0] ^ lbw[1]

    return df.pair_id.map(one_twin_lbw_dict)


def print_mortality(prefix, mortality):
    print(f'{prefix} mortality rate: {mortality:.2f}%')


def plot_regression(x, y, regression, regression_name):
    plt.scatter(x, y, color='black')
    plt.plot(x, regression, color='blue', linewidth=2)
    plt.title(f'{regression_name} regression')
    plt.xlabel('Body weight [g]')
    plt.ylabel('Mother smokes (1 - yes, 0 - no)')
    plt.show()


def plot_linear_regression(x, y, model):
    y_line = model.coef_[0] * x + model.intercept_
    plot_regression(x, y, y_line, 'Linear')


def logistic_value(x, a_v, b_v):
    return (1 / (1 + math.exp(- (x * a_v)))) + b_v


def plot_logistic_regression(x, y, model):
    a_v = model.coef_[0][0]
    b_v = model.intercept_[0]

    y_line = [logistic_value(x_i, a_v, b_v) for x_i in x]

    plot_regression(x, y, y_line, 'Logistic')