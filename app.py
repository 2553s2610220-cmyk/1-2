import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="친구관계 코칭 앱",
    page_icon="🤝",
    layout="centered"
)

# 제목
st.title("🤝 친구관계 코칭")
st.write("친구 고민을 입력하면 간단한 조언을 해드립니다.")

# 고민 유형 선택
category = st.selectbox(
    "고민 유형 선택",
    [
        "친구와 거리감",
        "싸움",
        "무시당하는 느낌",
        "새 친구 만들기",
        "단체생활",
        "배신감"
    ]
)

# 고민 입력
user_input = st.text_area(
    "고민 내용을 입력하세요",
    height=150,
    placeholder="예: 친구가 요즘 저를 피하는 것 같아요..."
)

# 코칭 함수
def friend_coaching(category, text):

    if category == "친구와 거리감":
        return "관계가 멀어졌다고 느껴질 때는 먼저 가볍게 안부를 건네보는 것이 좋습니다."

    elif category == "싸움":
        return "누가 맞는지보다 서로의 감정을 이해하려는 태도가 중요합니다."

    elif category == "무시당하는 느낌":
        return "상대 행동만 해석하기보다 자신의 감정을 차분히 전달해보세요."

    elif category == "새 친구 만들기":
        return "공통 관심사를 중심으로 자연스럽게 대화를 시작해보세요."

    elif category == "단체생활":
        return "모든 사람에게 맞추려 하기보다 편안한 관계 몇 개를 만드는 것이 중요합니다."

    elif category == "배신감":
        return "상처를 무시하지 말고, 관계를 계속 유지할 가치가 있는지 생각해보세요."

    return "조금 더 자세히 이야기해 주세요."

# 버튼
if st.button("코칭 받기 🤍"):

    if user_input.strip() == "":
        st.warning("고민 내용을 입력해주세요.")
    else:
        answer = friend_coaching(category, user_input)

        st.success("코칭 결과")
        st.write(answer)

        st.info("💡 모든 관계에서 가장 중요한 것은 솔직한 대화와 자기 존중입니다.")
