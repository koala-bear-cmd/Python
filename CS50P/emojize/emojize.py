import emoji

Content = input("please enter your content: ")

def convert(s):
    print(emoji.emojize(s, language="alias"))

convert(Content)
