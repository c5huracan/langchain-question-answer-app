from langchain.document_loaders import PyPDFDirectoryLoader
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings

# modifiy this directory path to where your pdfs are located; must use relative pathing
loader = PyPDFDirectoryLoader("../unity-training-docs/") 

pages=loader.load_and_split()

faiss_index = FAISS.from_documents(pages, OpenAIEmbeddings())
user_input = input("Enter your question: ")
docs = faiss_index.similarity_search(user_input, k=2)
for doc in docs:
    print(str(doc.metadata["page"]) + ":", doc.page_content[:300])
