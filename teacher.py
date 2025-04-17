import streamlit as st
import random
import datetime

st.set_page_config(page_title="The Secret Project", page_icon="✨", layout="wide")

# כותרת ופתיחה
st.title("✨ ברוך הבא לעולם ההפתעות של איתי ✨")
st.markdown("""
<style>
.big-font {
    font-size:40px !important;
    color: #4B8BBE;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-font">אתר שלא תדע מה יקרה בו... עד שתלחץ.</p>', unsafe_allow_html=True)

# תצוגת תאריך ושעה
now = datetime.datetime.now()
st.write(f"📅 היום: {now.strftime('%A, %d %B %Y')}")
st.write(f"🕒 השעה: {now.strftime('%H:%M:%S')}")

# תיבת הפתעה
if st.button("🎁 פתח הפתעה"):
    surprises = [
        "אתה גאון, תזכור את זה. 💡",
        "תצא החוצה, תשאף אוויר, ותחזור לכתוב קוד כמו אלוף. 🌳",
        "כל טעות בקוד היא צעד קדימה. תמשיך! 🧠",
        "פיתוח זה לא רק מה שאתה יוצר – זה מי שאתה נהיה. 🚀",
        "תן למוח שלך לעוף. כל רעיון יכול להפוך למציאות. 🧵"
    ]
    st.success(random.choice(surprises))

# טופס משוב נסתר
with st.expander("💬 רוצה לכתוב לי משהו?"):
    name = st.text_input("השם שלך:")
    message = st.text_area("הודעה חשאית:")
    if st.button("שלח הודעה"):
        if name and message:
            st.success("ההודעה נשלחה בהצלחה! (לא באמת 😅 אבל זה מרגיש טוב)")
        else:
            st.warning("מלא גם שם וגם הודעה כדי לשלוח!")

# שאלת קוד
st.header("👨‍💻 אתגר קטן")
st.write("מה לדעתך יודפס בקוד הבא?")
st.code("""
name = "Itay"
print("Hello " + name[::-1])
""", language="python")

answer = st.text_input("תשובתך:")
if answer:
    if answer.lower().strip() in ["hello yati", "hello yati"]:
        st.balloons()
        st.success("תשובה נכונה! אתה קוסם קוד 🧙")
    else:
        st.error("לא מדויק... נסה שוב!")

# סיום
st.markdown("---")
st.markdown("""<center>
Made with 💙 by Itay <br>
לחלום. לבנות. להפתיע.
</center>""", unsafe_allow_html=True)
