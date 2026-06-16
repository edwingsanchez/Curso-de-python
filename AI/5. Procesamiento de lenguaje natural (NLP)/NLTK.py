import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.probability import FreqDist

# Descargar paquetes necesarios la primera vez
nltk.download("punkt")
nltk.download("stopwords")

text = "NLTK es una librería para procesamiento de lenguaje natural en Python. " \
       "Permite tokenizar, filtrar palabras vacías, derivar palabras y más."

# Segmentar en oraciones y palabras
sentences = sent_tokenize(text, language="spanish")
words = word_tokenize(text, language="spanish")

# Filtrar stopwords
spanish_stopwords = set(stopwords.words("spanish"))
filtered_words = [w for w in words if w.isalpha() and w.lower() not in spanish_stopwords]

# Aplicar stemming
stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(w.lower()) for w in filtered_words]

# Frecuencia de palabras
frequency = FreqDist(filtered_words)

print("Oraciones:", sentences)
print("Palabras:", words)
print("Palabras filtradas:", filtered_words)
print("Palabras tras stemming:", stemmed_words)
print("5 palabras más frecuentes:", frequency.most_common(5))
