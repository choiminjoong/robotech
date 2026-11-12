import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm


# ggplot
plt.style.use('ggplot')
fig = plt.figure()

a = fig.add_subplot(111)
x = [3,4]
y = [1,2]

labels = ['english', 'math']
colors = ['red', 'blue']

#세로막대
#a.bar(x,y, tick_label=labels, color=colors)
#가로막대
a.barh(x,y, tick_label=labels, color=colors)

plt.show()