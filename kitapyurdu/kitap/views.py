from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

# https://www.kitapyurdu.com (verileri aldığım site)

def kitap_list(request):
    return render(request, "index.html")

def kitap1(request):
    url = "https://www.kitapyurdu.com/kitap/seker-portakali-ciltsiz/10139.html"
    get = requests.get(url)
    content = get.content
    soup = BeautifulSoup(content, "html.parser")
    kitap_adi = soup.find_all("div", {"class":"pr_header"})
    kitap_yazari = soup.find_all("div", {"class":"pr_producers__manufacturer"})
    yayin_evi = soup.find_all("div", {"class":"pr_producers__item"})
    kitap_resmi = soup.find("a", {"class":"js-jbox-book-cover"})["href"]
    sayfa_sayisi = soup.find("td", text="Sayfa Sayısı:")
    fiyat = soup.find_all("div", {"class":"price__item"})

    for kitap_adi in kitap_adi:
        kitap_adi = kitap_adi.text

    for kitap_yazari in kitap_yazari:
        kitap_yazari = kitap_yazari.text

    for yayin_evi in yayin_evi:
        yayin_evi = yayin_evi.text

    for sayfa_sayisi in sayfa_sayisi:
        sayfa_sayisi = sayfa_sayisi.find_next("td").text.strip()

    for fiyat in fiyat:
        fiyat = fiyat.text

    return render(request, "kitap1.html", 
                  {"kitap_adi":kitap_adi,
                   "kitap_yazari":kitap_yazari,
                   "yayin_evi":yayin_evi,
                   "kitap_resmi":kitap_resmi,
                   "sayfa_sayisi":sayfa_sayisi,
                   "fiyat":fiyat,
                   })

def kitap2(request):
    url = "https://www.kitapyurdu.com/kitap/kucuk-prens/569234.html&filter_name=kucuk+prens"
    get = requests.get(url)
    content = get.content
    soup = BeautifulSoup(content, "html.parser")
    kitap_adi = soup.find_all("div", {"class":"pr_header"})
    kitap_yazari = soup.find_all("div", {"class":"pr_producers__manufacturer"})
    yayin_evi = soup.find_all("div", {"class":"pr_producers__item"})
    kitap_resmi = soup.find("a", {"class":"js-jbox-book-cover"})["href"]
    sayfa_sayisi = soup.find("td", text="Sayfa Sayısı:")
    fiyat = soup.find_all("div", {"class":"price__item"})
    for kitap_adi in kitap_adi:
        kitap_adi = kitap_adi.text

    for kitap_yazari in kitap_yazari:
        kitap_yazari = kitap_yazari.text

    for yayin_evi in yayin_evi:
        yayin_evi = yayin_evi.text

    for sayfa_sayisi in sayfa_sayisi:
        sayfa_sayisi = sayfa_sayisi.find_next("td").text.strip()

    for fiyat in fiyat:
        fiyat = fiyat.text

    return render(request, "kitap2.html", 
                  {"kitap_adi":kitap_adi,
                   "kitap_yazari":kitap_yazari,
                   "yayin_evi":yayin_evi,
                   "kitap_resmi":kitap_resmi,
                   "sayfa_sayisi":sayfa_sayisi,
                   "fiyat":fiyat,
                   })

def kitap3(request):
    url = "https://www.kitapyurdu.com/kitap/harry-potter-ve-felsefe-tasi/32780.html&filter_name=harry+potter"
    get = requests.get(url)
    content = get.content
    soup = BeautifulSoup(content, "html.parser")
    kitap_adi = soup.find_all("div", {"class":"pr_header"})
    kitap_yazari = soup.find_all("div", {"class":"pr_producers__manufacturer"})
    yayin_evi = soup.find_all("div", {"class":"pr_producers__item"})
    kitap_resmi = soup.find("a", {"class":"js-jbox-book-cover"})["href"]
    sayfa_sayisi = soup.find("td", text="Sayfa Sayısı:")
    fiyat = soup.find_all("div", {"class":"price__item"})
    for kitap_adi in kitap_adi:
        kitap_adi = kitap_adi.text

    for kitap_yazari in kitap_yazari:
        kitap_yazari = kitap_yazari.text

    for yayin_evi in yayin_evi:
        yayin_evi = yayin_evi.text

    for sayfa_sayisi in sayfa_sayisi:
        sayfa_sayisi = sayfa_sayisi.find_next("td").text.strip()

    for fiyat in fiyat:
        fiyat = fiyat.text


    return render(request, "kitap3.html", 
                  {"kitap_adi":kitap_adi,
                   "kitap_yazari":kitap_yazari,
                   "yayin_evi":yayin_evi,
                   "kitap_resmi":kitap_resmi,
                   "sayfa_sayisi":sayfa_sayisi,
                   "fiyat":fiyat,
                   })

