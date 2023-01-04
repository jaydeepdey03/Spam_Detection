import pandas,pickle,nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from string import punctuation
nltk.download('stopwords')

ps = PorterStemmer()
def transform_text(text):
    text = text.lower()  # step1
    text = nltk.word_tokenize(text)  # tokenize
    y = list()
    # removing special Characters
    for i in text:
        if(i.isalnum()):
            y.append(i)
    text = y.copy()
    y.clear()
    # removing stop words
    for i in text:
        if i not in stopwords.words('english') and i not in punctuation:
            y.append(i)
    text = y.copy()
    y.clear()
    #  stemming
    for i in text:
        y.append(ps.stem(i))
    text = y.copy()
    y.clear()
    return ' '.join(text)