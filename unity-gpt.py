from langchain.llms import OpenAI
from langchain.document_loaders import PyPDFDirectoryLoader
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings


loader = PyPDFDirectoryLoader("../unity-training-docs/")

pages=loader.load_and_split()

llm = OpenAI(temperature=0.4)

faiss_index = FAISS.from_documents(pages, OpenAIEmbeddings())
docs = faiss_index.similarity_search("What version of Unity is best to make a 2D game?", k=2)
for doc in docs:
    print(str(doc.metadata["page"]) + ":", doc.page_content[:300])