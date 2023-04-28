# Importing necessary modules(libraries)
import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from gensim.models import Word2Vec

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

# Defining a function to preprocess the sentences
def preprocess(text):
    sentences = sent_tokenize(text)
    tokenized_sentences = [word_tokenize(sentence.lower()) for sentence in sentences]
    preprocessed_sentences = []
    for tokenized_sentence in tokenized_sentences:
        preprocessed_sentence = []
        for word in tokenized_sentence:
            if word not in stop_words and word.isalpha():
                preprocessed_sentence.append(lemmatizer.lemmatize(word))
        preprocessed_sentences.append(preprocessed_sentence)
    return preprocessed_sentences

# Defining a function to generate paraphrases after preprocess
def generate_paraphrases(text):
    preprocessed_sentences = preprocess(text)
    model = Word2Vec(preprocessed_sentences, min_count=1, size=300, workers=4)
    paraphrases = []
    for sentence in preprocessed_sentences:
        for word in sentence:
            similar_words = model.wv.most_similar(word, topn=3)
            for similar_word, score in similar_words:
                paraphrase = ' '.join([w if w != word else similar_word for w in sentence])
                paraphrases.append(paraphrase)
    return paraphrases

# Defining a function to further preprocess the paraphrase
def select_best_paraphrase(paraphrases, text):
    best_paraphrase = paraphrases[0]
    max_similarity = -1
    for paraphrase in paraphrases:
        similarity = text_similarity(text, paraphrase)
        if similarity > max_similarity:
            max_similarity = similarity
            best_paraphrase = paraphrase
    return best_paraphrase

# Defining a function to detect any similarity in the paraphrase
def text_similarity(text1, text2):
    # Implement your text similarity function here
    return 0

text = "Twinkle twinkle little star, how I i wonder what you are."
paraphrases = generate_paraphrases(text)
best_paraphrase = select_best_paraphrase(paraphrases, text)
print(f"Original Text: {text}")
print(f"Best Paraphrase: {best_paraphrase}")
