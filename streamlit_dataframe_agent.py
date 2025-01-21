import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain.agents.agent_types import AgentType
from langchain_openai import ChatOpenAI
import openai
import os

# Set page config
st.set_page_config(page_title="Data Analysis Assistant", layout="wide")

# Title and description
st.title("Pandas DataFrame Agent with OpenAI")
st.write("Upload your CSV file and ask questions about your data in natural language.")

# Sidebar for configurations
with st.sidebar:
    st.header("Configuration")
    api_key = st.text_input("Enter your OpenAI API Key", type="password")
    if api_key:
        openai.api_key = api_key  # Set the API key directly using the openai library
        os.environ["OPENAI_API_KEY"] = api_key  # Ensure compatibility with LangChain

    # Model selection
    model_option = st.selectbox(
        "Select OpenAI Model",
        ["gpt-4", "gpt-3.5-turbo"],
        help="GPT-4 is more capable but slower and more expensive"
    )

    # Temperature setting
    temperature = st.slider(
        "Temperature",
        min_value=0.0,
        max_value=1.0,
        value=0.0,
        step=0.1,
        help="Higher values make the output more creative but less precise"
    )

# File uploader
uploaded_file = st.file_uploader("Upload your CSV file", type="csv")

if uploaded_file is not None:
    # Load the data
    try:
        df = pd.read_csv(uploaded_file)

        # Show data info
        st.subheader("Dataset Information")
        col1, col2 = st.columns(2)
        with col1:
            st.write(f"Number of rows: {df.shape[0]}")
            st.write(f"Number of columns: {df.shape[1]}")
        with col2:
            st.write("Columns in dataset:")
            st.write(", ".join(df.columns))

        # Data preview with toggle
        if st.checkbox("Show data preview"):
            st.dataframe(df.head())

        # Basic statistics with toggle
        if st.checkbox("Show basic statistics"):
            st.write(df.describe())

        # Initialize the agent
        if api_key:
            try:
                # Initialize the LangChain agent
                agent = create_pandas_dataframe_agent(
                    ChatOpenAI(temperature=temperature, model=model_option),
                    df,
                    verbose=True,
                    allow_dangerous_code=True, # This cell is commented out, this allows the experimental
                    agent_executor_kwargs={"handle_parsing_errors": True},
                    agent_type=AgentType.OPENAI_FUNCTIONS,  # Adjust based on LangChain version
                )

                # Query interface
                st.subheader("Ask Questions About Your Data")
                st.write("Examples:")
                st.write("- What is the average value of [column]?")
                st.write("- Can you create a visualization of [relationship]?")
                st.write("- What are the top 5 entries by [column]?")

                # Create two columns for the input area
                col1, col2 = st.columns([3, 1])
                with col1:
                    user_query = st.text_input("Enter your question:")
                with col2:
                    analyze_button = st.button("Analyze", use_container_width=True)

                if user_query and analyze_button:
                    with st.spinner("Analyzing your data..."):
                        try:
                            # Get the response from the agent
                            response = agent.run(user_query)

                            # Display the response
                            st.subheader("Analysis Results")
                            st.write(response)

                            # Check if there are any matplotlib figures to display
                            if plt.get_fignums():
                                st.subheader("Visualization")
                                st.pyplot(plt.gcf())
                                plt.clf()  # Clear the figure for the next query

                        except Exception as e:
                            st.error(f"An error occurred during analysis: {str(e)}")

            except Exception as e:
                st.error("Error initializing the AI agent. Please check your API key and try again.")
                st.error(f"Details: {str(e)}")
        else:
            st.warning("Please enter your OpenAI API key in the sidebar to proceed.")

    except Exception as e:
        st.error(f"Error reading the CSV file: {str(e)}")
else:
    st.info("👆 Please upload a CSV file to begin analysis.")

# Add footer
st.markdown("---")
st.markdown("Built with Streamlit, LangChain, and OpenAI")

# Add some helpful tips in the sidebar
with st.sidebar:
    st.markdown("---")
    st.markdown("### Tips")
    st.markdown("""
        - Make sure your CSV file is properly formatted
        - Be specific in your questions
        - Try different temperature settings for varying results
        - GPT-4 generally provides more detailed analysis
    """)
