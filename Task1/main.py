from tools import *

seaborn.set_style('darkgrid')

disease_choice = 'Measles'
state_choice = 'California'

# TODO: Cit. Step #1 - 'Note that there is a weeks_reporting column. Take that
#  into account when computing the rate'
# Step #1
data = prepare_data(disease_choice)

# Step #2
plot_disease_rate_per_year(data, state=state_choice, disease=disease_choice)

# Step #3
print(data[(data['year'] == 1950) | (data['year'] == 1960)])
