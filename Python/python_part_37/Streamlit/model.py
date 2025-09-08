import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# 1. Load Data (Iris dataset)
@st.cache_data
def load_data():
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['species'] = iris.target
    return df, iris.target_names

df, target_names = load_data()

# 2. Train the Model
model = RandomForestClassifier()
model.fit(df.iloc[:, :-1], df['species'])

# 3. Sidebar inputs (user chooses flower measurements)
st.sidebar.title("Input Flower Features")
sepal_length = st.sidebar.slider("Sepal length (cm)", float(df['sepal length (cm)'].min()), float(df['sepal length (cm)'].max()))
sepal_width = st.sidebar.slider("Sepal width (cm)", float(df['sepal width (cm)'].min()), float(df['sepal width (cm)'].max()))
petal_length = st.sidebar.slider("Petal length (cm)", float(df['petal length (cm)'].min()), float(df['petal length (cm)'].max()))
petal_width = st.sidebar.slider("Petal width (cm)", float(df['petal width (cm)'].min()), float(df['petal width (cm)'].max()))

input_data = [[sepal_length, sepal_width, petal_length, petal_width]]

# 4. Prediction
prediction = model.predict(input_data)
predicted_species = target_names[prediction[0]]

# 5. Show result
st.subheader("Prediction")
st.write(f"The predicted flower species is: **{predicted_species}** 🌸")
