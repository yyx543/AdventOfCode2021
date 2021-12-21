from typing import DefaultDict


inp_str = '''KC -> F
CO -> S
FH -> K
VP -> P
KF -> S
SV -> O
CB -> H
PN -> F
NC -> N
BC -> F
NP -> O
SK -> F
HS -> C
SN -> V
OP -> F
ON -> N
FK -> N
SH -> B
HN -> N
BO -> V
VK -> H
SC -> K
KP -> O
VO -> V
HC -> P
BK -> B
VH -> N
PV -> O
HB -> H
VS -> F
KK -> B
HH -> B
CF -> F
PH -> C
NS -> V
SO -> P
NV -> K
BP -> N
SF -> V
SS -> K
FP -> N
PC -> S
OH -> B
CH -> H
VV -> S
VN -> O
OB -> K
PF -> H
CS -> C
PP -> O
NF -> H
SP -> P
OS -> V
BB -> P
NO -> F
VB -> V
HK -> C
NK -> O
HP -> B
HV -> V
BF -> V
KO -> F
BV -> H
KV -> B
OF -> V
NB -> F
VF -> C
PB -> B
FF -> H
CP -> C
KH -> H
NH -> P
PS -> P
PK -> P
CC -> K
BS -> V
SB -> K
OO -> B
OK -> F
BH -> B
CV -> F
FN -> V
CN -> P
KB -> B
FO -> H
PO -> S
HO -> H
CK -> B
KN -> C
FS -> K
OC -> P
FV -> N
OV -> K
BN -> H
HF -> V
VC -> S
FB -> S
NN -> P
FC -> B
KS -> N'''

start_seq = "OFSNKKHCBSNKBKFFCVNB"
count_dict = DefaultDict(int)
for i in start_seq:
    count_dict[i] += 1

pair_dict = DefaultDict(int)
for i in range(1, len(start_seq)):
    pair_dict[start_seq[i-1:i+1]] += 1

inp_dict = {}
for line in inp_str.split("\n"):
    seq, result = line.split(" -> ")
    inp_dict[seq] = result

def pair_insertion(seq_dict, loop):
    global inp_dict
    global count_dict
    prev_dict = seq_dict
    for i in range(loop):
        next_dict = DefaultDict(int)
        for el in prev_dict:
            insert = inp_dict[el]
            count_dict[insert] += prev_dict[el]
            next_dict[f"{el[0]}{insert}"] += prev_dict[el]
            next_dict[f"{insert}{el[1]}"] += prev_dict[el]
        prev_dict = next_dict
    return prev_dict

# PART 1
pair_dict = pair_insertion(pair_dict, 10)
minimum = 9999
maximum = 0
print(count_dict)
for el in count_dict:
    minimum = min(count_dict[el], minimum)
    maximum = max(count_dict[el], maximum)
print(f"Part 1: {maximum-minimum}")

# PART 2
pair_dict = pair_insertion(pair_dict, 30)
minimum = 99999999999999999999999999999
maximum = 0
for el in count_dict:
    minimum = min(count_dict[el], minimum)
    maximum = max(count_dict[el], maximum)
print(f"Part 2: {maximum-minimum}")