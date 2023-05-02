# creating an empty list
lst = []
#inputlist
lst = list(map(int, input("Input: nums = ").split())) 
#inputsum
sum = int(input("Enter Sum : "))
#state output has output or not? 
state = False
#Loop run number 1
for i in range(0,len(lst)-1):
    nums1=i
    #Loop run number 2
    for i in range(i+1,len(lst)):
        nums2=i
        #Condition check sum
        if lst[nums1]+lst[nums2] == sum :
            print("Output : "+str(nums1)+","+str(nums2))
            print("Explanation: Because nums["+str(nums1)+"] + nums["+str(nums2)+"] = "+str(sum))  
            state = True
        i+=1
#Condition State        
if(state == False):
        print("Output: no output"+"\n"+"Explanation: The are no two numbers that add up to 3" )           