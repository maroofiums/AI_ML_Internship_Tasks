
# **Task 4: Context-Aware RAG Chatbot**

**Internship:** AI/ML Engineering – DevelopersHub Corporation

## **Project Overview**

**Task 4** involved building a **context-aware chatbot** using **LangChain** and **Retrieval-Augmented Generation (RAG)**.
The chatbot can **remember previous conversations** and **retrieve information** from a custom document corpus, enabling **intelligent and context-aware responses**.

---

## **Problems / Challenges**

1. **Static chatbot limitations**: Normal chatbots respond only based on pre-trained models, without access to external documents.
2. **Context loss**: Chatbots often forget earlier messages in a conversation.
3. **Information retrieval**: Needed a system to find **relevant information** quickly from a large corpus.

---

## **Solutions / How I Solved It**

1. **Document Embeddings**: Converted all documents into **vector embeddings** using `SentenceTransformer`.
2. **Vector Store**: Stored embeddings in **FAISS** for efficient similarity search.
3. **Context Memory**: Implemented **conversation history** so the chatbot remembers previous messages.
4. **RAG Pipeline**: Integrated retrieval results with **HuggingFace LLM** for generating context-aware answers.
5. **Deployment**: Built a **Streamlit app** for live testing and interaction.

---

## **Skills Gained**

* Conversational AI development
* Document embedding & vector search
* Retrieval-Augmented Generation (RAG)
* HuggingFace LLM integration
* Streamlit-based deployment

---

## **Impact / Results**

* Chatbot can **answer questions using custom corpus** accurately.
* Maintains **context across multiple turns** of conversation.
* Can be **expanded to multiple document sources** or cloud deployment.