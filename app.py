import streamlit as st

# 標題與說明
st.title("紫微ㄋㄟㄋㄟ計算器")

st.markdown("""
### 使用說明 💁‍♀️ 紫微ㄋㄟㄋㄟ在線開掛！

你以為命盤只能算流年？NONONO～  
從命盤也是可以破解命宮裡的罩杯密碼喔 🔮👙  

操作方法超簡單：
1. 請打開你的紫微命盤，認真端詳「命宮、遷移宮、父母宮、疾厄宮」這四個重點宮位有什麼星曜閃閃發亮 ✨  
2. 接著依照這些宮位裡的**主星**、**桃花星**（越多越豐滿）、以及**煞忌星**（會縮水的那種），逐一勾選  
3. ㄋㄟㄋㄟ會幫你算出一個驚人但準確（？）的數值，再對照紫微界祕傳罩杯表，預測你的罩杯大小～  

> 👙 本工具為娛樂用途，由「**大悅老師**」原創發想  
> 📺 出處： [YouTube 影片連結](https://www.youtube.com/watch?v=-s7LXSS6wKo&list=PLJL36iDIoC2w3DEZKelNPzdt4D2-pRsZ-&index=1)  
> 👵 *紫微ㄋㄟㄋㄟ貼心叮嚀：準了不要太驚訝，沒中也別揍我嘿～*
""")

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

st.header("1️⃣ 請將這些宮位中有的主星勾選起來")
selected_main_stars = st.multiselect("主星", list(main_stars.keys()))

# ===== 桃花星（加分）=====
bonus_stars = ["龍池", "鳳閣", "天姚", "文曲", "紅鸞", "天喜"]

st.header("2️⃣ 請將這些宮位中有的桃花星勾選起來（每個+1）")
selected_bonus = st.multiselect("桃花星", bonus_stars)

# ===== 煞忌星（扣分）=====
penalty_stars = ["擎羊", "陀羅", "鈴星", "火星", "化忌"]

st.header("3️⃣ 請將這些宮位中有的煞忌星勾選起來（每個-1）")
selected_penalty = st.multiselect("煞忌星（不含化忌）", penalty_stars[:-1])
huaji_count = st.number_input("化忌出現幾次？", min_value=0, step=1)

# ===== 計算與結果 =====
if st.button("✨ 計算結果"):
    # 主星平均值
    if selected_main_stars:
        main_avg = sum([main_stars[star] for star in selected_main_stars]) / len(selected_main_stars)
    else:
        main_avg = 0

    # 加分與扣分數量
    bonus = len(selected_bonus)
    penalty = len(selected_penalty) + huaji_count

    # 最終分數
    total_score = round(main_avg + bonus - penalty)

    # 罩杯對應表與語錄
    cup_map = {
        1: ("A罩杯", "你命格清新脫俗，低調中自帶靈氣，小心被內行人一眼相中～"),
        2: ("B罩杯", "不張揚但穩當，適合慢熱型戀愛，走到哪都有微光環繞你～"),
        3: ("C罩杯", "剛剛好是最好的安排，桃花不多不少，貴人適時出現～"),
        4: ("D罩杯", "魅力逐漸解鎖中，姻緣開始動起來，出門別忘了帶笑容～"),
        5: ("E罩杯", "哎呀～你真是自帶戀愛體質，走進哪裡都像拍偶像劇！"),
        6: ("F罩杯", "姻緣犯規級別，桃花多到奶奶也看不完，小心桃花債喔～"),
    }

    final_result, comment = cup_map.get(total_score, ("超出範圍 😵", "這命格超出奶奶能預測的範圍，請低調行事..."))

    # 顯示結果
    st.subheader("💡 計算結果")
    st.write(f"主星平均值：{main_avg:.2f}")
    st.write(f"加分：+{bonus}，扣分：-{penalty}")
    st.write(f"最終數值：{total_score}")
    st.success(f"🧙‍♀️ 紫微奶奶預測結果：**{final_result}**\n\n💬 **奶奶開示：** {comment}")
