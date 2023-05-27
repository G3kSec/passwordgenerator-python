# Password Generator Using Python
import random

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "0123456789"
symbol = "[]{}#()*;._-?¿^%"

ans = lower_case + upper_case + num +symbol

length = 20

password = "".join(random.sample(ans, length))

print(f"Your Generated Password is:\n{password}")