import streamlit as st

# Matplotlib

import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.plot([1,2,3],[4,5,6])
st.pyplot(fig)

# Seaborn

import seaborn as sns
fig = sns.scatterplot(x=[1,2,3], y=[4,5,6])
st.pyplot(fig.figure)
