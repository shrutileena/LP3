c = 60
f = 45
conv_f = int((9 * (c / 5)) + 32)
conv_c = int(((f - 32) / 9) * 5)

print(str(c)+"\u00b0C is", conv_f, "in Fahrenheit")
print(str(f)+"\u00b0F is", conv_c, "in Celsius")