from random import choice
import matplotlib.pyplot as plt

loops = 10
i=0

list = ["heads", "tails"]

x = [a for a in range(loops)]
y = []



count_heads = 0
count_tails = 0



while i < loops : 
    a = choice(list)
    if a == "heads" :
        count_heads += 1
    else :
        count_tails += 1

    percent_heads = count_heads / (count_heads + count_tails)
    percent_heads = percent_heads * 100
    y.append(percent_heads)

    i += 1

plt.plot(x[:], y[:])
plt.show()




