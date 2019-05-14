#!/usr/bin/python3
import json

# C = 2 players, w=1
# 1B = 2 players, w=1
# 2B = 2 players, w=1
# 3B = 2 players, w=1
# SS = 2 players, w=1
# OF = 6 players, w=3
# Total : 16 players, w=8

def myAlgo(dataC, data1B, data2B, data3B, dataSS, dataOF, money):

    p1C_score = p2C_score = p11B_score = p21B_score = p12B_score = p22B_score = p13B_score = p23B_score = p1SS_score = p2SS_score = p1OF_score = p2OF_score = p3OF_score = p4OF_score = p5OF_score = p6OF_score = 0

    p1C_avg = p2C_avg = p1C = p2c = p1C_price = p2C_price = 0
    mon_curr = money
    for t_key in dataC:
        t_value = dataC[t_key]
        if (t_value[1]/t_value[0] > p1C_avg) and (t_value[0] < money / 16):
            p2C_avg = p1C_avg
            p2C_score = p1C_score
            p2C = p1C
            p2C_price = p1C_price
            p1C_avg = t_value[1]/t_value[0]
            p1C = t_key
            p1C_score = t_value[1]
            p1C_price = t_value[0]
        elif (t_value[1]/t_value[0] > p2C_avg) and (t_value[0] < money / 16):
            p2C_avg = t_value[1]/t_value[0]
            p2C = t_key
            p2C_score = t_value[1]
            p2C_price = t_value[0]

    if (p1C_avg == 0) or (p2C_avg == 0):
        print("Error : There is not enough C players in the dataset, or not enough money to buy enough players.")
        return

    mon_curr = mon_curr - p1C_price - p2C_price

    p11B_avg = p21B_avg = p11B = p22B = p11B_price = p21B_price = 0

    for t_key in data1B:
        t_value = data1B[t_key]
        if (t_value[1]/t_value[0] > p11B_avg) and (t_value[0] < money / 14):
            p21B_avg = p11B_avg
            p21B = p11B
            p21B_score = p11B_score
            p21B_price = p11B_price
            p11B_avg = t_value[1]/t_value[0]
            p11B = t_key
            p11B_price = t_value[0]
            p11B_score = t_value[1]
        elif (t_value[1]/t_value[0] > p21B_avg) and (t_value[0] < money / 14):
            p21B_avg = t_value[1]/t_value[0]
            p21B = t_key
            p21B_score = t_value[1]
            p21B_price = t_value[0]

    if (p11B_avg == 0) or (p21B_avg == 0):
        print("Error : There is not enough C players in the dataset, or not enough money to buy enough players.")
        return

    mon_curr = mon_curr - p11B_price - p21B_price

    p12B_avg = p22B_avg = p22B = p12B = p12B_price = p22B_price = 0

    for t_key in data2B:
        t_value = data2B[t_key]
        if (t_value[1]/t_value[0] > p12B_avg) and (t_value[0] < money / 12):
            p22B_avg = p12B_avg
            p22B = p12B
            p22B_score = p12B_score
            p22B_price = p12B_price
            p12B_avg = t_value[1]/t_value[0]
            p12B = t_key
            p12B_score = t_value[1]
            p12B_price = t_value[0]
        elif (t_value[1]/t_value[0] > p22B_avg) and (t_value[0] < money / 12):
            p22B_avg = t_value[1]/t_value[0]
            p22B = t_key
            p22B_score = t_value[1]
            p22B_price = t_value[0]

    if (p12B_avg == 0) or (p22B_avg == 0):
        print("Error : There is not enough C players in the dataset, or not enough money to buy enough players.")
        return

    mon_curr = mon_curr - p12B_price - p22B_price

    p13B_avg = p23B_avg = p13B = p23B = p13B_price = p23B_price = 0

    for t_key in data3B:
        t_value = data3B[t_key]
        if (t_value[1]/t_value[0] > p13B_avg) and (t_value[0] < money / 10):
            p23B_avg = p13B_avg
            p23B = p13B
            p23B_score = p13B_score
            p23B_price = p13B_price
            p13B_avg = t_value[1]/t_value[0]
            p13B = t_key
            p13B_score = t_value[1]
            p13B_price = t_value[0]
        elif (t_value[1]/t_value[0] > p23B_avg) and (t_value[0] < money / 10):
            p23B_avg = t_value[1]/t_value[0]
            p23B = t_key
            p23B_score = t_value[1]
            p23B_price = t_value[0]

    if (p13B_avg == 0) or (p23B_avg == 0):
        print("Error : There is not enough C players in the dataset, or not enough money to buy enough players.")
        return

    mon_curr = mon_curr - p13B_price - p23B_price

    p1SS_avg = p2SS_avg = p1SS = p2SS = p1SS_price = p2SS_price = 0

    for t_key in dataSS:
        t_value = dataSS[t_key]
        if (t_value[1]/t_value[0] > p1SS_avg) and (t_value[0] < money / 8):
            p2SS_avg = p1SS_avg
            p2SS = p1SS
            p2SS_score = p1SS_score
            p2SS_price = p1SS_price
            p1SS_avg = t_value[1]/t_value[0]
            p1SS = t_key
            p1SS_score = t_value[1]
            p1SS_price = t_value[0]
        elif (t_value[1]/t_value[0] > p2SS_avg) and (t_value[0] < money / 8):
            p2SS_avg = t_value[1]/t_value[0]
            p2SS = t_key
            p2SS_score = t_value[1]
            p2SS_price = t_value[0]

    if (p1SS_avg == 0) or (p2SS_avg == 0):
        print("Error : There is not enough C players in the dataset, or not enough money to buy enough players.")
        return

    mon_curr = mon_curr - p1SS_price - p2SS_price

    p1OF_avg = p2OF_avg = p3OF_avg = p4OF_avg = p5OF_avg = p6OF_avg = 0
    p1OF = p2OF = p3OF = p4OF = p5OF = p6OF = 0
    p1OF_price = p2OF_price = p3OF_price = p4OF_price = p5OF_price = p6OF_price = 0
    for t_key in dataOF:
        t_value = dataOF[t_key]
        if (t_value[1]/t_value[0] > p1OF_avg) and (t_value[0] < money / 6):
            p6OF_avg = p5OF_avg
            p6OF = p5OF
            p6OF_score = p5OF_score
            p6OF_price = p5OF_price
            p5OF_avg = p4OF_avg
            p5OF = p4OF
            p5OF_score = p4OF_score
            p5OF_price = p4OF_price
            p4OF_avg = p3OF_avg
            p4OF = p3OF
            p4OF_score = p3OF_score
            p4OF_price = p3OF_price
            p3OF_avg = p2OF_avg
            p3OF = p2OF
            p3OF_score = p2OF_score
            p3OF_price = p2OF_price
            p2OF_avg = p1OF_avg
            p2OF = p1OF
            p2OF_score = p1OF_score
            p2OF_price = p1OF_price
            p1OF_avg = t_value[1]/t_value[0]
            p1OF = t_key
            p1OF_score = t_value[1]
            p1OF_price = t_value[0]
        elif (t_value[1]/t_value[0] > p2OF_avg) and (t_value[0] < money / 6):
            p6OF_avg = p5OF_avg
            p6OF = p5OF
            p6OF_score = p5OF_score
            p6OF_price = p5OF_price
            p5OF_avg = p4OF_avg
            p5OF = p4OF
            p5OF_score = p4OF_score
            p5OF_price = p4OF_price
            p4OF_avg = p3OF_avg
            p4OF = p3OF
            p4OF_score = p3OF_score
            p4OF_price = p3OF_price
            p3OF_avg = p2OF_avg
            p3OF = p2OF
            p3OF_score = p2OF_score
            p3OF_price = p2OF_price
            p2OF_avg = t_value[1]/t_value[0]
            p2OF = t_key
            p2OF_score = t_value[1]
            p2OF_price = t_value[0]
        elif (t_value[1]/t_value[0] > p3OF_avg) and (t_value[0] < money / 6):
            p6OF_avg = p5OF_avg
            p6OF = p5OF
            p6OF_score = p5OF_score
            p6OF_price = p5OF_price
            p5OF_avg = p4OF_avg
            p5OF = p4OF
            p5OF_score = p4OF_score
            p5OF_price = p4OF_price
            p4OF_avg = p3OF_avg
            p4OF = p3OF
            p4OF_score = p3OF_score
            p4OF_price = p3OF_price
            p3OF_avg = t_value[1]/t_value[0]
            p3OF = t_key
            p3OF_score = t_value[1]
            p3OF_price = t_value[0]
        elif (t_value[1]/t_value[0] > p4OF_avg) and (t_value[0] < money / 6):
            p6OF_avg = p5OF_avg
            p6OF = p5OF
            p6OF_score = p5OF_score
            p6OF_price = p5OF_price
            p5OF_avg = p4OF_avg
            p5OF = p4OF
            p5OF_score = p4OF_score
            p5OF_price = p4OF_price
            p4OF_avg = t_value[1]/t_value[0]
            p4OF = t_key
            p4OF_score = t_value[1]
            p4OF_price = t_value[0]
        elif (t_value[1]/t_value[0] > p5OF_avg) and (t_value[0] < money / 6):
            p6OF_avg = p5OF_avg
            p6OF = p5OF
            p6OF_score = p5OF_score
            p6OF_price = p5OF_price
            p5OF_avg = t_value[1]/t_value[0]
            p5OF = t_key
            p5OF_score = t_value[1]
            p5OF_price = t_value[0]
        elif (t_value[1]/t_value[0] > p6OF_avg) and (t_value[0] < money / 6):
            p6OF_avg = t_value[1]/t_value[0]
            p6OF = t_key
            p6OF_score = t_value[1]
            p6OF_price = t_value[0]

    if (p1OF_avg == 0) or (p2OF_avg == 0) or (p3OF_avg == 0) or (p4OF_avg == 0) or (p5OF_avg == 0) or (p6OF_avg == 0):
        return

    mon_curr = mon_curr - p1OF_price - p2OF_price - p3OF_price - p4OF_price - p5OF_price - p6OF_price

    interrupt = False
    i = 0
    while (interrupt == False):
        ReplaceC = ReplaceB1 = ReplaceB2 = ReplaceB3 = ReplaceSS = ReplaceOF = ""
        GainC = Gain1B = Gain2B = Gain3B = GainSS = GainOF = 0

        for key in dataC:
            t_value = dataC[key]
            if (t_value[1] > p2C_score) and (GainC < (t_value[1] - p2C_score)) and (t_value[0] < mon_curr):
                ReplaceC = key
                GainC = t_value[1] - p2C_score
        for key in data1B:
            t_value = data1B[key]
            if (t_value[1] > p21B_score) and (Gain1B < (t_value[1] - p2C_score)) and (t_value[0] < mon_curr):
                Replace1B = key
                Gain1B = t_value[1] - p21B_score
        for key in data2B:
            t_value = data2B[key]
            if (t_value[1] > p22B_score) and (Gain2B < (t_value[1] - p22B_score)) and (t_value[0] < mon_curr):
                Replace2B = key
                Gain2B = t_value[1] - p22B_score
        for key in data3B:
            t_value = data3B[key]
            if (t_value[1] > p23B_score) and (Gain3B < (t_value[1] - p23B_score)) and (t_value[0] < mon_curr):
                Replace3B = key
                Gain3B = t_value[1] - p23B_score
        for key in dataSS:
            t_value = dataSS[key]
            if (t_value[1] > p2SS_score) and (GainSS < (t_value[1] - p2SS_score)) and (t_value[0] < mon_curr):
                ReplaceSS = key
                GainSS = t_value[1] - p2SS_score
        for key in dataOF:
            t_value = dataOF[key]
            if (t_value[1] > p2OF_score) and (GainOF < (t_value[1] - p2OF_score)) and (t_value[0] < mon_curr):
                ReplaceOF = key
                GainOF = t_value[1] - p2OF_score

        if (GainC == 0) and (Gain1B == 0) and (Gain2B == 0) and (Gain3B == 0) and (GainSS == 0) and (GainOF == 0):
            interrupt = True
        elif (GainC >= Gain1B) and (GainC >= Gain2B) and (GainC >= Gain3B) and (GainC >= GainSS) and (GainC >= GainOF):
            mon_curr = mon_curr + p2C_price
            p2C_price = dataC[p2C][0]
            mon_curr = mon_curr - p2C_price
            p2C = ReplaceC
            p2C_score = p2C_score + GainC
        elif (Gain1B >= GainC) and (Gain1B >= Gain2B) and (Gain1B >= Gain3B) and (Gain1B >= GainSS) and (Gain1B >= GainOF):
            mon_curr = mon_curr + p21B_price
            p21B_price = data1B[p21B][0]
            mon_curr = mon_curr - p21B_price
            p11BC = Replace1B
            p11B_score = p21B_score + Gain1B
        elif (Gain2B >= Gain1B) and (Gain2B >= GainC) and (Gain2B > Gain3B) and (Gain2B >= GainSS) and (Gain2B >= GainOF):
            mon_curr = mon_curr + p22B_price
            p22B_price = data2B[p22B][0]
            mon_curr = mon_curr - p22B_price
            p12B = Replace2B
            p12B_score = p22B_score + Gain2B
        elif (Gain3B >= Gain1B) and (Gain3B >= Gain2B) and (Gain3B >= GainC) and (Gain3B >= GainSS) and (Gain3B >= GainOF):
            mon_curr = mon_curr - p23B_price
            p23B_price = data3B[p23B][0]
            mon_curr = mon_curr + p23B_price
            p13B = Replace3B
            p13B_score = p23B_score + Gain3B
        elif (GainSS >= Gain1B) and (GainSS >= Gain2B) and (GainSS >= Gain3B) and (GainSS >= GainC) and (GainSS >= GainOF):
            mon_curr = mon_curr - p2SS_price
            p2SS_price = dataSS[p2SS][0]
            mon_curr = mon_curr + p2SS_price
            p1SS = ReplaceSS
            p1SS_score = p2SS_score + GainSS
        elif (GainOF >= Gain1B) and (GainOF >= Gain2B) and (GainOF >= Gain3B) and (GainOF >= GainSS) and (GainOF >= GainC):
            mon_curr = mon_curr - p2OF_price
            p2OF_price = dataOF[p2OF][0]
            mon_curr = mon_curr + p2OF_price
            p1OF = ReplaceOF
            p1OF_score = p2OF_score + GainOF
        else:
            interrupt = True

        i = i + 1
        if (i > 100):
            interrupt = True



    data = {}
    data['selected_players'] = {
        "C": {
          "p1": {"name": p1C, "score": p1C_score, "price": p1C_price, "average": p1C_avg},
          "p2": {"name": p2C, "score": p2C_score, "price": p2C_price, "average": p2C_avg}
        },
        "1B": {
          "p1": {"name": p11B, "score": p11B_score, "price": p11B_price, "average": p11B_avg},
          "p2": {"name": p21B, "score": p21B_score, "price": p21B_price, "average": p21B_avg}
        },
        "2B": {
          "p1": {"name": p12B, "score": p12B_score, "price": p12B_price, "average": p12B_avg},
          "p2": {"name": p22B, "score": p22B_score, "price": p22B_price, "average": p22B_avg}
        },
        "3B": {
          "p1": {"name": p13B, "score": p13B_score, "price": p13B_price, "average": p13B_avg},
          "p2": {"name": p23B, "score": p23B_score, "price": p23B_price, "average": p23B_avg}
        },
        "SS": {
          "p1": {"name": p1SS, "score": p1SS_score, "price": p1SS_price, "average": p1SS_avg},
          "p2": {"name": p2SS, "score": p2SS_score, "price": p2SS_price, "average": p2SS_avg}
        },
        "OF": {
          "p1": {"name": p1OF, "score": p1OF_score, "price": p1OF_price, "average": p1OF_avg},
          "p2": {"name": p2OF, "score": p2OF_score, "price": p2OF_price, "average": p2OF_avg},
          "p3": {"name": p3OF, "score": p3OF_score, "price": p3OF_price, "average": p3OF_avg},
          "p4": {"name": p4OF, "score": p4OF_score, "price": p4OF_price, "average": p4OF_avg},
          "p5": {"name": p5OF, "score": p5OF_score, "price": p5OF_price, "average": p5OF_avg},
          "p6": {"name": p6OF, "score": p6OF_score, "price": p6OF_price, "average": p6OF_avg}
        },
    }
    data['money'] = {
      "left": mon_curr,
      "total": money
    }
    return json.dumps(data)
