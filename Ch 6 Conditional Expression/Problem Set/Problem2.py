sub1 = 20
sub2 = 30
sub3 = 90

# totalSum = sub1+sub2+sub3

totalPerc = ((sub1+sub2+sub3) * 100)/300

sub = []

print(totalPerc)

if (totalPerc >= 40 and sub1 >= 35 and sub2 >= 35 and sub3 >= 35):
    print("You are passed: ", totalPerc)
else:

    if (sub1 < 35):
        sub.append("sub1")
    if (sub2 < 35):
        sub.append("sub2")
    if (sub3 < 35):
        sub.append("sub3")

    print("You failed in ", ", ".join(sub))
