import re

password = input("Enter a password: ")

strength = 0

if len(password) >= 8:
    strength += 1
if re.search(r"[A-Z]", password):
    strength += 1
if re.search(r"[a-z]", password):
    strength += 1
if re.search(r"\d", password):
    strength += 1
if re.search(r"[!@#$%^&*()_+=]", password):
    strength += 1

levels = [
    "Very Weak",
    "Weak",
    "Medium",
    "Strong",
    "Very Strong"
]

print("Password strength:", levels[strength - 1])
