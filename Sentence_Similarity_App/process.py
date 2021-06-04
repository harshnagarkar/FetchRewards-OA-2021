import collections
import heapq
import math

print("Imported Compare String Class")

# Sample String for console
s1="!The easiest way to earn points with Fetch Rewards is to just shop for the products you already love. If you have any participating brands on your receipt, you'll get points based on the cost of the products. You don't need to clip any coupons or scan individual barcodes. Just scan each grocery receipt after you shop and we'll find the savings for you."

s2="The easiest way to earn points with Fetch Rewards is to just shop for the items you already buy. If you have any eligible brands on your receipt, you will get points based on the total cost of the products. You do not need to cut out any coupons or scan individual UPCs. Just scan your receipt after you check out and we will find the savings for you."

s3="We are always looking for opportunities for you to earn more points, which is why we also give you a selection of Special Offers. These Special Offers are opportunities to earn bonus points on top of the regular points you earn every time you purchase a participating brand. No need to pre-select these offers, we'll give you the points whether or not you knew about the offer. We just think it is easier that way."

class CompareString(object):

    def removePunctuation(self,s):
        """Removes all the punctuation marks in the string

        Args:
            s ([str]): Sentence String

        Returns:
            [str]: Sentence without punctation marks
        """
        i=0

        while i<len(s):

            if s[i] in ".,!*^$@#()\{[]}/?;:'\"":

                s=s[:i]+s[i+1:]

            i+=1

        return s

    def returnDictionary(self,s):
        """Return the dictionary for the string s

        Args:
            s (str): Sentence string

        Returns:
            [collections.defaultdict(list)]: Return a default dictionary with keys as words and values contain Heap made of list containing indexes where the word occured
        """
        data=collections.defaultdict(list)

        for item in range(len(s)):
            heapq.heappush(data[s[item]],item)

        return data

    def manhattanDistance(self,point1,point2):
        """Calculates the manhattan distance between the points

        Args:
            point1 (int): index of word occurence in s1
            point2 (int): index of word occurence in s2

        Returns:
            [int]: manhattan distance calculated from origin
        """
        return abs(point2-point1)

    def checkRemainingDistance(self,s2,max_distance):
        """For the remaining items in s2 heap, max distance is added to the total distance where we consider that the word present is s2 is added to the end of sentence s1.

        Args:
            s2 (defaultdict): Sentence 2 default dictionary containing the remaining words not in Sentence one
            max_distance (int): length of dictionary of Sentence 1 or max length

        Returns:
            distance[int]: the total manhattan distance calculated per word index occurence
            count[int]:  The total count of indexes that were processed
        """
        distance=0
        count=0

        if len(s2)>0:

            for k,v in s2.items():

                while len(s2[k])>0:

                    d2=heapq.heappop(s2[k])
                    distance+=self.manhattanDistance(d2,max_distance)

                    count+=1

        return count,distance

    def calculateDistance(self,s1,s2,mx):
        """Calculates the manhattan distance between index for the words occuring the both of dictionary. 
        If word is present in Sentence 1 but not in Sentence 2 the max distance is added else 
        If word is present in Sentence 2 but not in Sentence 1 the word is processed in the checkRemainingDistance function.

        Args:
            s1 (defaultdict): Sentence 1 default dictionary where key is the word and value is the Heap made of list containing the indexes where the word occured
            s2 (defaultdict): Sentence 2 default dictionary where key is the word and value is the Heap made of list containing the indexes where the word occured
            mx (int): Max length of the sentence1 

        Returns:
            count[int]: Total number of word indexes processed in both of dictionaries
            distance[int]: total distance Sentence 2 is away from Sentence 1
            max_distance[int]: The length of the Sentence 1 
        """
        distance=0
        count=0

        max_distance=mx
        list_data=list(s1.items())


        while list_data:

            k,v=list_data[0]

            if k in s2:
                d2=heapq.heappop(s2[k])
                d1=heapq.heappop(s1[k])
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

        c2,d2=self.checkRemainingDistance(s2,max_distance)
        distance+=d2
        count+=c2

        return count,distance,max_distance
        

    def sentenceSimilarity(self,s1,s2):
        """This is the primary driver for the checking the sentence similarity where the query is Sentence 1 and document is Sentence 2. 
        The function pipelines.
        Preprocessing
            Sentences 1 and Sentence 2-> punctuations Removal -> split then with spaces -> converted in list -> Converted into defaultDict with key as word and value as heap list index
        Distance Calculation
            Distance is calculated for Sentence 1 being far away from Sentence 2
        Output:
            Normalizing-> Divides the distance caculated by the (total count times the max distance for Sentence 1)
            After the values are in range 0-1 
            Return the Cos function where if distance is less or close to zero then the similarity score is high or if the distance is more that is close to 1 then the similarity score is low


        Args:
            s1 (str): Sentence 1 String
            s2 (str): Sentence 2 String

        Returns:
            : [description]
        """
        s1=self.removePunctuation(s1)
        s2=self.removePunctuation(s2)
        
        s1=s1.split()
        mx=len(s1)
        
        s2=s2.split()

        s1=self.returnDictionary(s1)
        s2=self.returnDictionary(s2)
        
        count,similarDistance,max_distance=self.calculateDistance(s1,s2,mx)

        print("The similar distance is",similarDistance)

        return math.cos(similarDistance/(count*max_distance))


    
    
    
    
    
    
    
    
    
    
    
    
    