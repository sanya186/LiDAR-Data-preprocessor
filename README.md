# LiDAR Visualizer

This is a LiDAR image visualizer demo using Gradio, designed to upload LiDAR images and apply image processing techniques such as FFT and median filtering.

## Features
- Upload raw LiDAR image (grayscale conversion)
- Apply FFT or Median Filter processing
- Show raw and processed images side-by-side
- Display statistics: mean, median, standard deviation

## How to Run Locally

```bash
pip install -r requirements.txt
python app.py
```

## Project Structure
- `app.py`: Gradio app main script
- `processing.py`: Image processing functions
- `sample_data/`: Sample LiDAR images

## CI/CD
Includes a GitHub Actions workflow for testing (if added)
