from itertools import groupby
from operator import itemgetter

varsha_list = ['var','me','due','gaur','not','make','coming','know','take','Unknown','come','pain',
     'looking','want','Dog','Cat','found','asking','working','Dehradun','Monkey','out','call']

for letter, words in groupby(sorted(varsha_list), key=itemgetter(0)):
    print(letter)
    for word in words:
        print(word)