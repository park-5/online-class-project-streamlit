import streamlit as st
from PIL import Image
import folium
from streamlit_folium import st_folium
import time
import pandas as pd
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title='Park.J.H HOME',
    page_icon='💻'
)

game_img = 'game.jpg'
soccer_img = 'soccer.jpg'
sing_img = 'sing.jpg'
school_img = 'osung_high_school.jpg'
osadress_image = 'way_to_school.jpg'



with st.sidebar :
    selected = option_menu(
        menu_title= "park's Page",
        options=['자기소개', '학교소개', '동아리소개', '컴퓨터 부품','디지털 교과서'],
        icons=['fingerprint','bag','suit-club','pc','book']

    )
if selected == '자기소개' :
    st.title('자기소개')

    tab1, tab2 = st.tabs(['자기소개', '취미'])

    with tab1:
        st.subheader('박주하')
        st.write('생년월일 _2006.09.23_')
        st.write('e-mail _pjh2006789@gmail.com_')
        st.write('Phone number _010-9407-5767_')
        st.write('학교 _오성고등학교_')


    with tab2:
        bar1, bar2, bar3 = st.columns([2.6, 2.4, 2])  # columns 세로축

        with bar1:
            st.image(game_img) #게임
            st.write('게임')
        with bar2:
            st.image(soccer_img) #축구
            st.write('축구')
        with bar3:
            st.image(sing_img)#노래 듣기&부르기
            st.write('노래 듣기$부르기')


elif selected == '학교소개':

    st.title('학교소개')
    tab1, tab2, tab3 = st.tabs(['소개', '상징', '특징'])

    with tab1:
        st.header('오성고등학교')
        st.image(school_img, width=500)
        st.subheader('개요')
        st.write('1954년에 개교한 일반계 남자 사립 고등학교이다.')

        st.subheader('주소')
        st.write('대구광역시 수성구 달구벌대로 522길 78')
        m = folium.Map(location=[35.853500, 128.644790], zoom_start=16)
        folium.Marker(
            [35.853500, 128.644790], popup="오성고등학교"
        ).add_to(m)

        st_data = st_folium(m, width=725)

    with tab2: #상징
        st.header('상징')

        st.subheader('교가')
        st.video('https://www.youtube.com/watch?v=7asj3sO8zxs')

        bar1, bar2, bar3 = st.columns([2.5,2.5,2.5])

        with bar1:
            st.subheader('교목')
            image = Image.open('symbol_tree.jpg')
            st.image(image, caption='교목')
            st.write('히말라야시다')
            st.write('높은 기상과 안정의 상징으로 영원한 발전을 기원')
        with bar2:
            st.subheader('교화')
            image = Image.open('symbol_flower.jpg')
            st.image(image, caption='교화')
            st.write('장미')
            st.write('정열적 삶을 실천하고 향기로운 사회의 구성원이 되기를 희망함')
        with bar3:
            st.subheader('교조')
            image = Image.open('symbol_bird.jpg')
            st.image(image, caption='교조')
            st.write('까치')
            st.write('밝고 단아 타인과 사회에 기쁨과 희망을 주는 이타적인 사람이 되기를 기원함')

        st.subheader('교훈')
        st.write('순간적인 감정에 살지 말고 큰 흐름에 나를 찾아라')

    with tab3:
        st.subheader('특징')
        st.write('1. 오성중고등학교로 중학교와 고등학교가 같이 있다.')
        st.write('2. 인근학교에 비해 학생 인원수가 많이 적은 편이다.')
        st.write('3. 학교에 팬싱부가 있으며 오성고 팬싱부 출신으로 금메달리스트 국가대표 구본길, 오은석 선수가 있다.')

elif selected == '동아리소개' :
    st.header('동아리소개')
    st.subheader('공학수학')
    st.write('8명 / 부장 : 박주하')
    st.write('지오지브라를 이용하여 코딩을 하거나 아두이노로 작품을 만드는 활동을 한다')

    video_file = open('geo_string_art.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)
    image1 = Image.open('balancing_robot.jpg')
    st.image(image1, caption='벨런싱 로봇')


elif selected == '컴퓨터 부품' :
    st.title('컴퓨터부품')

    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(['MainBoard', 'CPU', 'Graphics Card','RAM', 'HDD', 'SSD', 'Power Supply'])

    with tab1:
        st.subheader('MainBoard')
        bar1, bar2 = st.columns([2, 2])
        with bar1:
            image = Image.open('mainboard.jpg')
            st.image(image)
        with bar2:
            st.write('컴퓨터 본체를 구성하는 부품 중 하나로 컴퓨터의 각 부품에 전원을 공급하고 부품간에 신호를 주고받는 통로를 담당하므로 순환계이자 신경계로 비유된다.')
            st.write('컴퓨터에는 CPU, 파워 서플라이, DRAM, 그래픽 카드, SSD, HDD 등 수많은 부속 제품들이 들어 있다. '
                     '그런데 이런 부품들이 서로 따로 놀 수는 없는 노릇이라, '
                     '각 부품들을 하나로 연결해주는 회로와 밖으로 신호를 보낼 수 있는 출력 포트를 가지고 있는 부품이 필요한데, '
                     '이 기능들을 가지고 있는 부품이 바로 메인보드이다.')

    with tab2:
        st.subheader('CPU')
        bar1, bar2 = st.columns([2, 2])
        with bar1:
            image1 = Image.open('cpu.jpg')
            st.image(image1)
        with bar2:
            st.write('Central Processing Unit, 중앙 처리 장치')
            st.write('CPU는 컴퓨터에서 기억, 해석, 연산, 제어라는 4대 주요 기능을 관할하는 장치를 말한다.')
            st.write('기억, 해석, 연산, 제어라는 매우 중요한 역할들을 도맡는, 컴퓨터의 대뇌라고 할 정도로 매우 중요한 부분 중 하나다.')


    with tab3:
        st.subheader('Graphics Card(GPU)')
        bar1, bar2 = st.columns([2, 2])
        with bar1:
            image2 = Image.open('gpu.jpg')
            st.image(image2)
        with bar2:
            st.write('그래픽 카드는 CPU의 명령하에 이루어지는 그래픽 작업을 전문적으로 빠르게 처리하고 디지털 신호를 영상 신호로 바꿔 모니터로 전송하는 장치이다.')
            st.write('이미지나 영상을 위한 처리 카드 입니다. 그래픽카드는 특히 게임 그리고 3D 툴을 구동할때 반드시 필요한 요소 이다.')


    with tab4:
        st.subheader('RAM')
        bar1, bar2 = st.columns([2, 2])
        with bar1:
            image3 = Image.open('ram.jpg')
            st.image(image3)
        with bar2:
            st.write('Random Access Memory, 주기억장치')
            st.write('사용자가 자유롭게 내용을 읽고 쓰고 지울 수 있는 기억장치.'
                     '컴퓨터가 켜지는 순간부터 CPU는 연산을 하고 동작에 필요한 모든 내용이 전원이 유지되는 내내 이 기억장치에 저장된다.'
                     '주기억장치로 분류되며 보통 램이 많으면 한번에 많은 일을 할 수 있기에 책상에 비유되곤 한다.')
            st.write('메인 메모리에 주로 사용되는 RAM은 일반적으로 전원이 차단되면 내용이 지워지는 휘발성 기억 장치이다.')


    with tab5:
        st.subheader('HDD')
        bar1, bar2 = st.columns([2, 2])
        with bar1:
            image4 = Image.open('hdd.jpg')
            st.image(image4)

        with bar2:
            st.write('Hard Disk Drive, 보조기억장치')
            st.write('HDD는 비휘발성, 순차접근이 가능한 컴퓨터의 보조 기억장치이다.')
            st.write('비휘발성 데이터 저장소 가운데 가장 대중적이고 용량 대비 가격이 가장 저렴하다. ')

    with tab6:
        st.subheader('SSD')
        bar1, bar2 = st.columns([2, 2])
        with bar1:
            image5 = Image.open('ssd.jpg')
            st.image(image5)
        with bar2:
            st.write('Solid-state drive')
            st.write('SSD는 기계적 구동부위가 없는 반도체를 사용하는 드라이브이다.'
                     'NAND 플래시 메모리와 고성능 컨트롤러를 탑재하여 C 드라이브 및 HDD의 지위를 대체하고 있는 보조 기억 장치이다.'
                     'Microsoft Windows에서는 반도체 드라이브라는 명칭을 사용한다.')
            st.write('비휘발성 데이터 저장소 가운데 가장 대중적이고 용량 대비 가격이 가장 저렴하다. ')


    with tab7:
        st.subheader('Power Supply')
        bar1, bar2 = st.columns([2, 2])
        with bar1:
            image6 = Image.open('power.jpg')
            st.image(image6)
        with bar2:
            st.write('컴퓨터 부품에 필요한 전압과 전류로 변환해 전원을 공급하는 컴퓨터 부품이다.')
            st.write('직류 변환 파워도 있지만 일반적으로는 220V 가정용 교류 전원을 직류 12V, 5V, 3.3V 등 컴퓨터 부품에 맞는 전압과 전류로 바꿔주는 변압기를 말한다.')
            st.write('컴퓨터의 두뇌가 CPU라면 파워서플라이는 컴퓨터의 심장이라고 불릴 정도로 중요한 부품이다.')



else :
    menu = st.selectbox('chapter', ['1.여러가지 운동', '2.힘', '3.뉴턴운동법칙'])

    if menu == '1.여러가지 운동':
        st.header('1.여러가지 운동')

        ch1 = st.checkbox('(1) 운동의 표현')
        if ch1 :
            st.subheader('(1) 운동의 표현')
            st.write('운동 : 물체의 위치가 시간에 따라 변하는 것을 운동이라 한다.')
            st.write('이동거리와 변위')
            df = pd.DataFrame({
                '개념': ['이동거리', '변위'],
                '정의': ['물체가 이동한 경로의 길이로 크기만 있고 방향은 없는 물리량', '처음 위치에서 나중 위치의 위치 변화량으로, 크기와 방향이 모두 있는 물리량']
            })
            st.dataframe(df)
            st.write('변위의 크기는 처음위치와 나중위치의 직선거리이고, 변위의 방향은 처음위치에서 나중위치를 향하는 방향이다.')

            tog1 = st.toggle('속력')
            if tog1:
                st.latex(r'''속력 = \frac{이동 거리}{걸린 시간} (단위:m/s)''')
                st.write('단위시간 동안 이동거리, 물체의 빠르기')

            tog2 = st.toggle('속도')
            if tog2:
                st.latex(r'''속도 = \frac{변위}{걸린 시간} (단위:m/s)''')
                st.write('단위시간 동안 변위, 물체의 빠르기 + 운동방향')

            tog3 = st.toggle('가속도')
            if tog3:
                st.latex(r'''가속도 = \frac{나중 속도 - 처음 속도}{걸린 시간}''')
                st.latex(r'''= \frac{속도 변화량}{걸린 시간} (단위:m/s^2)''')
                st.write('단위시간 속도변화량, 크기 + 방향')
                st.write('직선운동시')
                df = pd.DataFrame({
                    '상황': ['가속도 방향 = 운동방향', '가속도 방향 <-> 운동방향'],
                    '변화': ['속력 증가', '속력감소']
                })
                st.dataframe(df)

        ch2 = st.checkbox('(2) 운동의 분류')
        if ch2 :
            st.subheader('(2) 운동의 분류')


            col1, col2 = st.columns([1, 1])

            with col1:
                st.write('① 등속직선운동')
                st.write('물체의 속도가 일정한 운동, 빠르기와 운동방향은 변하지 않음 (=등속도 운동)')

            with col2:
                st.write('② 속력만 변하는 운동')
                st.write('물체의 운동방향은 변하지 않고 빠르기만 변하는 가속도 운동')

            col3, col4 = st.columns([1, 1])

            with col3:
                st.write('③ 운동방향만 변하는 운동')
                st.write('물체의 빠르기는 변하지 않고 운동 방향만 변하는 가속도 운동')

            with col4:
                st.write('④ 속력과 운동방향이 모두 변하는 운동')
                st.write('일상생활 대부분의 운동, 속력과 운동방향이 함께 변하는 가속도 운동')

        ch3 = st.checkbox('(3) 등가속도 직선 운동')
        if ch3:
            st.subheader('(3) 등가속도 직선 운동')
            st.write('직선상에서 속도가 일정하게 변하는 운동, 가속도가 일정한 직선운동')

            st.latex(r'''처음속도 = v₀ ,  나중속도 = v ,  걸린시간 = t ,  가속도 = a''')
            col1, col2 = st.columns([1, 1])
            with col1:
                st.write('①속도와 시간의 관계')
                st.latex(r'''속도 변화량 = v-v₀,가속도 a=\frac{v-v₀}{t}''')
                st.write('따라서')
                st.latex(r'''나중속도 v=v₀+at''')

            with col2:
                st.write('② 변위와 시간의 관계')
                st.write('속도-시간 그래프에서 그래프가 시간 축과 이루는 면적은 변위'
                         '따라서')
                st.latex(r'''변위 s=v₀t + \frac{at²}{2}''')

            col3, col4 = st.columns([1, 1])

            with col3:
                st.write('③ 속도 변위 관계')
                st.latex(r'''t=\frac{v-v₀}{a} , s=v₀t+\frac{at²}{2}''')
                st.write('t를 s에 대입하면')
                st.latex(r'''2as=v²-v₀²''')

            with col4:
                st.write('④ 평균속도')
                st.latex(r'''v평균 = \frac{v₀+v}{2}''')

            st.write('⑤ 등가속도 직선운동 그래프')
            image1 = Image.open('physics.jpg')
            st.image(image1)

    elif menu == '2.힘':
        st.header('2.힘')

        ch1 = st.checkbox('(1) 힘')
        if ch1:
            st.subheader('(1) 힘')
            st.write('힘의 표시 : 힘의 3요소인 크기 방향 작용점으로 나타낸다.')
            st.write('힘의 단위 : N(뉴턴)사용')
            st.write('1N은 질량 1kg인 물체를 1m/s²으로 가속시키는 힘')

        ch2 = st.checkbox('(2) 힘의 합성')
        if ch2:
            st.subheader('(2) 힘의 합성')

            col1, col2 = st.columns([1, 1])

            with col1:
                st.write('① 알짜힘(합력)')
                st.write('한 물체에 여러힘 작용할때 물체에 작용한 모든 힘 합친것')

            with col2:
                st.write('② 힘의 합성')
                st.write('물체의 운동방향은 변하지 않고 빠르기만 변하는 가속도 운동')

                col3, col4 = st.columns([1, 1])

                with col3:
                    st.write('• 같은방향, 두 힘 합성')
                    st.write('합력 = 두 힘 크기 합 , 방향 = 두 힘 방향')

                with col4:
                    st.write('• 반대방향, 두 힘 합성 ')
                    st.write('합력 = 두 힘 크기 차, 방향 = 크기가 큰 힘 방향')

        ch3 = st.checkbox('(3) 힘의 평형')
        if ch3:
            st.subheader('(3) 힘의 평형')
            st.write('한 물체에 작용하는 힘들의 합력이 0 일때, 이 힘들이 서로 평형을 이룬다고 한다.')

            st.write('① 정지해 있거나 등속 직선 운동(등속도 운동)을 하는 물체는 힘의 평형 상태')
            st.write('② 한 물체에 작용하는 두 힘의 크기가 같고 방향이 반대이면 두 힘의 평형을 이룸')

    else:
        st.header('3.뉴턴 운동 법칙')


        def page1_1():
            progress_text = "loading ..."
            my_bar = st.progress(0, text=progress_text)

            for percent_complete in range(100):
                time.sleep(0)
                my_bar.progress(percent_complete + 1, text=progress_text)
            time.sleep(0.5)
            my_bar.empty()
            st.subheader("(1)뉴턴 운동 제1법칙")
            st.divider()

        ch1 = st.checkbox('(1)뉴턴 운동 제1법칙')
        if ch1:
            page1_1()

            st.write('관성 : 물체가 자신의 운동상태를 계속 유지하려는 성질')
            st.write('① 정지해있는 물체는 계속 정지해 있으려는 성질이 있다.')
            st.write('② 운동하는 물체는 계속 같은 속도로 운동하려는 성질이 있다.')
            st.write('③ 질량이 클수록 운동상태를 변화시키기 어려우며 관성이 크다.')

            st.write('뉴턴 운동 제1법칙')
            st.write('물체에 작용하는 알짜힘이 0 일때, 정지해 있는 물체는 계속 정지해있고, 운동하는 물체는 계속 등선 직선 운동을 한다.'
                     '이것을 뉴턴 운동 제1법칙(관성 법칙) 이라 한다.')


        def page1_2():
            progress_text = "loading ..."
            my_bar = st.progress(0, text=progress_text)
            for percent_complete in range(100):
                time.sleep(0)
                my_bar.progress(percent_complete + 1, text=progress_text)
            time.sleep(0.5)
            my_bar.empty()
            st.subheader("(2)뉴턴 운동 제2법칙")
            st.divider()


        ch2 = st.checkbox('(2)뉴턴 운동 제2법칙')
        if ch2:
            page1_2()

            st.write('① 힘과 가속도의 관계')
            st.write('질량이 일정하면 가속도는 알짜힘에 비례한다.[a∝F(m:일정)]')
            st.write('② 질량과 가속도의 관계')
            st.write('힘이 일정하면 가속도는 질량에 반비례한다.[a∝1/m(F:일정)]')

            st.write('뉴턴 운동 제2법칙')
            st.write('가속도는 물체에 작용하는 알짜힘에 비례하고 질량에 반비례 한다.'
                         '이것을 뉴턴 운동 제2법칙(가속도 법칙) 이라 한다.')


        def page1_3():
            progress_text = "loading ..."
            my_bar = st.progress(0, text=progress_text)

            for percent_complete in range(100):
                time.sleep(0)
                my_bar.progress(percent_complete + 1, text=progress_text)
            time.sleep(0.5)
            my_bar.empty()
            st.subheader("(3)뉴턴 운동 제3법칙")
            st.divider()


        ch1 = st.checkbox('(3)뉴턴 운동 제3법칙')
        if ch1:
            page1_3()

            st.write('작용 반작용 : 힘은 두 물체 사이의 상호작용으로 항상 쌍으로 작용한다. 이때 두 힘은 크기가 같고 방향은 반대이다.'
                     '이때 각각의 힘을 작용 반작용 이라고 한다.')
            st.write('뉴턴 운동 제3법칙')
            st.write('작용 반작용은 항상 크기가 같고 방향은 반대이다. 이를 뉴턴 운동 제3법칙(작용 반작용 법칙)이라 한다.')
            # ①②③④⑤⑥