# PART C

NEWS = ["Boris Johnson Is Back in Britain, and Back in the Running for Prime Minister.", "The former Conservative leader, who was forced out of office after scandals this summer, has not declared his candidacy, but dozens of party lawmakers already support him.", "The former Conservative leader, who was forced out of office after scandals this summer, has not declared his candidacy, but dozens of party lawmakers already support him.", "Boris Johnson on Saturday at Gatwick Airport near London after returning from a vacation. While he was away, Prime Minister Liz Truss resigned.", "LONDON — Boris Johnson returned to Britain on Saturday, feeding expectations that he would seek to reclaim his old job after the resignation of Prime Minister Liz Truss last week. His former chancellor of the Exchequer, Rishi Sunak, also seemed poised to join the race to replace Ms. Truss.", "Mr. Johnson, who had been vacationing in the Dominican Republic, won the backing of his former home secretary, Priti Patel, a significant endorsement from a prominent figure on the right wing of the Conservative Party.", "Allies of Mr. Johnson claimed on Saturday afternoon that he had picked up support from more than 100 lawmakers. That is substantially larger than the number who have publicly declared for him. But if he were to cross that threshold, it would significantly raise the odds of him returning to 10 Downing Street.", "Contenders for party leader are required to have nominations from at least 100 of the 357 Conservative lawmakers to advance to a second round of voting, among the members of the party in Britain, a group with whom Mr. Johnson remains popular. Mr. Sunak already has 128 votes from party lawmakers, according to an unofficial count by the BBC."]

WORD_LIST =[]

for sentence in NEWS: 
    for word in sentence.split(): 
        WORD_LIST.append(word) 

SYMBOL_LIST = [";", ".", ":", ")", " ", "(", "*", "&", "%", "^", "$", ",", "?", "!", "@", "\\n"]

def CLEAN_MY_WORD(INPUT_STRING):
    CLEAN_WORD = ""
    for character in INPUT_STRING:
        if character in SYMBOL_LIST:
            break
        if character.isalpha():
            CLEAN_WORD += character
    return CLEAN_WORD
    
CLEAN_WORD_LIST = []

for word in WORD_LIST:
    CWORD = CLEAN_MY_WORD(word.lower())
    CLEAN_WORD_LIST.append(CWORD)

STOP_WORDS = ['i','', 'am','is','are','me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because','as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'has','have','had','not','hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn',"shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't", 'mr', 'ms', 'would']

def REMOVE_STOP_WORD(INPUT_LIST):
    NEW_LIST = []
    for word in INPUT_LIST:
        if word not in STOP_WORDS:
            NEW_LIST.append(word)
    return NEW_LIST

INPUT_LIST = CLEAN_WORD_LIST
WITHOUT_STOP_WORDS = REMOVE_STOP_WORD(INPUT_LIST)

print("Without stop words:", len(WITHOUT_STOP_WORDS))

for i in range(len(WITHOUT_STOP_WORDS)):
    print(i, "--", WITHOUT_STOP_WORDS[i])
