import pandas as pd
from scipy.stats import kurtosis
from collections import Counter



df = pd.read_csv("C:\\Users\\Admin\\Downloads\\Mall_Customers.csv")
print(df)


'''central tendency'''

'''mean'''
def mean(data):
    m_age = sum(age)/len(age)
    return m_age



'''median'''
def median(data):

    dataset=sorted(data)
    index = len(dataset) // 2
    
    if len(data) % 2 != 0:
        return dataset[index]
    
    return (dataset[index - 1] + dataset[index]) / 2

    if n % 2 == 0:
        m1=data[n//2]
        m2=data[(n-1)//2]
        median = (m1+m2)/2
    else:
        median = data[n//2]

    return median



'''mode'''

def mode(data):
    
    
    mo = Counter(data)
    d = dict(mo)

    max1=max(list(mo.values()))
    mod = [num for num, rep in d.items() if rep == max1]
    if len(mod) == len(data):
        print("No mode")
    else:
        return mod

age=df['Age']
mean_age= mean(age)
print(mean_age)

age_med=median(age)
print(age_med)

mode_age = mode(age)
print(mode_age)



'''Skewness'''
def skewness(data):
    
    skewness= (mean_age - age_med)/len(data)
    
    return skewness

sk = skewness(age)
print(sk)



















