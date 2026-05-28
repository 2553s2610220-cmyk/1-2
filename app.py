import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="연애 코칭 앱",
    page_icon="💌",
    layout="centered"
)

# 제목
st.title("💌 AI 연애 코칭")
st.write("연애 고민을 입력하면 간단한 코칭을 해드립니다.")

# 고민 유형 선택
category = st.selectbox(
    "고민 유형을 선택하세요",
    ["썸", "연애", "이별", "재회", "소개팅"]
)

# 사용자 입력
user_input = st.text_area(
    "고민 내용을 입력하세요",
    height=150,
    placeholder="예: 연락이 점점 뜸해졌어요..."
)

# 코칭 함수
def coaching_answer(category, text):
    if category == "썸":
        return "상대의 반응을 너무 조급하게 해석하지 말고 자연스럽게 대화를 이어가세요."

    elif category == "연애":
        return "감정 표현과 솔직한 대화가 가장 중요합니다."

    elif category == "이별":
        return "지금은 감정을 억누르기보다 충분히 받아들이는 시간이 필요합니다."

    elif category == "재회":
        return "재회는 감정만이 아니라 이전 문제의 해결 가능성이 중요합니다."

    elif category == "소개팅":
        return "처음부터 완벽하려 하지 말고 편안한 분위기를 만드는 데 집중하세요."

    return "조금 더 자세히 이야기해 주세요."

# 버튼
if st.button("코칭 받기 💖"):

    if user_input.strip() == "":
        st.warning("고민 내용을 입력해주세요.")
    else:
        answer = coaching_answer(category, user_input)

        st.success("코칭 결과")
        st.write(answer)

        st.info("💡 너무 불안할수록 상대 반응보다 자신의 감정을 먼저 돌보는 것이 중요해요.")
