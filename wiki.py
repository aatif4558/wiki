import wikipedia  # pip install wikipedia
x = input("What Do Want To Know: ")
data = wikipedia.page(x)
print(data.summary)
