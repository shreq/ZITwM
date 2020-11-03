from tools import *

seaborn.set_style('darkgrid')

disease_choice = 'Measles'
state_choice = 'California'

# Step #1
data = prepare_data(disease_choice)

# Step #2
plot_disease_rate_per_year(data, state=state_choice, disease=disease_choice)

# Step #3
data['count_sqrt'] = data['count'] ** 0.5
plot_histograms(data)

# Step #4
plot_distribution_over_years(data)
pyplot.show()

# 5
# Potwierdzanie hipotezy
# Szczepionka na Polio masowa zaczela byc używana w 1955 roku
data = prepare_data("Polio")
seaborn.regplot(x="year", y="per_100k", data=data)
pyplot.axvline(x=1955,
               linewidth=2, linestyle="--",
               color='red')
pyplot.show()

# Szczepionka wprowadzona w 1968 a wynaleziona w 1963
data = prepare_data("Measles")
seaborn.regplot(x="year", y="per_100k", data=data)
pyplot.axvline(x=1968,
               linewidth=2, linestyle="--",
               color='red')
pyplot.show()

# Wprowadzenie szczepionki na Hepatitis A w roku 1995 (USA) w europie w 1991
data = prepare_data("Hepatitis A")
seaborn.regplot(x="year", y="per_100k", data=data)
pyplot.axvline(x=1995,
               linewidth=2, linestyle="--",
               color='red')
pyplot.show()
