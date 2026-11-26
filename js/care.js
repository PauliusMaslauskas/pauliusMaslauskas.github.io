// Care & safety text from the printed care cards, shared by every product page.
// A page opts in with  <section class="care" data-power="12v"></section>  (or "220v").
// Edit the wording here once and every product page follows.
(function () {
    var EMAIL = '<a href="mailto:labas@glostoakis.lt">labas@glostoakis.lt</a>';

    var CARE = [
        'Dulkes valykite sausa arba vos drėgna šluoste. Valiklių nenaudokite.',
        'Betonas yra porėtas, todėl nemėgsta vandens, riebalų ir dažančių skysčių.',
        'Šviestuvas sunkus, todėl pernešdami laikykite už pagrindo, ne už laido.',
        'Statykite ant lygaus, tvirto paviršiaus.',
        'Skirtas naudoti tik sausose vidaus patalpose.',
        'Smulkios poros ir atspalvių skirtumai yra natūrali betono dalis.',
        'Kiekvienas gaminys turi savo tekstūrą – tai ne defektas.'
    ];

    var SAFETY = {
        '12v': [
            '<b>Maitinimas:</b> 12 V DC per pridedamą adapterį (jungiamas į 220–240 V ~ 50 Hz lizdą).',
            'Naudokite tik pridedamą adapterį. Keisdami rinkitės tokį patį: 12 V DC, ne mažiau kaip 1,0 A.',
            // "iki 12 W" = adapter maximum (12 V × 1,0 A); replace with the exact LED wattage if known.
            '<b>Šviesos šaltinis:</b> 12 V LED, iki 12 W. Nejunkite šviestuvo tiesiai į elektros tinklą.',
            'Ilgai nenaudodami ištraukite adapterį iš lizdo.',
            '<b>Kilus klausimams rašykite:</b> ' + EMAIL
        ],
        '220v': [
            '<b>Maitinimas:</b> 220–240 V ~ 50 Hz. Nenaudokite šviestuvo, jei pažeistas laidas ar kištukas.',
            'Prieš keisdami lemputę ištraukite kištuką iš lizdo ir palaukite, kol lemputė atvės.',
            '<b>Kilus klausimams rašykite:</b> ' + EMAIL
        ]
    };

    function paragraphs(lines) {
        return lines.map(function (l) { return '<p>' + l + '</p>'; }).join('');
    }

    document.querySelectorAll('.care[data-power]').forEach(function (el) {
        var safety = SAFETY[el.dataset.power];
        if (!safety) {
            console.warn('care.js: unknown data-power "' + el.dataset.power + '", use "12v" or "220v"');
            return;
        }
        el.innerHTML =
            '<h2>Priežiūra ir sauga</h2>' +
            '<div class="care-cols">' +
                '<div><h4>Kad šviestuvas gyvuotų ilgai:</h4>' + paragraphs(CARE) + '</div>' +
                '<div><h4>Kad šviestų saugiai:</h4>' + paragraphs(safety) + '</div>' +
            '</div>';
    });
})();
