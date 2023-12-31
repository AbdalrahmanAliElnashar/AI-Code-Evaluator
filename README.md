# 🧑🏻‍💻🔗 CodeMentor App

## Overveiw

CodeMentor Pro is a Streamlit web application that leverages the Google Palm Language Model to evaluate code based on a provided description. The app generates an evaluation considering factors such as code matching, modularity, performance, readability, and cleaning. Additionally, it provides enhancements and recommendations.

## Demp App
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://ai-code-evaluator.streamlit.app/)


## Key Features

- **Code Matching and Insightful Feedback:**
CodeMentor Pro employs advanced algorithms to evaluate the alignment between your code and its provided description. Receive comprehensive insights into modularity, performance, readability, and cleaning, allowing you to understand your code's strengths and areas for improvement.

- **Recommendations for Enhancement:**
Take your code to the next level with CodeMentor Pro's intelligent recommendations. Benefit from precise suggestions aimed at optimizing and elevating your coding standards. Whether you're refining existing code or starting a new project, CodeMentor Pro guides you towards best practices.

- **User-Friendly Interface:**
With a sleek and intuitive interface powered by Streamlit, CodeMentor Pro ensures a seamless user experience. Input your code and description effortlessly, and receive a comprehensive analysis at the click of a button. Streamlined navigation and clear visuals make CodeMentor Pro accessible to developers of all levels.

- **Metric Visualization:**
Gain a clear understanding of your code's performance through visual representations of key metrics. CodeMentor Pro visually presents the percentage of closeness, modularity, performance, readability, and cleaning. These visualizations facilitate quick and informed decision-making, empowering you to make impactful changes to your code.


## Usage
### Getting Started
Install the required Python packages by running:

``` bash
pip install streamlit langchain re
```
Make sure to have a valid Google API key for the Google Palm Language Model. You can obtain one [here](https://makersuite.google.com/app/apikey).

Run the app using the following command:

``` bash
streamlit run app.py
```

#### Description and Code Input
- Enter a description of the code in the "Description" text area.
- Provide the code in the "Code" text area.

#### Evaluation
- Enter your Google API Key in the sidebar.
- Click the "Evaluate" button to initiate the code evaluation.

#### Code Insights
- The app calculates percentages for Closeness, Modularity, Performance, Readability, and Cleaning of the code.
- The evaluation metrics are displayed using visuals and metrics in the main app area.


## Sidebar Configuration
Enter your Google API key in the sidebar to unlock the full potential of the Google Palm Language Model.

Need an API key? [Get Google PaLM API key.](https://makersuite.google.com/app/apikey)

## Conclusion
CodeMentor Pro is a tool designed to assist developers in assessing their code based on provided descriptions. It offers insights into code matching, modularity, performance, readability, and cleaning. The app aims to streamline the evaluation process and provide valuable recommendations for code improvement.
