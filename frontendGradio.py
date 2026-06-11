import gradio as gr
from backend import create_index, ask_question

def upload_pdf(pdf):
     if pdf is None:
          return None, "please upload a pdf file."
     index=create_index(pdf.name)

     return index, "PDF uploaded successfully."


def chat(message, history, index):

    if index is None:
        response = "Please upload a PDF file first."
    else:
        response = ask_question(index, message)

    history.append(
        {"role": "user", "content": message}
    )

    history.append(
        {"role": "assistant", "content": response}
    )

    return history

with gr.Blocks(
    fill_height=True,
    css="""
    body {
        background-color: #0f172a;
    }

    .gradio-container {
        background-color: #0f172a !important;
    }

    h1, h2, h3, p {
        color: white !important;
    }
    """
) as demo:

    gr.Markdown("""
    # 🤖 PDF Insight Chatbot
                
    Upload a PDF and ask questions about its content.
    Powered by LlamaIndex + Groq.
    """)

    index_state = gr.State()

    with gr.Row():

        # Left Panel
        with gr.Column(scale=1):

            pdf = gr.File(
                label="Upload PDF",
                file_types=[".pdf"]
            )

            upload_btn = gr.Button(
                "📄 Process PDF"
            )

            upload_status = gr.Textbox(
                label="Status",
                interactive=False
            )

        # Right Panel
        with gr.Column(scale=3):

            chatbot = gr.Chatbot(
                height=700,
                label="Chat with PDF"
            )

            msg = gr.Textbox(
                placeholder="Ask anything about the PDF...",
                label="Question"
            )

            send = gr.Button(
                "🚀 Send"
            )

    upload_btn.click(
        fn=upload_pdf,
        inputs=pdf,
        outputs=[index_state, upload_status]
    )

    send.click(
        fn=chat,
        inputs=[msg, chatbot, index_state],
        outputs=chatbot
    ).then(
        lambda: "",
        outputs=msg
    )

demo.launch(
    theme=gr.themes.Monochrome()
)