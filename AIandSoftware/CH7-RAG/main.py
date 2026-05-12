import os
from dotenv import load_dotenv
from langchain.chains import RetrievalQA
from langchain.document_loaders import TextLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS

load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")

# Get the absolute path of the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Create the absolute path for the document
doc_path = os.path.join(script_dir, "document.txt")

# Load the document
loader = TextLoader(doc_path)
documents = loader.load()

# Split the document into chunks
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(documents)

# Create embeddings
# Make sure to set your OPENAI_API_KEY as an environment variable
embeddings = OpenAIEmbeddings(api_key=API_KEY)

# Create a FAISS vector store
db = FAISS.from_documents(texts, embeddings)

# Create a retriever
retriever = db.as_retriever()

# Create a RetrievalQA chain
qa = RetrievalQA.from_chain_type(
    llm=OpenAI(), chain_type="stuff", retriever=retriever
)

# Run a query
query = "What color is the sky?"
print(qa.run(query))
