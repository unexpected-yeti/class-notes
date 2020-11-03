from textwrap import dedent
import nltk, re, string, collections
from nltk.util import ngrams
from nltk.corpus import stopwords

text = dedent("""\
        There is a nice restaurant in the center of New York. However, in the
        north of New York food is more cheap. It is more suited for visitors in
        their mid twenties, as it is a good alternative""")

# Problems
# - newlines & whitespace
# - gross / kleinschreibung am Anfgang vom Satz.
# Ungewollte / langweilige Kombinationen
# (is a) => 2
# (in the) => 2

# Replace newlines with whitespace
text = re.sub('\n', ' ', text)

punctuations = "[" + string.punctuation + "]"
text = re.sub(punctuations, "", text)

tokenized = text.split()

stop_words = set(stopwords.words('english'))

token_clean = [w for w in tokenized if not w in stop_words]

bigrams = nltk.bigrams(token_clean)

freq_bi = nltk.FreqDist(bigrams)
fdist = nltk.FreqDist(freq_bi)

for key, value in fdist.items():
    print(f"{key} => {value}")
