# Ryan GPT🤖
![image](https://github.com/ashakeem/RyanGPT/assets/125868067/b7314fbf-ad8d-423e-af85-11687abd4fdd)


This code is a Streamlit app that allows you to have a chat conversation with the Ryan GPT🤖 language model. It uses the langchain library, which is a wrapper around OpenAI's GPT models.

Please note that this code does not deploy the app due to the author running out of usage for the OpenAI API. However, you can run this code locally on your machine if you have the necessary dependencies and API access.

## Prerequisites
Before running this code, ensure that you have the following dependencies installed:
- Python 3.x
- Streamlit
- langchain
- OpenAI API key

## Getting Started
1. Install the required dependencies by running the following command:
   ```
   pip install streamlit langchain
   ```

2. Set up your OpenAI API key by replacing `st.secrets["openai_api_key"]` with your actual API key.

3. Run the code using the following command:
   ```
   streamlit run your_file.py
   ```

## Usage
Once the app is running, you can interact with the Ryan GPT🤖 chatbot by entering your messages in the chat input box and clicking the "Submit" button. The chat history will be displayed on the screen, showing both the user's messages (in blue) and the bot's responses (in gray).

Please note that due to the usage limits of the OpenAI API, the author of this code ran out of API usage and did not deploy the app. Therefore, you won't be able to use the app with the provided code alone. However, you can adapt the code to use your own API key or explore other deployment options.

## Acknowledgments
This code is based on the langchain library and utilizes the OpenAI GPT model. The langchain library provides convenient abstractions and utilities for working with GPT models in conversational settings.

Please refer to the official documentation of Streamlit, langchain, and OpenAI for more information on their usage and capabilities.
