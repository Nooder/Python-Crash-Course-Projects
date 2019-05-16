from die import Die
import pygal

# Create a D6 and D10 dice
die_1 = Die(6)
die_2 = Die(10)

# Make some rolls and store the results in a list
results = [die_1.roll() + die_2.roll() for i in range(50000)]

# Analyze the results
max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(i) for i in range(2, max_result + 1)]
print(frequencies)

# Visualize the results
hist = pygal.Bar()

hist.title = "Results of rolling D6 1000 times."
hist.x_labels = [str(i) for i in range(2, max_result + 1)]
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D6 + D10', frequencies)
hist.render_to_file('different_dice_visual.svg')