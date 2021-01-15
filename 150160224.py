import sys
from math import sqrt
from datetime import datetime

def readfile():
    f = open("location.txt", "r", encoding="utf8")
    lines = f.readlines()
    return lines

def createArray(lines,N):
    cities = []
    nCounter = 0
    for line in lines:
        if nCounter == N:
            break
        l = line.split("\t")
        city = { "name":l[0],"latitude":float(l[1]),"longitude":float(l[2]), "distance":0}
        cities.append(city)
        nCounter+=1
    return cities

def calculateDist(x1,y1,x2,y2):
    return sqrt((x2-x1)**2 + (y2-y1)**2)

def addDist(cities, latitude, longitude):
    for city in cities:
        distance = calculateDist(city["latitude"] , city["longitude"], latitude, longitude)
        city["distance"] = distance

def writeToFile(arr):
    fileToWrite = open("results.txt","w")
    for city in arr: 
        try:
            fileToWrite.write(str(city["name"])+'\t'+str(city["latitude"])+'\t'+str(city["longitude"])+'\n')
        except:
            fileToWrite.write("????????"+'\t'+str(city["latitude"])+'\t'+str(city["longitude"])+'\n')
    fileToWrite.close()

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[largest]["distance"] < arr[l]["distance"]:
        largest = l
    if r < n and arr[largest]["distance"] < arr[r]["distance"]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
 
def heapSort(arr):
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

def main():
    # N = {10, 100, 1000, 1000000} 
    # K = {1, 2, 10, N/2}
    N = int(sys.argv[1])
    K = int(sys.argv[2])
    latitude = float(sys.argv[3])
    longitude = float(sys.argv[4])


    cities = createArray(readfile(),N)
    addDist(cities, latitude, longitude)
    tstart = datetime.now()
    heapSort(cities)
    tend = datetime.now()
    cities = cities[0:K]



    print(tend - tstart)
    writeToFile(cities)

main()