
import streamlit as st
import joblib
import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer 
from sklearn.feature_extraction.text import TfidfVectorizer


site_header = st.container()
business_context = st.container()
data_desc = st.container()
performance = st.container()
tweet_input = st.container()
model_results = st.container()
sentiment_analysis = st.container()
contact = st.container()

with site_header:
    st.title('DETECCIÓN DE COMENTARIOS TÓXICOS EN YOUTUBE')
   

with tweet_input:
    st.header('¿Tiene tu texto la consideración de tóxico?')
    user_text = st.text_input('INTRODUCE TU TEXTO EN LA CAJA INFERIOR', max_chars=280)

with model_results:    
    st.subheader('Predicción:')
    if user_text:
    # processing user_text
        # removing punctuation
        user_text = re.sub('[%s]' % re.escape(string.punctuation), '', user_text)
        # make text lowercase
        user_text = user_text.lower()
        # removing text within parentheses
        user_text = re.sub('', '', user_text)
        # removing numbers
        user_text = re.sub('\w*\d\w*', '', user_text)
        # if there's more than 1 whitespace, then make it just 1
        user_text = re.sub('\s+', ' ', user_text)
        # if there's a new line, then make it a whitespace
        user_text = re.sub('\n', ' ', user_text)
        # removing any quotes
        user_text = re.sub('\"+', '', user_text)
        # getting rid of punctuations
        user_text = re.sub('[%s]' % re.escape(string.punctuation), '', user_text)
        # tokenizing
        stop_words = set(stopwords.words('english'))
        tokens = nltk.word_tokenize(user_text)
        # removing stop words
        stopwords_removed = [token.lower() for token in tokens if token.lower() not in stop_words]
        # taking root word
        lemmatizer = WordNetLemmatizer() 
        lemmatized_output = []
        for word in stopwords_removed:
            lemmatized_output.append(lemmatizer.lemmatize(word))

        # instantiating tfidf vectorizor
        tfidf = TfidfVectorizer(stop_words= stop_words, ngram_range=(1,2))
        X_train = joblib.load(open('X_train_final.pickel', 'rb'))
        X_test = lemmatized_output
        X_train_count = tfidf.fit_transform(X_train)
        X_test_count = tfidf.transform(X_test)

        # loading in model
        final_model = joblib.load(open('final_catboost.pickel', 'rb'))

        # applying the model to make predictions
        prediction = final_model.predict(X_test_count[0])

        if prediction == 0:
            st.write('**NO ES TÓXICO**')
        else:
            st.write('**ES TÓXICO**')
        st.text('')