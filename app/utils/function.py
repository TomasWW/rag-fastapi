def get_context(user_question, qdrant, k=5):
    """
    Retrieve the k most relevant text chunks from Qdrant
    and concatenate them as context for the LLM.
    """
    docs = qdrant.similarity_search(user_question, k=k)
    context = "\n".join([doc.page_content for doc in docs])
    return context