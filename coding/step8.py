user=input("Enter the text")
data=cv.transform([user]).toarray()
output=model.predict(data)
print(output)