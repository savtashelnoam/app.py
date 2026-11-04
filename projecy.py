import streamlit as st
import pandas as pd

# הגדרת תצורת הדף
st.set_page_config(page_title="פרויקט 1 - הכרות עם הדאטה", layout="wide")

st.title("🎬 פרויקט 1: הכרות עם הדאטה-סט")
st.subheader("יצירתה של תבונה: בחירות קטנות, השפעות גדולות")

# טעינת הנתונים מקישור ישיר (למניעת שגיאות קובץ חסר)
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/algoscale/TMDB-5000-Movies-Analysis/master/tmdb_5000_movies.csv"
    return pd.read_csv(url)

df = load_data()

# 1. הסבר על הדאטה שנבחר
st.header("1. הסבר על הדאטה שנבחר")
st.write("""
* **על מה הדאטה-סט:** הנתונים מבוססים על מסד הנתונים TMDB (The Movie Database) ומכילים מידע על כ-5,000 סרטי קולנוע (תקציבים, הכנסות, דירוגים, ז'אנרים ואורך הסרט).
* **מה מייצגת כל שורה:** כל שורה בדאטה-סט מייצגת **סרט קולנוע יחיד**.
""")

st.subheader("תצוגה מקדימה של הנתונים")
st.dataframe(df.head())

st.divider()

# 2. מידע על הנתונים
st.header("2. מידע על הנתונים")

col1, col2 = st.columns(2)
with col1:
    st.metric("מספר שורות (סרטים)", df.shape[0])
with col2:
    st.metric("מספר עמודות", df.shape[1])

col_missing, col_stats = st.columns(2)

with col_missing:
    st.subheader("ערכים חסרים")
    missing = df.isnull().sum()
    missing_df = pd.DataFrame({
        'ערכים חסרים': missing,
        'אחוז חסר (%)': (missing / len(df) * 100).round(2)
    })
    st.dataframe(missing_df[missing_df['ערכים חסרים'] > 0])

with col_stats:
    st.subheader("ממוצעים ומדדים מספריים")
    numeric_cols = ['budget', 'revenue', 'runtime', 'popularity', 'vote_average']
    st.dataframe(df[numeric_cols].describe().round(2))

st.divider()

# 3. מה נרצה לחזות (y) ובאמצעות אילו עמודות (X)
st.header("3. הגדרת משתני החיזוי והנימוקים")

st.success("🎯 **עמודת החיזוי (y):** `revenue` (הכנסות הסרט בקופות בדולרים) - משתנה מספרי רציף המייצג הצלחה מסחרית.")

st.subheader("משתנים לחיזוי (X) ונימוקים:")

st.markdown("""
1. **`budget` (תקציב הסרט):**
   * **נימוק:** תקציב הפקה גבוה מאפשר להשקיע באפקטים, בשחקנים מובילים ובקמפיין שיווק נרחב, המשפיעים ישירות על מכירות הכרטיסים.
2. **`popularity` (מדד פופולריות ב-TMDB):**
   * **נימוק:** משקף את רמת העניין, החיפושים והציפייה של הקהל לסרט.
3. **`runtime` (אורך הסרט בדקות):**
   * **נימוק:** משפיע על כמות ההקרנות היומית שניתן לשבץ בבתי הקולנוע ועל תפיסת הצופה.

---
⚠️ **מניעת Data Leakage:**
נמנענו משימוש בעמודה `vote_count` (מספר המדרגים), כיוון שהיא נצברת ומתגלה רק **לאחר** שהסרט כבר הופץ והכניס את רווחיו בקופות.
""")
