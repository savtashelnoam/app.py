import streamlit as st

# ---------------------------------------------------------
# הגדרות עמוד עיקריות
# ---------------------------------------------------------
st.set_page_config(
    page_title="ניתוח וחיזוי הכנסות סרטים | דשבורד פרויקט",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------------------------------------------------
# CSS מותאם אישית – פלטת צבעים: שחור, כתום וצהוב (RTL)
# ---------------------------------------------------------
st.markdown("""
    <style>
    /* כפיית צבע רקע שחור אחיד לכל האפליקציה */
    .stApp, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        background-color: #09090b !important;
        direction: rtl;
        text-align: right;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* כפיית צבע טקסט בהיר וקריא לכל רכיבי ה-Streamlit */
    h1, h2, h3, h4, h5, h6, p, span, li, label, div, .stMarkdown {
        color: #f4f4f5 !important;
    }

    /* כותרת ראשית מעוצבת בכתום וצהוב */
    .main-header {
        text-align: center;
        padding: 25px 15px;
        background: linear-gradient(135deg, #18181b 0%, #09090b 100%);
        border-radius: 12px;
        border: 2px solid #f97316;
        margin-bottom: 30px;
        box-shadow: 0 4px 20px rgba(249, 115, 22, 0.25);
    }
    .main-title {
        font-size: 2.3rem;
        font-weight: 800;
        color: #facc15 !important;
        margin-bottom: 8px;
    }
    .main-subtitle {
        font-size: 1.15rem;
        color: #f97316 !important;
        font-weight: 600;
    }

    /* כרטיסיות מידע ברקע כהה עם מסגרת כתומה/צהובה */
    .metric-card {
        background-color: #18181b !important;
        border: 1px solid #27272a;
        border-radius: 12px;
        padding: 22px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.6);
        transition: transform 0.2s ease, border-color 0.2s ease;
        text-align: center;
        margin-bottom: 20px;
    }
    .metric-card:hover {
        transform: translateY(-3px);
        border-color: #facc15;
    }
    .metric-title {
        color: #a1a1aa !important;
        font-size: 1.05rem;
        font-weight: 600;
        margin-bottom: 8px;
    }
    .metric-value {
        color: #ffffff !important;
        font-size: 2rem;
        font-weight: 800;
    }
    .metric-subtitle {
        color: #f97316 !important;
        font-size: 0.9rem;
        margin-top: 6px;
        font-weight: 600;
    }

    /* קופסאות תוכן ומסקנות (שחור, כתום, צהוב) */
    .insight-box {
        background-color: #18181b !important;
        border-right: 6px solid #f97316;
        border-radius: 10px;
        padding: 22px 25px;
        margin-bottom: 25px;
        line-height: 1.8;
        color: #f4f4f5 !important;
        font-size: 1.05rem;
    }
    .conclusion-box {
        background-color: #18181b !important;
        border-right: 6px solid #facc15;
        border-radius: 10px;
        padding: 22px 25px;
        margin-bottom: 25px;
        color: #ffffff !important;
        line-height: 1.8;
        font-size: 1.05rem;
    }
    .warning-box {
        background-color: #27120a !important;
        border-right: 6px solid #ea580c;
        border-radius: 10px;
        padding: 22px 25px;
        margin-bottom: 25px;
        color: #ffffff !important;
        line-height: 1.8;
        font-size: 1.05rem;
    }

    /* כותרות סעיפים בצהוב בולט */
    .section-header {
        font-size: 1.8rem;
        font-weight: 800;
        color: #facc15 !important;
        border-bottom: 2px solid #27272a;
        padding-bottom: 10px;
        margin-top: 40px;
        margin-bottom: 25px;
    }
    
    .stCaption {
        color: #a1a1aa !important;
        font-size: 0.9rem !important;
    }

    ul {
        margin-right: 20px;
    }
    li {
        margin-bottom: 8px;
        color: #f4f4f5 !important;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# כותרת ראשית (תחילת העמוד)
# ---------------------------------------------------------
st.markdown("""
<div class="main-header">
    <div class="main-title">🎬 פרויקט ניתוח וחיזוי הכנסות סרטים</div>
    <div class="main-subtitle">TMDB 5000 Movie Metadata Dataset | מודל רגרסיה לחיזוי הצלחה מסחרית בקופות הקולנוע</div>
    <div style="color: #d4d4d8; margin-top: 10px; font-weight: 500;">מגיש: בן קוטיקוב | כיתה יא׳</div>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# חלק 1: סקירת הפרויקט והדאטה
# ---------------------------------------------------------
st.markdown('<div class="section-header">📌 1. סקירת הפרויקט והדאטה שנבחר</div>', unsafe_allow_html=True)

st.markdown("""
<div class="insight-box">
    <h3 style="color: #f97316 !important; margin-top: 0;">על מה הדאטה?</h3>
    פרויקט זה מבוסס על מאגר הנתונים <b>TMDB 5000 Movie Metadata</b> המכיל מידע מפורט על אלפי סרטי קולנוע, מאפייני ההפקה שלהם, נתוני פופולריות והכנסות בקופות[cite: 1].<br><br>
    <b>מה מייצגת כל שורה בדאטה?</b><br>
    כל שורה מייצגת <b>סרט קולנוע יחיד</b>, שעבורו נאספו 20 מאפיינים שונים הכוללים נתונים כמותיים (כמו תקציב, הכנסות, אורך סרט) ונתונים קטגוריאליים (כמו ז'אנר, שפת מקור, חברות הפקה)[cite: 1].
</div>
""", unsafe_allow_html=True)

st.subheader("🔍 פירוט 20 המאפיינים בדאטה (עמודות)")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
- **budget** — תקציב הפקת הסרט בדולרים (`Int64`).
- **genres** — ז'אנרים אליהם משויך הסרט (`String JSON`).
- **homepage** — קישור לאתר הרשמי של הסרט (`String`).
- **id** — מזהה ייחודי של הסרט במסד הנתונים (`Int64`).
- **keywords** — מילות מפתח המתארות את העלילה (`String JSON`).
- **original_language** — שפת המקור של הסרט (`String`).
- **original_title** — שם הסרט בשפת המקור (`String`).
- **overview** — תקציר העלילה (`String`).
- **popularity** — מדד הפופולריות ב-TMDB (`Float64`).
- **production_companies** — חברות ההפקה (`String JSON`).
    """)

with col2:
    st.markdown("""
- **production_countries** — מדינות ההפקה (`String JSON`).
- **release_date** — תאריך יציאה לאקרנים (`String`).
- **revenue** — הכנסות הסרט בדולרים (`Int64`). **משתנה המטרה שאותו נחזה (y)**.
- **runtime** — אורך הסרט בדקות (`Float64`).
- **spoken_languages** — השפות המדוברות בסרט (`String JSON`).
- **status** — סטטוס ההפצה (`String`).
- **tagline** — סלוגן שיווקי של הסרט (`String`).
- **title** — שם הסרט באנגלית (`String`).
- **vote_average** — ממוצע הדירוגים בסולם 0–10 (`Float64`).
- **vote_count** — מספר המדרגים (`Int64`).
    """)

st.markdown("---")

# ---------------------------------------------------------
# חלק 2: מדדי הנתונים והממוצעים
# ---------------------------------------------------------
st.markdown('<div class="section-header">📊 2. מידע סטטיסטי ומדדי הנתונים</div>', unsafe_allow_html=True)

# כרטיסיות מדדים מרכזיים
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">סה"כ תצפיות (סרטים)</div>
        <div class="metric-value">4,803</div>
        <div class="metric-subtitle">שורות במאגר הנתונים</div>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">סה"כ מאפיינים</div>
        <div class="metric-value">20</div>
        <div class="metric-subtitle">עמודות לכל סרט</div>
    </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">הכנסות ממוצעות (Revenue)</div>
        <div class="metric-value">$82.26M</div>
        <div class="metric-subtitle">ממוצע בקופות</div>
    </div>
    """, unsafe_allow_html=True)
with col4:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">תקציב ממוצע (Budget)</div>
        <div class="metric-value">$29.04M</div>
        <div class="metric-subtitle">תקציב הפקה ממוצע</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.subheader("📐 ניתוח ממוצעים והתפלגות")

m_col1, m_col2, m_col3 = st.columns(3)

with m_col1:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">💵 תקציב (`budget`)</div>
        <div class="metric-value">$29.04M</div>
        <div class="metric-subtitle">ממוצע תקציב הפקה</div>
    </div>
    """, unsafe_allow_html=True)
    st.caption("נתון הגיוני לתעשיית הקולנוע ההוליוודית, אך מוטה כלפי מעלה בשל מספר קטן של סרטי ענק בתקציבי עתק.")

with m_col2:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">💰 הכנסות (`revenue`)</div>
        <div class="metric-value">$82.26M</div>
        <div class="metric-subtitle">ממוצע הכנסות כולל</div>
    </div>
    """, unsafe_allow_html=True)
    st.caption("מציג רווחיות ממוצעת חיובית, אך ההתפלגות ימנית כיוון שמעט סרטי שובר קופות מרוויחים סכומי שיא.")

with m_col3:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">⏱️ אורך סרט (`runtime`)</div>
        <div class="metric-value">106.88</div>
        <div class="metric-subtitle">דקות (כ-1:47 שעות)</div>
    </div>
    """, unsafe_allow_html=True)
    st.caption("מייצג אורך סטנדרטי ומקובל של סרט קולנוע באורך מלא.")

st.markdown("---")

# ---------------------------------------------------------
# חלק 3: הגדרת מודל החיזוי (y vs X)
# ---------------------------------------------------------
st.markdown('<div class="section-header">🎯 3. הגדרת ארכיטקטורת החיזוי (y vs X)</div>', unsafe_allow_html=True)

col_y, col_x = st.columns(2)

with col_y:
    st.markdown("""
    <div class="insight-box">
        <h2 style="color: #ffffff !important;">🎯 עמודת החיזוי: <code>y</code></h2>
        <h3 style="color: #f97316 !important;">revenue (הכנסות בדולרים)</h3>
        <p><b>סוג משתנה:</b> מספרי רציף (Continuous Numerical).</p>
        <p><b>סוג המודל:</b> מודל רגרסיה (Regression Model).</p>
        <p><b>נימוק לבחירה:</b> מטרת הפרויקט היא לחזות את ההצלחה המסחרית של סרט בקופות. הכנסות הן המדד הכלכלי המרכזי המגדיר הצלחה זו.</p>
    </div>
    """, unsafe_allow_html=True)

with col_x:
    st.markdown("""
    <div class="insight-box">
        <h2 style="color: #ffffff !important;">🧩 המשתנים המסבירים: <code>X</code></h2>
        <ul>
            <li><b>budget (תקציב הפקה):</b> תקציב מניע איכות הפקה, אפקטים ויזואליים, כוכבים ושיווק.</li>
            <li><b>popularity (מדד פופולריות):</b> מציג את רמת העניין, הבאזז והציפייה של הקהל לסרט.</li>
            <li><b>runtime (אורך הסרט בדקות):</b> מראה האם לאורך הסרט יש השפעה על כמות ההקרנות והרווחים.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="warning-box">
    <h4 style="color: #f97316 !important; font-size: 1.2rem;">🛡️ בדיקת זליגת נתונים (Data Leakage Verification)</h4>
    <b>פסילת העמודה <code>vote_count</code> (מספר המדרגים):</b><br>
    זליגת נתונים מתרחשת כאשר משתמשים במשתנה שערכו נודע רק <i>לאחר</i> שאירוע החיזוי כבר התרחש.<br>
    העמודה <code>vote_count</code> נפסלה מלהיות חלק מ-X, כיוון שמספר המדרגים נצבר ומתגלה <b>רק לאחר שהסרט כבר הופץ והקרנותיו בקופות הסתיימו</b>.
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ---------------------------------------------------------
# חלק 4: תובנות ומסקנות מהגרפים
# ---------------------------------------------------------
st.markdown('<div class="section-header">📈 4. תובנות ומסקנות מסקר הגרפים</div>', unsafe_allow_html=True)

st.markdown("""
<div class="conclusion-box">
    <h3 style="color: #facc15 !important; margin-top: 0;">1. גרף תקציב מול הכנסות: Budget vs Revenue (Scatter Plot)</h3>
    <p><b>מסקנה אנליטית:</b> קיים קשר חיובי ברור וחזק בין התקציב לבין ההכנסות בקופות (r = 0.73).</p>
    <p><b>משמעות עסקית:</b> ככל שהושקע תקציב גבוה יותר בהפקת הסרט ובשיווקו, ההכנסות של הסרט נוטות להיות גבוהות יותר באופן משמעותי.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="conclusion-box">
    <h3 style="color: #facc15 !important; margin-top: 0;">2. התפלגות אורך הסרטים: Runtime Distribution (Hist Plot)</h3>
    <p><b>מסקנה אנליטית:</b> אורך רובם המכריע של הסרטים מתרכז בטווח צר שבין 90 ל-120 דקות.</p>
    <p><b>משמעות עסקית:</b> אורך של שעה וחצי עד שעתיים מהווה את הסטנדרט התעשייתי האופטימלי להפצת סרט בקולנוע, המאפשר מספר הקרנות יומי מירבי מבלי לעייף את הצופים.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="conclusion-box">
    <h3 style="color: #facc15 !important; margin-top: 0;">3. מפת מתאמים: Correlation Matrix (Heatmap)</h3>
    <p><b>מסקנה אנליטית:</b> המתאם החזק ביותר להכנסות הוא התקציב (r = 0.73), ולאחריו מדד הפופולריות (r = 0.64). לעומת זאת, דירוג האיכות הממוצע (<code>vote_average</code>) מציג מתאם חלש בלבד (r = 0.20).</p>
    <p><b>משמעות עסקית:</b> הצלחה מסחרית של סרט מושפעת משמעותית מתקציב ושיווק ולא בהכרח מביקורות האיכות של הצופים.</p>
</div>
""", unsafe_allow_html=True)

st.caption("בן קוטיקוב | הגשת פרויקט 1 יא׳ - ניתוח וחיזוי הכנסות סרטים")
