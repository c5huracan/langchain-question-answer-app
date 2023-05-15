# langchain-question-answering-script

Using the LangChain PyPDF Directory Loader, the FAISS vectorstore, and OpenAI Embeddings to make a basic question answering python script to query multiple locally stored PDF files. In this case, Unity documentation but this could be a directory with any PDF files with which you would like to interact.

### Installation:

```shell
git clone https://github.com/c5huracan/langchain-question-answering-script.git
```

```
cd langchain-question-answering-script
```

```
conda env create -f environment.yaml
```

```
conda activate test-env
```

```
export OPENAI_API_KEY=your-openai-api-key-here
```

### Running the script:

```
python unity-gpt.py
```

## Disclaimer

This script is experimental and not at all ready for production. Please use accordingly. For example, on an individual machine or in a non-production environment.

Additionally, the OpenAI API has a cost associated with its usage. Additional details can be found here: https://openai.com/pricing
