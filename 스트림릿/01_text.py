### 스트림릿 설치
    # pip install streamlit
### 스트림릿 설치 확인
    # streamlit hello
### 스트림릿 실행
    # streamlit run 파일명.py


import streamlit as st

# 타이틀 만들기
st.title("이것은 타이틀 입니다!")

# 헤더 만들기
st.header("헤더도 입력할 수 있어요!")

# 서브 헤더 만들기
st.subheader("이것은 subheader 입니다!")

# 캡션 만들기
st.caption("캡션도 한 번 넣어 봤습니다.")

# 임의로 코드 만들기
sample_code = '''
def function() : 
    print('hello, world')
'''

# 코드블럭 생성하기
# code(코드가 담긴 변수명, langutage='적용할 언어')
st.code(sample_code, language="python")

# 마크다운 문법에서 볼드체 사용하는법
st.markdown("streamlit은 **마크다운 문법**을 지원합니다.")

# 마크다운 문법에서 선 그리기
st.markdown('---')

# 마크다운 문법에서 텍스트에 색상 적용하기
st.markdown('텍스트의 색상을 :green[초록색]으로, 그리고 **:blue[파란색]** 볼드체로 설정할 수 있습니다.')

# Latex 문법
st.latex(r'\sqrt{x^2+y^2}=1')