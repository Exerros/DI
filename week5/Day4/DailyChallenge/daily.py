class Text():
    def __init__(self,sentence:str): 
        self.sentence = sentence
        splitted = sentence.split(" ")
        self.words = {}
        for word in splitted:
            if word in self.words:
                self.words[word] += 1
            else:
                self.words[word] = 1
        
    def __str__(self):
        return f"{self.sentence}\n {self.words}"

    
    def frequency (self,word:str):
        if word in self.words:
            return self.words[word]
        else:
            return 0
  
    def most_common(self):
        # max = 0
        # highest_key = ""
        # for key in self.words.keys():
        #     value = self.words[key]
        #     if value > max:
        #         max = value 
        #         highest_key = key
        # return highest_key
    
        highest_common = max(self.words, key = lambda k: self.words[k] )
        return highest_common
    
    def unique_words (self):
        unique_words = []
        for key in self.words.keys():
            value = self.words[key]
            if value == 1 :
                unique_words.append(key)
        return unique_words
                 
        
mytext = Text("A good book would sometimes cost as much as a good house. as" )
print(mytext)
print("--------------------------------------------")
print(mytext.frequency("book"))
print("--------------------------------------------")
print(mytext.frequency("good"))
print("--------------------------------------------")
print(mytext.frequency("daniel"))
print(mytext.most_common())
print(mytext.unique_words())


