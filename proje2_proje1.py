# -*- coding: utf-8 -*-
"""Proje2-Proje1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1D9KZYiK1RU60cz0SWvi94pCYtm_GGQe4
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("NetflixOriginals.csv",encoding="ISO-8859-1")
df.head()

df.info()

#Veri setine göre uzun soluklu filmler hangi dilde oluşturulmuştur? Görselleştirme yapınız.
UzunFilmler = df[["Title","Runtime","Language"]].sort_values("Runtime",ascending = False)
UzunFilmler.head(15)

diller = list(UzunFilmler["Language"].values)
grup_diller = []
for i in diller:
    if i in grup_diller:
        continue
    else:
        grup_diller.append(i)
grup_diller_degerleri = UzunFilmler["Language"].value_counts()
grup_diller_degerleri

plt.figure(figsize = (25,25))
plt.xticks(rotation=90)
sns.barplot(x = grup_diller,y = grup_diller_degerleri)

aylar = {"January":"1","February":"2","March":"3","April":"4","May":"5","June":"6","July":"7","August":"8","September":"9","October":"10","November":"11","December":"12"}
#2019 Ocak ile 2020 Haziran tarihleri arasında 'Documentary' türünde çekilmiş filmlerin IMDB değerlerini bulup görselleştiriniz.
ad = df.copy()
premiere_list = ad["Premiere"]
result_premiere_list = []

for tarih in premiere_list:
    text = tarih.split(" ")
    ay = text[0]
    ay = aylar[ay]
    text[0] = ay
    result = ""
    for i in text:
        result += i + " "
        
    result = result.rstrip(" ")
    result_premiere_list.append(result)
ad["Premiere"] = result_premiere_list

ay_imdb_dict = {}
for i in range(len(ad)):
    satir = ad.iloc[i]
    if satir["Premiere"].split(" ")[2] == "2019" or (satir["Premiere"].split(" ")[2] == "2020" and int((satir["Premiere"].split(" ")[1]).split(",")[0])<= 6):
        ay_imdb_dict[satir["Title"]] = satir["IMDB Score"]
        
film_isimleri = []
film_imdb_score = []

for key in ay_imdb_dict:
    film_isimleri.append(key)
    film_imdb_score.append(ay_imdb_dict[key])

plt.figure(figsize = (25,25))
plt.xticks(rotation = 90)
sns.barplot(x = film_isimleri, y = film_imdb_score)

#İngilizce çekilen filmler içerisinde hangi tür en yüksek IMDB puanına sahiptir?
ingFilm = df[df["Language"] == "English"]
ingFilm

ingFilm = ingFilm.sort_values("IMDB Score",ascending = False)
ingFilm.iloc[0]

#'Hindi' Dilinde çekilmiş olan filmlerin ortalama 'runtime' suresi nedir?
hinFilm = df[df["Language"] == "Hindi"]
hinFilm.head()

ortalama_hint_filmi_süresi = sum(hinFilm["Runtime"])/(len(hinFilm))
ortalama_hint_filmi_süresi

#'Genre' Sütunu kaç kategoriye sahiptir ve bu kategoriler nelerdir? Görselleştirerek ifade ediniz.
filmTurleri = []
for var in df["Genre"]:
    if var in filmTurleri:
        continue
    else:
        filmTurleri.append(var)

plt.figure(figsize = (25,25))
plt.xticks(rotation = 90)
sns.barplot(x = filmTurleri,y = df["Genre"].value_counts())

df["Genre"].value_counts()

#Veri setinde bulunan filmlerde en çok kullanılan 3 dili bulunuz.
grup_diller_degerleri[:3]

#IMDB puanı en yüksek olan ilk 10 film hangileridir?
df.sort_values("IMDB Score",ascending = False).head(10)

#IMDB puanı ile 'Runtime' arasında nasıl bir korelasyon vardır? İnceleyip görselleştiriniz.
plt.figure(figsize = (25,25))
sns.pairplot(df)

#IMDB Puanı en yüksek olan ilk 10 'Genre' hangileridir? Görselleştiriniz.
turlerin_imdb_puan_ortalamasi = {}
for tur in filmTurleri:
    data = df[df["Genre"] == tur]
    imdb_score = sum(data["IMDB Score"])/(len(data))
    turlerin_imdb_puan_ortalamasi[tur] = imdb_score

key = list(turlerin_imdb_puan_ortalamasi.keys())
values = list(turlerin_imdb_puan_ortalamasi.values())

genreImdbDf = pd.DataFrame(columns = ["Genre","Imdb Score"])
genreImdbDf["Genre"] = key
genreImdbDf["Imdb Score"] = values
genreImdbDf = genreImdbDf.sort_values("Imdb Score",ascending = False)
genreImdbDf.index = range(len(genreImdbDf))
genreImdbDf.head(10)

plt.figure(figsize = (25,25))
plt.xticks(rotation = 90)
sns.barplot(x = genreImdbDf["Genre"].head(10).values, y = genreImdbDf["Imdb Score"].head(10).values)

plt.figure(figsize = (25,25))
plt.xticks(rotation = 90)
plt.title("Tüm Türlerin Imdb Ortalaması")
sns.barplot(x = genreImdbDf["Genre"].values, y = genreImdbDf["Imdb Score"].values)

#Runtime değeri en yüksek olan ilk 10 film hangileridir? Görselleştiriniz.
runtime = df.sort_values("Runtime",ascending = False)[:10]
runtime

plt.figure(figsize = (10,10))
plt.xticks(rotation = 90)
sns.barplot(x = runtime["Title"],y = runtime["Runtime"])

#Hangi yılda en fazla film yayımlanmıştır? Görselleştiriniz.
yıllar = df["Premiere"]
yillarin_film_data = {}
for tarih in yıllar:
    yıl = tarih.split(" ")[2]
    if yıl in yillarin_film_data:
        yillarin_film_data[yıl] +=1
    else:
        yillarin_film_data[yıl] = 1
        
key_yil = list(yillarin_film_data.keys())
value_yil = list(yillarin_film_data.values())

plt.figure(figsize = (10,10))
plt.xticks(rotation = 90)
sns.barplot(x = key_yil,y = value_yil)

#Hangi dilde yayımlanan filmler en düşük ortalama IMBD puanına sahiptir? Görselleştiriniz.

dusukImdb = df.sort_values("IMDB Score")
dusukImdb

dil_imdb = []
for i in grup_diller:
    dil = df[df["Language"] == i]
    imdb = sum(dil["IMDB Score"])/len(dil)
    dil_imdb.append(imdb)

plt.figure(figsize = (15,15))
plt.xticks(rotation = 90)
sns.barplot(x = grup_diller, y= dil_imdb)

#Hangi yılın toplam "runtime" süresi en fazladır?
yillar_dictionary = {}
for yil in key_yil:
    yillar_dictionary[yil] = 0
yillar_dictionary

yillar = []
for tarih in df["Premiere"]:
    yil = tarih.split(" ")
    yil = yil[2]
    yillar.append(yil)
df["Yıl"] = yillar
df.head()

YilRun = df[["Runtime","Yıl"]]
for yil in key_yil:
    dataYil = YilRun[YilRun["Yıl"] == yil]
    yillar_dictionary[yil] = sum(dataYil["Runtime"])
    
yillar_dictionary

result = 0
yil_result = 0
for deger in yillar_dictionary:
    tmp = yillar_dictionary[deger]
    if tmp > result:
        yil_result = deger
        result = tmp
print("{} toplam runtime ile {} yılıdır".format(result,yil_result))

#Her bir dilin en fazla kullanıldığı "Genre" nedir?
dil_genre = {}
for dil in grup_diller:
    liste = []
    dilDf = df[df["Language"] == dil]
    genre_counter = dict(dilDf["Genre"].value_counts())
    control = 0
    for i in genre_counter:
        if control<1:
            liste.append(i)
            liste.append(genre_counter[i])
            control = 1
        else:
            control = 1
            break
    dil_genre[dil] = liste
    
dil_genre

#Veri setinde outlier veri var mıdır? Açıklayınız.
outlier = df.copy()
outlier = outlier.select_dtypes(["float64","int64"])
outlier

sns.boxplot(x= outlier["Runtime"])

q1 = outlier["Runtime"].quantile(0.25)
q3 = outlier["Runtime"].quantile(0.75)

ıqr = q3 - q1

lower_bound = q1 - 1.5*ıqr
upper_bound = q3 + 1.5*ıqr

print("Lower Bound: {}\nUpper Bound: {}".format(lower_bound,upper_bound))

"""### Runtime özelliği için 53.0 değerinin altında kalan ve 141.0 değerinin üstünde kalan her değer outlier`dır. Bu yüzden Runtime için outlier vardır."""

sns.boxplot(x = outlier["IMDB Score"])

q1 = outlier["IMDB Score"].quantile(0.25)
q3 = outlier["IMDB Score"].quantile(0.75)

ıqr = q3 - q1

lower_bound = q1 - 1.5*ıqr
upper_bound = q3 + 1.5*ıqr

print("Lower Bound: {}\nUpper Bound: {}".format(lower_bound,upper_bound))

"""### IMDB Score için 3.750 değerinin altında kalan ve 8.95 değerinin üstünde kalan her değer outlier`dir. Bu yüzden IMDB Score için outlier vardır."""



"""Proje 1"""

import pandas as pd

df = pd.DataFrame(columns = ["Name","Surname","School No","Class","Vize","Final","Average","Letter Score","Result"])

def letter_score(exam_score):
    result = ""
    if(90<=exam_score<=100):
        result = "AA"
    elif(80<=exam_score<90):
        result = "AB"
    elif(70<=exam_score<80):
        result = "BB"
    elif(60<=exam_score<70):
        result = "CC"
    elif(50<=exam_score<60):
        result = "DD"
    elif(0<=exam_score<50):
        result = "FF"
    else:
        result = ""
    return result

def lesson_result(exam_score):
    result = ""
    if(exam_score>=50):
        result = "Success"
        
    elif(0<=exam_score<50):
        result = "Left"
        
    else:
        result = ""
        
    return result

while True:
    name = input("Enter name(Press 'q' for exit):")
    if name == "q":
        df.to_csv("OgrenciNotlari.csv")
        break   
    surname = input("Enter surname:")
    school_number = input("Enter school number:")
    lesson = input("Enter lesson:")
    midterm_exam = int(input("Enter midterm exam score:"))
    final = int(input("Enter final exam score:"))
    average = midterm_exam*(0.4) + final*(0.6)
    letter = letter_score(average)
    result = lesson_result(average)
    dictionary = {}
    info = list(df.columns)
    List = [name,surname,school_number,lesson,midterm_exam,final,average,letter,result]
    for i in range(len(List)):
        dictionary[info[i]] = List[i]
    df = df.append(dictionary,ignore_index = True)

df