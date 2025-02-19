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
    df = df[~df['state'].isin(['Alaska', 'Hawaii'])]
    if disease is not None:
        df = df[df['disease'] == disease].drop('disease', axis=1)
    df['population'] = df['population'].astype('int64')
    df['per_100k'] = (df['count'] / df['weeks_reporting'] * 52) / df['population'] * 100_000
    df['per_100k'].fillna(0, inplace=True)
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


def plot_histograms(df: pandas.DataFrame):
    fig, axes = pyplot.subplots(3, 2, sharex='col', sharey='col')
    df1 = df.groupby(['year', 'state']).sum().reset_index()
    seaborn.barplot(x='state',
                    y='count',
                    data=df1[df1['year'] == 1950],
                    ax=axes[0, 0])
    seaborn.barplot(x='state',
                    y='count_sqrt',
                    data=df1[df1['year'] == 1950],
                    ax=axes[0, 1])
    seaborn.barplot(x='state',
                    y='count',
                    data=df1[df1['year'] == 1960],
                    ax=axes[1, 0])
    seaborn.barplot(x='state',
                    y='count_sqrt',
                    data=df1[df1['year'] == 1960],
                    ax=axes[1, 1])
    seaborn.barplot(x='state',
                    y='count',
                    data=df1[df1['year'] == 1970],
                    ax=axes[2, 0])
    seaborn.barplot(x='state',
                    y='count_sqrt',
                    data=df1[df1['year'] == 1970],
                    ax=axes[2, 1])
    fig.suptitle('Histogram of case counts across the states')
    axes[0, 0].set_title('1950')
    axes[0, 0].set_xlabel('')
    axes[0, 1].set_title('1950')
    axes[0, 1].set_xlabel('')
    axes[0, 1].set_ylabel('')
    axes[1, 0].set_title('1960')
    axes[1, 0].set_xlabel('')
    axes[1, 1].set_title('1960')
    axes[1, 1].set_xlabel('')
    axes[1, 1].set_ylabel('')
    axes[2, 0].set_title('1970')
    axes[2, 1].set_title('1970')
    axes[2, 1].set_xlabel('square root count')
    axes[2, 1].set_ylabel('')
    axes[2, 0].tick_params(labelrotation=90)
    axes[2, 1].tick_params(labelrotation=90)
    pyplot.tight_layout()


def plot_distribution_over_years(df: pandas.DataFrame):
    pyplot.figure(figsize=[1.5 * x for x in pyplot.rcParams.get('figure.figsize')])
    seaborn.boxplot(x=df["year"], y=df["per_100k"])
    pyplot.xticks(rotation=90, fontsize=8)
    pyplot.tight_layout()


def plot_heatmap(df: pandas.DataFrame, disease: str):
    heat_df = df.groupby(['state', 'year'])['count'].sum().unstack()
    plot = seaborn.heatmap(heat_df, cmap='Blues', yticklabels=True)
    vaccine_year_index = heat_df.columns.to_list().index(diseases[disease])
    plot.axvline(vaccine_year_index, color='g')
    pyplot.tight_layout()