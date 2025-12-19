import streamlit as st
import google.generativeai as genai

# --- 初期設定 ---
API_KEY = "DMMIYAZAKI01"
genai.configure(api_key=API_KEY)

# ページの設定
st.set_page_config(page_title="チーム専用AIツール", layout="centered")

st.title("🚀 チーム専用 Gemini ツール")
st.write("AI Studioで作成したロジックをここで動かせます。")

# --- UI部分 ---
user_input = st.text_area("依頼内容を入力してください:", height=150)

if st.button("AIに依頼する"):
    if user_input:
        with st.spinner("AIが考えています..."):
            try:
                # AI Studioで設定したモデル名
                model = genai.GenerativeModel('gemini-1.5-flash')
                
                # AIへのリクエスト
                response = model.generate_content(user_input)
                
                # 結果表示
                st.subheader("回答結果:")
                st.success(response.text)
            except Exception as e:
                st.error(f"エラーが発生しました: {e}")
    else:
        st.warning("何か文字を入力してください。")