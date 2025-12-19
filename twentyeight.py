# Car Insurance Premium

cat = input("A/B/C: ").upper()
val = float(input("Car value: "))
if cat=="A": print("Premium =", 0.02 * val)
elif cat=="B": print("Premium =", 0.03 * val)
elif cat=="C": print("Premium =", 0.05 * val)

