# -*- coding: utf-8 -*-
"""

@author: Anil Sen & Beyza Arslan

"""

import pandas as pd
import numpy as np

#cleaned and matched ready master dataset
high_schools_data="data/public_high_schools_data.xlsx"

#GDP per capita data for each province
gdp_file='data/gdp_data.xlsx'

#read master data
data = pd.read_excel(high_schools_data, "Data")

#read gdp per capita data
gdppercapita = pd.read_excel(gdp_file, " Per capita GDP ($)")

#gerekli mi emin değilim
#gdppercapita = gdppercapita.apply(lambda x: x.astype(str).str.upper())



# add gdp per capita data to master data
gdpdata=[]
for province in data["province"]:
    gdpdata.append(round(float(gdppercapita[2019][pd.Index(gdppercapita["province"]).get_loc(province)]),2))

data["gdpdata"]=gdpdata

#"Pansiyon(Kız/Erkek)","Pansiyon(Erkek)" and "Pansiyon(Kız)" mean that the high school has a dormitory.
#"Pansiyon yok" means that the high school has not a dormitory.

#Instead of these values, we wrote 1 if the high school has a dormitory and 0 if it does not.
data["high_school_dormitory"] = data["high_school_dormitory"].map({"Pansiyon(Kız/Erkek)":1, "Pansiyon(Erkek)" : 1, "Pansiyon(Kız)" : 1, "Pansiyon Yok" : 0})

#""Hazırlık + 4 yıl"" means that the high school has a prep school.
#"4 yıl" means that the high school has not a prep school.

#Instead of these values, we wrote 1 if the high school has a prep school and 0 if it does not.
data["high_school_with_prep"] = data["high_school_with_prep"].map({"Hazırlık + 4 yıl":1, "4 yıl" : 0})


#you can run the following loop to create the lists
"""
for i in range(1, 7):
    command_variable = data + str(i) + " = [] "
    exec(command_variable)
"""

#veride öğrencilerin bilgileri yer alıyor, liselerin bilgilerinin yer aldığı bir dataframe oluşturacağız.
data1,data2,data3,data4,data5,data6=[],[],[],[],[],[]

datahschool1,datahschool2,datahschool3,datahschool4=[],[],[],[]
datahschool5,datahschool6,datahschool7,datahschool8=[],[],[],[]




# tüm unique lise isimlerini loop'a alıyoruz
for i in pd.unique(data["high_school_name"]):
    #bu lisede yer alan tüm öğrencilerin verisi
    k_data=data.loc[data['high_school_name']==i]
    #okulun öğrenci sayısının birden fazla olması gerekiyor
    if len(k_data)>0:
        #yeni mezun olan öğrencilerin verilerini filtreliyor
        newly=k_data[k_data["newly_graduated_student"].values==1]
        #eğer yeni öğrenci sayısı birden fazlaysa,
        #bu öğrencilerin diploma notlarının ve üniversite sınavı
        #puanlarının ortalamasını alıp listelere ekliyoruz
        if len(newly) >0:
           data1.append(np.average(newly["lowest_score"]))
           data4.append(np.average(newly["average_diploma_grade"]))
        #hiç öğrenci yoksa 0'lar ekliyoruz.
        else:
            data1.append(0)
            data4.append(0)
        #önceden mezun olan öğrencilerin verilerini filtreliyor
        grad=k_data[k_data["former_graduate_student"].values==1]
        #eğer önceden mezun olan öğrenci sayısı birden fazlaysa,
        #bu öğrencilerin diploma notlarının ve üniversite sınavı
        #puanlarının ortalamasını alıp listelere ekliyoruz
        if len(grad) >0:
            data5.append(np.average(grad["lowest_score"]))
            data6.append(np.average(grad["average_diploma_grade"]))
        #hiç öğrenci yoksa 0'lar ekliyoruz.
        else:
            data5.append(0)
            data6.append(0)
        
        #sırayla gerekli bilgileri listelere ekliyoruz.
            
        #lisenin toplam yeni mezun ettiği öğrenci sayısı
        data2.append(np.sum(k_data["newly_graduated_student"]))
        #lisenin toplam eskiden mezun ettiği öğrenci sayısı
        data3.append(np.sum(k_data["former_graduate_student"]))
        #lisenin ismi
        datahschool1.append(np.array(k_data["high_school_name"])[0])
        #lisenin percentile'ı
        datahschool2.append(np.array(k_data["percentile_of_2019"])[0])
        #lisenin kotası
        datahschool3.append(np.array(k_data["high_school_quota_2019"])[0])
        #lisenin prep school'unun olup olmamaması
        datahschool4.append(np.array(k_data["high_school_with_prep"])[0])
        #lisenin yurdunun olup olmamaması
        datahschool5.append(np.array(k_data["high_school_dormitory"])[0])
        #lisenin türü
        datahschool6.append(np.array(k_data["high_school_type"])[0])
        #lisenin bulunduğu ilin gdp per capitası
        datahschool7.append(np.array(k_data["gdpdata"])[0])
        #lisenin bulunduğu il
        datahschool8.append(np.array(k_data["province"])[0])

#oluşturduğumuz listelerle bir dataframe oluşturuyoruz.    

highschool=pd.DataFrame({"lowest_score":data1,
                     "newly_graduated_student":data2,
                     "former_graduate_student":data3,
                     "average_diploma_grade":data4,
                     "high_school_name":datahschool1,
                     "percentile_of_2019":datahschool2,
                     "high_school_quota_2019":datahschool3,
                     "high_school_with_prep":datahschool4,
                     "high_school_dormitory":datahschool5,
                     "high_school_type":datahschool6,
                     "gdpdata":datahschool7,
                     "province":datahschool8}           
    )

#liselerin faktör verimliliklerini aşağıdaki formülle hesaplıyoruz:
    #(newly graduated student* high school average university exam score)/high school quota

highschool["factor"]=list((highschool["newly_graduated_student"]*highschool["lowest_score"])/highschool["high_school_quota_2019"])

#differanibale olabilmesi için boyutlar arasındaki farkı arttıyoruz.
highschool["bubblesize"]=(highschool["high_school_quota_2019"]**1.5)/10

#her lise tipinin açıklamasını ekliyoruz
high_school_type=[]
for number in highschool["high_school_type"]:
    if number==1:
        high_school_type.append("Science High School")
    
    if number==2:
        high_school_type.append("Anatolian High School")

    if number==3:
        high_school_type.append("Anatolian Imam Hatip High School")

    if number==4:
        high_school_type.append("Vocational High School")

    if number==5:
        high_school_type.append("Social Science High School")

#yukarıdaki veriyi dataframe'e ekliyoruz.
highschool["high_school_type"]=high_school_type

#If you want, you can work on this excel file by 
#converting this dataframe to an excel file.

#highschool.to_excel("data/high_school_dataset.xlsx",sheet_name='Data')



#veride öğrencilerin bilgileri yer alıyor, şehirlerin bilgilerinin yer aldığı bir dataframe oluşturacağız.
#yukarıda süreci şehirler için tekrar ediyoruz.

province1,province2,province3,province4,province5,province6=[],[],[],[],[],[]

provincedata1,provincedata2,provincedata3,provincedata4=[],[],[],[]
provincedata5,provincedata6,provincedata7,provincedata8=[],[],[],[]


for i in pd.unique(data["province"]):
    k_data=data.loc[data['province']==i]
    if len(k_data)>0: 
        newly=k_data[k_data["newly_graduated_student"].values==1]
        if len(newly) >0:
           province1.append(np.average(newly["lowest_score"]))
           province4.append(np.average(newly["average_diploma_grade"]))
        else:
            province1.append(0)
            province4.append(0)
        grad=k_data[k_data["former_graduate_student"].values==1]
        if len(grad) >0:
            province5.append(np.average(grad["lowest_score"]))
            province6.append(np.average(grad["average_diploma_grade"]))
        else:
            province5.append(0)
            province6.append(0)
        province2.append(np.sum(k_data["newly_graduated_student"]))
        province3.append(np.sum(k_data["former_graduate_student"]))
        provincedata2.append(np.average(k_data["percentile_of_2019"]))
        holding="0"
        k_quota=0
        for i in range(len(k_data["high_school_name"])):
            if np.array(k_data["high_school_name"])[i]==holding:
                pass
            else:
                k_quota+=np.array(k_data["high_school_quota_2019"])[i]
                holding=np.array(k_data["high_school_name"])[i]
        provincedata3.append(k_quota)
        k_quota=0
        provincedata4.append(np.average(k_data["high_school_with_prep"]))
        provincedata5.append(np.average(k_data["high_school_dormitory"]))
        provincedata7.append(np.array(k_data["gdpdata"])[0])
        provincedata8.append(np.array(k_data["province"])[0])


provinces=pd.DataFrame()

provinces=pd.DataFrame({"lowest_score":province1,
                     "newly_graduated_student":province2,
                     "former_graduate_student":province3,
                     "average_diploma_grade":province4,
                     "percentile_of_2019":provincedata2,
                     "high_school_quota_2019":provincedata3,
                     "high_school_with_prep":provincedata4,
                     "high_school_dormitory":provincedata5,
                     "gdpdata":provincedata7,
                     "province":provincedata8}           
    )


provinces["factor"]=list((provinces["newly_graduated_student"]*provinces["lowest_score"])/provinces["high_school_quota_2019"])


#If you want, you can work on this excel file by 
#converting this dataframe to an excel file.

#provinces.to_excel("data/provinces_dataset.xlsx",sheet_name='Data')
