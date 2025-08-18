from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from typing import List
from langchain.schema import Document
from langchain.embeddings import HuggingFaceEmbeddings
# Extract text from PDF files
def load_pdf_files(data):
    loader = DirectoryLoader(
        data,
        glob="*.pdf",
        loader_cls=PyPDFLoader
    )

    documents = loader.load()
    return documents


def filter_extracted_data(docs: List[Document]) -> List[Document]:
    """
    Given a list of Document objects, return a new list of Document objects
    containing only 'source' in metadata and the original page_content.
    """
    filtered_extracted_data: List[Document] = []
    for doc in docs:
        src = doc.metadata.get("source")
        filtered_extracted_data.append(
            Document(
                page_content=doc.page_content,
                metadata={"source": src}
            )
        )
    return filtered_extracted_data

# Split the documents into smaller chunks
def text_to_chunks(filtered_extracted_data):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=20,
    )
    chunks = text_splitter.split_documents(filtered_extracted_data)
    return chunks


def download_embedding_model():
    """
    Download and return the HuggingFace embeddings model.
    """
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
    embeddings = HuggingFaceEmbeddings(
        model_name=model_name
    )
    return embeddings