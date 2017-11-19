def split_sentence(file_name):
    sentences = []
    text = ''.join(open(file_name).readlines())
    f = open('q5.out', 'w');
    
    create_sentences(text, sentences)
    print_sentences(sentences, f);
    f.close();
    
def create_sentences(text, s):
    terminators = ['.', '?', '!']
    titles = ['Mr.', 'Dr.', 'Mrs.', 'Ms.', 'Jr.']
    misc = ['e.g', 'i.e.']
    
    words = text.split()
    sentence = ""
    
    for i in range(len(words)):
        word = words[i].strip() 
        sentence += " " + word;
        
        # Check if the word ends in one of the terminators
        # If it word isn't a title or in misc, end the sentence add to s and start new sentence 
        if word[len(word) - 1] in terminators and word not in titles and word not in misc:
            
            # Check if the next word starts with an upper case
            if i + 1 < len(words) and words[i+1][0].isupper():
                s.append(sentence)
                sentence = ""
                
            # Check if the last word starts with lowercase (ie part of same sentence)
            # Adds the sentence to s
            elif i == len(words) - 1:
                s.append(sentence)
            
    return 
    
def print_sentences(sentences, f):
    for s in sentences: 
        f.write(s + "\n");
        print s;

if __name__ == "__main__":
    split_sentence('q5_input.txt')