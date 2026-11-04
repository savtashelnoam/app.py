import streamlit as st
import pandas as pd

# הגדרת תצורת עמוד
st.set_page_config(page_title="ניתוח דאטה-סט סרטי TMDB", layout="wide")

st.title("🎬 פרויקט 1: הכרות עם דאטה-סט TMDB 5000 Movies")
st.markdown("אפליקציה זו מציגה ניתוח חקרני של נתוני סרטים לקראת בניית מודל רגרסיה לחיזוי הכנסות.")

# טעינת הנתונים מקובץ מקומי
@st.cache_data
def load_data():
    df = pd.read_csv("tmdb_5000_movies.csv")
    return df

df = load_data()

# לשוניות באפליקציה
tab1, tab2, tab3, tab4 = st.tabs(["📋 סקירת הדאטה", "🔍 ערכים חסרים וממוצעים", "🎯 הגדרת החיזוי (y, X)", "📊 גרפים ומסקנות"])

with tab1:
    st.header("סקירה כללית")
    st.write("הדאטה-סט מכיל נתונים על כ-5,000 סרטים מתוך מסד הנתונים TMDB.")
    col1, col2 = st.columns(2)
    col1.metric("מספר שורות (סרטים)", df.shape[0])
    col2.metric("מספר עמודות (מאפיינים)", df.shape[1])
    
    st.subheader("תצוגה מקדימה של הנתונים")
    st.dataframe(df.head())

with tab2:
    st.header("ערכים חסרים ומדדים מרכזיים")
    
    col_a, col_b = st.columns(2)
    
    with col_a:
        st.subheader("ערכים חסרים")
        missing_df = pd.DataFrame({
            'ערכים חסרים': df.isnull().sum(),
            'אחוז (%)': (df.isnull().sum() / len(df) * 100).round(2)
        })
        st.dataframe(missing_df[missing_df['ערכים חסרים'] > 0])
        st.info("הערכים החסרים המרכזיים נמצאים ב-homepage וב-tagline, והם אינם משפיעים על ניתוח מספרי.")

    with col_b:
        st.subheader("ממוצעים מספריים")
        numeric_cols = ['budget', 'revenue', 'runtime', 'popularity', 'vote_average']
        st.dataframe(df[numeric_cols].describe().round(2))

with tab3:
    st.header("הגדרת עמודת החיזוי והמשתנים המנבאים")
    st.success("🎯 **עמודת החיזוי (y):** `revenue` - הכנסות הסרט בקופות בדולרים.")
    
    st.subheader("משתנים לחיזוי (X):")
    st.write("1. **`budget` (תקציב):** תקציב הפקה גבוה קשור ישירות להשקעה בשיווק ובכוכבים.")
    st.write("2. **`popularity` (פופולריות):** מדד הציפייה והעניין של הקהל.")
    st.write("3. **`runtime` (אורך הסרט):** משפיע על כמות ההקרנות היומית בבתי הקולנוע.")
    
    st.warning("⚠️ **בדיקת Data Leakage:** נמנענו משימוש ב-`vote_count` כיוון שהוא נצבר רק לאחר הפצת הסרט.")

with tab4:
    st.header("גרפים ומסקנות")
    
    # גרף 1: גרף פיזור מובנה ב-Streamlit
    st.subheader("1. קשר בין תקציב להכנסות")
    st.scatter_chart(df, x='budget', y='revenue')
    st.caption("מסקנה: קיים קשר חיובי חזק. תקציב גבוה יותר יוצר בדרך כלל הכנסות גבוהות יותר בקופות.")
    
    st.divider()
    
    # גרף 2: התפלגות אורך סרטים (גרף עמודות מובנה ב-Streamlit)
    st.subheader("2. התפלגות אורך הסרטים")
    runtime_counts = df['runtime'].dropna().value_counts(bins=20).sort_index()
    hist_data = pd.DataFrame({
        'כמות סרטים': runtime_counts.values
    }, index=[f"{int(b.left)} עד {int(b.right)}" for b in runtime_counts.index])
    
    st.bar_chart(hist_data)
    st.caption("מסקנה: אורך הסרטים מתרכז בעיקר בטווח של 90–120 דקות.")
    
    st.divider()
    
    # גרף 3: מפת מתאמים מוצגת כטבלה מעוצבת ב-Pandas
    st.subheader("3. מפת מתאמים")
    cols = ['revenue', 'budget', 'popularity', 'runtime', 'vote_average']
    corr_df = df[cols].corr().round(2)
    st.dataframe(corr_df.style.background_gradient(cmap='Blues'), use_container_width=True)
    st.caption("מסקנה: המשתנה בעל המתאם הגבוה ביותר ל-revenue הוא budget (0.73), ולאחריו popularity (0.64).")
