import streamlit as st
from langchain.llms import GooglePalm
from langchain.prompts import PromptTemplate
import re


# Extract metrices percentages from text
def extract_percentages(text):
    # Define a regular expression pattern to match percentages
    pattern = r'(\w+):\s*(\d{1,2})%\s*'

    # Find all matches in the text
    matches = re.findall(pattern, text)

    # Create a dictionary to store the percentages for each category
    percentages = {}    
    for match in matches:
        category, percentage = match
        percentages[category] = int(percentage)

    return percentages



# Streamlit App
# Page Configuration
st.set_page_config(page_title='🧑🏻‍💻 AI Code Evaluator', page_icon='✍️', layout='wide', initial_sidebar_state='auto')

# Title
c1, c2 = st.columns([0.17, 3], gap='small')

with c1:
    st.caption("")
    st.image("icon.png", width=70)

with c2:
    st.title("AI Code Evaluator")

st.divider()


# Sidebar Section
st.sidebar.title('🐧 AI Code Evaluator')
st.sidebar.write('This app evaluates code based on a description of the code. The app generates the evaluation using the Google Palm Language Model. The app is powered by LLMs and Streamlit.')
st.sidebar.caption('Made by [Abdalrahman Ali Elnashar](https://www.linkedin.com/in/abdalrahman-ali-el-nashar)')
st.sidebar.divider()
palm_api_key = st.sidebar.text_input('Enter your Google API Key:', key='PaLM_api_key', type='password')
st.sidebar.link_button('Get Google PaLM API key', url='https://makersuite.google.com/app/apikey')



# About Section
st.write('In this app you can evaluate your code based on a description of the code.\
          The app will check if the code matches the description or not and how the code is close to the description.\
          The app will also check the Modularity, Performance, Readability and Cleaning of this code.\
         The app also will recommend some enhancements and optimization for the code and then write an enhanced code for you.🙈')




# Description and Code Input
col1, col2 = st.columns(2, gap='large')

with col1:
    st.markdown("<h1 style='text-align: left; color: white; font-size: 40px; margin-bottom: -30px; margin-top: 20px'> ✍️ Description</h1>", unsafe_allow_html=True)

    description = st.text_area(label='Description:', height=300)
with col2:
    st.markdown("<h1 style='text-align: left; color: white; font-size: 40px; margin-bottom: -30px; margin-top: 20px'> 👨🏻‍💻 Code </h1>", unsafe_allow_html=True)

    code = st.text_area(label='Code:', height=300)


# Evaluation Button
col1, col2, col3 = st.columns((2, 1, 2), gap='large')

with col2:
    st.caption('')

    button = st.button('Evaluate', type='primary', use_container_width=True)
    
if button:
        if not palm_api_key:
            st.error('Please enter your Google API Key in the sidebar.')
            st.stop()


# Code Matching
col1, col2 = st.columns((2, 1), gap='large')
with col1:

    if button:
        try:
            st.write('Evaluating code ...')
            st.write('This may take a few minutes.')

            # LLMS [Google Palm] 
            palm = GooglePalm(google_api_key=palm_api_key, temperature=0.6, max_tokens=16000)
            prompt_template = """
            I will give you a code and description of it.
            Imagine that you are a code evaluator tool.
            The First thing create a header section called "Description Matching" to check if the code matches the description or not and create another header called "Closness" to how the code is close to the description.
            The second thing create 4 header sections to check the Modularity, Performance, Readability and Cleaning of this code and give feedback about each section.
            After evaluating create a header section called "Recommendations" to recommend some enhancements and optimization for the code and then write the correct code after a header called "Enhanced Code".
            The last thing create a header called "Conclusion" to write a conclusion about the code.
            take care of that every header section must be started with "##".
            the description: 
            {description}
            the code:
            {code}
            """

            PT_evaluator = PromptTemplate(
            template=prompt_template,
            input_variables= ['description', 'code'])

            prompt = PT_evaluator.format(description=description, code=code)
            result = palm(prompt)
            st.write(result)
        except:
            st.error('Something went wrong! Please try again.')
            st.stop()


# Code Insights 
with col2:
    if button:
        st.write('Evaluating Metrics ...')
        st.write('This may take a few minutes.')

        c1, c2 = st.columns([0.4, 3], gap='large')
        with c1:

            st.image("evaluation.png", width=80)

        with c2:
            st.header('Evaluation Metrics')
        

        # LLMS For Code Insights [Google Palm]
        palm = GooglePalm(google_api_key=palm_api_key, temperature=0.6)
        prompt_template = """
        I will give you a code and description of it.
        Imagine that you are a code evaluator tool.
        Calculate the Percentage of Closeness of the code to the description.
        Calculate Percentage of the Modularity, Performance, Readability, and Cleaning of the code based on Coding Standards.

        The response style must be like this: Closeness: 50%, Modularity: 50%, Performance: 50%, Readability: 50%, Cleaning: 50%.
        Only return the evaluation name and the percentage.
        Don't make Closeness percentage equal to 100% Maximum is 99%.
        Make sure that the percentage is between 0 and 100 and it was calculated correctly.
        the description: 
        {description}
        the code:
        {code}
        """
        PT_code = PromptTemplate(
        template=prompt_template,
        input_variables= ['description', 'code'])

        prompt = PT_code.format(description=description, code=code)
        result = palm(prompt)
        # Extract metrices percentages from text
        percentages = extract_percentages(result)


        # Display Perecentage Metrics 
        c1, c2 = st.columns([0.5, 3], gap='large')
        
        with c1:
    
            st.image("closeness.png", width=70)
            st.image("modularity.png", width=70)
            st.image("performance.png", width=70)
            st.image("readability.png", width=70)
            st.image("cleaning.png", width=70)

        with c2:
           try:
                st.metric(label='Closeness', value=str(percentages['Closeness'])+'%')
                st.metric(label='Modularity', value=str(percentages['Modularity'])+'%')
                st.metric(label='Performance', value=str(percentages['Performance'])+'%')
                st.metric(label='Readability', value=str(percentages['Readability'])+'%')
                st.metric(label='Cleaning', value=str(percentages['Cleaning'])+'%')

           except:
                st.error('Something went wrong! Please try again.')
            
# End of the App