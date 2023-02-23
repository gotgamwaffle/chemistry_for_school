import streamlit as st

def page1():

    st.header('화학반응 양적 관계 기본 OX QUIZ')
    st.write('<h5>화학반응 양적 관계의 일관적 풀이를 익히기 전에 간단한 워밍업 문제를 풀어보세요!</h5>', unsafe_allow_html=True)
    st.write('<h5>화학반응 양적 관계는 무엇보다도 기본 개념이 가장 중요합니다!</h5>', unsafe_allow_html=True)
    st.write('')
    st.write('')
    st.write('')
    st.write('')

    def answer_give(user_input, answer):
        if user_input == answer:
            return 0
        else:
            return 1

    def ox_quiz(question, answer, key, keyox):
        col1, col2 = st.columns([3, 1])
        with col1:
            user_input = st.radio(question, ['O', 'X'], key=keyox)
        with col2:
            st.write('')
            st.write('')
            st.write('')
            if st.button('Submit', key=key):
                if user_input == answer:
                    st.write('<h5>정답입니다.</h5>', unsafe_allow_html=True)
                    return 0, 0
                else:
                    st.write('<h5>정답이 아닙니다.</h5>', unsafe_allow_html=True)
                    return user_input, answer
        return 0, 0

    # Quiz 1
    st.header('Quiz 1')
    st.write('<h5>원자량은 질량수가 12인 C의 원자량을 12로 정하여 기준으로 삼는다.</h5>', unsafe_allow_html=True)
    user_input, answer=ox_quiz(' ', 'O', 'question1', 'ox1')
    if answer_give(user_input, answer)==1:
        st.write('원자량은 실제 질량이 아닌 상대적인 비율로써, 단위가 존재하지 않습니다.')

    # Quiz 2
    st.header('Quiz 2')
    st.write('<h5>H20 2몰에 들어있는 수소의 몰수는 2몰이다.</h5>', unsafe_allow_html=True)
    user_input, answer = ox_quiz(' ', 'X', 'question2', 'ox2')
    if answer_give(user_input, answer) == 1:
        st.write('H20 1몰에 들어있는 수소는 2몰입니다. 이 문제에서 H20는 2몰 존재하므로 수소는 총 4몰 존재합니다.')

    # Quiz 3
    st.header('Quiz 3')
    st.write('<h5>같은 질량의 질소(N) 원자와 산소(O) 원자의 개수 비는 N:O=7:8이다. (단, N, O의 원자량은 각각 14, 16이다.)</h5>', unsafe_allow_html=True)
    user_input, answer = ox_quiz(' ', 'X', 'question3', 'ox3')
    if answer_give(user_input, answer) == 1:
        st.write('정답은 8:7입니다. 질소 원자(N)과 산소 원자(O)의 원자량의 비가 7:8이므로, 같은 질량에서는 개수비가 그 반대인 8:7이어야 합니다.')
        st.write('예를 들어, 동일한 112g이 존재하는 경우, 질소 원자(N)는 8몰, 산소 원자(O)는 7몰 존재합니다.')

    # Quiz 4
    st.header('Quiz 4')
    st.write('<h5>온도와 압력이 같을 때 기체의 밀도는 분자량에 반비례한다.</h5>', unsafe_allow_html=True)
    user_input, answer = ox_quiz(' ', 'X', 'question4', 'ox4')
    if answer_give(user_input, answer) == 1:
        st.write('1')


    # Quiz 5
    st.header('Quiz 5')
    st.write('<h5>화학 반응식에서 반응물의 계수의 합은 생성물의 계수의 합과 항상 같다.</h5>', unsafe_allow_html=True)
    user_input, answer = ox_quiz(' ', 'X', 'question5', 'ox5')
    if answer_give(user_input, answer) == 1:
        st.write('물 생성 반응으로 예를 들어보겠습니다.')
        st.latex(r'2H_2 + O_2 \longrightarrow 2H_20')
        st.write('이 때, 반응물의 계수의 합은 3인 반면, 생성물의 계수의 합은 2임을 알 수 있습니다.')

    # Quiz 6
    st.header('Quiz 6')
    st.write('<h5>화학 반응식의 계수 비는 반응 몰 비와 같다.</h5>', unsafe_allow_html=True)
    user_input, answer = ox_quiz(' ', 'O', 'question6', 'ox6')
    if answer_give(user_input, answer) == 1:
        st.write('기본적으로 화학 반응에서는 화학 반응식의 계수 비와 동일한 몰 수로 반응합니다.')

    # Quiz 7
    st.header('Quiz 7')
    st.write('<h5>온도와 압력이 일정할 때 화학 반응식의 계수 비는 기체의 반응 부피비와 같다.</h5>', unsafe_allow_html=True)
    user_input, answer = ox_quiz(' ', 'O', 'question7', 'ox7')
    if answer_give(user_input, answer) == 1:
        st.write('이상기체 상태방정식은 다음과 같습니다.')
        st.latex(r'PV = nRT')
        st.write('온도와 압력이 일정하다면, P, T는 상수입니다. R 또한 리드베리 상수입니다.')
        st.write('따라서, n(몰 수)는 V(부피)에 비례합니다.')
        st.write('Quiz 6에 의거하여, 화학 반응식의 계수 비는 반응 몰 비와 동일하기에 기체의 반응의 부피와도 동일합니다.')

    # Quiz 8
    st.header('Quiz 8')
    st.latex(r'2CO(g) + O_2(g) \longrightarrow 2CO_2(g)')
    st.write('<h5>위 화학반응식에서의 반응 질량비는</h5>', unsafe_allow_html=True)
    st.latex(r'CO : O_2 : CO_2 = 2 : 1 : 2')
    st.write('<h5>이다.</h5>', unsafe_allow_html=True)
    user_input, answer = ox_quiz(' ', 'X', 'question8', 'ox8')
    if answer_give(user_input, answer) == 1:
        st.write('Quiz 6에 의거하여, 화학반응식의 계수 비는 반응 몰 비와 동일한 것은 사실이나,')
        st.write('이 것이 반응 질량비와는 동일하지 않습니다.')
        st.write('C의 원자량은 12, O의 원자량은 16이므로')
        st.write('CO의 분자량은 28, O2의 분자량은 32, CO2의 분자량은 44입니다.')
        st.write('따라서 반응 질량비는 다음과 같습니다.')
        st.latex(r'CO : O_2 : CO_2 = 28*2 : 32*1 : 44*2')
        st.write('약분한다면 답은 다음과 같습니다.')
        st.latex(r'CO : O_2 : CO_2 = 7 : 4 : 11')