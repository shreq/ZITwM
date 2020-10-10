import pandas
import seaborn
from matplotlib import pyplot

diseases = {'Hepatitis A': 1996,
            'Measles': 1963,
            'Mumps': 1967,
            'Pertussis': 1926,
            'Polio': 1955,
            'Rubella': 1969,
            'Smallpox': 1796}


def prepare_data(disease: str = None) -> pandas.DataFrame:
    df = pandas.read_csv('us_contagious_diseases.csv').drop('Unnamed: 0', axis=1)
    if disease is not None:
        df = df[df['disease'] == disease].drop('disease', axis=1)
    df = df[~df['state'].isin(['Alaska', 'Hawaii'])]
    df['population'] = df['population'].astype('int64')
    df['per_100k'] = df['count'] / df['population'] * 100_000
    return df


def plot_disease_rate_per_year(df: pandas.DataFrame,
                               state: str = None,
                               disease: str = None) -> None:
    if state is not None:
        df = df[df['state'] == state]
    seaborn.lineplot(x='year',
                     y='per_100k',
                     data=df)
    if disease is not None:
        pyplot.axvline(diseases[disease], color='green')
    pyplot.title(f'{disease if disease is not None else ""} disease rate per year'
                 f'{" for " + state if state is not None else ""}')
    pyplot.ylabel('disease rate per 100k')
    pyplot.tight_layout()
    pyplot.show()
    pyplot.clf()
