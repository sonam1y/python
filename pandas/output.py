import pandas as pd
Customer={
    "cstmr_name":["Arjun","Anurag","Archana","Priyanshu","Akash"],
    "cstmr_age":[54,65,13,54,65],
    "cstmr_address":["Jaunpur","Agra","Mujaffarpur","Patna","Jaunpur"],
    "cstmr_gender":["M","M","F","M","M"]
}
Dtf=pd.DataFrame(Customer)
Dtf.to_csv("output.csv",index=False)


import pandas as pd
df=pd.read_csv("output.csv")
print(df)



import pandas as pd
df=pd.read_csv("details.csv")
print(df.head())


import pandas as pd
df=pd.read_csv("details.csv")
print(df.tail())

import pandas as pd
df=pd.read_csv("details.csv")
print(df.sample())


import pandas as pd
df=pd.read_csv("details.csv")
print(df.shape)


import pandas as pd
df=pd.read_csv("details.csv")
print(df.info())


import pandas as pd
df=pd.read_csv("details.csv")
print(df.describe())



import pandas as pd
df=pd.read_csv("details.csv")
print(df.dtypes)

import pandas as pd
df=pd.read_csv("details.csv")
print(df.columns)


import pandas as pd
df=pd.read_csv("details.csv")
print(df.index)




import pandas as pd
df=pd.read_csv("details.csv")
print(df.isnull().sum())
print(df.dropna().isnull().sum())








