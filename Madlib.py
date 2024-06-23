with open("story.txt","r") as f:
    story= f.read()

start_word = "<"
end_word = ">"
start_idx = -1

words =set()

for i,char in enumerate(story):
    if char == start_word:
        start_idx=i

    if char == end_word and start_idx!=-1: 
        word =story[start_idx:i+1]
        words.add(word) 

answers ={}

for word in words:
    answers[word]=input("Enter value for "+word + " : ")

for word in words:
    story = story.replace(word,answers[word])  
    
print(story)