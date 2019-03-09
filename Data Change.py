#change all string to integer for training the data

import pandas as pd
data=pd.read_csv("a.csv")
data.job[data.job=="admin."]=1
data.job[data.job=="blue-collar"]=2
data.job[data.job=="entrepreneur"]=3
data.job[data.job=="housemaid"]=4
data.job[data.job=="management"]=5
data.job[data.job=="retired"]=6
data.job[data.job=="self-employed"]=7
data.job[data.job=="services"]=8
data.job[data.job=="student"]=9
data.job[data.job=="technician"]=10
data.job[data.job=="unemployed"]=11
data.job[data.job=="unknown"]=0

data.marital[data.marital=="divorced"]=1
data.marital[data.marital=="married"]=2
data.marital[data.marital=="single"]=3
data.marital[data.marital=="unknown"]=0

data.education[data.education=="basic.4y"]=1
data.education[data.education=="basic.6y"]=2
data.education[data.education=="basic.9y"]=3
data.education[data.education=="high.school"]=4
data.education[data.education=="illiterate"]=5
data.education[data.education=="professional.course"]=6
data.education[data.education=="university.degree"]=7
data.education[data.education=="unknown"]=0

data.default[data.default=="no"]=1
data.default[data.default=="yes"]=2
data.default[data.default=="unknown"]=0

data.housing[data.housing=="no"]=1
data.housing[data.housing=="yes"]=2
data.housing[data.housing=="unknown"]=0

data.loan[data.loan=="no"]=1
data.loan[data.loan=="yes"]=2
data.loan[data.loan=="unknown"]=0

data.contact[data.contact=="cellular"]=1
data.contact[data.contact=="telephone"]=2

data.month[data.month=="jan"]=1
data.month[data.month=="feb"]=2
data.month[data.month=="mar"]=3
data.month[data.month=="apr"]=4
data.month[data.month=="may"]=5
data.month[data.month=="jun"]=6
data.month[data.month=="jul"]=7
data.month[data.month=="aug"]=8
data.month[data.month=="sep"]=9
data.month[data.month=="oct"]=10
data.month[data.month=="nov"]=11
data.month[data.month=="dec"]=12

data.day_of_week[data.day_of_week=="mon"]=1
data.day_of_week[data.day_of_week=="tue"]=2
data.day_of_week[data.day_of_week=="wed"]=3
data.day_of_week[data.day_of_week=="thu"]=4
data.day_of_week[data.day_of_week=="fri"]=5

data.poutcome[data.poutcome=="failure"]=1
data.poutcome[data.poutcome=="nonexistent"]=2
data.poutcome[data.poutcome=="success"]=3

data.y[data.y=="yes"]=1
data.y[data.y=="no"]=0

print(data)

data.to_csv("bank-additional-full_update.csv",encoding='utf-8',index=False)

data=pd.read_csv("bank-additional-full_update.csv")
print(data)
