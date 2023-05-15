# langchain-question-answering-script

Using the LangChain PyPDF Directory Loader, the FAISS vectorstore, and OpenAI Embeddings to make a basic question answering python script to query multiple locally stored PDF files. In this case, Unity documentation but this could be a directory with any PDF files with which you would like to interact.

## Installation:

mkdir <new-directory> && cd <new-directory>

git clone https://github.com/c5huracan/langchain-question-answering-script.git

conda create --name <environment-name>

conda activate <environment-name>

conda install python

conda install langchain -c conda-forge

export OPENAI_API_KEY=<your-openai-api-key>

conda install openai

conda install tiktoken

conda install faiss

conda install pypdf

## Running the script:

python unity-gpt.py
