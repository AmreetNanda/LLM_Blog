# AI Blog Generator with Llama 2

Generate high-quality blogs for different job profiles using **Llama 2 Chat 7B** locally.

It includes:
- LLM model 
- A Streamlit interface for entering the blog topics
- A modular codebase
---

## Features

- Generate blogs for different audiences: Researchers, Data Scientists, Common People
- Adjustable word count, creativity (temperature), and GPU layers
- Save generated blogs automatically
- Download blogs as `.txt` files
- Fast local inference with CTransformers and optional GPU acceleration


## Technologies Used:
- Streamlit, Python
- Models used: Llama-2-7b-chat.ggmlv3.q8_0

## Project Structure

```bash
Blog_Generator/
├── app.py # Streamlit app
├── llm_module.py
├── utils.py
├── Models
│   └── Llama-2-7b-chat.ggmlv3.q8_0.bin
├── requirements.txt # Python dependencies
├── Dockerfile # Optional Docker container
├── run.sh # Optional to run the script
└── setup.py # Optional
```
## Installation

## 🛠 Installation (without Docker)

### 1. Clone the repo
```bash
git clone https://github.com/AmreetNanda/LLM_Blog.git
cd Blog_Generator
```
### 2. Requirements.txt
```bash
ctransformers 
langchain 
langchain_community 
streamlit
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Download the model
```bash
Models/llama-2-7b-chat.ggmlv3.q8_0.bin
```

### 5. Run Streamlit app
```bash
streamlit run app.py
```
Open in your browser:
```
👉 http://127.0.0.1:5000/
👉 Enter the blog topic that you want
👉 Click the "submit" button.
👉 The model generates the blog and displays it on the screen
```

## 🐳 Running with Docker (optional)
### Build the image
```bash
docker build -t blog_generator .

```

### Run the container
```bash
docker run -p 8501:8501 blog_generator

```
Open: 👉 http://localhost:8501

## Screenshots
##### Home page
![App Screenshot](https://github.com/AmreetNanda/LLM_Blog/blob/main/Screenshot%202025-11-30%20143837.png)

## Demo
https://github.com/user-attachments/assets/7a3132da-ef45-44de-b31a-5c8b0f7b0de9

## License
[MIT](https://choosealicense.com/licenses/mit/)
