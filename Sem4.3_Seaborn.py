import seaborn as sns
import matplotlib.pyplot as plt

# Load an example dataset
iris = sns.load_dataset("iris")

# Create a scatter plot of sepal length vs sepal width
sns.set_style("whitegrid")
plot = sns.scatterplot(data=iris, x="sepal_length", y="sepal_width", hue="species")
plot.set_title("Iris Sepal Dimensions")

plt.tight_layout()
plt.show()
