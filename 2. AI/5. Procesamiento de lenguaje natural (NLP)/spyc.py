import spacy


def main():
    """Simple spaCy example for NLP processing."""
    try:
        nlp = spacy.load("en_core_web_sm")
    except OSError:
        raise SystemExit(
            "The spaCy model 'en_core_web_sm' is not installed. "
            "Run: python -m spacy download en_core_web_sm"
        )

    text = (
        "spaCy is an open-source library for advanced Natural Language Processing "
        "in Python. It features tokenization, part-of-speech tagging, named entity recognition, "
        "and more."
    )

    doc = nlp(text)

    print("Tokens:")
    for token in doc:
        print(f"{token.text}\t{token.lemma_}\t{token.pos_}\t{token.dep_}")

    print("\nNamed Entities:")
    for ent in doc.ents:
        print(f"{ent.text}\t{ent.label_}")


if __name__ == "__main__":
    main()
