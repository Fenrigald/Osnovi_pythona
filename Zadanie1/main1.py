with open("nginx_logs.txt", "r", encoding="utf-8") as f:
    ml = []
    for l in f:
        ad = l[:l.find("")]
        t = l[:l.find('"') + 1:l.find('"') + 4]
        res = l[l.find('/d'):l.find('HTTP') - 1]
        tupl = (ad, t, res)
        ml.append(tupl)
        print(tupl)