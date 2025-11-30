from langchain_core.prompts import PromptTemplate
from langchain_community.llms import CTransformers
import ctransformers

# Load Llama 2 model
def load_llm(model_path="Models/llama-2-7b-chat.ggmlv3.q8_0.bin", gpu_layers=50, max_tokens=256, temperature=0.01):
    llm = CTransformers(
        model=model_path,
        model_type='llama',
        gpu_layers=gpu_layers,
        config={'max_new_tokens': max_tokens, 'temperature': temperature}
    )
    return llm

# Generate blog using prompt
def generate_blog(llm, input_text, no_of_words, blog_style):
    template = """Write a blog for {blog_style} job profile for a topic {input_text} within {no_of_words} words"""
    prompt = PromptTemplate(
        input_variables=["blog_style","input_text","no_of_words"], 
        template=template
    )
    prompt_text = prompt.format(blog_style=blog_style, input_text=input_text, no_of_words=no_of_words)
    response = llm.invoke(prompt_text)
    return response
