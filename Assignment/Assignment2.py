def swap_case(text):
  return "".join([c.lower() if c.isupper() else c.upper() for c in text])

original = "Hello Python"
result = swap_case(original)
print(result) 

# No2
def compress_string(s):
    if not s:
        return ""
    
    compressed = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed.append(s[i - 1] + str(count))
            count = 1
            
    compressed.append(s[-1] + str(count))
    return "".join(compressed)


input_str = "aaaabbcddd"
print(compress_string(input_str)) 

# No3
def are_anagrams(str1, str2):
    s1 = str1.replace(" ", "").lower()
    s2 = str2.replace(" ", "").lower()
    return sorted(s1) == sorted(s2)

print(are_anagrams("silent", "listen"))  
print(are_anagrams("hello", "world"))      

# No4
s = "Programming."
res = "".join(dict.fromkeys(s))
print(res)

#No5
def find_longest_word(sentence):
    import string
    cleaned_sentence = sentence.translate(str.maketrans('', '', string.punctuation))
    
    words = cleaned_sentence.split()
    
    if not words:
        return ""
    
    longest_word = max(words, key=len)
    
    return longest_word

input_sentence = "The quick brown fox jumped over the lazy dog"
print(find_longest_word(input_sentence))  

#No6
def count_vowels(s):
    
    s = s.lower()
    
    vowels = "aeiou"
    
    for v in vowels:
        count = s.count(v)
        print(f"'{v}': {count}")

input_str = "Programming in Python is amazing!"
count_vowels(input_str)

#no7
def is_palindrome(s):
    
    cleaned = "".join(char.lower() for char in s if char.isalnum())
    
    return cleaned == cleaned[::-1]

print(is_palindrome("Racecar"))                 
print(is_palindrome("Hello"))                 
print(is_palindrome("A man, a plan, a canal: Panama"))

#no8
import string

def remove_punctuation(s):
   
    translator = str.maketrans('', '', string.punctuation)
    return s.translate(translator)

input_str = "Hello world! how's life?"
print(remove_punctuation(input_str)) 

# No9
def sum_of_digits(s):
   
    return sum(int(char)
           for char in s 
           if char.isdigit())

input_str = "abc123xyz45"
print(sum_of_digits(input_str)) 

#No10
from collections import Counter
import string

def find_most_common_word(sentence):
   
    cleaned_sentence = sentence.translate(str.maketrans('', '', string.punctuation)).lower()
    
    words = cleaned_sentence.split()
    
    if not words:
        return ""
    
    word_counts = Counter(words)
    
    most_common = word_counts.most_common(1)
    
    return most_common[0][0]

input_sentence = "The quick brown fox jumps over the lazy dog, and the fox is quick."
print(find_most_common_word(input_sentence))  

# No11
import string

def sort_words_by_length(sentence):
    
    cleaned = sentence.translate(str.maketrans('', '', string.punctuation))
    
    words = cleaned.split()
    
    return sorted(words, key=len)

input_sentence = "The quick brown fox jumps over the lazy dog"
print(sort_words_by_length(input_sentence))

#No12
def is_isogram(s):
 
    letters = [char.lower() for char in s if char.isalpha()]
    
    return len(set(letters)) == len(letters)

print(is_isogram("ermat"))      
print(is_isogram("programming")) 
print(is_isogram("Lumberjacks")) 

# No13
from collections import Counter

def second_most_frequent_char(s):
    s = s.replace(" ", "")
    
    if len(set(s)) < 2:
        return "Not enough unique characters to find a second most frequent one."

    char_counts = Counter(s)
    
    most_common_list = char_counts.most_common(2)
    
    return most_common_list[1][0]

input_str = "success"
print(second_most_frequent_char(input_str)) 

# No14
import string

def find_words_starting_with(sentence, letter):
   
    cleaned = sentence.translate(str.maketrans('', '', string.punctuation))
    words = cleaned.split()
    
    target = letter.lower()
    
    matching_words = [word for word in words if word.lower().startswith(target)]
    
    return matching_words

input_sentence = "The quick brown fox jumps over the lazy dog, and the fox is fast."
print(find_words_starting_with(input_sentence, 'f'))

#No15
def count_character_types(s):
    uppercase_count = sum(1 for c in s if c.isupper())
    lowercase_count = sum(1 for c in s if c.islower())
    special_count = sum(1 for c in s if not c.isalpha()) # includes spaces, numbers, punctuation
    
    return {
        "Uppercase": uppercase_count,
        "Lowercase": lowercase_count,
        "Special/Other": special_count
    }


text = """In cryptography, a Caesar cipher is a very simple encryption techniques in which each
letter in the plain text is replaced by a letter some fixed number of positions down the
alphabet. For example, with a shift of 3, A would be replaced by D, B would become E, and
so on. The method is named after Julius Caesar, who used it to communicate with his
generals. ROT-13 ("rotate by 13 places") is a widely used example of a Caesar cipher
where the shift is 13. In Python, the key for ROT-13 may be represented by means of the
following dictionary:..."""

counts = count_character_types(text)
for k, v in counts.items():
    print(f"{k}: {v}")

   
key = {
    'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b',
    'p':'c', 'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k', 'y':'l', 'z':'m', 
    'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S', 'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 
    'N':'A', 'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I', 'W':'J', 'X':'K', 'Y':'L', 'Z':'M'
}

def rot13_codec(message):
   
    return "".join(key.get(char, char) for char in message)

secret_message = "Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!"

decoded_message = rot13_codec(secret_message)
print("Decoded Message:", decoded_message)