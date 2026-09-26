import streamlit as st


st.title("自己紹介アプリ 🌎")
st.write("このアプリは、自己紹介を簡単に作成してコピーまでできる便利なアプリです。")

lang = st.radio("表示する言語を選んでね / Choose Language", ["日本語 (Japanese)", "English"])


name = st.text_input("名前を入力してください。 / Name")
birthday = st.date_input("あなたの誕生日を入力してください。 / Birthday", value=None)
blood_type = st.select_slider("血液型は？ / Blood Type", options=["A型", "B型", "O型", "AB型"])
age = st.number_input("年齢は？ / Age", min_value=0, max_value=120, value=0)
hobby = st.text_area("趣味は？ / Hobbies")
addicted = st.text_area("ハマっていることは？ / Current Obsession")
TV = st.text_area("好きなテレビ番組は？ / Favorite TV Shows")
skill = st.text_area("得意なことは？ / Skills")
job = st.text_area("将来の夢は？ / Future Dream")

st.markdown("---")


if lang == "日本語 (Japanese)":
    st.subheader("あなたの自己紹介は以下の通りです")
    
    intro_text = f"""【自己紹介】
■ 名前: {name}
■ 誕生日: {birthday if birthday else '未入力'}
■ 血液型: {blood_type}
■ 年齢: {age}歳
■ 趣味: {hobby}
■ ハマっていること: {addicted}
■ 好きなテレビ番組: {TV}
■ 得意なこと: {skill}
■ 将来の夢: {job}"""

    instruction = "※ 右上のアイコンからワンクリックでコピーできます。"

else:
   
    st.subheader("Your Profile in English")
    
    intro_text = f"""【My Profile】
■ Name: {name if name else 'Not specified'}
■ Birthday: {birthday if birthday else 'Not specified'}
■ Blood Type: {blood_type}
■ Age: {age if age > 0 else 'Not specified'}
■ Hobbies: {hobby}
■ Current Obsession: {addicted}
■ Favorite TV Shows: {TV}
■ Skills: {skill}
■ Future Dream: {job}"""

    instruction = "* Click the icon in the upper right corner to copy the text."


st.text_area(lang, value=intro_text, height=280)
st.caption(instruction)


st.snow()
st.write("このアプリは、Streamlitで作成されています。")

