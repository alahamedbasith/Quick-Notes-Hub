import numpy as np
import pandas as pd
import streamlit as st

# DataFrame
df = pd.DataFrame({"A":[1,2,3], "B":[4,5,6]})
st.dataframe(df)

# Chart using DataFrame
chart_data=pd.DataFrame(
np.random.randn(20,3),columns=['a','b','c']
)
st.line_chart(chart_data)

# Filter DataFrame
num = st.slider("Filter A", 1, 3, 2)
st.write(df[df["A"] >= num])

