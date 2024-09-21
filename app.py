import streamlit as st

st.title('My Streamlit App')
st.write('This is a simple Streamlit app!')

# Import necessary libraries
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set the title of the Streamlit app
st.title("Gaussian Distribution Analysis")

# Sidebar input: Number of data points for the Gaussian distribution
st.sidebar.header("Configuration")
num_points = st.sidebar.slider("Select number of data points", 100, 5000, 1000)

# Sidebar input: Mean and standard deviation of the distribution
mean_value = st.sidebar.number_input("Mean", value=0.0)
std_dev = st.sidebar.number_input("Standard Deviation", value=1.0)

# Generate a random Gaussian distribution using numpy
data = np.random.normal(loc=mean_value, scale=std_dev, size=num_points)

# Display basic statistics
st.write("### Statistical Properties")
st.write(f"Mean: {np.mean(data):.2f}")
st.write(f"Standard Deviation: {np.std(data):.2f}")
st.write(f"25th Quantile: {np.percentile(data, 25):.2f}")
st.write(f"Median: {np.median(data):.2f}")
st.write(f"75th Quantile: {np.percentile(data, 75):.2f}")

# Plot the Gaussian distribution curve
st.write("### Gaussian Distribution Plot")
fig, ax = plt.subplots()
sns.histplot(data, bins=30, kde=True, ax=ax, color='blue')
ax.set_title('Gaussian Distribution')
ax.set_xlabel('Value')
ax.set_ylabel('Frequency')
st.pyplot(fig)

# Calculate and display more detailed metrics
st.write("### Additional Metrics")
st.write(f"Minimum Value: {np.min(data):.2f}")
st.write(f"Maximum Value: {np.max(data):.2f}")
st.write(f"Variance: {np.var(data):.2f}")
st.write(f"Skewness: {np.abs(np.mean(data) - np.median(data)):.2f}")

# Adding an interactive section for users to compare two distributions
st.write("### Compare with Another Gaussian Distribution")
mean2 = st.sidebar.number_input("Mean of second distribution", value=1.0)
std_dev2 = st.sidebar.number_input("Standard Deviation of second distribution", value=2.0)

# Generate the second Gaussian distribution
data2 = np.random.normal(loc=mean2, scale=std_dev2, size=num_points)

# Plot the comparison of the two distributions
st.write("### Comparison Plot of Two Gaussian Distributions")
fig, ax = plt.subplots()
sns.histplot(data, bins=30, kde=True, ax=ax, color='blue', label="Distribution 1")
sns.histplot(data2, bins=30, kde=True, ax=ax, color='red', label="Distribution 2")
ax.set_title('Comparison of Two Gaussian Distributions')
ax.set_xlabel('Value')
ax.set_ylabel('Frequency')
ax.legend()
st.pyplot(fig)

st.write("### Thank you for exploring Gaussian distributions!")
