import pandas as pd
import streamlit as st
import requests
import json

import warnings
warnings.filterwarnings('ignore')

def convert_df(df):
    return df.to_csv(index=False).encode('utf-8')

def main():
    #st.header("ikanam-ai✔️", divider='rainbow')
    api_url = "https://aae5-83-143-66-61.ngrok-free.app/generate"

    st.title("Приведение номенклатуры к официальному Классификатору Строительных Ресурсов")
    txt = st.text_area(
        "⚙️ Как это работает?",
        "Модель на основе ИИ анализирует введенные данные, "
        "используя NLP для распознавания и сопоставления с классификатором,"
        "и возвращает результат с процентом точности."
        )

    tab1, tab2 = st.tabs(["Одно наименование😎📊", "CSV-файл🚀💻"])
    

    with tab1:
        vacancy_url = st.text_input("Введите некорректное наименование :")

        if st.button("Привести к правильному виду",key="single_button"):
            example = vacancy_url
            payload = {'req':example}

            st.markdown(f'<a href="{"https://raw.githubusercontent.com/Y1OV/dl_homework_dashboard/main/logo-2.jpg"}"><img src="{"https://raw.githubusercontent.com/Y1OV/dl_homework_dashboard/main/logo-2.jpg"}" alt="Foo" width="500" height="250"/></a>', unsafe_allow_html=True)


            #st.markdown(f"<span style='color:red'>{'**Неправильный формат** '}{payload['req']}</span>", unsafe_allow_html=True)


            response = requests.post(api_url, json=payload)
            #st.text(response)
            data = json.loads(response.text)

            
            #st.text(data)

            col1, col2 = st.columns(2)
            with col1:
                st.header("**Входное КСР**")
                st.markdown(f"<span style='color:red'>{payload['req']}</span>", unsafe_allow_html=True)

            with col2:
                st.header("**Правильный формат**")
                st.markdown(
                        f"<span style='color:green'>{'Код КСР: '+str(data['predict'][0])}</span>",
                        unsafe_allow_html=True
                    )
                st.markdown(
                        f"<span style='color:green'>{'Название КСР: '+str(data['predict'][1])}</span>",
                        unsafe_allow_html=True
                    )
                st.markdown(
                        f"<span style='color:#FFA500'>{'Степень уверенности: '+str(round(data['predict'][3], 2))}</span>",
                        unsafe_allow_html=True
                    )


            # st.markdown(f"**Правильный формат**")
            # st.markdown(
            #     f"<span style='color:green'>{'Код КСР: '+str(data['predict'][0])}</span>",
            #     unsafe_allow_html=True
            # )
            # st.markdown(
            #     f"<span style='color:green'>{'Название КСР: '+str(data['predict'][1])}</span>",
            #     unsafe_allow_html=True
            # )
            # st.markdown(
            #     f"<span style='color:#FFA500'>{'Степень уверенности: '+str(round(data['predict'][3], 2))}</span>",
            #     unsafe_allow_html=True
            # )
    with tab2:
        st.title('CSV File Uploader')

        # Загружаем CSV файл
        uploaded_file = st.file_uploader("Выберете CSV файл", type="csv")

        if uploaded_file is not None:
            # Читаем CSV файл
            df = pd.read_csv(uploaded_file)
            #st.write(df)

        if st.button("Привести к правильному виду",key="csv_button"):

            st.markdown(f'<a href="{"https://raw.githubusercontent.com/Y1OV/dl_homework_dashboard/main/logo-2.jpg"}"><img src="{"https://raw.githubusercontent.com/Y1OV/dl_homework_dashboard/main/logo-2.jpg"}" alt="Foo" width="500" height="250"/></a>', unsafe_allow_html=True)

            data_for_csv = pd.DataFrame(columns=['name', 'Код КСР', 'Название КСР', 'Коэффициент пересчёта'])

            for i in df['name']:

                example = i
                payload = {'req':example}


                #st.markdown(f"<span style='color:red'>{'**Неправильный формат** '}{payload['req']}</span>", unsafe_allow_html=True)


                response = requests.post(api_url, json=payload)
                data = json.loads(response.text)

                new_row = {'name': i, 'Код КСР': data['predict'][0],
                 'Название КСР': data['predict'][1], 'Коэффициент пересчёта': data['predict'][4]}

                new_row_df = pd.DataFrame([new_row])
                data_for_csv = pd.concat([data_for_csv, new_row_df], ignore_index=True)




                col1, col2 = st.columns(2)
                with col1:
                    st.header("**Входное КСР**")
                    st.markdown(f"<span style='color:red'>{payload['req']}</span>", unsafe_allow_html=True)

                with col2:
                    st.header("**Правильный формат**")
                    st.markdown(
                    f"<span style='color:green'>{'Код КСР: '+str(data['predict'][0])}</span>",
                    unsafe_allow_html=True
                )
                    st.markdown(
                    f"<span style='color:green'>{'Название КСР: '+str(data['predict'][1])}</span>",
                    unsafe_allow_html=True
                )
                    st.markdown(
                    f"<span style='color:#FFA500'>{'Степень уверенности: '+str(round(data['predict'][3], 2))}</span>",
                    unsafe_allow_html=True
                )



                # st.markdown(f"**Правильный формат**")
                # #st.markdown(
                # #    f"<span style='color:green'>{data}</span>",
                # #    unsafe_allow_html=True
                # #)
                # st.markdown(
                #     f"<span style='color:green'>{'Код КСР: '+str(data['predict'][0])}</span>",
                #     unsafe_allow_html=True
                # )
                # st.markdown(
                #     f"<span style='color:green'>{'Название КСР: '+str(data['predict'][1])}</span>",
                #     unsafe_allow_html=True
                # )
                # st.markdown(
                #     f"<span style='color:#FFA500'>{'Степень уверенности: '+str(data['predict'][3])}</span>",
                #     unsafe_allow_html=True
                # )
                st.write("---")
            # data_for_csv
            #data_for_csv['len'] = df['len']
            #data_for_csv['hash'] = df['hash']

            csv = convert_df(data_for_csv)
            st.title('CSV файл с правильными наименованиями')
            st.write('Нажмите на кнопку ниже, чтобы скачать CSV файл.')
            st.download_button(
                        label="Скачать CSV",
                        data=csv,
                        file_name='true.csv',
                        mime='text/csv',
                                )

if __name__ == "__main__":
    main()
