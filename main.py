import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time 

st.title('Streamlit 入門')
 
st.write('プログレスバーの表示')

"start!"

latest_iteration=st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.01)

"done!!"
# -----------------------------------
if st.checkbox('show image'):
 
    img = Image.open('C:/Users/hiramatu/Desktop/pythonwk/Test.jpg')
    #ブラウザの横幅に合わせるuse_column_width
    st.image(img, caption='aiueo',use_column_width='true')
 
# -----------------------------------
option = st.selectbox(
    'あなたが好きな数字を教えて下さい。',
    list(range(1,11))
)
'あなたの好きな数字は、', option, 'です。'
 
# -----------------------------------
st.write('Interactive Widgets')

left_column,right_column=st.columns(2)
left_column.button('右カラムに文字を表示')

#if button:
#    right_column.write('ここは右カラム')

expander = st.expander('問い合わせ')
expander.write('問い合わせ内容をかく')

expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ回答1')

expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ回答2')



