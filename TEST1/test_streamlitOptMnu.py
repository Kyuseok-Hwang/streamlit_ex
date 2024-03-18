import streamlit as st
from streamlit_option_menu import option_menu

# 옵션 메뉴 생성
selected = option_menu(
    menu_title=None, # 메뉴 타이틀 (선택 사항)
    options=["Home", "Settings", "About"], # 메뉴 옵션들
    icons=["house", "gear", "info-circle"], # 아이콘들 (선택 사항)
    menu_icon="cast", # 메뉴 아이콘 (선택 사항)
    default_index=0, # 기본 선택 인덱스 (선택 사항)
)

# 선택된 옵션에 따른 액션
if selected == "Home":
    st.write("This is the home page")
elif selected == "Settings":
    st.write("Here are some settings")
elif selected == "About":
    st.write("This is the about page")