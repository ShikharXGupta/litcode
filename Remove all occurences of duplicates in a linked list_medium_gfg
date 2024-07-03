from collections import OrderedDict

class Solution:
    
    # Finding the unique element while maintaning the sequence 
    def findUniqueElements(self, arr):
        count_dict = OrderedDict()
        
        # Count occurrences of each element
        for num in arr:
            if num in count_dict:
                count_dict[num] += 1
            else:
                count_dict[num] = 1
        
        # Collect elements that appear exactly once, maintaining order
        unique_elements = [num for num, count in count_dict.items() if count == 1]
        
        return unique_elements
    
    
    def removeAllDuplicates(self, head):
        #code here
        arr=[]
        temp = head 
        while temp:
            arr.append(temp.data)
            temp =temp.next 
            
        ans =[]
        ans =self.findUniqueElements(arr)
            
            
        temp = head 
        i = 0
        while  temp and i < len(ans):
            temp.data = ans[i]
            i+=1 
            if  i  == len(ans):temp.next = None 
            else : temp = temp.next
              
        return head 
