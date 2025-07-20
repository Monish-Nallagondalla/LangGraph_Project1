import streamlit as st
import os
from datetime import date

from langchain_core.messages import AIMessage,HumanMessage
from src.langgraphagenticai.ui.uiconfigfile import Config


class LoadStreamlitUI:

    def __init__(self):
        self.config = Config()
        self.user_controls = {}

    def initialize_session(self):
        return {
            "current_step":"requirements",
            'requirements':"",
            'user_storeies':"",
            "po_feedback":"",
            "generated_code":"",
            "review_feedback":"",
            "decision":None
            
        }
    
    def render_requirements(self):
        st.markdown("## Requirements Submission ")

        st.session_state.state['Requirements'] = st.text_area(
            "Enter your requirements:",
            height = 200,
            key="req_input"
        )

        if st.button("submit Requirements ",key= "submit_req"):
            st.session_state.state['current_step'] = "generate_user_stories"
            st.session_state.IsSDLC = True

    def load_streamlit_ui(self):
        st.set_page_config(page_title = '🤖'+ self.config.get_page_title(),layout='wide')
        st.header("🤖 " + self.config.get_page_title())
        st.session_state.timeframe = ''
        st.session_state.IsFetchButtonClicked = False
        st.session_state.IsSDLC = False

        with st.sidebar:
            llm_options = self.config.get_llm_options()
            usecase_options = self.config.get_usecase_options()

            self.user_controls['selected_llm'] = st.selectbox("select LLM",llm_options)

            if self.user_controls['selected_llm'] == 'Groq':

                model_options = self.config.get_groq_model_options()