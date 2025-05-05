import csv
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
import math

def makeurl(q, n, k):
    BASE = "http://codetables.de/QECC.php?"
    urlstr = BASE + "q=" + str(q) + "&n=" + str(n) + "&k=" + str(k)
    return urlstr

def find(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    page = urlopen(req).read()
    readsoup = soup(page, "html.parser")
    record = readsoup.findAll('pre')
    distance = None
    for block in record:
        text = block.get_text()
        if "]] quantum code:" in text:
            parts = text.split("]] quantum code:")
            if len(parts) > 1:
                # Extract the number right before "]] quantum code:"
                distance = parts[0].strip().split()[-1]
                distance = distance.split(",")[-1]
                break
    return distance

def main():
    maxDict = {
        4: 256,
        9: 100,
        16: 100,
        25: 100,
        49: 100,
        64: 100,
    }
    
    with open("QECC_output.csv", 'w', newline='') as csvfile:
        fieldnames = ['Q', 'N', 'K', 'D', 'link', 'MDS']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for q in maxDict:
            for n in range(2, maxDict[q]):
                for k in range(0, n):
                    thisurl = makeurl(q, n, k)
                    distance = find(thisurl)
                    if distance is not None:
                        distance = int(distance)
                        Q = math.isqrt(q)
                        MDS = "TRUE" if k <= n - 2 * distance + 2 else "FALSE"
                        writer.writerow({
                            'Q': Q,
                            'N': n,
                            'K': k,
                            'D': distance,
                            'link': "http://www.codetables.de",
                            'MDS': MDS
                        })
                        print(f"{Q} {n} {k} {distance} http://www.codetables.de {MDS}")

main()