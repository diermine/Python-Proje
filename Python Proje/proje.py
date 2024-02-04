import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

veri = pd.read_csv("cost_of_living.csv", 
                   names=["Sıralama", "Ülke", "Yaşam Maliyeti Endeksi", "Kira Endeksi", "Yaşam Maliyeti + Kira Endeksi", "Marketler Endeksi", "Restoran Fiyat Endeksi", "Yerel Satın Alma Gücü Endeksi"], header=0)

print(veri.columns)


def soru1(data_frame):
    sorted_data = data_frame.sort_values("Yaşam Maliyeti Endeksi", ascending=True)
    top10 = sorted_data.head(10)
    colors = sns.color_palette("viridis", len(top10))
    plt.figure(figsize=(8, 8))
    plt.pie(top10["Yaşam Maliyeti Endeksi"], labels=top10["Ülke"], colors=colors, autopct='%1.1f%%', startangle=90)
    plt.gca().add_artist(plt.Circle((0,0),0.70,fc='white')) 
    plt.title("En Düşük Toplam Yaşam Maliyetine Sahip 10 Ülke")
    plt.show()

def soru2(data_frame):
    sorted_data = data_frame.sort_values("Yaşam Maliyeti Endeksi", ascending=False)
    bottom10 = sorted_data.head(10)
    colors = sns.color_palette("magma", len(bottom10))
    plt.figure(figsize=(8, 8))
    plt.pie(bottom10["Yaşam Maliyeti Endeksi"], labels=bottom10["Ülke"], colors=colors, autopct='%1.1f%%', startangle=90)
    plt.gca().add_artist(plt.Circle((0,0),0.70,fc='white'))
    plt.title("En Yüksek Toplam Yaşam Maliyetine Sahip 10 Ülke")
    plt.show()

def soru3(data_frame):
    komut = data_frame[data_frame["Yerel Satın Alma Gücü Endeksi"] > 40]
    plt.figure(figsize=(15, 8))
    sns.barplot(x="Ülke", y="Yerel Satın Alma Gücü Endeksi", data=komut, palette="coolwarm")
    plt.title("Yerel Satın Alma Güçleri  40'tan Yüksek Olan Ülkeler")
    plt.xticks(rotation=90)
    plt.ylabel("Yerel Satın Alma Gücü Endeksi")
    plt.xlabel("Ülkeler")
    plt.show()

def soru4(data_frame):
    plt.figure(figsize=(15, 8))
    sns.scatterplot(x="Kira Endeksi", y="Yaşam Maliyeti Endeksi", data=data_frame, hue="Ülke", palette="Set2")
    plt.title("Kiralama Endeksine Göre Ülkelerin Karşılaştırılması")
    plt.ylabel("Yaşam Maliyeti Endeksi")
    plt.xlabel("Ülkeler")
    plt.xlabel("Kira Endeks Oranı")
    plt.show()

def soru5(data_frame):
    italy_data = data_frame[data_frame["Ülke"] == "Italy"]
    categories = ["Yaşam Maliyeti Endeksi", "Kira Endeksi", "Yaşam Maliyeti + Kira Endeksi", "Marketler Endeksi", "Restoran Fiyat Endeksi", "Yerel Satın Alma Gücü Endeksi"]
    values = italy_data[categories].values.flatten()
    explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
    plt.figure(figsize=(10, 8))
    plt.pie(values, labels=categories, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors, explode=explode)
    plt.title("İtalya'nın Alt Kategorilerdeki Endeks Karşılaştırması")
    plt.xlabel("Katagoriler")
    plt.show()


    #Sığmadığından dolayı sadece ilk csv dosyasındaki ilk 40 veriyi baz alarak yapıldı
def soru6(data_frame):
    plt.figure(figsize=(25, 8))
    sns.barplot(x="Ülke", y="Restoran Fiyat Endeksi", data=data_frame.sort_values("Restoran Fiyat Endeksi", ascending=False).head(40), palette="YlOrRd")
    plt.title("Ülkelerin Restoran Fiyat Endeksine Göre Sıralaması")
    plt.xlabel("Ülkeler")
    plt.xticks(rotation=45, ha="right")  
    plt.ylabel("Restoran Fiyat Endeksi")
    plt.show()


def soru7(data_frame):
    plt.figure(figsize=(12, 8))
    sns.scatterplot(x="Kira Endeksi", y="Yaşam Maliyeti Endeksi", data=data_frame, hue="Ülke", palette="viridis")
    plt.title("Ülkelerin Ortalama Kiralama Endeksi ve Yaşam Maliyeti İlişkisi")
    plt.xlabel("Ülkeler")
    plt.ylabel("Yaşam Maliyeti Endeksi")
    plt.xlabel("Kira Endeksi Oranı")
    plt.show()

def soru8(data_frame):
    kira_endeksi_sıralı = data_frame.sort_values("Kira Endeksi", ascending=True)
    en_düşük_10_kira = kira_endeksi_sıralı.head(14)
    explode = [0.1] * len(en_düşük_10_kira)
    plt.figure(figsize=(8, 8))
    plt.pie(en_düşük_10_kira["Kira Endeksi"], labels=en_düşük_10_kira["Ülke"], autopct='%1.1f%%', startangle=90, colors=sns.color_palette("coolwarm"), explode=explode)
    plt.xlabel("Ülkeler")
    plt.xticks(rotation=30, ha="right")  
    plt.title("En Düşük Kiralama Endeksine Sahip 14 Ülke")
    plt.show()


def soru9(data_frame):
    kira_endeksi_sıralı = data_frame.sort_values("Kira Endeksi", ascending=True)
    en_yüksek_10_kira = kira_endeksi_sıralı.tail(10)
    plt.figure(figsize=(12, 6))
    sns.scatterplot(x="Ülke", y="Kira Endeksi", data=en_yüksek_10_kira, color="skyblue")
    plt.title("En Yüksek Kiralama Endeksine Sahip Olan 10 Ülke")
    plt.xlabel("Ülkeler")
    plt.ylabel("Kira Endeksi")
    plt.xticks(rotation=30, ha="right") 
    plt.show()


def soru10(data_frame):
    yerel_alma_gücü_sıralı = data_frame.sort_values("Yerel Satın Alma Gücü Endeksi", ascending=False)
    en_yüksek_10_alma_gücü = yerel_alma_gücü_sıralı.head(10)
    plt.figure(figsize=(12, 6))
    sns.barplot(x="Ülke", y="Yerel Satın Alma Gücü Endeksi", data=en_yüksek_10_alma_gücü, palette="YlGnBu")
    plt.title("Yüksek Yerel Satın Alma Gücüne Sahip Olan 10 Ülke")
    plt.xlabel("Ülkeler")
    plt.ylabel("Yerel Satın Alma Gücü Endeksi")
    plt.xlabel("Ülkeler")
    plt.show()

def soru11(data_frame):
    yerel_alma_gücü_sıralı = data_frame.sort_values("Yerel Satın Alma Gücü Endeksi", ascending=False)
    en_düşük_5_alma_gücü = yerel_alma_gücü_sıralı.tail(14)
    plt.figure(figsize=(12, 6))
    sns.barplot(x="Ülke", y="Yerel Satın Alma Gücü Endeksi", data=en_düşük_5_alma_gücü, palette="Oranges")
    plt.title("Düşük Yerel Satın Alma Gücüne Sahip Olan 14 Ülke")
    plt.xlabel("Ülkeler")
    plt.ylabel("Yerel Satın Alma Gücü Endeksi")
    plt.xticks(rotation=30, ha="right") 
    plt.show()

#Sığmadığından dolayı sadece ilk csv dosyasındaki ilk 40 veriyi baz alarak yapıldı
def soru12(data_frame):
    plt.figure(figsize=(15, 8))
    pivot_table = data_frame.pivot_table(index="Ülke", values="Yaşam Maliyeti + Kira Endeksi")
    sns.heatmap(pivot_table.head(40), cmap="YlGnBu", annot=True, fmt=".2f", linewidths=.5)
    plt.title("Ülkelerin Genel Maliyet İndeksine Göre Renkli Haritası")
    plt.xlabel("Ülkeler")
    plt.show()

def soru13(data_frame):
    kira_endeksi_filtrelenmiş_güncel = data_frame[(data_frame["Kira Endeksi"] >= 6) & (data_frame["Kira Endeksi"] <= 8)]
    plt.figure(figsize=(12, 6))
    sns.lineplot(x="Ülke", y="Kira Endeksi", data=kira_endeksi_filtrelenmiş_güncel, marker="o")
    plt.title("Kira Endeksi 6-8 Arasındaki Ülkeler")
    plt.xlabel("Ülkeler")
    plt.xticks(rotation=45)
    plt.ylabel("Kira Endeksi")
    plt.show()


soru1(veri)

"""
soru1(veri)
soru2(veri)
soru3(veri)
soru4(veri)
soru5(veri)
soru6(veri)
soru7(veri)
soru8(veri)
soru9(veri)
soru10(veri)
soru11(veri)
soru12(veri)
soru13(veri)
"""