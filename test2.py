import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# 一様分布に従ってランダムサンプル
x1 = np.random.rand(100)

# 正規分布に従ってランダムサンプル
x2 = np.random.randn(100)

# dataframeの作成
size = len(x2)
df = pd.DataFrame({"sample value":np.concatenate([x1,x2]), "type": ["uniform random"]*size+["normal random"]*size, "sample index": np.concatenate([np.arange(size),np.arange(size)])})

# 標準出力
st.write("dataframeの表示")
df

# 選択ボックス
chart_type = st.selectbox('グラフの種類を選択してください', ['折れ線グラフ', '散布図'])
if chart_type == '折れ線グラフ':
    fig = px.line(df,x="sample index", y="sample value", color="type")
else:
    fig = px.scatter(df,x="sample index", y="sample value", color="type")

st.plotly_chart(fig)


