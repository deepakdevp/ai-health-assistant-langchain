# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an AI Health Assistant built with LangChain that provides medical question-answering capabilities using RAG (Retrieval-Augmented Generation). The system processes medical documents, creates embeddings, and uses a Flask web interface to answer health-related questions.

## Architecture

The application follows a multi-component architecture:

- **Flask Web App** (`app.py`): Main server handling HTTP requests and responses
- **Document Processing** (`src/helper.py`): PDF loading, text chunking, and embedding functions
- **Prompt Engineering** (`src/prompt.py`): System prompts for the medical assistant
- **Vector Store Setup** (`store-index.py`): Pinecone index creation and document ingestion
- **Research Notebook** (`research/trials.ipynb`): Development and testing environment

### Data Flow
1. PDFs in `data/` directory are processed into chunks via `src/helper.py`
2. Text chunks are embedded using HuggingFace sentence-transformers model
3. Embeddings are stored in Pinecone vector database
4. Flask app retrieves relevant context and generates answers using OpenAI GPT-4o
5. RAG chain combines retrieval and generation for medical Q&A

## Development Commands

### Environment Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Install in development mode
pip install -e .
```

### Running the Application
```bash
# Start the Flask development server
python app.py
```
The app runs on http://0.0.0.0:8080 with debug mode enabled.

### Vector Store Management
```bash
# Create/update Pinecone index with PDF documents
python store-index.py
```

### Research and Development
```bash
# Launch Jupyter notebook for experimentation
jupyter notebook research/trials.ipynb
```

## Key Configuration

### Required Environment Variables
- `PINECONE_API_KEY`: Pinecone vector database API key
- `OPENAI_API_KEY`: OpenAI API key for GPT-4o model

### Pinecone Index Configuration
- Index name: "ai-health-assistant-langchain"
- Dimension: 384 (matches sentence-transformers/all-MiniLM-L6-v2)
- Metric: cosine similarity
- Cloud: AWS us-east-1

### Text Processing Settings
- Chunk size: 500 characters
- Chunk overlap: 20 characters
- Retrieval: Top 3 similar documents
- Model: GPT-4o for response generation

## File Structure

- `app.py` - Main Flask application
- `src/helper.py` - Document processing utilities
- `src/prompt.py` - System prompt definitions
- `store-index.py` - Vector store initialization
- `data/` - Medical PDF documents (Medical_book.pdf)
- `research/trials.ipynb` - Development notebook

## Important Notes

The system is designed specifically for medical question-answering using a curated medical document corpus. The assistant is configured to only answer based on provided context and will state "I don't know" for information not in the knowledge base.