import streamlit as st
import pandas as pd
import plotly.express as px

st.title("BMW Used Car Data - Interactive Dashboard")

# Load data
df = pd.read_csv("bmw.csv")

# Clean data
df = df[df['engineSize'] != 0]
df['iselectric'] = df['fuelType'].isin(['Electric', 'Other'])
df_non_electric = df[df['iselectric'] == False]


# Distribution of Fuel Types

st.subheader("Distribution of Fuel Types")

fuel_counts = df['fuelType'].value_counts().reset_index()
fuel_counts.columns = ['fuelType', 'count']

fig1 = px.bar(
    fuel_counts,
    x='fuelType',
    y='count',
    color='fuelType',
    labels={'fuelType': 'Fuel Type', 'count': 'Count'}
)
st.plotly_chart(fig1)


#  Distribution of Transmission

st.subheader("Distribution of Transmission Types")

trans_counts = df['transmission'].value_counts().reset_index()
trans_counts.columns = ['transmission', 'count']

fig2 = px.bar(
    trans_counts,
    x='transmission',
    y='count',
    color='transmission'
)
st.plotly_chart(fig2)


# Year vs Price Trend
avg_year_price = df.groupby('year')['price'].mean().reset_index()

st.subheader("Price Trend Over Years")

fig3 = px.line(
    avg_year_price,
    x='year',
    y='price',
    markers=True
)
st.plotly_chart(fig3)




#  Car Model vs Average Price

st.subheader("Average Price by Car Model")

car_avg = df.groupby('model')['price'].mean().sort_values(ascending=False).reset_index()

fig5 = px.bar(
    car_avg,
    x='model',
    y='price',
    color='price'
)
fig5.update_layout(xaxis={'categoryorder':'total descending'})
st.plotly_chart(fig5)


#  Price Distribution

st.subheader("Distribution of Car Prices")

fig6 = px.histogram(
    df,
    x='price',
    nbins=30,
    marginal='box'
)
st.plotly_chart(fig6)


# Mileage Distribution

st.subheader("Distribution of Mileage")

fig7 = px.histogram(
    df,
    x='mileage',
    nbins=30,
    marginal='box'
)
st.plotly_chart(fig7)


# Correlation Heatmap

st.subheader("Correlation Heatmap")

corr = df[['price','mileage','mpg','engineSize','tax']].corr()

fig8 = px.imshow(
    corr,
    text_auto=True,
    color_continuous_scale='RdBu'
)
st.plotly_chart(fig8)


# Average Price by Transmission

st.subheader("Average Price by Transmission Type")

avg_trans = df.groupby('transmission')['price'].mean().reset_index()

fig9 = px.bar(
    avg_trans,
    x='transmission',
    y='price',
    color='transmission'
)
st.plotly_chart(fig9)


# Top 5 Most Expensive Models

st.subheader("Top 5 Most Expensive Car Models")

top5 = car_avg.head(5)

fig10 = px.bar(
    top5,
    x='model',
    y='price',
    color='price'
)
st.plotly_chart(fig10)
