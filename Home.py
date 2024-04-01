import streamlit as st

st.set_page_config(
        page_title="Stock Prediction ",
)

st.title("Stock Prediction 📈")
st.subheader("what is stock market?")
st.write("A stock market is a public market where you can buy and sell shares for publicly listed companies. The stocks, also known as equities, represent ownership in the company. The stock exchange is the mediator that allows the buying and selling of shares.")
st.subheader("Importance of Stock market")
st.markdown("Stock markets help companies to raise capital.")
st.markdown("It helps generate personal wealth.")
st.markdown("Stock markets serve as an indicator of the state of the economy.")
st.markdown("It is a widely used source for people to invest money in companies with high growth potential.")
st.subheader("Need of analysis?")
st.write("Stock price analysis has been a critical area of research and is one of the top applications of machine learning. This tutorial will teach you how to perform stock price prediction using machine learning and deep learning techniques. Here, you will use an LSTM network to train your model with yahoo stocks data.")
st.subheader("Model")
st.write(" In this LLM, I have use langchain, openai API, and streamlit to build a stock research tool that can be used by equity research analysts to conduct their research. This end-to-end NLP project will give you a good experience in building a real-life that will add a lot of value to your data scientist or NLP engineer.")
st.write("In Second Part I have build Stock Trend Prediction Web Application in Python. by using an open-source Python library, that makes it easy to build beautiful custom web apps for Machine Learning and Data Science.")
st.sidebar.success("Select a page above.")