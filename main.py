import streamlit as st
from PIL import Image
#import time
st.header('Hiranmai Karedla')

st.info('**Data Scientist** | **Machine Learning Engineer** | **Python Backend Developer**')

with st.sidebar:
#     st.markdown("""
#     <div class="circle-image">
#         <img src="Hiranmai.jpeg" alt="My Rectangular Image">
#     </div>

# """, unsafe_allow_html=True)
    st.sidebar.image("Hiranmai.jpeg")
    st.write("Mail: hkaredla@gmu.edu")
    st.write("Mail: hiranmai.karedla@gmail.com")
    st.write("Location: Virginia, USA")
    st.write("Linkedin: https://www.linkedin.com/in/hiranmaikaredla/")
    st.write("Github: https://github.com/HiranmaiKaredla")
    


tab1, tab2, tab3 = st.tabs(["**Experience**", "**Skills**", "**Projects**"])


#expander1 = st.expander(label = "**Experience**", expanded=True)
with tab2:
    st.write("**Programming**: Python, C, C++, R")
    st.divider()
    st.write("**Data Science**: Pytorch, Scikit Learn, Databricks, Spacy, NLP, OpenCV, Tableau, Streamlit, Lambda, ETL ")
    st.divider()
    st.write("**Software**: FastAPI, Flask, Django, Athena, Kafka, Git, Linux, Pyspark, Docker, MongoDB, SQL, Postman ")
    st.divider()
    st.write("**Tools**: AWS, GCP, Azure, Transformers, LLAMA, Langchain, RASA, Tensorflow ")
    st.divider()


with tab1:
    st.warning("**Data Science Researcher**, Center for Air Transportation Systems Research &nbsp;&nbsp;  *Jan 2024 - May 2024*")
    st.write('''
        • Architected predictive models to forecast ice super-saturated regions, curbing contrail formation. Leveraged weather data sourced from NOAA, employing AWS services for data management and analysis.
\n
• Created interactive dashboard analytics for real-time insights and decision-making.
        ''')
    
    st.success("**Data Science Intern**, 22nd Century Technologies &nbsp;&nbsp; *May 2023 - Jul 2023*")
    st.write('''
        • Engineered a robust Llama index-based mechanism using Generative AI to enable quick and accurate answers to user queries from the document set. Streamlined document processing, S3 storage, and vector embeddings with Fastapi.
        ''')
    st.success("**Data Scientist**, Spotflock Technologies &nbsp;&nbsp; *Sep 2020 - Jul 2022*")
    st.write('''
        • Worked on cryptocurrency price prediction project using historical data and statistical indexes with the fbprophet
machine learning models. Created dashboards of price variations with streamlit. Obtained 74% accuracy.
\n
• Developed worker safety helmet detection using object detection models. Revamped the system with Raspberry Pi for real-time alerts with an accuracy of 81%.
\n
• Managed object detection training pipeline integrating computer vision and Neural Network models as an open source SDK feature, incorporating barcode detection and OCR. Implemented dataset upload, model storage on AWS S3, and evaluation metrics using seamless microservice integration.
\n
• Built advanced conversational chatbots with NLP techniques and RASA software, seamlessly integrating them with websites, social media accounts for 3 state government portals’ communication needs.
\n
        ''')
    st.success("**Data Science Engineer**, Nikulsan Technologies  &nbsp;&nbsp; *Aug 2019 - Jul 2020*")
    st.write('''
        • Developed a Neo4j graph database for website traffic and device-data relationships, expanding it into a CRM platform
and integrated with product analytics, resulting in a 12% sales boost through accurate customer matching.
\n
• Implemented live face detection and recognition with Intel OpenVino and Raspberry Pi, enhancing customer identifi- cation and communication, resulting in a 15% conversion rate increase.
        ''')

#     st.write(
#             '''**Data Science Researcher**, Center for Air Transportation Systems Research  &nbsp;&nbsp; Jan 2024 - May 2024\n
# • Architected predictive models to forecast ice super-saturated regions, curbing contrail formation. Leveraged weather data sourced from NOAA, employing AWS services for data management and analysis.
# \n
# • Created interactive dashboard analytics for real-time insights and decision-making.
# \n
# **Data Science Intern**, 22nd Century Technologies May 2023 - Jul 2023 \n
# • Engineered a robust Llama index-based mechanism using Generative AI to enable quick and accurate answers to user queries from the document set. Streamlined document processing, S3 storage, and vector embeddings with Fastapi.
#     \n
#  **Data Scientist**, Spotflock Technologies Sep 2020 - Jul 2022 \n
# • Worked on cryptocurrency price prediction project using historical data and statistical indexes with the fbprophet
# machine learning models. Created dashboards of price variations with streamlit. Obtained 74% accuracy.
# \n
# • Developed worker safety helmet detection using object detection models. Revamped the system with Raspberry Pi for real-time alerts with an accuracy of 81%.
# \n
# • Managed object detection training pipeline integrating computer vision and Neural Network models as an open source SDK feature, incorporating barcode detection and OCR. Implemented dataset upload, model storage on AWS S3, and evaluation metrics using seamless microservice integration.
# \n
# • Built advanced conversational chatbots with NLP techniques and RASA software, seamlessly integrating them with websites, social media accounts for 3 state government portals’ communication needs.
# \n

# **Data Science Engineer**, Nikulsan Technologies Aug 2019 - Jul 2020
# \n
# • Developed a Neo4j graph database for website traffic and device-data relationships, expanding it into a CRM platform
# and integrated with product analytics, resulting in a 12% sales boost through accurate customer matching.
# \n
# • Implemented live face detection and recognition with Intel OpenVino and Raspberry Pi, enhancing customer identifi- cation and communication, resulting in a 15% conversion rate increase.
    
#     '''
#     )

# expander2 = st.expander(label = "Projects")
# expander2.write('project 1')