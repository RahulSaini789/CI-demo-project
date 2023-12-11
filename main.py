import matplotlib.pyplot as plt

fig, ax = plt.subplots()

fruits = ['apple', 'blueberry', 'orange', 'cherry']
counts = [140, 10, 30, 45]
bar_labels = ['red', 'green', '_red', 'orange']
bar_colors = ['tab:blue', 'tab:orange','tab:red','tab:red']

ax.bar(fruits, counts, label=bar_labels, color=bar_colors)

ax.set_ylabel('frult supply')
ax.set_title('Fruit supply by kind and color')
ax.legend(title = 'Fruit color')

plt.savefig('bars.png', bbox_inches='tight')

cat = ["bored", "happy", "happy","happy", "happy", "happy"]
dog = ["bored", "bored", "bored","happy", "bored", "bored"]
activity = ["combing", "drinking", "feeding", "nappijng", "playing", "washing"]

fig, ax = plt.subplots()
ax.plot(activity, dog, label="dog")
ax.plot(activity, cat, label="cat")
ax.legend()

plt.savefig('lines.png', bbox_inches='tight')
              