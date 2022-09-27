# 函式與流程控制
def calculate(min, max, step):
    sum = 0
    while min <= max:
        sum+=min
        min+=step
    print(sum)

calculate(1,3,1)
calculate(4,8,2)
calculate(-1,2,2)

print("------------------------------")

# 字典與列表
def avg(data):
    sum=0
    count = 0
    employees = data["employees"] # list all employees data as employees
    for employee in employees: # for every employee
        if employee["manager"]==False: # point out manager or not
            sum+=employee["salary"] # sum all employee's salary
            count+=1 # count employee without manager
    mean = sum/count # mean
    print(mean)

avg({
    "employees":[
        {
            "name":"John",
            "salary":30000,
            "manager":False
        },
        {
            "name":"Bob",
            "salary":60000,
            "manager":True
        },
        {
            "name":"Jenny",
            "salary":50000,
            "manager":False
        },
        {
            "name":"Tony",
            "salary":40000,
            "manager":False
        }
    ]
})

print("------------------------------")


# 要求三
def func(a):
    def mul(n1, n2):
        print(a + (n1 * n2))
    return mul

func(2)(3, 4)
func(5)(1, -5)
func(-3)(2, 9)

print("------------------------------")

# 要求四
def maxProduct(nums):
    # set first number to compared
    m = nums[0]*nums[1]
    # for loop to calculate every answer
    for i in range(len(nums)-1):
        for j in nums[i+1:]:
            # comparaed with m. if larget, replace it 
            result = nums[i]*j
            if result > m:
                m = result
    print(m)

maxProduct([5, 20, 2, 6]) # 得到 120
maxProduct([10, -20, 0, 3]) # 得到 30
maxProduct([10, -20, 0, -3]) # 得到 60
maxProduct([-1, 2]) # 得到 -2
maxProduct([-1, 0, 2]) # 得到 0
maxProduct([5,-1, -2, 0]) # 得到 2
maxProduct([-5, -2]) # 得到 10

print("------------------------------")

# 要求五
def twoSum(nums, target):
    for i in range(len(nums)):
        # check difference 
        dif = target-nums[i]
        # find dif
        if dif in nums and nums.index(dif) != i:
            return [i, nums.index(dif)]

result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9

print("------------------------------")

# 要求六
def maxZeros(nums):
    # set a series and count
    series = 0
    count = 0
    # count 0
    for i in nums:
        if i == 0:
            count += 1
            # replace series number
            if count>series:
                series = count
        else:
            count = 0
    print(series)

maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4
maxZeros([1, 1, 1, 1, 1]) # 得到 0
maxZeros([0, 0, 0, 1, 1]) # 得到 3


