from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

from infer_candidates import infer_candidate_fuzzy
from query_database import get_context_text_from_query
from prompt_template import get_prompt_with_context
from models.candidate_model import Candidate

# Load environment variables from .env file
load_dotenv()


def main():
    query_text = "Provide details such as name, birth date and DNI for the candidate Alfonso Lopez Chau."

    inferred_candidate = infer_candidate_fuzzy(query_text)
    if inferred_candidate is None:
        print("No candidate information could be inferred from the query.")
        return

    context_text_and_results = get_context_text_from_query(
        query_text, candidate=inferred_candidate
    )
    if context_text_and_results is None:
        print("No relevant context found for the query.")
        return

    context_text, results = context_text_and_results

    model = ChatOpenAI(model="gpt-4o")
    model_with_structure = model.with_structured_output(Candidate)

    prompt = get_prompt_with_context(context_text, query_text)
    response = model_with_structure.invoke(prompt)

    sources = [doc.metadata.get("source", None) for doc, _ in results]

    print("Prompt:", prompt)
    print("Sources:", sources)
    print("Object:", response)


if __name__ == "__main__":
    main()
