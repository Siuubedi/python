name = "Tony Stark"
print(name.upper())  # Output: TONY STARK
print(name.lower())  # Output: tony stark

print(name.find("ark"))  # Output: 7
print(name.find("Ton"))  # Output: 0
print(name.find("Hello"))  # Output: -1

print(name.replace("ark", "art"))  # Output: Tony Start
print(name.replace("Tony Stark", "Gaurav Subedi"))  # Output: Gaurav Subedi
print(name)  # Output: Tony Stark

# Check for presence of substring
print("S" in name)  # Output: True
print("Start" in name)  # Output: False
