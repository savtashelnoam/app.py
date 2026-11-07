%%writefile app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="TMDB Movie Analysis", layout="wide")
st.title("🎬 פרויקט 1: הכרות עם דאטה-סט TMDB 5000 Movies")

@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/algoscale/TMDB-5000-Movies-Analysis/master/tmdb_5000_movies.csv"
    return pd.read_csv(url)

df = load_data()

tab1, tab2, tab3, tab4 = st.tabs(["📋 סקירת הדאטה", "🔍 ערכים חסרים וממוצעים", "🎯 הגדרת החיזוי (y, X)", "📊 גרפים ומסקנות"])

with tab1:
    st.header("סקירה כללית")
    col1, col2 = st.columns(2)
    col1.metric("מספר שורות (סרטים)", df.shape[0])
    col2.metric("מספר עמודות", df.shape[1])
    st.dataframe(df.head())

with tab2:
    st.header("ערכים חסרים וממוצעים")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("ערכים חסרים")
        missing = df.isnull().sum()
        st.dataframe(missing[missing > 0])
    with col2:
        st.subheader("מדדים מספריים")
        st.dataframe(df[['budget', 'revenue', 'runtime', 'popularity', 'vote_average']].describe().round(2))

with tab3:
    st.header("מטרת החיזוי")
    st.success("🎯 **עמודת החיזוי (y):** revenue (הכנסות בדולרים)")
    st.info("💡 **משתנים לחיזוי (X):** budget, popularity, runtime (ללא Data Leakage)")

with tab4:
    st.header("גרפים ומסקנות")
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.scatterplot(data=df, x='budget', y='revenue', ax=ax, color='blue')
    ax.set_title("Budget vs Revenue")
    st.pyplot(fig)
    st.caption("מסקנה: קיים קשר חיובי חזק בין תקציב הסרט להכנסותיו.")
