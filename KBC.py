q = [
['1. Which one of the following river flows between Vindhyan and Satpura ranges?', 'a Narmada', '(b) Mahanadi', '(c) Son', '(d) Netravati', 1],
['2. The Central Rice Research Station is situated in?', 'a Chennai', '(b) Cuttack', '(c) Bangalore', '(d) Quilon', 2],
['3. Who among the following wrote Sanskrit grammar?', 'a Kalidasa', '(b) Charak', '(c) Panini', '(d) Aryabhatt', 3],
['4. Which among the following headstreams meets the Ganges in last?', 'a Alaknanda', '(b) Pindar', '(c) Mandakini', '(d) Bhagirathi', 4],
['5. The metal whose salts are sensitive to light is?', 'a Zinc', '(b) Silver', '(c) Copper', '(d) Aluminum', 2],
['6. Patanjali is well known for the compilation of ', 'a Yoga Sutra', '(b) Panchatantra', '(c) Brahma Sutra', '(d) Ayurveda', 1],
['7. River Luni originates near Pushkar and drains into which one of the following?', 'a Rann of Kachchh', '(b) Arabian Sea', '(c) Gulf of Cambay', '(d) Lake Sambhar', 1],
['8. Which one of the following rivers originates in Brahmagiri range of Western Ghats?', '(a) Pennar', '(b) Cauvery', '(c) Krishna', '(d) Tapti', 2],
['9. The country that has the highest in Barley Production?', 'a China', '(b) India', '(c) Russia', '(d) France', 3],
['10. Tsunamis are not caused by', 'a Hurricanes', '(b) Earthquakes', '(c) Undersea landslides', '(d) Volcanic eruptions', 1],
['11. Chambal river is a part of ', 'a Sabarmati basin', '(b) Ganga basin', '(c) Narmada basin', '(d) Godavari basin', 3],
['12. D.D.T. was invented by?', 'a Mosley', '(b) Rudolf', '(c) Karl Benz', '(d) Dalton', 1],
['13. Volcanic eruption do not occur in the', 'a Baltic sea', '(b) Black sea', '(c) Caribbean sea', '(d) Caspian sea', 1],
['14. Indus river originates in ', 'a Kinnaur', '(b) Ladakh', '(c) Nepal', '(d) Tibet', 4],
['15. The hottest planet in the solar system?', 'a Mercury', '(b) Venus', '(c) Mars', '(d) Jupiter', 2],
['16. With which of the following rivers does Chambal river merge?', 'a Banas', '(b) Ganga', '(c) Narmada', '(d) Yamuna', 4],
['17. Where was the electricity supply first introduced in India ', 'a Mumbai', '(b) Dehradun', '(c) Darjeeling', '(d) Chennai', 3],
]
lvl = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 7500000, 10000000, 75000000]
def qask(a):
    print(a[0])
    print(a[1])
    print(a[2])
    print(a[3])
    print(a[4])
def aask(b):
    a = int(input("Enter Answer 1 to 4:\n0 to quit:\n"))
    if a == b[5]:
        print("Correct")
        return True
    else:
        print("Wrong")
        return False
questionDecider = 0
answerDecider = 0
moneyDecider = 0
forNextPrinterChecker = 16
print("For ₹1000 answer this question")
while questionDecider < len(q)  and answerDecider <= len(q) and moneyDecider < len(lvl):
    qask(q[questionDecider])
    ans = aask(q[answerDecider])
    if ans == True:
        print(f"You have won ₹{lvl[moneyDecider]}")
        if moneyDecider < forNextPrinterChecker:
            forNextPrinter = moneyDecider + 1
            print(f"For ₹{lvl[forNextPrinter]} answer this question")
        questionDecider = questionDecider + 1
        answerDecider = answerDecider + 1
        moneyDecider = moneyDecider + 1
    else:
        break
print("Thanks for playing")