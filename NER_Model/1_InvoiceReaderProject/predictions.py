#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
import cv2
import pytesseract
from glob import glob
import spacy
import re
import string
import warnings
warnings.filterwarnings('ignore')

### load NER model best
model_ner = spacy.load('./output/model-best/')

def cleanText(txt):
    whitespace = string.whitespace
    punctuation = '!#$%&\'*+:;<=>?[\\]^`{|}~'
    tableWhitespace = str.maketrans('','',whitespace)
    tablePunctuation = str.maketrans('','',punctuation)
    text = str(txt)
    removewhitespace = text.translate(tableWhitespace)
    removepunctuation = removewhitespace.translate(tablePunctuation)
    
    return str(removepunctuation)

# group the labels
class groupgen():
    def __init__(self):
        self.id = 0
        self. text = ''
        
    def get_group(self,text):
        if self.text == text:
            return self.id
        else:
            self.id +=1
            self.text = text
            return self.id

def parser(text,label):
    if label == 'BETRAG':
        text = text
        
    elif label in ('RNUM'):
        text = text
    
    elif label == 'DATUM':
        text = text
            
    elif label == 'ADRESSE':
        allow_special_char = '-.()ßÜüÖöÄä'
        text = re.sub(r'[^A-Za-z0-9{} ]'.format(allow_special_char), '', text)
    
    elif label in ('NAME'):
        text = text
    
    elif label == 'ORG':
        text = re.sub(r'[^A-Za-z0-9. ]', '', text)
    
    return text

grp_gen = groupgen()

def getPredictions(image):
    # extract data using pytesseract
    tessData = pytesseract.image_to_data(image, lang='deu')
    # convert into Dataframe
    tessList = list(map(lambda x: x.split('\t'), tessData.split('\n')))
    df = pd.DataFrame(tessList[1:], columns=tessList[0])
    df.dropna(inplace=True)
    df['conf'] =df['conf'].astype(float).astype(int)
    df['text'] =df['text'].apply(cleanText)

    # convert data into content
    df_clean = df.query("text != '' ")
    content = " ".join([w for w in df_clean['text']])

    # get prediction from NER model
    doc = model_ner(content)

    # converting doc into json
    docjson = doc.to_json()
    doc_text = docjson['text']

    #  creating tokens
    dataFrame_tokens = pd.DataFrame(docjson['tokens'])
    dataFrame_tokens['tokens'] = dataFrame_tokens[['start', 'end']].apply(lambda x: doc_text[x[0]:x[1]], axis= 1)

    right_table = pd.DataFrame(docjson['ents'])[['start', 'label']]
    dataFrame_tokens = pd.merge(dataFrame_tokens, right_table, how='left', on='start')
    dataFrame_tokens.fillna('O', inplace=True)

    # join label to df_clean dataFrame
    df_clean['end'] = df_clean['text'].apply(lambda x: len(x) + 1).cumsum() - 1
    df_clean['start'] = df_clean[['text', 'end']].apply(lambda x: x[1] - len(x[0]), axis=1)

    # inner join with start
    dataframe_info = pd.merge(df_clean, dataFrame_tokens[['start', 'tokens', 'label']], how='inner', on='start')

    # Bounding Box
    bb_df = dataframe_info.query("label != 'O' ")

    bb_df['label'] = bb_df['label'].apply(lambda x: x[2:])
    bb_df['group'] = bb_df['label'].apply(grp_gen.get_group)

    # right and bottom of bounding box
    bb_df[['left', 'top', 'width', 'height']] = bb_df[['left', 'top', 'width', 'height']].astype(int)
    bb_df['right'] = bb_df['left'] + bb_df['width']
    bb_df['bottom'] = bb_df['top'] + bb_df['height']

    # Tagging: groupby group
    col_group = ['left', 'top', 'right', 'bottom', 'label', 'tokens', 'group']
    group_tag_img = bb_df[col_group].groupby(by='group')
    img_tagging = group_tag_img.agg({

        'left':min,
        'right':max,
        'top':min,
        'bottom':max,
        'label':np.unique,
        'tokens':lambda x: " ".join(x)
    })


    img_bb = image.copy()
    for l,r,t,b,label,token in img_tagging.values:
        cv2.rectangle(img_bb, (l,t), (r,b), (0,255,0), 2)
        cv2.putText(img_bb, label, (l-350,t+42), cv2.FONT_HERSHEY_PLAIN, 6, (255, 0, 0), 3)

    # entities
    info_array = dataframe_info[['tokens', 'label']].values
    entities = dict(NAME=[], ORG=[], DATUM=[], ADRESSE=[], BETRAG=[], RNUM=[])
    previous = 'O'

    for token, label in info_array:
        bio_tag = label[0]
        label_tag = label[2:]

        # step -1 parse the token
        text = parser(token, label_tag)

        if bio_tag in ('B', 'I'):

            if previous != label_tag:
                entities[label_tag].append(text)

            else:
                if bio_tag == "B":
                    entities[label_tag].append(text)

                else:
                    if label_tag in ("NAME", 'ORG', 'DATUM', 'ADRESSE', 'BETRAG', 'RNUM'):
                        entities[label_tag][-1] = entities[label_tag][-1] + " " + text

                    else:
                        entities[label_tag][-1] = entities[label_tag][-1] + text


        previous = label_tag

    return img_bb, entities
    
