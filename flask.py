from flask import Flask, flash, jsonify, render_template, request,g
from st_app import (get_pdf_text,
                    get_text_chunks,
                    get_vectorstore,
                    get_conversation_chain,
                    load_conversation)
from dotenv import load_dotenv

parser = argparse.ArgumentParser()

parser.add_argument("--vdb",type=str,default="./vector_db",help="Add directory for vectorstore database")
args=parser.parse_args()
VECTORSTORE_DIR=args.vdb



app=Flask(__name__)
load_dotenv()

if "conversation" not in g:
    g.conversation=load_conversation(VECTORSTORE_DIR)
if "chat_history" not in g:
    g.chat_history=None

def handle_userinput(user_question):
    response=g.conversation({"question": user_question})
    return response['chat_history']
    # for i, message in enumerate(g.chat_history):
    #     if i%2==0:
    #         st.write(user_template.replace(
    #             "{{MSG}}",message.content),unsafe_allow_html=True)
    #     else:
    #         st.write(bot_template.replace(
    #             "{{MSG}}",message.content),unsafe_allow_html=True)


@app.route('/',methods=['GET','POST'])
def index():
    user_question=request.form['user_q']
    g.chat_history=handle_userinput(user_question)
    return render_template('query.html',chat_history=g.chat_history)

@app.route('/upload',methods=["POST"])
def load_docs():
    pdf_docs=request.form['pdf_docs']
    raw_text=get_pdf_text(pdf_docs)
    text_chunks=get_text_chunks(raw_text)
    vectorstore=get_vectorstore(text_chunks)
    g.conversation=get_conversation_chain(vectorstore)
    return render_template('uploads.html')

