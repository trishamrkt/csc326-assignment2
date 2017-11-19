def find_popular(file_name):
    with open(file_name) as fileobj:
        word_dict = {};
        for line in fileobj:
            update_dict(line, word_dict)
    
        popular = sorted(word_dict, key=word_dict.get, reverse=True)[:10]
    return popular

def update_dict(line, d):
    words = line.split();
    
    for word in words:
        if word in d: 
            d[word] += 1;
        else: 
            d[word] = 1;

if __name__ == "__main__":
    print find_popular("test_file.txt")