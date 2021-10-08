import pandas as pd
from matplotlib import pyplot as plt


def draw_plot(my_data):
    plt.plot(my_data.Date, my_data.Maximum)
    plt.tick_params(labelsize=40)
    # Display the plot
    #  plt.savefig('alltimes.png', dpi=300, bbox_inches='tight')
    plt.show()


# Function to show summary stats and distribution for a column
def show_distribution(var_data):
    # Get statistics
    min_val = var_data.min()
    max_val = var_data.max()
    mean_val = var_data.mean()
    med_val = var_data.median()
    mod_val = var_data.mode()[0]

    print(var_data.name, '\nMinimum:{:.2f}\nMean:{:.2f}\nMedian:{:.2f}\nMode:{:.2f}\nMaximum:{:.2f}\n'.format(min_val,
                                                                                                              mean_val,
                                                                                                              med_val,
                                                                                                              mod_val,
                                                                                                              max_val))

    # Create a figure for 2 subplots (2 rows, 1 column)
    fig, ax = plt.subplots(2, 1, figsize=(10, 4))

    # Plot the histogram
    ax[0].hist(var_data)
    ax[0].set_ylabel('Frequency')

    # Add lines for the mean, median, and mode
    ax[0].axvline(x=min_val, color='gray', linestyle='dashed', linewidth=2)
    ax[0].axvline(x=mean_val, color='cyan', linestyle='dashed', linewidth=2)
    ax[0].axvline(x=med_val, color='red', linestyle='dashed', linewidth=2)
    ax[0].axvline(x=mod_val, color='yellow', linestyle='dashed', linewidth=2)
    ax[0].axvline(x=max_val, color='gray', linestyle='dashed', linewidth=2)

    # Plot the boxplot
    ax[1].boxplot(var_data, vert=False)
    ax[1].set_xlabel('Value')

    # Add a title to the Figure
    fig.suptitle(var_data.name)
    # Save the figure
    plt.savefig('plot_{}.png'.format(var_data.name), dpi=300, bbox_inches='tight')
    # Show the figure
    fig.show()


# Call the function for each delay field
fields = ["Maximum",
          "Symbicort Turbuhaler",
          "Salbutamol",
          "Relvar Ellipta",
          "Pulmicort"]


data = pd.read_excel("peak_flow_metry_new.xlsx")
#  print(data.head)
#  print(data.isnull().sum())
#  print(data['Relvar Ellipta'])
#  for col in fields:
#      show_distribution(data[col])
print(data[fields].describe())

#  for i in range(1, len(fields)):
#    my_plot = data.boxplot(column='Maximum', by=fields[i], figsize=(8, 5))
#    plt.savefig('my_plot{}.png'.format(i), dpi=300, bbox_inches='tight')
#    plt.show()

"""my_plot = data.boxplot(column='Maximum', by=fields[1:], figsize=(8, 5))
plt.savefig('my_plot.png', dpi=300, bbox_inches='tight')
plt.show()"""

#  my_plot = data.plot(x='Date', y=["Maximum", "Salbutamol"], kind='bar', figsize=(60, 5))

#  print(data.describe())

fig = plt.figure(figsize=(60, 30))
draw_plot(data)


