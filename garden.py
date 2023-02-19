import spacy

nlp = spacy.load('en_core_web_sm')

# My garden path sentences along with the list of all of them

gardenPath1 = u"The horse raced past the barn fell."
gardenPath2 = u"Helen is expecting tomorrow to be a bad day."
gardenPath3 = u"The florist sent the flowers was pleased."
gardenPath4 = u"The cotton clothing is made of grows in Mississippi."
gardenPath5 = u"Mary gave the child the dog bit a Band-Aid."
gardenpathSentences = [gardenPath1, gardenPath2, gardenPath3, gardenPath4, gardenPath5]

# Creating a loop to tokenise and use entity recognition on each sentence

for sentence in gardenpathSentences:
    doc = nlp(sentence)

    print([token.orth_ for token in doc if not token.is_punct | token.is_space])   # Tokenisation

    print([(i, i.label_, i.label) for i in doc.ents])   # Entity recognition

# Spacy grouped a some words giving as "a bad day" has been considered a date.
# Spacy picked up on Mississippi as a GPE (country,city or state).
# I mostly expected the outcome of what entity recognition has picked up, the only exceptions is the fact it did not
# pick up on the name "Helen" and the grouping of "a bad day".


