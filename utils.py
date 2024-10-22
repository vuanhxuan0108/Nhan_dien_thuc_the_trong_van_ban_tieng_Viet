import numpy as np

def process_corpus(corpus):
    unique_words = set()
    word_to_id = {}
    current_id = 1
    
    for text in corpus:
        words = text.lower().split()
        for word in words:
            if word not in unique_words:
                unique_words.add(word)
                word_to_id[word] = current_id
                current_id += 1
    
    return unique_words, word_to_id

def encode_text(text, vocab):
    max_len = 150
    words = text.split()
    encoded_text = [vocab[word.lower()] if word.lower() in vocab else -1 for word in words]
    if np.array(words).shape[0] < max_len:
        encoded_text = encoded_text + ([0]*(max_len-np.array(words).shape[0]))
    else:
        encoded_text = encoded_text[:max_len]
    return encoded_text

def preprocess_tags(tags2id, Y):
    
    Y_pre = []
    max_len = 150
    for y in Y:
        
        Y_place_holder = []
        
        for tag in y:
            Y_place_holder.append(tags2id[tag])
        if np.array(Y_place_holder).shape[0] < max_len:
            padded_tags = Y_place_holder + ([0] * (max_len - np.array(Y_place_holder).shape[0]))
        else:
            padded_tags = padded_tags[:150]
        Y_pre.append(padded_tags)
        
    return Y_pre

def make_prediction(data_test, word_to_id, model, i, id2tag):
    
    len_orginal_sententce = np.array(data_test['Word'].iloc[i].split()).shape[0]

    X_test = encode_text(data_test['Word'].iloc[i], word_to_id)
    
    prediction = model.predict(np.array(X_test).reshape((1, 150)), verbose = 0)
    prediction = np.argmax(prediction[0], axis=1)
    
    prediction = list(prediction)[ : len_orginal_sententce] 
    
    pred_tag_list = []
    for tag_id in prediction:
        pred_tag_list.append(id2tag[tag_id])
    
    return pred_tag_list



