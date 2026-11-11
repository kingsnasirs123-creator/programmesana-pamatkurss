# Programmēšana - pamatkurss
Autors: **Bruno Bluzmanis**
## Kā palaist
-Atver github desktop
-Tālāk izvēlēties visual studio code
## Licence
Tā ir pasaulē populārākā vizuālā programmēšanas valoda bērniem.
**vienu vārdu treknrakstā ar diviem zvaigznīšu pāriem**
# .md fails nav parasts teksta fails, jo tas satur strukturētu iezīmēšanas valodu (Markdown), kas ļauj tekstam pievienot formatējumu un vizuālos elementus (piemēram, virsrakstus, sarakstus, saites un attēlus), kurus lietotnes var automātiski pārveidot tīrā, vizuāli noformētā dokumentā vai HTML kodā.


<class 'str'> ir a
<class 'int'> ir b
<class 'float'> ir c

Aprēķini ar 17 un 5:

- 17 / 5 = 3.4 — parastā dalīšana.
- 17 // 5 = 3 — pilno dalījumu skaits.
- 17 % 5 = 2 — atlikums.
- 2 ** 3 = 8 — kāpināšana pakāpē.

Tātad 17 dalīts ar 5 ir 3 pilnas reizes, un pāri paliek 2.
Inventāra kalkulators ar 17 mantām un 5 vietām somā izvada 3 pilnas somas un 2 mantas pāri.

Kalkulatora izvade ar f-string ir: Vajag 3 somas un 2 mantas paliks pāri. Vidējais aritmētiskais ir 3.4 somas. Formāts :.1f attēlo skaitli ar vienu ciparu aiz komata. Šajā piemērā arī neformatētais rezultāts ir 3.4; citām vērtībām formatēšana var noapaļot redzamo rezultātu.

## Koda lasāmības pārbaude

Šī programma simulē vienkāršu spēles mehāniku, kurā tiek aprēķināts tēla veselības stāvoklis pēc saņemta trieciena.
Klasesbiedram viss bija skaidrs.
Labs mainīgā vārds pats par sevi kalpo kā dokumentācija, padarot kodu pašizskaidrojošu.

## Spēles pseidokods

### Ievade

1 Pajautā spēlētāja vārdu.
2 Pajautā spēlētāja sākotnējo veselības punktu skaitu.
3 Pajautā uzbrukuma spēku.

### Apstrāde

4 Aprēķini spēlētāja atlikušos veselības punktus, no sākotnējiem punktiem atņemot uzbrukuma spēku.

### Izvade

5 Parādi spēlētāja vārdu.
6 Parādi spēlētāja atlikušos veselības punktus.

## Spēles mainīgie un formula

| Mainīgā vārds       |Datu tipi| Ko glabā                                  |
| speletaja_vards     | str     | Spēlētāja vārdu                           |
| hp_punkti           | int     | Spēlētāja sākotnējos veselības punktus    |
| uzbrukuma_jauda     | float   | Uzbrukuma spēku                           |
| atlikusie_hp_punkti | float   | Spēlētāja veselības punktus pēc veiktā uzbrukuma |

Formula: atlikusie_hp_punkti = hp_punkti - uzbrukuma_jauda
speletaja_vards, hp_punkti un uzbrukuma_jauda vērtības tiek iegūtas no input(). atlikusie_hp_punkti tiek izrēķināts ar formulu.
Formulā izmantotie mainīgie ir norādīti tabulā.

## Formulas pārbaude
| Pārbaude            | hp_punkti   | uzbrukuma_jauda   | Aprēķins  | atlikusie_hp_punkti  |
| Maza vērtību kopa   | 100         | 5                 | 100 - 25  | 75                   |
| Vidēja vērtību kopa | 100         | 50                | 100 - 50  | 50                   |
| Liela vērtību kopa  | 100         | 75                | 100 - 75  | 25                   |

Secinājums: Formulas testēšana pirms koda izstrādes palīdz laikus novērst loģikas kļūdas un garantē precīzu rezultātu.