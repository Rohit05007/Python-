# Question (1)----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
name = input("Enter your name : ")
print("Good Afternoon", name)
print(f"Good Afternoon {name} ")  # new method (use all this nowdays )

# Question (2)----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
letter = """Dear <|Name|>,
You are selected !
<|Date|> """
print(
    letter.replace("<|Name|>", "Rohit").replace("<|Date|>", "16 August 2025")
)  # Chaining Replace Method

# Question (3)----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
namethird = "Rohit is a good  boy and"
print(namethird.find("  "))

# Question (4)----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
namethird = "Rohit is a good  boy and"
print(namethird.replace("  ", " "))
print(
    namethird
)  # String are immutable which mean that you ca not chamge them by running functions on them

# Question (5)----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Letterfirst = "Dear Harry , this python cource is nice. thanks!"
print(Letterfirst)
Lettersecond = "Dear Harry,\n\tthis python cource is nice.\n thanks!"
print(Lettersecond)
