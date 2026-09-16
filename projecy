import streamlit as st

st.title("🍹 מחשבון חלוקת חשבון במסעדה")

st.caption("אפליקציה קטנה שעוזרת לחשב כמה כל אחד צריך לשלם במסעדה")

name = st.text_input("מה השם שלך?")
num_people = st.number_input("כמה אנשים אתם?", min_value=1, step=1)
total_bill = st.number_input("מה סכום החשבון הכולל (בש\"ח)?", min_value=0.0, step=5.0)

if st.button("חשב חלוקה"):
    
    if not name:
        st.warning("נא להזין שם כדי להמשיך.")
    elif total_bill <= 0:
        st.error("סכום החשבון חייב להיות גדול מ-0!")
    else:
    
        amount_per_person = total_bill / num_people
        
        st.success("החישוב בוצע בהצלחה!")
        
        st.write(f"היי {name}, החלק של כל אחד מתוך {num_people} האנשים הוא **{amount_per_person:.2f} ש\"ח**.")
