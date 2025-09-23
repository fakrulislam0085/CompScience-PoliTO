import unicodedata 
# more info about this package here: https://docs.python.org/3/library/unicodedata.html

def main() : 
    emoji_1 = "😜"
    emoji_2 = "😘"
    emoji_3 = "😎"

    # function ord() returns the unicode character encoding
    print(f"U+{ord(emoji_1):4X} - {unicodedata.name(emoji_1):40} - {emoji_1} - Rank 2: Naughty energy")
    print(f"U+{ord(emoji_2):4X} - {unicodedata.name(emoji_2):40} - {emoji_2} - Rank 1: My future wifey")
    print(f"U+{ord(emoji_3):4X} - {unicodedata.name(emoji_3):40} - {emoji_3} - Rank 3: Big brain coding vibes")

if __name__ == "__main__" : 
    main() 

''' 
ord((emoji_1):4X) -> here 'X' indicates to convert the ord code to Hexadecimal code
and '4' indicates the width of the output which should be minimum 4 characters. 

For Example:
ord('😜') = 128540
hex(128540) = '1F61C'

So, with :4X → '1F61C' is printed as is (since it's already longer than 4 chars).
'''
