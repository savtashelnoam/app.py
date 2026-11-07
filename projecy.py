import streamlit as st
import pandas as pd
import kagglehub

# הגדרת תצורת העמוד
st.set_page_config(page_title="TMDB 5000 - פרויקט 1", layout="wide")

# עיצוב מימין לשמאל (RTL)
st.markdown("""
<style>
    html, body, [class*="css"] {
        direction: rtl;
        text-align: right;
    }
    .stMarkdown, p, h1, h2, h3 {
        direction: rtl;
        text-align: right;
    }
</style>
""", unsafe_allow_html=True)

st.title("🎬 פרויקט 1: הכרות עם הדאטה - TMDB 5000 Movies")

# טעינת הנתונים מ-Kaggle
@st.cache_data
def load_data():
    path = kagglehub.dataset_download("tmdb/tmdb-movie-metadata")
    return pd.read_csv(f"{path}/tmdb_5000_movies.csv")

try:
    df = load_data()
except Exception as e:
    st.error(f"שגיאה בטעינת הנתונים: {e}")
    st.stop()

# ---------------------------------------------------------
# סעיף 1: הסבר על הדאטה שנבחר
# ---------------------------------------------------------
st.header("1. הסבר על הדאטה שנבחר")
st.write(
    "הדאטה-סט שנבחר נטען מ-Kaggle ומכיל את מסד הנתונים TMDB 5000 Movies, "
    "כאשר כל שורה בטבלה מייצגת סרט קולנוע יחיד ומכילה מאפיינים שונים כגון תקציב, הכנסות, פופולריות, אורך ופרטי הפקה."
)

# ---------------------------------------------------------
# סעיף 2: מידע על הנתונים (שורות, עמודות, חסרים וממוצעים)
# ---------------------------------------------------------
st.header("2. מידע על הנתונים")

col1, col2 = st.columns(2)
col1.metric("מספר שורות (סרטים)", df.shape[0])
col2.metric("מספר עמודות", df.shape[1])

st.subheader("ערכים חסרים")
missing = df.isnull().sum()
missing_pct = (missing / len(df)) * 100
missing_df = pd.DataFrame({
    'ערכים חסרים': missing,
    'אחוז חסר (%)': missing_pct.round(2)
})
st.dataframe(missing_df[missing_df['ערכים חסרים'] > 0].sort_values(by='ערכים חסרים', ascending=False))

st.subheader("ממוצעים ומדדים סטטיסטיים")
numeric_cols = ['budget', 'revenue', 'runtime', 'popularity', 'vote_average', 'vote_count']
st.dataframe(df[numeric_cols].describe().round(2))

st.write(
    "ממוצע התקציב (budget) הוא כ-29.04 מיליון דולר, נתון הגיוני לתעשיית הקולנוע ההוליוודית אך מוטה כלפי מעלה בשל מספר קטן של סרטי ענק בתקציבים של מאות מיליונים; "
    "ממוצע ההכנסות (revenue) עומד על כ-82.26 מיליון דולר, מציג רווחיות ממוצעת חיובית אך ההתפלגות ימנית כיוון שמעט סרטים מרוויחים סכומי שיא; "
    "וממוצע אורך הסרט (runtime) הוא כ-106.88 דקות (כ-1:47 שעות), המייצג אורך סטנדרטי של סרט קולנוע."
)

# ---------------------------------------------------------
# סעיף 3: מה נרצה לחזות (y) ובאמצעות אילו עמודות (X) כולל נימוקים
# ---------------------------------------------------------
st.header("3. מה נרצה לחזות (y) ובאמצעות אילו עמודות (X)")

st.write(
    "משתנה המטרה לחיזוי (y) הוא revenue (הכנסות בדולרים), משתנה מספרי רציף המייצג הצלחה מסחרית. "
    "העמודות שנבחרו לחיזוי (X) הן budget (תקציב הפקה המניע איכות הפקה, אפקטים ושיווק), "
    "popularity (מדד המציג את העניין והציפייה של הקהל לסרט), "
    "ו-runtime (מראה האם אורך הסרט משפיע על כמות ההקרנות והרווחים). "
    "כדי למנוע Data Leakage, נפסלה העמודה vote_count (מספר המדרגים), כיוון שהיא נצברת ומתגלה רק לאחר שהסרט הופץ והקרנותיו בקופות הסתיימו."
)
