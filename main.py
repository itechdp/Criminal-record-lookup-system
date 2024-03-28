import pandas as pd
import streamlit as st

class Main:
    def __init__(self,file_name) -> None:
        st.header("Criminal Detection System")
        if str(file_name).endswith('.xlsx'):
            self.df = pd.read_excel(file_name)
        else:
            self.df = pd.read_csv(file_name)

        self.df[['Name', 'Crime', 'City', 'Gender']] = self.df[['Name', 'Crime', 'City', 'Gender']].apply(lambda x: x.str.lower())
    

    def information_form(self):
        self.name = st.text_input("Enter Name:")
        self.city = st.text_input('Enter City:')
        self.age = st.number_input("Enter Age:")
        self.gender = st.radio('Select Gender:',['male',"female"])

    def _convert_to_lowercase(self, string):
        return string.lower()
    
    def validate(self):
        self.name = self._convert_to_lowercase(self.name)
        self.city = self._convert_to_lowercase(self.city)
        query_result = self.df[(self.df["Name"] == self.name) & (self.df["City"] == self.city) & (self.df["Age"] == self.age) & (self.df["Gender"] == self.gender)]
        btn_search = st.button("Search Records")
        if btn_search:
            if not query_result.empty:
                st.warning("Criminal Record Found!")
                st.success(f"Crime: {query_result['Crime'].values[0]}")   
                st.success(f"Sentence Length: {query_result['Sentence Length'].values[0]}")
                arrest_date = pd.to_datetime(query_result['Arrest Date'].values[0]).strftime('%d/%m/%Y')
                st.success(f"Arrest Date: {arrest_date}")
    
            else:
                st.success("No Criminal Record Found.")

object = Main('Crime_database(1).xlsx')
object.information_form()
object.validate()