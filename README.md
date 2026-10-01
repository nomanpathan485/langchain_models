# LangChain Learning Repository 🚀

This repository is dedicated to learning and experimenting with **LangChain** and various Large Language Models (LLMs). It serves as a structured playground for exploring chat models, embeddings, and integration with different AI providers.

## 📂 Project Structure

The project is organized by core concepts to make learning progressive:

- **`1.LLMS/`**: Basic demonstrations of interacting with Large Language Models.
- **`2.Chatmodels/`**: Exploration of chat-specific interfaces across different providers:
    - `1.chatmodels_openai.py`: Integration with OpenAI.
    - `2.huggingface.py`: Using Hugging Face models.
    - `3.huggingface_local.py`: Running Hugging Face models locally.
- **`3.Embeddings/`**: Learning about vector representations and semantic search:
    - `1_embedding_openai.py`: Generating embeddings using OpenAI.
    - `2_embedding_huggingface.py`: Generating embeddings using Hugging Face.
    - `3_document_similarity.py`: Practical implementation of document similarity.

## 🛠️ Tech Stack

- **Framework**: [LangChain](https://python.langchain.com/)
- **Language**: Python 3.x
- **Integrations**: 
    - OpenAI
    - Anthropic
    - Google Gemini
    - Hugging Face
- **Utilities**: `python-dotenv` (Environment variables), `numpy`, `scikit-learn`

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd langchain_model
```

### 2. Set up a virtual environment
```bash
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the root directory and add your API keys:
```env
OPENAI_API_KEY=your_openai_key
ANTHROPIC_API_KEY=your_anthropic_key
GOOGLE_API_KEY=your_google_key
HUGGINGFACEHUB_API_TOKEN=your_hf_token
```

## 📚 Learning Goals
- [ ] Understand the difference between LLMs and ChatModels.
- [ ] Implement RAG (Retrieval Augmented Generation) basics using Embeddings.
- [ ] Compare performance and latency between local and cloud-based models.
- [ ] Master prompt engineering within the LangChain ecosystem.

---
*Happy learning!* 🌟
