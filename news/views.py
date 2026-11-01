from django.shortcuts import render


news = [
    {
        "id": 1,
        "title": '"Azərbaycanlılar "Old Trafford"da "Sabah"ı tək qoymayacaq"',
        "content": "Azərbaycanlılar Old Trafford-da Sabahı tək qoymayacaq. "
                   "Bunu klubun mətbuat xidmətinin rəhbəri Elnur Həmidov "
                   "Offsideplus.az saytına açıqlamasında söyləyib. "
                   "Hələ dəqiq say bəlli deyil. Lakin təxminən 300 nəfər "
                   "həmvətənimizin komandamızı stadiondan dəstəkləməsi gözlənilir. "
                   "Oyun gününə kimi bu say dəyişə bilər, deyə klub rəsmisi açıqlayıb. "
                   "Qeyd edək ki, Mançester Yunayted - Sabah oyunu 10 sentyabr "
                   "Bakı vaxtı ilə saat 23:00-da baş tutacaq."
    },

    {
        "id": 2,
        "title": "Bo Nikal UFC-də Şara Bulletlə döyüş istədiyini açıqlayıb",
        "content": """Amerikalı UFC döyüşçüsü Bo Nikal təşkilatdan Şarabutdin Maqomedovla qarşılaşma təşkil etməsini xahiş etdiyini bildirib. O, bu döyüşün özü üçün maraqlı olacağını düşündüyünü qeyd edib.

Offsideplus.az xəbər verir ki, Nikalın sözlərinə görə, UFC bu təklifi qəbul etməyib. Hazırda Bo Nikalın hesabında doqquz qələbə və bir məğlubiyyət var. Son iki döyüşünü nokautla başa vuran idmançı Xamzat Çimayevlə də döyüşməyə hazır olduğunu vurğulayıb.""",
        "image": "news2.jpg"
    },

    {
        "id": 3,
        "title": 'Alek Piters "Olimpiya Milan"a keçidini izah edib',
        "content": """Amerikalı forvard Alek Piters karyerasını "Olimpiya Milan"da davam etdirmək qərarının səbəblərini açıqlayıb. 31 yaşlı basketbolçu bu addımın uzun müddət ərzində yetişdiyini bildirib.

    Offsideplus.az xəbər verir ki, Piters yaxın dostları, o cümlədən Kayl Hayns və Brayant Danstonla klubun inkişaf istiqamətini mütəmadi müzakirə etdiyini qeyd edib. Hər iki sabiq "Olimpiya Milan" oyunçusu klub barədə müsbət fikirlər səsləndirib və Pitersin qərar verməsində mühüm rol oynayıb.

    O, transferinin yalnız iddialı layihəyə qoşulmaq istəyi ilə deyil, həm də "Olimpiya Milan"ı Avropa basketbolunun zirvəsinə qaytarmaq məqsədi ilə bağlı olduğunu vurğulayıb.

    "Burada özümü uğurlu görürəm. Düşünürəm ki, hamımızda eyni hiss var idi: birlikdə uğur qazana bilərik", – deyə Piters bildirib."""
    },

    {
        "id": 4,
        "title": "Adel Taarabt 37 yaşında yaşıl meydanlarla vidalaşdı",
        "content": """Təcrübəli yarımmüdafiəçi Adel Taarabt 37 yaşında peşəkar futbol karyerasını bitirdiyini açıqlayıb.

    Offsideplus.az xəbər verir ki, qoca kontinentin müxtəlif klublarında və milli komandada iz qoyan mərakeşli oyunçu zəngin xatirələrlə bu yoldan ayrılır.

    - Statistika göstəriciləri: Mərakeşli futbolçu karyerası ərzində klub və milli komanda səviyyəsində 500-dən artıq matçda meydana çıxıb və ümumilikdə 169 qol töhfəsi ilə yadda qalıb.

    - Klub titulları: "Tottenhem Hotspur" ilə 2008–09 mövsümündə Liqa Kubokunun finalçısı olan oyunçu "Kuinz Park Reyncers" ilə 2010–11 mövsümündə Çempionşip çempionluğu qazanıb.

    - "Benfika"da çıxış edərkən 2018–19 Primeyra Liqa və 2019 Superkubok çempionu olub, həmçinin Portuqaliya Kubokunun finalçısı adını qazanıb.

    - Fərdi mükafatlar: 2010–11 mövsümündə Çempionşipdə mövsümün oyunçusu seçilib və liqanın simvolik 11-liyinə daxil olub.

    - Vida açıqlaması: Taarabt yaşadığı gözəl anların, çətinliklərin, səhvlərin və möhtəşəm gecələrin onun səyahətinin bir parçası olduğunu bildirib."""
    },

    {
        "id": 5,
        "title": '"Real Madrid" Ruben Neves transferini yenidən gündəmə gətirə bilər',
        "content": """ "Real Madrid" Joze Mourinyonun yanvar ayında yarımmüdafiə xəttinə gücləndirilmə istəməsi halında Ruben Nevesə olan marağını yenidən alovlandıra bilər.

    Offsideplus.az xəbər verir ki, "Əl-Hilal"ın yarımmüdafiəçisi ötən ilin yanvar ayında "Madrid" klubuna təklif olunmuşdu, lakin İspaniya nəhəngi transferi davam etdirməmək qərarına gəlmişdi.

    Neves həmin vaxtdan bəri "Əl-Hilal" ilə 2029-cu ilin yayına qədər uzadılan yeni müqavilə imzalayıb. Bu isə "Real"ın futbolçunu heyətinə qatmaq üçün Səudiyyə Ərəbistanı klubu ilə rəsmi danışıqlar aparmasını zəruri edir."""
    },

    {
        "id": 6,
        "title": '"Çelsi" ötən il "Barselona"nın ulduzunu 50 milyona ala bilərmiş',
        "content": """İngiltərənin "Çelsi" klubu 2025-ci ilin yayında "Barselona"nın ulduzunu ala bilərmiş.

    Offsideplus.az xəbər verir ki, londonlular yarımmüdafiəçi Fermin Lopesi transfer etmək şansına sahib olsa da, məbləğin 50 milyon avrodan yuxarı qaldırılmasına razı olmayaraq bu keçiddən imtina etmişdi.

    Kataloniya təmsilçisində qalan gənc futbolçu qısa müddətdə komandanın əsas oyunçularından birinə çevrilməyi bacarıb.

    - Parlaq start: İspaniyalı yarımmüdafiəçi cari mövsümdə La Liqanın ilk dörd matçında 4 qol və 2 məhsuldar ötürmə ilə yadda qalıb.

    - Lempard bənzərliyi: Lopesin cərimə meydançasına vaxtında və təhlükəli şəkildə daxil olmaq bacarığı onu "Çelsi"nin əfsanəvi oyunçusu Frank Lempard ilə müqayisə etməyə əsas verib."""
    }
    ,

    {
        "id": 7,
        "title": "Jezus Çempionlar Liqasını qazanmaq arzusundan danışıb",
        "content": """Braziliyalı hücumçu Qabriel Jezus "Barselona"ya keçidindən sonra Çempionlar Liqasını qazanmaq istəyindən bəhs edib.

    Offsideplus.az xəbər verir ki, 29 yaşlı futbolçu yay transfer pəncərəsində "Arsenal"dan "Barselona"ya keçib. O, turnirin finalında iki dəfə uduzub: ötən mövsüm "Arsenal"la, 2021-ci ildə isə "Mançester Siti" ilə.

    "Barselona"ya keçmək imkanını öyrəndiyim gündən Çempionlar Liqasını qazanmaq fikri məni tərk etmir. Bu, mənim arzumdur", – deyə Jezus bildirib."""
    },

    {
        "id": 8,
        "title": "İan Gerri: Prates Maxaçevi nokaut edə bilər",
        "content": """UFC döyüşçüsü İan Gerri mümkün qarşılaşmada Karlus Pratesi yarımorta çəki çempionu İslam Maxaçevə qarşı favorit hesab etdiyini bildirib. O, bu döyüşün hər iki idmançı üçün təhlükəli olacağını qeyd edib.

    Offsideplus.az xəbər verir ki, Gerri açıqlamasında bunları deyib:

    "Bu, hər iki tərəf üçün riskli qarşılaşmadır. Karlus məndən xeyli aqressivdir, amma qrapplinqdə o qədər də güclü deyil. Maraqlı döyüş olacaq. Prates zərbəsini çatdırıb Maxaçevi nokaut edə biləcəkmi, yoxsa İslam onu yerə salıb bitirəcək? Çətindir, amma ürəyim deyir ki, Karlus bunu bacaracaq. O zaman biz yenidən qarşılaşarıq".

    Karlus Pratesin aktivində 24 qələbə və 7 məğlubiyyət var. Son 13 qələbəsini nokautla qazanıb. İslam Maxaçev isə 29 qələbə və 1 məğlubiyyətə sahibdir, ardıcıl 17 döyüşdə qalib gəlib."""
    }
    ,

    {
        "id": 9,
        "title": "U16 millimiz Yalovada beynəlxalq turnirdə",
        "content": """16 yaşadək oğlanlardan ibarət Azərbaycan milli basketbol komandası Türkiyənin Yalova şəhərində keçirilən “EVOQ Challenge Cup Pre Season Yalova” beynəlxalq turnirində iştirak edir.

    Offsideplus.az Azərbaycan Basketbol Federasiyasının mətbuat xidmətinə istinadən xəbər verir ki, Yalovada millilərimizin çıxışı davam edir. Bu gün U14 komandamız turniri ikinci pillədə başa vurub, indi isə mübarizəni U16 millimiz davam etdirir.

    8–12 sentyabr tarixlərində keçirilən U16 turnirində millimizlə yanaşı:

    • Konya Diltaş Basketbol
    • Eskişehir Çağdaş Koleji Spor Kulübü
    • Rilski Sportist
    • Viktor Sanikidze Academy Basketball
    • Bakırköy Kartaltepe Spor Kulübü
    • Fenerbahçe
    • Eskişehir Gelişim Falcons

    komandaları da iştirak edir.

    Turnir komandamıza fərqli basketbol məktəblərinin təmsilçiləri ilə qarşılaşmaq, rəqabətli oyunlar keçirmək və beynəlxalq təcrübəsini artırmaq imkanı verəcək."""
    }
    ,

{
    "id": 10,
    "title": 'Enso Fernandesin "Real"a transferi niyə baş tutmadı?',
    "content": """Yay transfer pəncərəsində "Çelsi"dən "Mançester Siti"yə qoşulan Enso Fernandesin karyerası ilə bağlı maraqlı detallar üzə çıxıb.

Offsideplus.az xəbər verir ki, məlum olub ki, argentinalı yarımmüdafiəçi İngiltərə daxilində və ya başqa klublara yollanmazdan əvvəl İspaniya nəhənginə üz tutmağı arzulayırmış.

- "Real Madrid" gözləntisi: Enso Fernandes "Çelsi"dən ayrılmamışdan əvvəl əsas üstünlük kimi "Real Madrid"i seçmişdi və İspaniya nəhəngindən gələcək hər hansı bir addımı və ya təklifi səbirsizliklə gözləyirdi. Lakin Madrid təmsilçisi transfer üçün hər hansı bir addım atmadı.

- Mançesterə keçid: "Real"dan cavab gəlmədikdən sonra, Enso Mareskanın şəxsi təkidi və onu komandanın mərkəzi oyunçusu etmək istəməsi nəticəsində futbolçu karyerasını "Mançester Siti"də davam etdirməyə qərar verib."""
}
]


def home(request):
    return render(request, "home.html", {"news": news})


def details(request, id):
    abc = None

    for item in news:
        if item["id"] == id:
            abc = item
            break

    return render(request, "details.html", {"news": abc})