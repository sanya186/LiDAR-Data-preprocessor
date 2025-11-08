import gradio as gr
import numpy as np
import cv2
from PIL import Image
import processing

def process_image(img, option):
    img_np = np.array(img.convert("L"))  # grayscale
    if option == "FFT":
        processed = processing.fft_process(img_np)
    elif option == "Median Filter":
        processed = processing.median_filter(img_np)
    else:
        processed = img_np
    stats = {
        "Mean": np.mean(processed),
        "Median": np.median(processed),
        "Std Dev": np.std(processed)
    }
    processed_img = Image.fromarray(processed).convert("L")
    return img, processed_img, stats["Mean"], stats["Median"], stats["Std Dev"]

with gr.Blocks() as demo:
    gr.Markdown("# LiDAR Image Visualizer")
    with gr.Row():
        with gr.Column():
            img_input = gr.Image(label="Upload LiDAR Image", type="pil")
            option = gr.Radio(["FFT", "Median Filter"], label="Processing Option", value="FFT")
            btn = gr.Button("Process")
        with gr.Column():
            raw_img = gr.Image(label="Raw Image")
            proc_img = gr.Image(label="Processed Image")
    with gr.Row():
        mean = gr.Textbox(label="Mean", interactive=False)
        median = gr.Textbox(label="Median", interactive=False)
        stddev = gr.Textbox(label="Standard Deviation", interactive=False)
    btn.click(process_image, inputs=[img_input, option], outputs=[raw_img, proc_img, mean, median, stddev])

if __name__ == '__main__':
    demo.launch()
