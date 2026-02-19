from rapidfuzz import process, fuzz
from pathlib import Path

DATA_PATH = "data/hojas-vida"


def get_all_candidates_slug():
    paths = Path(DATA_PATH).glob("*.pdf")
    return [p.stem for p in paths]


def normalize(text: str):
    return text.lower().replace(" ", "-")


def infer_candidate_fuzzy(query_text: str):
    query_norm = normalize(query_text)

    choices = get_all_candidates_slug()

    best_match = process.extractOne(query_norm, choices, scorer=fuzz.partial_ratio)

    if best_match and best_match[1] > 80:  # Threshold for a good match
        return best_match[0]
    return None
