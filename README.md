# Pandas DataFrame Agent for Querying your CSV files

## Overview

The **Pandas DataFrame Agent** is a Streamlit application that allows users to upload a CSV file and analyze their data using natural language queries powered by OpenAI's GPT models and LangChain. This app simplifies data exploration by providing intuitive querying and visualizations without requiring advanced programming knowledge.



Ask Your Data Questions With Your Own AI Data Scientist Using LangChain's Pandas Data Frame Agent and ChatGPT



Interact with your data via question and answer format as well as generate charts and figures with written commands.



The Rundown:

If you don’t know Python, no worries! All of the code is already written, you just need to ask your data questions.

If you know some Python, great! You will most likely understand what is happening under the hood.

If you are a Python expert, even better! You probably understand this better than I do!

In this tutorial, we will explore how to leverage LLMs (Large Language Models) to do Exploratory Data Analysis (EDA), data visualization and interpretation by incorporating Langchain's Pandas Dataframe Agent. EDA is a critical first step in data analysis for data science, academic research and even understanding your own data, personal or business. The process involves exploring the data from multiple angles to begin to see trends that will allow the elucidation of important insights. EDA can include looking at the features (generally the columns in your dataset), maximum and minimums, correlations, building charts and graphs for easy visualization and communication and generating takeaways form your data to inform decisions and take action. Here we will explore the dataset and look at some basic EDA, visualization and statistical techniques using AI.

Pre-requisite step:



Sign up for OpenAI and get an API Key

&#x20;  \- Go to [platform.openai.com]\([https://platform.openai.com/](https://platform.openai.com/)) and sign in with an OpenAI account. You get some free tokens just for signing up so no payment necessary!

&#x20;  \- Click on the lock icon in the left hand tray “API keys”.

&#x20;  \- Click "Create New Secret Key" to generate a new API key.

&#x20;  \- Copy and paste the key somewhere, once you close this window you will not be able to access the key again and will have to generate a new one

---

## Features

### Data Exploration

- Upload CSV files for analysis.
- View dataset information, including the number of rows, columns, and column names.
- Preview the dataset and generate basic statistics.

### AI-Powered Querying

- Use OpenAI's GPT models (e.g., GPT-4, GPT-3.5-turbo) to analyze data.
- Query the dataset in natural language for insights such as averages, relationships, and rankings.
- Create visualizations like scatter plots, bar charts, or line graphs based on your queries.

### Configurable Options

- **API Key Input**: Securely input your OpenAI API key to authenticate the app.
- **Model Selection**: Choose between GPT-4 (more capable) or GPT-3.5-turbo (faster and cheaper).
- **Temperature Adjustment**: Control the creativity of the model's responses.

### Error Handling

- Handles CSV file format errors gracefully.
- Provides detailed feedback if API or agent initialization fails.

---

## Installation

### Prerequisites

- Python 3.8 or higher.
- An OpenAI API key. Obtain your key from [OpenAI](https://platform.openai.com/).

### Required Libraries

Install the dependencies using:

```bash
pip install streamlit pandas matplotlib seaborn langchain langchain-openai openai
```

---

## How to Run the Application

1. Clone the repository or download the source code:

   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

3. Open the app in your browser at `http://localhost:8501` (or the port specified in the terminal).

---

## Usage

### Step 1: Configuration

- Enter your OpenAI API key in the sidebar.
- Select the desired OpenAI model (GPT-4 or GPT-3.5-turbo).
- Adjust the temperature slider for more creative or precise responses.

### Step 2: Upload CSV File

- Use the file uploader to upload a valid CSV file.
- Once uploaded, the app displays dataset information, column names, and optional previews/statistics.

### Step 3: Query the Data

- Enter your natural language query in the text box provided.
- Example queries:
  - "What is the average value of column A?"
  - "Create a scatter plot of column X vs column Y."
  - "What are the top 5 entries by column Z?"
- Click "Analyze" to get the results.

### Step 4: View Results

- The app displays the analysis in text or visual format (if applicable).
- Visualizations (e.g., matplotlib plots) appear in a dedicated section.

---

## Example Queries

1. "What is the correlation between sales and profit?"
2. "Show a bar chart of the top 5 products by revenue."
3. "Calculate the mean, median, and standard deviation of column X."
4. "What are the top 10 countries by population?"

---

## Known Issues

- Some queries may fail if the dataset lacks the required structure or columns.
- Performance may vary based on the size of the dataset and the selected OpenAI model.

---

## Future Enhancements

- Add support for additional file formats (e.g., Excel).
- Integrate advanced visualizations with libraries like Plotly.
- Improve error handling for unsupported queries.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## Acknowledgments

- [Streamlit](https://streamlit.io/) for the framework.
- [LangChain](https://langchain.com/) for enabling natural language data querying.
- [OpenAI](https://platform.openai.com/) for the GPT models.


