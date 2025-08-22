"""
Helper functions for retrieving and formatting context from Qdrant.

Useful for similarity search and preparing input for language models.
"""


def get_context(user_question, qdrant, k=5):
    """
    Retrieve the top-k most relevant text chunks from a Qdrant vector store.

    This function performs a similarity search using the user's question
    and returns a concatenated string of the retrieved document contents.

    Args:
        user_question (str): The query or question to search for.
        qdrant (QdrantClient): An instance of the Qdrant client with loaded embeddings.
        k (int, optional): Number of top results to retrieve. Defaults to 5.

    Returns:
        str: A single string containing the contents of the top-k documents,
             separated by newline characters.
    """
    docs = qdrant.similarity_search(user_question, k=k)
    return "\n".join([doc.page_content for doc in docs])