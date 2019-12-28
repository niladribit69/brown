import nltk
from nltk.corpus import brown
brown.categories()
//OUTPUT-['adventure',
          'belles_lettres',
          'editorial',
          'fiction',
          'government',
          'hobbies',
          'humor',
          'learned',
          'lore',
          'mystery',
          'news',
          'religion',
          'reviews',
          'romance',
          'science_fiction']
 
 brown.words(categories='romance')
 //OUTPUT-['They', 'neither', 'liked', 'nor', 'disliked', 'the', ...]
 
rom_text = brown.words(categories='romance')
fdist = nltk.FreqDist([w.lower() for w in rom_text])
modals = ['we', 'our', 'love', 'romance', 'air', 'flower']
for m in modals:
    print (m + ':', fdist[m])
//OUTPUT-we: 109
         our: 28
         love: 36
         romance: 1
         air: 20
         flower: 1   
         
cfd = nltk.ConditionalFreqDist(
                    (genre, word)
                    for genre in brown.categories()
                    for word in brown.words(categories=genre))
 genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']
 modals = ['we', 'our', 'love', 'romance', 'air', 'flower']
cfd.tabulate(conditions=genres, samples=modals)
//OUTPUT-




                     we     our    love romance     air  flower 
           news      77      55       3       0       8       1 
       religion     176      77      13       0       4       0 
        hobbies     100      77       6       0      31       2 
science_fiction      30       6       3       0       1       0 
        romance      78      25      32       1      19       1 
          humor      32      30       4       2       4       0 
