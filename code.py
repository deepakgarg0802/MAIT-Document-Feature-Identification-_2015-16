#Code by Deepak
##----------------code optimized,refined,revised---------##
#### matching with corpora ####
### more accurate,fast than regex ######


import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import brown
import shutil   #for file find,move related operations
import os
import glob

######## for compatibility with both versions #############
import sys
if sys.version_info[0] > 2:
    # py3k
    pass
else:
    # py2
    import codecs
    import warnings
    def open(file, mode='r', buffering=-1, encoding=None,
             errors=None, newline=None, closefd=True, opener=None):
        if newline is not None:
            warnings.warn('newline is not supported in py2')
        if not closefd:
            warnings.warn('closefd is not supported in py2')
        if opener is not None:
            warnings.warn('opener is not supported in py2')
        return codecs.open(filename=file, mode=mode, encoding=encoding,
                    errors=errors, buffering=buffering)
                    
########### function to get max key value pair

def keywithmaxval(d): 
     v=list(d.values())
     k=list(d.keys())
     return k[v.index(max(v))]

#############main program

path_of_input_files= './csc_files/'
no_of_words_matched = 500
category= ''
features_dict={}
filename=''

for filename in glob.glob(os.path.join(path_of_input_files , '*.txt')):
    inpfile = open(filename,encoding='Windows-1252').read()
    
    nouns_of_inpfile=[]    #list initialized
    top_words_content=[]
    top_words_category=[]
    count=0

    #print (filename )
    #------------- finding most freq nouns of input file-------#
    tokens= word_tokenize(inpfile)
    tagged_tuple_list= nltk.pos_tag (tokens)    #each word is associated with its pos tag now
    for tuple in tagged_tuple_list :
        if tuple[1]=='NN' or tuple[1] =='NNS' or tuple[1]=='NNP' or tuple[1]=='NNPS':       ###all the nouns includng names like Deepak Garg also returned,
            nouns_of_inpfile.append(tuple[0])                                                          #if pos tag is 'noun'/pluralnoun/proper noun/proper noun plural
        

    content_words_freq = (nltk.FreqDist(nouns_of_inpfile)) # list() to maintain the order
    top_content = content_words_freq.most_common(no_of_words_matched)
    for x in top_content :
        top_words_content.append(x[0])

    #print( top_words_content)

    #--------------------finding most freq words and comparing from each category in corpora------#
        
    for category in brown.categories():
        words_of_category = brown.words(categories=category)
        category_word_freq = nltk.FreqDist(words_of_category)
        top_in_category = category_word_freq.most_common(no_of_words_matched)
        for i in top_in_category:
            top_words_category.append(i[0])
    
        count=0
        key=category
        for i in top_words_content:
            if i in top_words_category:
                count+=1
        features_dict[key]= count

    maxkey= keywithmaxval(features_dict )
    #print (features_dict)
    print (filename , "  ", maxkey)

    #shutil.copy(filename,'./csc_files/{}'.format(category))
    

        
