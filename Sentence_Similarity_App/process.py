import collections
import heapq
import math
print("Hello World!")


s1="!The easiest way to earn points with Fetch Rewards is to just shop for the products you already love. If you have any participating brands on your receipt, you'll get points based on the cost of the products. You don't need to clip any coupons or scan individual barcodes. Just scan each grocery receipt after you shop and we'll find the savings for you."

s2="The easiest way to earn points with Fetch Rewards is to just shop for the items you already buy. If you have any eligible brands on your receipt, you will get points based on the total cost of the products. You do not need to cut out any coupons or scan individual UPCs. Just scan your receipt after you check out and we will find the savings for you."

s3="We are always looking for opportunities for you to earn more points, which is why we also give you a selection of Special Offers. These Special Offers are opportunities to earn bonus points on top of the regular points you earn every time you purchase a participating brand. No need to pre-select these offers, we'll give you the points whether or not you knew about the offer. We just think it is easier that way."

class CompareString:

    def removePunctuation(self,s):
        i=0
        while i<len(s):
            if s[i] in ".,!*^$@#()\{[]}/?;:'\"":
                print(s[i])
                s=s[:i]+s[i+1:]
            i+=1
        return s
        
    def returnDictionary(self,s):
        data=collections.defaultdict(list)
        for item in range(len(s)):
            heapq.heappush(data[s[item]],item)
        return data

    def manhattanDistance(self,point1,point2):
        return abs(point2-point1)

    def checkRemainingDistance(self,s2,max_distance):
        distance=0
        count=0
        if len(s2)>0:
            for k,v in s2.items():
                while len(s2[k])>0:
                    d2=heapq.heappop(s2[k])
                    distance+=self.manhattanDistance(d2,max_distance)
                    count+=1
        return count,distance

    def calculateDistance(self,s1,s2):
        distance=0
        count=0
        max_distance=len(s1)
        # print(list(s1.items()))
        list_data=list(s1.items())
        while list_data:
            k,v=list_data[0]
            if k in s2:
                d2=heapq.heappop(s2[k])
                d1=heapq.heappop(s1[k])
                # print(list_data[0],k,v)
                # list_data[0]=(list_data[0][0],list_data[0][1]-1)
                distance+=self.manhattanDistance(d1,d2)
                if len(s2[k])==0:
                    del s2[k]
                if len(s1[k])==0:
                    del s1[k]
                    del list_data[0]
            else:
                d1=heapq.heappop(s1[k])
                if len(s1[k])==0:
                    del s1[k]
                    del list_data[0]
                distance+=max_distance
            count+=1
        # print("before distance",distance)
        c2,d2=self.checkRemainingDistance(s2,max_distance)
        distance+=d2
        count+=c2
        # print("after distance",distance)
        return count,distance,max_distance
        

    def sentenceSimilarity(self,s1,s2):
        s1=self.removePunctuation(s1)
        s2=self.removePunctuation(s2)
        # print(s1)
        s1=s1.split()
        s2=s2.split()
        s1=self.returnDictionary(s1)
        s2=self.returnDictionary(s2)
        # print(s1)
        
        count,similarDistance,max_distance=self.calculateDistance(s1,s2)
        print("The similar distance is",similarDistance)
        return math.cos(similarDistance/(count*max_distance))

# print(math.cos(sentenceSimilarity(s1,s2)))

# print(math.cos(sentenceSimilarity(s1,s3)))
    
    
    
    
    
    
    
    
    
    
    
    
    
    