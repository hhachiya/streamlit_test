import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.title('My first app')
st.write("Here's our first attempt at using data to create a table:")

st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

st.write("Here's our first attempt at using data to create a line chart:")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])
st.line_chart(chart_data)

st.write("Here's our first attempt at using data to create a bar chart:")
st.bar_chart(chart_data)

df = pd.DataFrame({
    '果物': ['りんご', 'バナナ', 'みかん', 'レモン'],
    '数量': [10, 20, 30, 40],
    '市': ['東京', '大阪', '東京', '大阪']
})

st.write(df)

fig = px.bar(df, x='果物', y='数量', color='市', barmode='group')
st.plotly_chart(fig)

chart_type = st.selectbox('チャートの種類を選択してください', ['折れ線グラフ', '棒グラフ'])
if chart_type == '折れ線グラフ':
    st.line_chart(chart_data)
else:
    st.bar_chart(chart_data)

st.plotly_chart(fig, use_container_width=True)


