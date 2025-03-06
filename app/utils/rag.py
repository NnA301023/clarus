from langchain_core.documents import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain_groq import ChatGroq
import os
from PyPDF2 import PdfReader
from dotenv import load_dotenv

load_dotenv()

class RAGSystem:
    def __init__(self):
        # Initialize embeddings
        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2",
            model_kwargs={'device': 'cpu'},
            encode_kwargs={'normalize_embeddings': True}
        )
        
        # Initialize vector store
        self.vector_store = Chroma(
            persist_directory="chroma_db",
            embedding_function=self.embeddings
        )
        
        # Initialize LLM with Groq
        self.llm = ChatGroq(
            api_key=os.getenv('GROQ_API_KEY'),
            model_name="mixtral-8x7b-32768",
            temperature=0.5,
            max_tokens=4096
        )
        
        # Initialize QA chain
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=self.vector_store.as_retriever(
                search_kwargs={"k": 5}
            ),
            verbose=True
        )
        
        # Initialize text splitter
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )
    
    def add_document(self, file_path):
        """Process and add a document to the RAG system."""
        # Extract text from PDF
        if file_path.lower().endswith('.pdf'):
            text = self._extract_text_from_pdf(file_path)
        else:
            with open(file_path, 'r', encoding='utf-8') as f:
                text = f.read()
        
        # Split text into chunks
        chunks = self.text_splitter.split_text(text)
        
        # Create documents
        documents = [Document(page_content=chunk) for chunk in chunks]
        
        # Add to vector store
        self.vector_store.add_documents(documents)
    
    def get_answer(self, question: str) -> str:
        """Get answer for a question using the RAG system."""
        try:
            result = self.qa_chain.invoke(question)
            return result['result']
        except Exception as e:
            raise Exception(f"Error getting answer: {str(e)}")
    
    def _extract_text_from_pdf(self, pdf_path: str) -> str:
        """Extract text from a PDF file."""
        with open(pdf_path, 'rb') as file:
            pdf_reader = PdfReader(file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
        return text
