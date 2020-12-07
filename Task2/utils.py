import matplotlib.pyplot as plt
import numpy as np


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


def plot_linear_regression(x, y, model):
    plt.scatter(x, y, color='black')

    y_line = model.coef_[0] * x + model.intercept_

    plt.plot(x, y_line, color='blue', linewidth=2)
    plt.title('Linear regression')
    plt.xlabel('Body weight [g]')
    plt.ylabel('Mother smokes (1 - yes, 0 - no)')
    plt.show()