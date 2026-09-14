# Faces.py
# Define the Function
def convert(s:str):

    s = s.replace(":(", "🙁")
    s = s.replace(":)", "🙂")
    return s

def main():

    text = input("Please Enter the text: ")
    converted = convert (text)

    print(converted)

main()

