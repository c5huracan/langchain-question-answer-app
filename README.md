# langchain-question-answering-script

Using the LangChain PyPDF Directory Loader, the FAISS vectorstore, and OpenAI Embeddings to make a basic question answering python script to query multiple locally stored PDF files. In this case, Unity documentation but this could be a directory with any PDF files with which you would like to interact.

### Installation:

```shell
mkdir new-directory && cd new-directory

git clone https://github.com/c5huracan/langchain-question-answering-script.git

conda create --name new-environment

conda activate new-environment

export OPENAI_API_KEY=your-openai-api-key-here

conda install python

conda install langchain -c conda-forge

conda install openai

conda install tiktoken

conda install faiss

conda install pypdf
```

### Running the script:

`python unity-gpt.py`

## Disclaimer

This script is experimental and not at all ready for production. Please use accordingly. For example, on an individual machine or a non-production environment.

Additionally, the OpenAI API has a cost associated with its usage. Additional details can be found here: https://openai.com/pricing
