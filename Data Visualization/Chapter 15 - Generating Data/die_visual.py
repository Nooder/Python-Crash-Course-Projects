from die import Die
import pygal

# Create a D6
die = Die()

# Make some rolls and store the results in a list
results = [die.roll() for i in range(1000)]

# Analyze the results
frequencies = [results.count(i) for i in range(1, die.num_sides+1)]
print(frequencies)

# Visualize the results
hist = pygal.Bar()

hist.title = "Results of rolling D6 1000 times."
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')