from tools import *

seaborn.set_style('darkgrid')

disease_choice = 'Measles'
state_choice = 'California'

# Step #1
data = prepare_data(disease_choice)

# Step #2
plot_disease_rate_per_year(data, state=state_choice, disease=disease_choice)

# TODO: check this
# Step #3
data['count_sqrt'] = data['count'] ** 0.5
plot_histograms(data)

pyplot.show()

#4  
#boxplot
pyplot.figure(figsize=(20, 40))
chart=seaborn.boxplot( x=data["year"], y=data["per_100k"] )
chart.set_xticklabels(chart.get_xticklabels(), rotation=45)
pyplot.show()