#Kutuphane kurulumlari
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sbn

#Veri aktarma
df=pd.read_csv(r"C:\Users\90507\Desktop\yazılım\Dataset\eksikveriler.csv")

#Eksik veri bulma
df.isnull().sum()

#Eksik verilerin yerini doldurma
from sklearn.impute import SimpleImputer
imputer=SimpleImputer(missing_values=np.nan, strategy="mean")

yas=df.iloc[:,1:4].values
imputer=imputer.fit(yas[:,1:4])
yas[:,1:4]=imputer.transform(yas[:,1:4])

#One Hot Encoding
ulke=df.iloc[:,0:1].values
from sklearn import preprocessing
le=preprocessing.LabelEncoder()
ohe=preprocessing.OneHotEncoder()
ulke[:,0]=le.fit_transform(df.iloc[:,0])
ulke=ohe.fit_transform(ulke).toarray()

#Veri birlestirme
cinsiyet=veri.iloc[:,-1]

sonuc=pd.DataFrame(data=ulke, index=range(22),columns=["fr","tr","us"])
sonuc2=pd.DataFrame(data=yas,index=range(22),columns=["boy","kilo","yas"])
sonuc3=pd.DataFrame(data=cinsiyet,index=range(22),columns=["cinsiyet"])

s=pd.concat([sonuc,sonuc2],axis=1)
s2=pd.concat([s,sonuc3],axis=1)

#Veri Kumeleri Egitimi
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(s,sonuc3,test_size=0.3,random_state=0)

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
X_train=sc.fit_transform(x_train)
X_test=sc.fit_transform(x_test)

#Linear Regrasyon Olusturma
from sklearn.linear_model import LinearRegression
lr=LinearRegression()
lr.fit(x_train,y_train)

#Linear Regrasyon Cıktısı Alma
tahmin=lr.predict(x_test)

x_train=x_train.sort_index()
y_train=y_train.sort_index()

plt.plot(x_train,y_train)
plt.plot(x_test,lr.predict(x_test))
plt.title("aylara gore satis")
plt.xlabel("aylar")
plt.ylabel("satislar")

#Ogrenme zimbirtisi ayarlama
regrassor=LinearRegression()
regrassor.fit(x_train,y_train)
y_pred=regrassor.predict(x_test)
import statsmodels.api as sm
X = np.append(arr=np.ones((22,1)).astype(int),values=veri,axis=1)

X_l=veri.iloc[:,[0,1,2,3,4,5]].values
X_l=np.array(X_l,dtype=float)
model=sm.OLS(boy,X_l).fit()
model.summary()