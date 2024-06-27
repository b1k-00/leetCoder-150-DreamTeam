class Solution(object):
    def intervalIntersection(self, firstListofints, secondListofints):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        
        #if none match give them a new array thats blank
        if not firstListofints or not secondListofints:
            return []
        
        #initialize my pointers
        #they will search through the interval
        pointer1 = 0
        pointer2 = 0


        result = []


        #pointer 1 & 2 less than both list
        while pointer1 < len(firstListofints) and pointer2 < len(secondListofints):
            startCount1, endCount1 = firstListofints[pointer1]
            startCount2, endCount2 = secondListofints[pointer2]

            if startCount1 > endCount2:
                pointer2 +=1
            elif startCount2> endCount1:
                pointer1 +=1
            else:
                
                result.append([max(startCount1,startCount2), min(endCount1, endCount2)])

                if endCount1 > endCount2:
                    pointer2 +=1
                else:
                    pointer1 +=1
        return result
