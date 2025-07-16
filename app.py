import gradio as gr
import pandas as pd

def get_recommendations(user_input_interests):
    sample_data = pd.DataFrame([
        {"title": "Sample Article", "url": "https://example.com"}
    ])
    return "✅ Test passed", sample_data

demo = gr.Interface(
    fn=get_recommendations,
    inputs=gr.Textbox(label="Enter your interests"),
    outputs=[
        gr.Textbox(label="Status"),
        gr.Dataframe(label="Recommended Articles")
    ],
    title="📰 IntelliFeed Pro - Test Mode",
    description="Minimal test to confirm Hugging Face deployment."
)

demo.launch()