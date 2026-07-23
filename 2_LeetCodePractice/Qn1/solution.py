from collections import Counter
import pandas as pd

class Solution:
    
    def isVaccinated(self, doses):

        expected_doses = {
            'PZ': 2,
            'MD': 2,
            'CV': 2,
            'JJ': 1
        }
            
        # sort doses based on second element in each array element ['PZ', 12], sort based on 12
        doses.sort(key=lambda x: x[1]) # ascending O(nlogn)

        # keep a dict of number of doses for each vaccine
        running_count = {
            'PZ': 0,
            'MD': 0,
            'CV': 0,
            'JJ': 0
        }

        prev_dose = ""
        # traverse doses and update running_count
        for idx, dose in enumerate(doses):
            vaccine = dose[0]

            # reduce the count of prev_dose by 1
            if prev_dose:
                if prev_dose == vaccine:
                    # firstly update the running count
                    running_count[vaccine] += 1

                    prev_dose = vaccine
                    
                    # compare running_count withe expected_doses
                    for k, v in running_count.items():
                        if expected_doses[k] == running_count[k]:
                            return 'vaccinated'
                else:
                    running_count[prev_dose] -= 1
                    if running_count[prev_dose] < 0:
                        running_count[prev_dose] = 0

            # firstly update the running count
            running_count[vaccine] += 1

            prev_dose = vaccine
            
            # compare running_count withe expected_doses
            for k, v in running_count.items():
                if expected_doses[k] == running_count[k]:
                    return 'vaccinated'

        # return false otherwise
        return 'not_vaccinated'
            


