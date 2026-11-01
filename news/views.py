
from django.shortcuts import render
from django.http import Http404


news = [
    {
        "id": 1,
        "title": '"Azərbaycanlılar "Old Trafford"da "Sabah"ı tək qoymayacaq"',
        "content": """Azərbaycanlılar Old Trafford-da Sabahı tək qoymayacaq. Bunu klubun mətbuat xidmətinin rəhbəri Elnur Həmidov Offsideplus.az saytına açıqlamasında söyləyib.

Hələ dəqiq say bəlli deyil. Lakin təxminən 300 nəfər həmvətənimizin komandamızı stadiondan dəstəkləməsi gözlənilir.

Qeyd edək ki, Mançester Yunayted - Sabah oyunu 10 sentyabr Bakı vaxtı ilə saat 23:00-da baş tutacaq."""
    },
    {
        "id": 2,
        "title": "Bo Nikal UFC-də Şara Bulletlə döyüş istədiyini açıqlayıb",
        "content": """Amerikalı UFC döyüşçüsü Bo Nikal təşkilatdan Şarabutdin Maqomedovla qarşılaşma təşkil etməsini xahiş etdiyini bildirib.

Offsideplus.az xəbər verir ki, Nikalın sözlərinə görə, UFC bu təklifi qəbul etməyib. Hazırda Bo Nikalın hesabında doqquz qələbə və bir məğlubiyyət var."""
    },
    {
        "id": 3,
        "title": 'Alek Piters "Olimpiya Milan"a keçidini izah edib',
        "content": """Amerikalı forvard Alek Piters karyerasını Olimpiya Milanda davam etdirmək qərarının səbəblərini açıqlayıb.

31 yaşlı basketbolçu yaxın dostları Kayl Hayns və Brayant Danstonla klubun inkişaf istiqamətini müzakirə etdiyini bildirib.

O, transferinin məqsədinin Olimpiya Milana Avropa basketbolunun zirvəsinə qayıtmaqda kömək etmək olduğunu vurğulayıb."""
    },
    {
        "id": 4,
        "title": "Adel Taarabt 37 yaşında yaşıl meydanlarla vidalaşdı",
        "content": """Təcrübəli yarımmüdafiəçi Adel Taarabt peşəkar futbol karyerasını bitirdiyini açıqlayıb.

Mərakeşli futbolçu karyerası ərzində müxtəlif klublarda çıxış edib.

O, Benfica ilə 2018-19 Primeyra Liqa və 2019 Superkubok çempionu olub."""
    },
    {
        "id": 5,
        "title": '"Real Madrid" Ruben Neves transferini yenidən gündəmə gətirə bilər',
        "content": """"Real Madrid" yarımmüdafiəçi Ruben Nevesə olan marağını yenidən artıra bilər.

Offsideplus.az xəbər verir ki, futbolçu ötən ilin yanvar ayında Madrid klubuna təklif olunmuşdu.

Neves hazırda Əl-Hilal klubunda çıxış edir və 2029-cu ilə qədər müqaviləyə sahibdir."""
    },
    {
        "id": 6,
        "title": '"Çelsi" ötən il "Barselona"nın ulduzunu 50 milyona ala bilərmiş',
        "content": """İngiltərənin Çelsi klubu 2025-ci ilin yayında Barselonanın futbolçusu Fermin Lopeslə maraqlanıb.

Londonlular futbolçunu transfer etmək imkanına sahib olsalar da, 50 milyon avrodan artıq ödəməyə razı olmayıblar.

Fermin Lopes Barselonada əsas oyunçulardan birinə çevrilib."""
    },
    {
        "id": 7,
        "title": "Jezus Çempionlar Liqasını qazanmaq arzusundan danışıb",
        "content": """Braziliyalı hücumçu Qabriel Jezus Çempionlar Liqasını qazanmaq istəyindən bəhs edib.

O, bu turnirin finalında iki dəfə məğlub olduğunu bildirib.

Jezus üçün Çempionlar Liqasını qazanmaq əsas karyera arzularından biridir."""
    },
    {
        "id": 8,
        "title": "İan Gerri: Prates Maxaçevi nokaut edə bilər",
        "content": """UFC döyüşçüsü İan Gerri mümkün qarşılaşmada Karlus Pratesi İslam Maxaçevə qarşı favorit hesab etdiyini bildirib.

Gerri bu döyüşün hər iki idmançı üçün təhlükəli olacağını qeyd edib.

Karlus Pratesin aktivində 24 qələbə və 7 məğlubiyyət var."""
    },
    {
        "id": 9,
        "title": "U16 millimiz Yalovada beynəlxalq turnirdə",
        "content": """16 yaşadək oğlanlardan ibarət Azərbaycan milli basketbol komandası Türkiyənin Yalova şəhərində keçirilən EVOQ Challenge Cup turnirində iştirak edir.

Turnirdə müxtəlif ölkələrin basketbol komandaları mübarizə aparır.

Bu yarış millimizə beynəlxalq təcrübə qazanmaq imkanı yaradır."""
    },
    {
        "id": 10,
        "title": 'Enso Fernandesin "Real"a transferi niyə baş tutmadı?',
        "content": """Enso Fernandesin Real Madridə transferi ilə bağlı maraqlı detallar üzə çıxıb.

Argentinalı yarımmüdafiəçi Çelsidən ayrılmamışdan əvvəl Real Madridə keçmək istəyib.

Lakin Madrid klubu transfer üçün addım atmayıb və futbolçu karyerasını başqa klubda davam etdirmək qərarına gəlib."""
    }
]


def home(request):
    return render(request, "home.html", {"news": news})


def details(request, id):
    selected_news = next(
        (item for item in news if item["id"] == id),
        None
    )

    if selected_news is None:
        raise Http404("News not found")

    return render(
        request,
        "details.html",
        {"news": selected_news}
    )
