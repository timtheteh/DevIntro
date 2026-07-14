from solution import Solution

s = Solution()

def check(actual, expected, label):
    if actual != expected:
        print(f"FAIL [{label}]: got {actual}, expected {expected}")
    else:
        print(f"PASS [{label}]")


check(
    s.isVaccinated([['PZ', 30], ['PZ', 47]]), 
    'vaccinated',  
    "test case 1")

running_count = {
            'PZ': 2,
            'MD': 0,
            'CV': 0,
            'JJ': 0
        }

check(
    s.isVaccinated([['MD', 30], ['CV', 40], ['MD', 37]]), 
    'vaccinated',  
    "test case 2")

check(
    s.isVaccinated([['JJ', 10], ['CV', 35]]), 
    'vaccinated',  
    "test case 3")

check(
    s.isVaccinated([['CV', 10], ['CV', 17], ['MD', 35]]), 
    'vaccinated',  
    "test case 4")

check(
    s.isVaccinated([['PZ', 30], ['PZ', 73], ['MD', 48], ['MD', 105]]), 
    'not_vaccinated',  
    "test case 5")

check(
    s.isVaccinated([['PZ', 30], ['PZ', 73], ['MD', 48], ['MD', 105], ['MD', 80]]), 
    'vaccinated',  
    "test case 6")

# triple
check(
    s.isVaccinated([['PZ', 30], ['CV', 73], ['MD', 48], ['MD', 105], ['MD', 80]]), 
    'vaccinated',  
    "test case 7")

# multiple valid
check(
    s.isVaccinated([['JJ', 15], ['CV', 73], ['PZ', 30], ['PZ', 73], ['MD', 48], ['CV', 74], ['MD', 105], ['MD', 80]]), 
    'vaccinated',  
    "test case 8")

# [['PZ', 30], ['MD', 48], ['PZ', 73], ['MD', 105]]

# running_count = {
#             'PZ': 2,
#             'MD': 1,
#             'CV': 0,
#             'JJ': 0
#         }
