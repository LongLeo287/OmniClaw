import spacy
from spacy.matcher import Matcher

# Load the spaCy model for entity detection
nlp = spacy.load('en_core_web_sm')
def detect_entities(text):
    doc = nlp(text)
    matcher = Matcher(nlp.vocab)
    pattern = [{'ENT_TYPE': 'PERSON'}, {'ENT_TYPE': 'ORG'}]
    matcher.add('Entities', None, pattern)
    matches = matcher(doc)
    entities = [doc[start:end].text for _, start, end in matches]
    return {entity: doc[doc.indexOf(entity)].label_ for entity in entities}