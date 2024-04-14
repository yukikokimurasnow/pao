import streamlit as st
import numpy as np
import pandas as pd

st.title('PAO Beauty Tone')
#Toneは情筋を鍛えることを示唆し、健康的で美しい表情を目指すことを表現している

import datetime
import streamlit as st

min_date = datetime.date(2024, 4, 1)
max_date = datetime.date(2100, 12, 31)
d = st.sidebar.date_input('1.日付を選択してください', min_value=min_date, max_value=max_date)