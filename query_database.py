from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

CHROMA_PATH = "chroma"


def get_context_text_from_query(query_text: str, candidate: str, k=3):
    embedding_function = OpenAIEmbeddings()
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

    # Search the database, filter by candidate
    results = db.similarity_search_with_relevance_scores(
        query_text, k, filter={"person": candidate}
    )
    if len(results) == 0 or results[0][1] < 0.7:
        return None

    context_text = "\n\n---\n\n".join(
        [document.page_content for document, _ in results]
    )
    return context_text, results
