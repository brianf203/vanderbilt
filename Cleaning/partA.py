# PART A

NEWS = ["Boris Johnson Is Back in Britain, and Back in the Running for Prime Minister.", "The former Conservative leader, who was forced out of office after scandals this summer, has not declared his candidacy, but dozens of party lawmakers already support him.", "The former Conservative leader, who was forced out of office after scandals this summer, has not declared his candidacy, but dozens of party lawmakers already support him.", "Boris Johnson on Saturday at Gatwick Airport near London after returning from a vacation. While he was away, Prime Minister Liz Truss resigned.", "LONDON — Boris Johnson returned to Britain on Saturday, feeding expectations that he would seek to reclaim his old job after the resignation of Prime Minister Liz Truss last week. His former chancellor of the Exchequer, Rishi Sunak, also seemed poised to join the race to replace Ms. Truss.", "Mr. Johnson, who had been vacationing in the Dominican Republic, won the backing of his former home secretary, Priti Patel, a significant endorsement from a prominent figure on the right wing of the Conservative Party.", "Allies of Mr. Johnson claimed on Saturday afternoon that he had picked up support from more than 100 lawmakers. That is substantially larger than the number who have publicly declared for him. But if he were to cross that threshold, it would significantly raise the odds of him returning to 10 Downing Street.", "Contenders for party leader are required to have nominations from at least 100 of the 357 Conservative lawmakers to advance to a second round of voting, among the members of the party in Britain, a group with whom Mr. Johnson remains popular. Mr. Sunak already has 128 votes from party lawmakers, according to an unofficial count by the BBC."]

WORD_LIST =[]

for sentence in NEWS: 
    for word in sentence.split(): 
        WORD_LIST.append(word)

print(WORD_LIST)
