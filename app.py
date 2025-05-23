import streamlit as st

# ===== 美化標題區 =====
st.markdown("""
<div style="background-color:#f0f0ff; padding:20px; border-radius:10px; text-align:center;">
  <h1 style="font-size:26px; font-weight:bold; color:#4B0082;">🔮 『罩』得住的命盤？</h1>
  <p style="font-size:14px; color:gray; margin-top:-10px;">✨ 紫微斗數解析你的 Cup 運！ ✨</p>
</div>
""", unsafe_allow_html=True)

# ===== 使用說明區 =====
st.markdown("""
<br>
<div style='font-size:18px; font-weight:bold;'>🧭 怎麼預測你的罩杯命？看這裡！</div>

- 🗺️ 打開紫微命盤，鎖定 **命宮、遷移宮、父母宮、疾厄宮**  
- 🌸 找出這些宮位中的 **主星**、**桃花星**（越多越豐滿）  
- ⚡ 找出 **煞忌星**（可能會縮水的小可憐）  
- 📊 勾選完畢後，系統將預測你的命定罩杯！
""", unsafe_allow_html=True)

# ===== 主星區 =====
main_stars = {
    "太陽": 4,
    "貪狼": 4,
    "天同": 3,
    "天府": 3,
    "破軍": 3,
    "紫微": 3,
    "太陰": 3,
    "廉貞": 3,
    "天機": 2,
    "七殺": 2,
    "天梁": 2,
    "武曲": 2,
}

st.markdown("<h2 style='font-size:18px;'>1️⃣ 勾選這些宮位中的主星</h2>", unsafe_allow_html=True)
selected_main_stars = st.multiselect("主星", list(main_stars.keys()))

# ===== 桃花星區 =====
bonus_stars = ["龍池", "鳳閣", "天姚", "文曲", "紅鸞", "天喜"]
st.markdown("<h2 style='font-size:18px;'>2️⃣ 勾選這些宮位中的桃花星（每個+1）</h2>", unsafe_allow_html=True)
selected_bonus = st.multiselect("桃花星", bonus_stars)

# ===== 煞忌星區 =====
penalty_stars = ["擎羊", "陀羅", "鈴星", "火星", "化忌"]
st.markdown("<h2 style='font-size:18px;'>3️⃣ 勾選這些宮位中的煞忌星（每個-1）</h2>", unsafe_allow_html=True)
selected_penalty = st.multiselect("煞忌星（不含化忌）", penalty_stars[:-1])
huaji_count = st.number_input("化忌出現幾次？", min_value=0, step=1)

# ===== 計算邏輯與結果顯示 =====
if st.button("✨ 計算結果"):
    if selected_main_stars:
        main_avg = sum([main_stars[star] for star in selected_main_stars]) / len(selected_main_stars)
    else:
        main_avg = 0

    bonus = len(selected_bonus)
    penalty = len(selected_penalty) + huaji_count
    total_score = round(main_avg + bonus - penalty)

    cup_map = {
        1: ("A罩杯", "你命格清新脫俗，低調中自帶靈氣，小心被內行人一眼相中～"),
        2: ("B罩杯", "不張揚但穩當，適合慢熱型戀愛，走到哪都有微光環繞你～"),
        3: ("C罩杯", "剛剛好是最好的安排，桃花不多不少，貴人適時出現～"),
        4: ("D罩杯", "魅力逐漸解鎖中，姻緣開始動起來，出門別忘了帶笑容～"),
        5: ("E罩杯", "哎呀～你真是自帶戀愛體質，走進哪裡都像拍偶像劇！"),
        6: ("F罩杯", "姻緣犯規級別，桃花多到神仙也記不完，小心桃花債喔～"),
    }

    final_result, comment = cup_map.get(total_score, ("超出範圍 😵", "這命格超出能預測的範圍，請低調行事..."))

    st.markdown("<h2 style='font-size:18px;'>💡 計算結果</h2>", unsafe_allow_html=True)
    st.write(f"主星平均值：{main_avg:.2f}")
    st.write(f"加分：+{bonus}，扣分：-{penalty}")
    st.write(f"最終數值：{total_score}")
    st.success(f"🔮 紫微罩杯預測結果：**{final_result}**\n\n💬 **命盤解語：** {comment}")
