# Langchain OpenAI Document QA
ChatGPT-based chatbot that maybe used for querying on custom, uploadable documents. **(OpenAI paid API key required)**




**Installation & Testing:**
- Install required packages from requirements.txt (run "pip install -r requirements.txt")
- Create ".env" file for storing hidden api keys and store OpenAI API Key in the format "OPENAI_API_KEY=<api_access_token>". \
  ![envsample](https://github.com/noorraghib12/Langchain-OpenAI-Document-QA/blob/main/readme_png/_env_.png)
- Arguments: Only one argument to be added (--vdb) for specifying vector database directory
- Run "streamlit run app.py -- --vdb VECTOR_DATABASE_DIRECTORY" where VECTOR_DATABASE_DIRECTORY is the path in which you want your vector database to persist in. \
![run](https://github.com/noorraghib12/Langchain-OpenAI-Document-QA/blob/main/readme_png/app_sc.png)


**Document Format:**
For now, the chatbot only supports uploading of pdf documents. Changes for txt,docx,etc can be made easily through code in app.py.
