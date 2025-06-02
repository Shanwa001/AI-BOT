This project is a basic AI chatbot built using Streamlit for the frontend and Groq’s API to access the LLaMA 3 70B language model. It allows users to interact with the chatbot in a simple and intuitive chat interface.
The chatbot is initialized with a system message that sets its role and identity, and it responds to user inputs based on this context.
Each message—both user and assistant—is stored in `st.session_state` to maintain chat history during the session. When a user sends a message, it is formatted and sent as a prompt to the LLM, 
and the response is displayed in the chat interface. The model is configured with a temperature of 0 for deterministic output. This project does not include document upload or retrieval features,
meaning it is **not a Retrieval-Augmented Generation (RAG)** system. It purely depends on the LLM's own knowledge and prompt engineering. To upgrade this into a PDF-based RAG app, 
it would need additional components like PDF text extraction, embedding generation, vector storage, and similarity-based context retrieval before querying the LLM. As it stands, 
the project serves as a clean and minimal example of a chatbot using LLaMA 3 via Groq.
