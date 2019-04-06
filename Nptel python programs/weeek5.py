'''
The library at the Hogwarts School of Witchcraft and Wizardry has computerized its book issuing process. The relevant information is provided as text from standard input in three parts: information about books, information about borrowers and information about checkouts. Each part has a specific line format, described below.

Information about books
Line format: Accession Number~Title

Information about borrowers
Line format: Username~Full Name

Information about checkouts
Line format: Username~Accession Number~Due Date
Note: Due Date is in YYYY-MM-DD format.

You may assume that the data is internally consistent. For every checkout, there is a corresponding username and accession number in the input data, and no book is simultaneously checked out by two people.

Each section of the input starts with a line containing a single keyword. The first section begins with a line containing Books. The second section begins with a line containing Borrowers. The third section begins with a line containing Checkouts. The end of the input is marked by a line containing EndOfInput.

Write a Python program to read the data as described above and print out details about books that have been checked out. Each line should describe to one currently issued book in the following format:

Due Date~Full Name~Accession Number~Title
Your output should be sorted in increasing order of due date. For books due on the same date, sort in increasing order of full name. If the due date and full name are both the same, sort based on the accession number, and, finally, the title of the book.

Here is a sample input and its corresponding output.

Sample Input

Books
APM-001~Advanced Potion-Making
GWG-001~Gadding With Ghouls
APM-002~Advanced Potion-Making
DMT-001~Defensive Magical Theory
DMT-003~Defensive Magical Theory
GWG-002~Gadding With Ghouls
DMT-002~Defensive Magical Theory
Borrowers
SLY2301~Hannah Abbott
SLY2302~Euan Abercrombie
SLY2303~Stewart Ackerley
SLY2304~Bertram Aubrey
SLY2305~Avery
SLY2306~Malcolm Baddock
SLY2307~Marcus Belby
SLY2308~Katie Bell
SLY2309~Sirius Orion Black
Checkouts
SLY2304~DMT-002~2019-03-27
SLY2301~GWG-001~2019-03-27
SLY2308~APM-002~2019-03-14
SLY2303~DMT-001~2019-04-03
SLY2301~GWG-002~2019-04-03
EndOfInput
Sample Output

2019-03-14~Katie Bell~APM-002~Advanced Potion-Making
2019-03-27~Bertram Aubrey~DMT-002~Defensive Magical Theory
2019-03-27~Hannah Abbott~GWG-001~Gadding With Ghouls
2019-04-03~Hannah Abbott~GWG-002~Gadding With Ghouls
2019-04-03~Stewart Ackerley~DMT-001~Defensive Magical Theory
Sample Test Cases
Input	Output
Test Case 1	
Books
APM-001~Advanced Potion-Making
GWG-001~Gadding With Ghouls
APM-002~Advanced Potion-Making
DMT-001~Defensive Magical Theory
DMT-003~Defensive Magical Theory
GWG-002~Gadding With Ghouls
DMT-002~Defensive Magical Theory
Borrowers
SLY2301~Hannah Abbott
SLY2302~Euan Abercrombie
SLY2303~Stewart Ackerley
SLY2304~Bertram Aubrey
SLY2305~Avery
SLY2306~Malcolm Baddock
SLY2307~Marcus Belby
SLY2308~Katie Bell
SLY2309~Sirius Orion Black
Checkouts
SLY2304~DMT-002~2019-03-27
SLY2301~GWG-001~2019-03-27
SLY2308~APM-002~2019-03-14
SLY2303~DMT-001~2019-04-03
SLY2301~GWG-002~2019-04-03
EndOfInput
2019-03-14~Katie Bell~APM-002~Advanced Potion-Making
2019-03-27~Bertram Aubrey~DMT-002~Defensive Magical Theory
2019-03-27~Hannah Abbott~GWG-001~Gadding With Ghouls
2019-04-03~Hannah Abbott~GWG-002~Gadding With Ghouls
2019-04-03~Stewart Ackerley~DMT-001~Defensive Magical Theory
Test Case 2	
Books
GTF-001~A Beginner's Guide to Transfiguration
GTF-002~A Beginner's Guide to Transfiguration
GTF-003~A Beginner's Guide to Transfiguration
WET-001~Great Wizarding Events of the Twentieth Century
WET-002~Great Wizarding Events of the Twentieth Century
WTC-001~Great Wizards of the Twentieth Century
WTC-002~Great Wizards of the Twentieth Century
WTC-003~Great Wizards of the Twentieth Century
WTC-004~Great Wizards of the Twentieth Century
IBI-001~Invisible Book of Invisibility
IBI-002~Invisible Book of Invisibility
JFJ-001~Jinxes for the Jinxed
JFJ-002~Jinxes for the Jinxed
LDM-001~Men Who Love Dragons Too Much
LDM-002~Men Who Love Dragons Too Much
LDM-003~Men Who Love Dragons Too Much
NTN-001~New Theory of Numerology
MFM-001~One Minute Feasts - It's Magic!
PYN-001~Powers You Never Knew You Had and What To Do With Them Now You've Wised Up
PYN-002~Powers You Never Knew You Had and What To Do With Them Now You've Wised Up
PYN-003~Powers You Never Knew You Had and What To Do With Them Now You've Wised Up
PDM-001~Practical Defensive Magic and Its Use Against the Dark Arts
PDM-002~Practical Defensive Magic and Its Use Against the Dark Arts
PDM-003~Practical Defensive Magic and Its Use Against the Dark Arts
PDM-004~Practical Defensive Magic and Its Use Against the Dark Arts
QAQ-001~Quintessence: A Quest
QAQ-002~Quintessence: A Quest
STS-001~Saucy Tricks for Tricky Sorts
STS-002~Saucy Tricks for Tricky Sorts
STS-003~Saucy Tricks for Tricky Sorts
STS-004~Saucy Tricks for Tricky Sorts
Borrowers
SLY2301~Hannah Abbott
SLY2307~Marcus Belby
SLY2311~Susan Bones
SLY2313~Eleanor Branstone
SLY2319~Eddie Carmichael
GRF3703~Dennis Creevey
GRF3708~J. Dorny
GRF3715~Basil Fronsac
RAV4308~Olive Hornby
RAV4309~Angelina Johnson
RAV5902~Isobel MacDougal
RAV5905~Laura Madley
RAV5906~Draco Malfoy
RAV5907~Natalie McDonald
GRF9104~Lily Moon
GRF9107~Garrick Ollivander
Checkouts
RAV5906~GTF-001~2019-03-22
GRF3708~GTF-002~2019-03-26
SLY2307~GTF-003~2019-03-01
GRF3708~WET-001~2019-03-06
SLY2301~WET-002~2019-03-23
SLY2307~WTC-001~2019-02-26
SLY2311~WTC-002~2019-03-12
SLY2313~WTC-003~2019-03-06
SLY2301~WTC-004~2019-03-12
RAV5906~IBI-001~2019-03-12
SLY2307~IBI-002~2019-03-23
GRF3715~JFJ-001~2019-03-23
RAV5905~JFJ-002~2019-03-16
SLY2311~LDM-001~2019-02-26
RAV4308~LDM-002~2019-03-20
SLY2307~LDM-003~2019-03-22
GRF3703~NTN-001~2019-03-09
RAV4308~MFM-001~2019-03-07
SLY2311~PYN-001~2019-03-03
RAV5902~PYN-002~2019-03-02
GRF9104~PYN-003~2019-03-16
GRF3708~PDM-001~2019-03-13
RAV5907~PDM-002~2019-03-26
SLY2307~PDM-003~2019-02-26
SLY2313~PDM-004~2019-03-01
RAV4309~QAQ-001~2019-03-14
RAV5907~QAQ-002~2019-03-17
RAV5905~STS-001~2019-03-12
SLY2319~STS-002~2019-03-11
GRF3703~STS-003~2019-03-19
RAV5907~STS-004~2019-03-17
EndOfInput
2019-02-26~Marcus Belby~PDM-003~Practical Defensive Magic and Its Use Against the Dark Arts
2019-02-26~Marcus Belby~WTC-001~Great Wizards of the Twentieth Century
2019-02-26~Susan Bones~LDM-001~Men Who Love Dragons Too Much
2019-03-01~Eleanor Branstone~PDM-004~Practical Defensive Magic and Its Use Against the Dark Arts
2019-03-01~Marcus Belby~GTF-003~A Beginner's Guide to Transfiguration
2019-03-02~Isobel MacDougal~PYN-002~Powers You Never Knew You Had and What To Do With Them Now You've Wised Up
2019-03-03~Susan Bones~PYN-001~Powers You Never Knew You Had and What To Do With Them Now You've Wised Up
2019-03-06~Eleanor Branstone~WTC-003~Great Wizards of the Twentieth Century
2019-03-06~J. Dorny~WET-001~Great Wizarding Events of the Twentieth Century
2019-03-07~Olive Hornby~MFM-001~One Minute Feasts - It's Magic!
2019-03-09~Dennis Creevey~NTN-001~New Theory of Numerology
2019-03-11~Eddie Carmichael~STS-002~Saucy Tricks for Tricky Sorts
2019-03-12~Draco Malfoy~IBI-001~Invisible Book of Invisibility
2019-03-12~Hannah Abbott~WTC-004~Great Wizards of the Twentieth Century
2019-03-12~Laura Madley~STS-001~Saucy Tricks for Tricky Sorts
2019-03-12~Susan Bones~WTC-002~Great Wizards of the Twentieth Century
2019-03-13~J. Dorny~PDM-001~Practical Defensive Magic and Its Use Against the Dark Arts
2019-03-14~Angelina Johnson~QAQ-001~Quintessence: A Quest
2019-03-16~Laura Madley~JFJ-002~Jinxes for the Jinxed
2019-03-16~Lily Moon~PYN-003~Powers You Never Knew You Had and What To Do With Them Now You've Wised Up
2019-03-17~Natalie McDonald~QAQ-002~Quintessence: A Quest
2019-03-17~Natalie McDonald~STS-004~Saucy Tricks for Tricky Sorts
2019-03-19~Dennis Creevey~STS-003~Saucy Tricks for Tricky Sorts
2019-03-20~Olive Hornby~LDM-002~Men Who Love Dragons Too Much
2019-03-22~Draco Malfoy~GTF-001~A Beginner's Guide to Transfiguration
2019-03-22~Marcus Belby~LDM-003~Men Who Love Dragons Too Much
2019-03-23~Basil Fronsac~JFJ-001~Jinxes for the Jinxed
2019-03-23~Hannah Abbott~WET-002~Great Wizarding Events of the Twentieth Century
2019-03-23~Marcus Belby~IBI-002~Invisible Book of Invisibility
2019-03-26~J. Dorny~GTF-002~A Beginner's Guide to Transfiguration
2019-03-26~Natalie McDonald~PDM-002~Practical Defensive Magic and Its Use Against the Dark Arts
Test Case 3	
Books
AIC-001~Achievements in Charming
AIC-002~Achievements in Charming
AIC-003~Achievements in Charming
AIC-004~Achievements in Charming
AIC-005~Achievements in Charming
APM-001~Advanced Potion-Making
APM-002~Advanced Potion-Making
APM-003~Advanced Potion-Making
APM-004~Advanced Potion-Making
AMM-001~The Adventures of Martin Miggs, the Mad Muggle
AMM-002~The Adventures of Martin Miggs, the Mad Muggle
AMM-003~The Adventures of Martin Miggs, the Mad Muggle
AMM-004~The Adventures of Martin Miggs, the Mad Muggle
AMM-005~The Adventures of Martin Miggs, the Mad Muggle
AMM-006~The Adventures of Martin Miggs, the Mad Muggle
AMM-007~The Adventures of Martin Miggs, the Mad Muggle
AMM-008~The Adventures of Martin Miggs, the Mad Muggle
AMM-009~The Adventures of Martin Miggs, the Mad Muggle
AMM-010~The Adventures of Martin Miggs, the Mad Muggle
AMM-011~The Adventures of Martin Miggs, the Mad Muggle
AMM-012~The Adventures of Martin Miggs, the Mad Muggle
AMM-013~The Adventures of Martin Miggs, the Mad Muggle
ART-001~Ancient Runes Translation
ART-002~Ancient Runes Translation
ART-003~Ancient Runes Translation
ART-004~Ancient Runes Translation
ART-005~Ancient Runes Translation
ART-006~Ancient Runes Translation
ART-007~Ancient Runes Translation
MEE-001~An Appraisal of Magical Education in Europe
MEE-002~An Appraisal of Magical Education in Europe
MEE-003~An Appraisal of Magical Education in Europe
MEE-004~An Appraisal of Magical Education in Europe
AAV-001~Asiatic Anti-Venoms
AAV-002~Asiatic Anti-Venoms
AAV-003~Asiatic Anti-Venoms
AAV-004~Asiatic Anti-Venoms
AAV-005~Asiatic Anti-Venoms
AAV-006~Asiatic Anti-Venoms
AAV-007~Asiatic Anti-Venoms
AAV-008~Asiatic Anti-Venoms
AAV-009~Asiatic Anti-Venoms
AAV-010~Asiatic Anti-Venoms
AAV-011~Asiatic Anti-Venoms
AAV-012~Asiatic Anti-Venoms
AAV-013~Asiatic Anti-Venoms
HBV-001~Basic Hexes for the Busy and Vexed
HBV-002~Basic Hexes for the Busy and Vexed
HBV-003~Basic Hexes for the Busy and Vexed
HBV-004~Basic Hexes for the Busy and Vexed
HBV-005~Basic Hexes for the Busy and Vexed
HBV-006~Basic Hexes for the Busy and Vexed
HBV-007~Basic Hexes for the Busy and Vexed
HBV-008~Basic Hexes for the Busy and Vexed
HBV-009~Basic Hexes for the Busy and Vexed
HBV-010~Basic Hexes for the Busy and Vexed
HBV-011~Basic Hexes for the Busy and Vexed
HBV-012~Basic Hexes for the Busy and Vexed
HBV-013~Basic Hexes for the Busy and Vexed
GTF-001~A Beginner's Guide to Transfiguration
GTF-002~A Beginner's Guide to Transfiguration
GTF-003~A Beginner's Guide to Transfiguration
GTF-004~A Beginner's Guide to Transfiguration
GTF-005~A Beginner's Guide to Transfiguration
WFT-001~Broken Balls: When Fortunes Turn Foul
WFT-002~Broken Balls: When Fortunes Turn Foul
WFT-003~Broken Balls: When Fortunes Turn Foul
WFT-004~Broken Balls: When Fortunes Turn Foul
WFT-005~Broken Balls: When Fortunes Turn Foul
WFT-006~Broken Balls: When Fortunes Turn Foul
WFT-007~Broken Balls: When Fortunes Turn Foul
WFT-008~Broken Balls: When Fortunes Turn Foul
WFT-009~Broken Balls: When Fortunes Turn Foul
WFT-010~Broken Balls: When Fortunes Turn Foul
CYC-001~Charm Your Own Cheese
CYC-002~Charm Your Own Cheese
CYC-003~Charm Your Own Cheese
CYC-004~Charm Your Own Cheese
MAA-001~Common Magical Ailments and Afflictions
MAA-002~Common Magical Ailments and Afflictions
MAA-003~Common Magical Ailments and Afflictions
MAA-004~Common Magical Ailments and Afflictions
MAA-005~Common Magical Ailments and Afflictions
MAA-006~Common Magical Ailments and Afflictions
MAA-007~Common Magical Ailments and Afflictions
MAA-008~Common Magical Ailments and Afflictions
CCC-001~A Compendium of Common Curses and Their Counter-Actions
CCC-002~A Compendium of Common Curses and Their Counter-Actions
CCC-003~A Compendium of Common Curses and Their Counter-Actions
CCC-004~A Compendium of Common Curses and Their Counter-Actions
CCC-005~A Compendium of Common Curses and Their Counter-Actions
CCC-006~A Compendium of Common Curses and Their Counter-Actions
CCC-007~A Compendium of Common Curses and Their Counter-Actions
CCC-008~A Compendium of Common Curses and Their Counter-Actions
CCC-009~A Compendium of Common Curses and Their Counter-Actions
CCC-010~A Compendium of Common Curses and Their Counter-Actions
DAO-001~The Dark Arts Outsmarted
DAO-002~The Dark Arts Outsmarted
DAO-003~The Dark Arts Outsmarted
DAO-004~The Dark Arts Outsmarted
DAO-005~The Dark Arts Outsmarted
DMT-001~Defensive Magical Theory
DMT-002~Defensive Magical Theory
DMT-003~Defensive Magical Theory
DMT-004~Defensive Magical Theory
DMT-005~Defensive Magical Theory
DGB-001~Dragon Species of Great Britain and Ireland
DGB-002~Dragon Species of Great Britain and Ireland
DGB-003~Dragon Species of Great Britain and Ireland
DGB-004~Dragon Species of Great Britain and Ireland
DGB-005~Dragon Species of Great Britain and Ireland
DGB-006~Dragon Species of Great Britain and Ireland
DGB-007~Dragon Species of Great Britain and Ireland
DGB-008~Dragon Species of Great Britain and Ireland
DGB-009~Dragon Species of Great Britain and Ireland
DGB-010~Dragon Species of Great Britain and Ireland
DGB-011~Dragon Species of Great Britain and Ireland
DGB-012~Dragon Species of Great Britain and Ireland
DGB-013~Dragon Species of Great Britain and Ireland
EBA-001~Enchantment in Baking
EBA-002~Enchantment in Baking
EBA-003~Enchantment in Baking
EBA-004~Enchantment in Baking
DDA-001~The Essential Defence Against the Dark Arts
DDA-002~The Essential Defence Against the Dark Arts
DDA-003~The Essential Defence Against the Dark Arts
DDA-004~The Essential Defence Against the Dark Arts
DDA-005~The Essential Defence Against the Dark Arts
DDA-006~The Essential Defence Against the Dark Arts
DDA-007~The Essential Defence Against the Dark Arts
DDA-008~The Essential Defence Against the Dark Arts
DDA-009~The Essential Defence Against the Dark Arts
DDA-010~The Essential Defence Against the Dark Arts
FBW-001~Fantastic Beasts and Where to Find Them
FBW-002~Fantastic Beasts and Where to Find Them
FBW-003~Fantastic Beasts and Where to Find Them
FBW-004~Fantastic Beasts and Where to Find Them
FBW-005~Fantastic Beasts and Where to Find Them
FBW-006~Fantastic Beasts and Where to Find Them
FBW-007~Fantastic Beasts and Where to Find Them
FET-001~Flesh-Eating Trees of the World
FET-002~Flesh-Eating Trees of the World
FET-003~Flesh-Eating Trees of the World
FET-004~Flesh-Eating Trees of the World
FET-005~Flesh-Eating Trees of the World
FET-006~Flesh-Eating Trees of the World
SHG-001~Fowl or Foul? A Study of Hippogriff Brutality
SHG-002~Fowl or Foul? A Study of Hippogriff Brutality
SHG-003~Fowl or Foul? A Study of Hippogriff Brutality
SHG-004~Fowl or Foul? A Study of Hippogriff Brutality
SHG-005~Fowl or Foul? A Study of Hippogriff Brutality
SHG-006~Fowl or Foul? A Study of Hippogriff Brutality
DKG-001~From Egg to Inferno, A Dragon Keeper's Guide
DKG-002~From Egg to Inferno, A Dragon Keeper's Guide
DKG-003~From Egg to Inferno, A Dragon Keeper's Guide
DKG-004~From Egg to Inferno, A Dragon Keeper's Guide
DKG-005~From Egg to Inferno, A Dragon Keeper's Guide
DKG-006~From Egg to Inferno, A Dragon Keeper's Guide
DKG-007~From Egg to Inferno, A Dragon Keeper's Guide
DKG-008~From Egg to Inferno, A Dragon Keeper's Guide
GHP-001~Gilderoy Lockhart's Guide to Household Pests
GHP-002~Gilderoy Lockhart's Guide to Household Pests
GHP-003~Gilderoy Lockhart's Guide to Household Pests
GHP-004~Gilderoy Lockhart's Guide to Household Pests
GHP-005~Gilderoy Lockhart's Guide to Household Pests
GHP-006~Gilderoy Lockhart's Guide to Household Pests
GHP-007~Gilderoy Lockhart's Guide to Household Pests
GHP-008~Gilderoy Lockhart's Guide to Household Pests
GHP-009~Gilderoy Lockhart's Guide to Household Pests
GHP-010~Gilderoy Lockhart's Guide to Household Pests
GHP-011~Gilderoy Lockhart's Guide to Household Pests
GHP-012~Gilderoy Lockhart's Guide to Household Pests
GHP-013~Gilderoy Lockhart's Guide to Household Pests
WET-001~Great Wizarding Events of the Twentieth Century
WET-002~Great Wizarding Events of the Twentieth Century
WET-003~Great Wizarding Events of the Twentieth Century
WET-004~Great Wizarding Events of the Twentieth Century
WET-005~Great Wizarding Events of the Twentieth Century
WET-006~Great Wizarding Events of the Twentieth Century
WET-007~Great Wizarding Events of the Twentieth Century
WET-008~Great Wizarding Events of the Twentieth Century
ATF-001~Guide to Advanced Transfiguration
ATF-002~Guide to Advanced Transfiguration
ATF-003~Guide to Advanced Transfiguration
ATF-004~Guide to Advanced Transfiguration
ATF-005~Guide to Advanced Transfiguration
ATF-006~Guide to Advanced Transfiguration
ATF-007~Guide to Advanced Transfiguration
ATF-008~Guide to Advanced Transfiguration
ATF-009~Guide to Advanced Transfiguration
ATF-010~Guide to Advanced Transfiguration
ATF-011~Guide to Advanced Transfiguration
HBC-001~Handbook of Do-It-Yourself Broom Care
HBC-002~Handbook of Do-It-Yourself Broom Care
HBC-003~Handbook of Do-It-Yourself Broom Care
HBC-004~Handbook of Do-It-Yourself Broom Care
THH-001~The Healer's Helpmate
THH-002~The Healer's Helpmate
THH-003~The Healer's Helpmate
THH-004~The Healer's Helpmate
THH-005~The Healer's Helpmate
THH-006~The Healer's Helpmate
THH-007~The Healer's Helpmate
THH-008~The Healer's Helpmate
THH-009~The Healer's Helpmate
THH-010~The Healer's Helpmate
THH-011~The Healer's Helpmate
HOM-001~A History of Magic
HOM-002~A History of Magic
HOM-003~A History of Magic
HOM-004~A History of Magic
HOM-005~A History of Magic
HOM-006~A History of Magic
HOM-007~A History of Magic
HOM-008~A History of Magic
HOM-009~A History of Magic
HOM-010~A History of Magic
HOM-011~A History of Magic
HOM-012~A History of Magic
HWH-001~Holidays With Hags
HWH-002~Holidays With Hags
HWH-003~Holidays With Hags
HWH-004~Holidays With Hags
HWH-005~Holidays With Hags
HWH-006~Holidays With Hags
HWH-007~Holidays With Hags
HWH-008~Holidays With Hags
MMD-001~Important Modern Magical Discoveries
MMD-002~Important Modern Magical Discoveries
MMD-003~Important Modern Magical Discoveries
MMD-004~Important Modern Magical Discoveries
MMD-005~Important Modern Magical Discoveries
MMD-006~Important Modern Magical Discoveries
MMD-007~Important Modern Magical Discoveries
MMD-008~Important Modern Magical Discoveries
MMD-009~Important Modern Magical Discoveries
MMD-010~Important Modern Magical Discoveries
ITF-001~Intermediate Transfiguration
ITF-002~Intermediate Transfiguration
ITF-003~Intermediate Transfiguration
ITF-004~Intermediate Transfiguration
ITF-005~Intermediate Transfiguration
ITF-006~Intermediate Transfiguration
ITF-007~Intermediate Transfiguration
ITF-008~Intermediate Transfiguration
ITF-009~Intermediate Transfiguration
ITF-010~Intermediate Transfiguration
LAB-001~The Life and Lies of Albus Dumbledore
LAB-002~The Life and Lies of Albus Dumbledore
LAB-003~The Life and Lies of Albus Dumbledore
LAB-004~The Life and Lies of Albus Dumbledore
LAB-005~The Life and Lies of Albus Dumbledore
LAB-006~The Life and Lies of Albus Dumbledore
LAB-007~The Life and Lies of Albus Dumbledore
MDP-001~Magical Drafts and Potions
MDP-002~Magical Drafts and Potions
MDP-003~Magical Drafts and Potions
MDP-004~Magical Drafts and Potions
MDP-005~Magical Drafts and Potions
MME-001~Magical Me
MME-002~Magical Me
MME-003~Magical Me
MME-004~Magical Me
MME-005~Magical Me
MME-006~Magical Me
MME-007~Magical Me
MME-008~Magical Me
MTH-001~Magical Theory
MTH-002~Magical Theory
MTH-003~Magical Theory
MTH-004~Magical Theory
MTH-005~Magical Theory
MTH-006~Magical Theory
MTH-007~Magical Theory
MTH-008~Magical Theory
MTH-009~Magical Theory
MKE-001~Magick Most Evile
MKE-002~Magick Most Evile
MKE-003~Magick Most Evile
MKE-004~Magick Most Evile
MKE-005~Magick Most Evile
MKE-006~Magick Most Evile
MKE-007~Magick Most Evile
MKE-008~Magick Most Evile
MKE-009~Magick Most Evile
MKE-010~Magick Most Evile
MMH-001~Modern Magical History
MMH-002~Modern Magical History
MMH-003~Modern Magical History
MMH-004~Modern Magical History
MMH-005~Modern Magical History
MMH-006~Modern Magical History
MMH-007~Modern Magical History
MBM-001~Monster Book of Monsters
MBM-002~Monster Book of Monsters
MBM-003~Monster Book of Monsters
MBM-004~Monster Book of Monsters
MBM-005~Monster Book of Monsters
MBM-006~Monster Book of Monsters
MNT-001~Notable Magical Names of Our Time
MNT-002~Notable Magical Names of Our Time
MNT-003~Notable Magical Names of Our Time
MNT-004~Notable Magical Names of Our Time
MNT-005~Notable Magical Names of Our Time
MNT-006~Notable Magical Names of Our Time
MFM-001~One Minute Feasts - It's Magic!
MFM-002~One Minute Feasts - It's Magic!
MFM-003~One Minute Feasts - It's Magic!
MFM-004~One Minute Feasts - It's Magic!
MFM-005~One Minute Feasts - It's Magic!
MHF-001~One Thousand Magical Herbs and Fungi
MHF-002~One Thousand Magical Herbs and Fungi
MHF-003~One Thousand Magical Herbs and Fungi
MHF-004~One Thousand Magical Herbs and Fungi
MHF-005~One Thousand Magical Herbs and Fungi
MHF-006~One Thousand Magical Herbs and Fungi
PDM-001~Practical Defensive Magic and Its Use Against the Dark Arts
PDM-002~Practical Defensive Magic and Its Use Against the Dark Arts
PDM-003~Practical Defensive Magic and Its Use Against the Dark Arts
PDM-004~Practical Defensive Magic and Its Use Against the Dark Arts
PDM-005~Practical Defensive Magic and Its Use Against the Dark Arts
PDM-006~Practical Defensive Magic and Its Use Against the Dark Arts
PDM-007~Practical Defensive Magic and Its Use Against the Dark Arts
PDM-008~Practical Defensive Magic and Its Use Against the Dark Arts
PDM-009~Practical Defensive Magic and Its Use Against the Dark Arts
PDM-010~Practical Defensive Magic and Its Use Against the Dark Arts
PDM-011~Practical Defensive Magic and Its Use Against the Dark Arts
STS-001~Saucy Tricks for Tricky Sorts
STS-002~Saucy Tricks for Tricky Sorts
STS-003~Saucy Tricks for Tricky Sorts
STS-004~Saucy Tricks for Tricky Sorts
STS-005~Saucy Tricks for Tricky Sorts
STS-006~Saucy Tricks for Tricky Sorts
STS-007~Saucy Tricks for Tricky Sorts
STS-008~Saucy Tricks for Tricky Sorts
SDA-001~Secrets of the Darkest Art
SDA-002~Secrets of the Darkest Art
SDA-003~Secrets of the Darkest Art
SDA-004~Secrets of the Darkest Art
SDA-005~Secrets of the Darkest Art
SDA-006~Secrets of the Darkest Art
SDA-007~Secrets of the Darkest Art
SDA-008~Secrets of the Darkest Art
SDA-009~Secrets of the Darkest Art
SDA-010~Secrets of the Darkest Art
SDA-011~Secrets of the Darkest Art
SDA-012~Secrets of the Darkest Art
SDS-001~Self-Defensive Spellwork
SDS-002~Self-Defensive Spellwork
SDS-003~Self-Defensive Spellwork
SDS-004~Self-Defensive Spellwork
SDS-005~Self-Defensive Spellwork
SDS-006~Self-Defensive Spellwork
SDS-007~Self-Defensive Spellwork
SDS-008~Self-Defensive Spellwork
SDS-009~Self-Defensive Spellwork
SDS-010~Self-Defensive Spellwork
SDS-011~Self-Defensive Spellwork
SDS-012~Self-Defensive Spellwork
SDS-013~Self-Defensive Spellwork
SPS-001~Spellman's Syllabary
SPS-002~Spellman's Syllabary
SPS-003~Spellman's Syllabary
SPS-004~Spellman's Syllabary
SPS-005~Spellman's Syllabary
SPS-006~Spellman's Syllabary
SPS-007~Spellman's Syllabary
SPS-008~Spellman's Syllabary
SPS-009~Spellman's Syllabary
SPS-010~Spellman's Syllabary
SPS-011~Spellman's Syllabary
SPS-012~Spellman's Syllabary
RDW-001~A Study of Recent Developments in Wizardry
RDW-002~A Study of Recent Developments in Wizardry
RDW-003~A Study of Recent Developments in Wizardry
RDW-004~A Study of Recent Developments in Wizardry
RDW-005~A Study of Recent Developments in Wizardry
RDW-006~A Study of Recent Developments in Wizardry
VWV-001~Voyages With Vampires
VWV-002~Voyages With Vampires
VWV-003~Voyages With Vampires
VWV-004~Voyages With Vampires
VWV-005~Voyages With Vampires
VWV-006~Voyages With Vampires
VWV-007~Voyages With Vampires
VWV-008~Voyages With Vampires
VWV-009~Voyages With Vampires
VWV-010~Voyages With Vampires
WWW-001~Wanderings With Werewolves
WWW-002~Wanderings With Werewolves
WWW-003~Wanderings With Werewolves
WWW-004~Wanderings With Werewolves
WWW-005~Wanderings With Werewolves
WWW-006~Wanderings With Werewolves
WWW-007~Wanderings With Werewolves
WWW-008~Wanderings With Werewolves
WWW-009~Wanderings With Werewolves
WWW-010~Wanderings With Werewolves
WDS-001~Weird Wizarding Dilemmas and Their Solutions
WDS-002~Weird Wizarding Dilemmas and Their Solutions
WDS-003~Weird Wizarding Dilemmas and Their Solutions
WDS-004~Weird Wizarding Dilemmas and Their Solutions
WDS-005~Weird Wizarding Dilemmas and Their Solutions
WDS-006~Weird Wizarding Dilemmas and Their Solutions
WDS-007~Weird Wizarding Dilemmas and Their Solutions
WTW-001~Where There's a Wand, There's a Way
WTW-002~Where There's a Wand, There's a Way
WTW-003~Where There's a Wand, There's a Way
WTW-004~Where There's a Wand, There's a Way
WTW-005~Where There's a Wand, There's a Way
WTW-006~Where There's a Wand, There's a Way
WTW-007~Where There's a Wand, There's a Way
WTW-008~Where There's a Wand, There's a Way
WTW-009~Where There's a Wand, There's a Way
WTW-010~Where There's a Wand, There's a Way
WTW-011~Where There's a Wand, There's a Way
WTW-012~Where There's a Wand, There's a Way
WTW-013~Where There's a Wand, There's a Way
Borrowers
SLY2302~Euan Abercrombie
SLY2303~Stewart Ackerley
SLY2304~Bertram Aubrey
SLY2305~Avery
SLY2307~Marcus Belby
SLY2311~Susan Bones
SLY2312~Terry Boot
SLY2315~Mandy Brocklehurst
SLY2316~Lavender Brown
SLY2319~Eddie Carmichael
SLY2320~Owen Cauldwell
SLY2321~Cho Chang
GRF3701~Vincent Crabbe
GRF3702~Colin Creevey
GRF3703~Dennis Creevey
GRF3704~Roger Davies
GRF3706~Harold Dingle
GRF3709~B. Dunstan
GRF3710~Marietta Edgecombe
GRF3711~S. Fawcett
GRF3712~Justin Finch-Fletchley
GRF3713~Seamus Finnigan
GRF3716~Anthony Goldstein
RAV4301~Hermione Jean Granger
RAV4302~Daphne Greengrass
RAV4304~Davey Gudgeon
RAV4305~Rubeus Hagrid
RAV4306~Ciceron Harkiss
RAV4307~Geoffrey Hooper
RAV4309~Angelina Johnson
HUF7201~Gwenog Jones
HUF7204~Viktor Krum
HUF7206~Bellatrix Lestrange
HUF7208~Luna Lovegood
HUF7210~Mary Macdonald
RAV5901~Oliver Wood
RAV5904~Ernest Macmillan
RAV5905~Laura Madley
RAV5906~Draco Malfoy
RAV5907~Natalie McDonald
RAV5908~M. G. McGonagall
GRF9102~Laverne de Montmorency
GRF9103~Montgomery sisters
GRF9104~Lily Moon
GRF9105~Harold Potter
GRF9106~Theodore Nott
GRF9107~Garrick Ollivander
GRF9108~Pansy Parkinson
GRF9109~Padma Patil
GRF9110~Parvati Patil
Checkouts
SLY2304~AIC-001~2019-03-09
GRF3713~AIC-002~2019-02-26
SLY2315~AIC-003~2019-03-21
RAV4309~AIC-004~2019-03-19
HUF7208~AIC-005~2019-03-15
GRF9102~APM-001~2019-03-21
RAV5906~APM-002~2019-03-09
GRF9105~APM-003~2019-03-25
RAV4304~APM-004~2019-02-25
GRF9106~AMM-001~2019-03-02
GRF3702~AMM-002~2019-03-20
RAV5904~AMM-003~2019-03-01
SLY2303~AMM-004~2019-03-07
GRF3702~AMM-005~2019-03-26
RAV5901~AMM-006~2019-03-04
HUF7206~AMM-007~2019-03-02
SLY2307~AMM-008~2019-03-14
HUF7201~AMM-009~2019-03-14
GRF9107~AMM-010~2019-03-24
GRF3710~AMM-011~2019-03-19
SLY2319~AMM-012~2019-03-06
HUF7210~AMM-013~2019-03-12
GRF3709~ART-001~2019-03-25
HUF7206~ART-002~2019-02-28
SLY2315~ART-003~2019-02-27
GRF9109~ART-004~2019-02-28
GRF9107~ART-005~2019-03-06
SLY2303~ART-006~2019-03-24
GRF9105~ART-007~2019-02-28
RAV5907~MEE-001~2019-03-05
SLY2305~MEE-002~2019-03-11
GRF9104~MEE-003~2019-03-11
HUF7210~MEE-004~2019-03-03
RAV4304~AAV-001~2019-03-05
SLY2312~AAV-002~2019-03-20
GRF9105~AAV-003~2019-03-18
RAV5906~AAV-004~2019-03-26
HUF7210~AAV-005~2019-03-24
GRF3710~AAV-006~2019-03-08
HUF7206~AAV-007~2019-03-11
SLY2303~AAV-008~2019-03-20
SLY2319~AAV-009~2019-03-13
RAV4306~AAV-010~2019-03-11
RAV4309~AAV-011~2019-03-16
GRF9109~AAV-012~2019-03-25
RAV4304~AAV-013~2019-03-14
GRF9103~HBV-001~2019-03-02
HUF7206~HBV-002~2019-02-28
SLY2321~HBV-003~2019-03-11
RAV5905~HBV-004~2019-03-09
GRF3701~HBV-005~2019-02-28
SLY2321~HBV-006~2019-03-21
SLY2321~HBV-007~2019-03-13
RAV5901~HBV-008~2019-03-11
RAV5904~HBV-009~2019-03-18
RAV5901~HBV-010~2019-03-24
GRF9109~HBV-011~2019-03-05
GRF9104~HBV-012~2019-03-19
GRF3709~HBV-013~2019-03-25
SLY2321~GTF-001~2019-02-25
SLY2315~GTF-002~2019-03-06
GRF3711~GTF-003~2019-03-17
HUF7201~GTF-004~2019-03-17
GRF3706~GTF-005~2019-03-04
SLY2321~WFT-001~2019-03-16
GRF3716~WFT-002~2019-03-12
SLY2319~WFT-003~2019-03-10
SLY2302~WFT-004~2019-03-05
GRF3716~WFT-005~2019-02-27
HUF7204~WFT-006~2019-03-15
HUF7204~WFT-007~2019-03-17
SLY2303~WFT-008~2019-03-17
RAV5906~WFT-009~2019-03-23
RAV5905~WFT-010~2019-03-14
RAV4307~CYC-001~2019-03-19
RAV4302~CYC-002~2019-03-13
HUF7201~CYC-003~2019-03-05
GRF9105~CYC-004~2019-02-25
SLY2320~MAA-001~2019-03-20
SLY2315~MAA-002~2019-03-15
GRF9103~MAA-003~2019-03-05
SLY2305~MAA-004~2019-03-08
RAV4309~MAA-005~2019-03-11
RAV4306~MAA-006~2019-03-04
SLY2303~MAA-007~2019-03-20
GRF9103~MAA-008~2019-03-05
GRF3701~CCC-001~2019-03-07
SLY2312~CCC-002~2019-03-20
RAV5901~CCC-003~2019-02-28
GRF9102~CCC-004~2019-03-25
GRF3701~CCC-005~2019-03-08
GRF3703~CCC-006~2019-03-11
SLY2320~CCC-007~2019-03-08
GRF3710~CCC-008~2019-03-16
GRF3701~CCC-009~2019-03-12
RAV4306~CCC-010~2019-03-15
RAV5901~DAO-001~2019-03-24
GRF9105~DAO-002~2019-02-27
GRF3710~DAO-003~2019-03-20
GRF3706~DAO-004~2019-03-19
GRF9109~DAO-005~2019-03-05
RAV5906~DMT-001~2019-03-09
SLY2315~DMT-002~2019-02-25
RAV4305~DMT-003~2019-02-26
RAV5907~DMT-004~2019-02-27
GRF3710~DMT-005~2019-02-27
RAV4301~DGB-001~2019-03-17
SLY2305~DGB-002~2019-03-16
RAV5901~DGB-003~2019-03-01
SLY2312~DGB-004~2019-03-20
HUF7210~DGB-005~2019-03-23
HUF7208~DGB-006~2019-03-06
RAV4306~DGB-007~2019-03-13
RAV4301~DGB-008~2019-03-08
HUF7208~DGB-009~2019-03-14
GRF3710~DGB-010~2019-03-17
RAV4306~DGB-011~2019-03-12
GRF3713~DGB-012~2019-03-01
SLY2302~DGB-013~2019-03-25
RAV4306~EBA-001~2019-03-03
GRF3712~EBA-002~2019-03-09
SLY2320~EBA-003~2019-03-01
RAV5908~EBA-004~2019-03-07
SLY2319~DDA-001~2019-03-07
HUF7204~DDA-002~2019-03-05
RAV4304~DDA-003~2019-03-20
RAV4306~DDA-004~2019-03-09
GRF3702~DDA-005~2019-03-21
SLY2303~DDA-006~2019-03-24
HUF7210~DDA-007~2019-03-15
SLY2312~DDA-008~2019-03-16
RAV4307~DDA-009~2019-03-06
RAV5904~DDA-010~2019-03-19
SLY2303~FBW-001~2019-03-19
GRF3713~FBW-002~2019-03-10
GRF9103~FBW-003~2019-03-08
SLY2315~FBW-004~2019-03-04
RAV5907~FBW-005~2019-03-04
RAV4305~FBW-006~2019-02-25
RAV5907~FBW-007~2019-03-14
HUF7210~FET-001~2019-03-14
GRF3701~FET-002~2019-03-22
GRF9106~FET-003~2019-03-26
SLY2312~FET-004~2019-03-21
SLY2303~FET-005~2019-03-08
GRF3710~FET-006~2019-03-21
SLY2311~SHG-001~2019-03-01
SLY2307~SHG-002~2019-03-21
RAV5901~SHG-003~2019-02-28
GRF3716~SHG-004~2019-03-20
GRF9104~SHG-005~2019-03-03
SLY2312~SHG-006~2019-03-15
SLY2307~DKG-001~2019-03-08
GRF9103~DKG-002~2019-03-03
HUF7204~DKG-003~2019-03-04
GRF9107~DKG-004~2019-03-12
RAV5905~DKG-005~2019-03-06
RAV4305~DKG-006~2019-03-18
GRF3713~DKG-007~2019-02-26
SLY2311~DKG-008~2019-03-12
SLY2315~GHP-001~2019-02-28
HUF7204~GHP-002~2019-03-07
SLY2312~GHP-003~2019-03-14
SLY2305~GHP-004~2019-03-11
SLY2320~GHP-005~2019-03-06
RAV5904~GHP-006~2019-03-15
HUF7204~GHP-007~2019-03-18
GRF3710~GHP-008~2019-03-03
RAV5908~GHP-009~2019-03-20
RAV4302~GHP-010~2019-03-21
SLY2316~GHP-011~2019-03-10
SLY2320~GHP-012~2019-03-26
SLY2316~GHP-013~2019-03-15
RAV5908~WET-001~2019-03-26
GRF3716~WET-002~2019-03-12
GRF9107~WET-003~2019-03-17
RAV5906~WET-004~2019-03-05
GRF9103~WET-005~2019-03-25
SLY2311~WET-006~2019-03-02
RAV4307~WET-007~2019-03-09
GRF9107~WET-008~2019-03-04
SLY2302~ATF-001~2019-03-11
RAV5906~ATF-002~2019-03-19
GRF3702~ATF-003~2019-03-13
GRF9108~ATF-004~2019-03-06
SLY2312~ATF-005~2019-02-27
SLY2316~ATF-006~2019-03-23
GRF9103~ATF-007~2019-03-19
RAV5906~ATF-008~2019-03-17
SLY2312~ATF-009~2019-02-25
RAV4304~ATF-010~2019-03-15
RAV4305~ATF-011~2019-03-09
GRF3706~HBC-001~2019-03-07
SLY2305~HBC-002~2019-03-13
RAV5908~HBC-003~2019-03-03
GRF3716~HBC-004~2019-02-28
GRF3701~THH-001~2019-02-27
HUF7204~THH-002~2019-03-11
GRF3711~THH-003~2019-02-27
SLY2311~THH-004~2019-02-26
RAV5907~THH-005~2019-03-13
RAV5905~THH-006~2019-03-21
SLY2316~THH-007~2019-03-07
SLY2320~THH-008~2019-03-06
GRF9109~THH-009~2019-03-16
GRF3712~THH-010~2019-03-10
SLY2302~THH-011~2019-03-22
HUF7206~HOM-001~2019-03-25
SLY2307~HOM-002~2019-03-16
RAV4309~HOM-003~2019-03-22
HUF7201~HOM-004~2019-03-21
GRF3704~HOM-005~2019-03-06
RAV5904~HOM-006~2019-03-21
RAV4302~HOM-007~2019-03-19
GRF3716~HOM-008~2019-03-02
RAV4307~HOM-009~2019-03-19
RAV4309~HOM-010~2019-03-18
SLY2320~HOM-011~2019-03-23
SLY2321~HOM-012~2019-02-28
GRF9103~HWH-001~2019-03-09
RAV4304~HWH-002~2019-03-09
RAV4304~HWH-003~2019-02-25
SLY2307~HWH-004~2019-03-16
GRF9102~HWH-005~2019-03-07
GRF3710~HWH-006~2019-03-23
GRF9107~HWH-007~2019-03-16
HUF7201~HWH-008~2019-02-27
SLY2319~MMD-001~2019-03-12
RAV4301~MMD-002~2019-03-07
GRF3713~MMD-003~2019-03-02
SLY2321~MMD-004~2019-03-11
GRF3712~MMD-005~2019-03-17
RAV4309~MMD-006~2019-02-27
GRF3709~MMD-007~2019-03-09
RAV5907~MMD-008~2019-03-19
SLY2307~MMD-009~2019-03-02
GRF9106~MMD-010~2019-03-24
GRF3712~ITF-001~2019-03-14
GRF3704~ITF-002~2019-03-26
SLY2321~ITF-003~2019-02-25
SLY2304~ITF-004~2019-03-02
RAV5901~ITF-005~2019-03-10
HUF7206~ITF-006~2019-03-15
GRF3701~ITF-007~2019-03-11
SLY2307~ITF-008~2019-03-12
RAV4304~ITF-009~2019-03-08
GRF9107~ITF-010~2019-03-04
GRF3704~LAB-001~2019-03-20
GRF3716~LAB-002~2019-03-04
HUF7204~LAB-003~2019-03-01
SLY2302~LAB-004~2019-03-18
SLY2321~LAB-005~2019-03-03
SLY2304~LAB-006~2019-03-04
RAV5904~LAB-007~2019-03-09
RAV4304~MDP-001~2019-02-27
RAV4306~MDP-002~2019-03-22
RAV5901~MDP-003~2019-02-27
GRF3713~MDP-004~2019-03-25
GRF9102~MDP-005~2019-03-18
HUF7206~MME-001~2019-02-27
GRF9105~MME-002~2019-02-28
HUF7208~MME-003~2019-03-06
GRF3702~MME-004~2019-03-23
SLY2315~MME-005~2019-03-10
SLY2311~MME-006~2019-03-06
GRF3716~MME-007~2019-03-16
SLY2311~MME-008~2019-03-11
SLY2302~MTH-001~2019-03-16
RAV5907~MTH-002~2019-03-09
GRF3703~MTH-003~2019-03-14
HUF7208~MTH-004~2019-03-21
GRF3716~MTH-005~2019-03-16
SLY2302~MTH-006~2019-03-26
GRF3702~MTH-007~2019-03-19
GRF3713~MTH-008~2019-03-13
RAV5905~MTH-009~2019-03-24
RAV5908~MKE-001~2019-02-28
HUF7201~MKE-002~2019-03-02
RAV5905~MKE-003~2019-02-28
GRF9108~MKE-004~2019-03-11
SLY2311~MKE-005~2019-03-02
GRF9105~MKE-006~2019-02-28
SLY2312~MKE-007~2019-03-01
GRF3712~MKE-008~2019-03-16
GRF9108~MKE-009~2019-03-17
RAV4304~MKE-010~2019-03-24
SLY2316~MMH-001~2019-02-27
GRF9104~MMH-002~2019-03-12
RAV5905~MMH-003~2019-03-14
SLY2315~MMH-004~2019-03-17
GRF3704~MMH-005~2019-03-25
GRF9104~MMH-006~2019-03-20
RAV4306~MMH-007~2019-03-24
GRF3711~MBM-001~2019-03-21
GRF3710~MBM-002~2019-03-23
RAV4304~MBM-003~2019-03-06
RAV5908~MBM-004~2019-03-08
SLY2305~MBM-005~2019-03-25
SLY2315~MBM-006~2019-03-14
SLY2303~MNT-001~2019-03-13
SLY2311~MNT-002~2019-03-05
GRF3701~MNT-003~2019-03-07
GRF3712~MNT-004~2019-03-01
SLY2316~MNT-005~2019-03-12
SLY2307~MNT-006~2019-03-05
RAV5907~MFM-001~2019-03-13
RAV4306~MFM-002~2019-03-13
GRF3709~MFM-003~2019-03-22
RAV5904~MFM-004~2019-03-22
HUF7208~MFM-005~2019-03-19
RAV4306~MHF-001~2019-03-15
GRF3706~MHF-002~2019-03-22
SLY2307~MHF-003~2019-03-18
SLY2319~MHF-004~2019-03-01
GRF3711~MHF-005~2019-02-26
GRF3711~MHF-006~2019-03-16
RAV4309~PDM-001~2019-02-26
RAV4309~PDM-002~2019-03-06
GRF9105~PDM-003~2019-03-20
GRF3711~PDM-004~2019-03-16
RAV5905~PDM-005~2019-02-25
RAV5905~PDM-006~2019-03-21
RAV4309~PDM-007~2019-02-26
GRF9105~PDM-008~2019-03-06
RAV4302~PDM-009~2019-03-03
GRF9107~PDM-010~2019-03-09
RAV4309~PDM-011~2019-02-25
GRF3709~STS-001~2019-02-25
GRF3706~STS-002~2019-03-08
GRF9104~STS-003~2019-03-15
RAV4302~STS-004~2019-02-25
RAV4309~STS-005~2019-03-04
GRF3710~STS-006~2019-03-02
SLY2307~STS-007~2019-03-11
GRF9107~STS-008~2019-03-10
RAV4305~SDA-001~2019-03-21
SLY2303~SDA-002~2019-03-06
GRF3702~SDA-003~2019-03-07
SLY2303~SDA-004~2019-03-21
GRF3706~SDA-005~2019-03-13
GRF9107~SDA-006~2019-03-17
SLY2305~SDA-007~2019-03-06
RAV4302~SDA-008~2019-03-17
GRF9102~SDA-009~2019-02-26
SLY2321~SDA-010~2019-03-15
RAV4305~SDA-011~2019-03-13
GRF3712~SDA-012~2019-03-07
SLY2307~SDS-001~2019-03-16
GRF9105~SDS-002~2019-03-18
SLY2303~SDS-003~2019-02-25
GRF9106~SDS-004~2019-02-26
GRF9109~SDS-005~2019-03-15
SLY2315~SDS-006~2019-02-28
GRF3711~SDS-007~2019-03-07
SLY2307~SDS-008~2019-03-18
GRF9106~SDS-009~2019-02-28
HUF7208~SDS-010~2019-03-01
RAV4309~SDS-011~2019-03-26
SLY2305~SDS-012~2019-03-14
SLY2316~SDS-013~2019-02-27
SLY2321~SPS-001~2019-03-23
RAV4305~SPS-002~2019-03-12
HUF7201~SPS-003~2019-03-13
RAV5901~SPS-004~2019-03-01
RAV5904~SPS-005~2019-03-04
RAV4307~SPS-006~2019-03-05
HUF7210~SPS-007~2019-02-28
GRF3702~SPS-008~2019-03-13
SLY2316~SPS-009~2019-03-13
GRF3706~SPS-010~2019-03-15
GRF3711~SPS-011~2019-03-12
GRF3704~SPS-012~2019-03-13
RAV5905~RDW-001~2019-03-04
RAV4302~RDW-002~2019-03-10
GRF3702~RDW-003~2019-03-15
GRF3704~RDW-004~2019-03-16
HUF7210~RDW-005~2019-03-23
GRF9102~RDW-006~2019-03-05
SLY2304~VWV-001~2019-03-13
SLY2312~VWV-002~2019-02-27
SLY2321~VWV-003~2019-03-05
HUF7204~VWV-004~2019-03-18
GRF3706~VWV-005~2019-03-01
SLY2304~VWV-006~2019-03-23
RAV4302~VWV-007~2019-03-14
GRF3710~VWV-008~2019-03-22
RAV4307~VWV-009~2019-03-15
RAV5905~VWV-010~2019-02-28
GRF3710~WWW-001~2019-03-22
GRF3709~WWW-002~2019-03-05
SLY2316~WWW-003~2019-03-21
HUF7201~WWW-004~2019-03-22
GRF3709~WWW-005~2019-03-09
GRF3703~WWW-006~2019-02-26
RAV4301~WWW-007~2019-03-22
GRF3704~WWW-008~2019-03-17
GRF3716~WWW-009~2019-03-11
SLY2305~WWW-010~2019-03-26
HUF7206~WDS-001~2019-03-16
RAV5906~WDS-002~2019-03-17
RAV5904~WDS-003~2019-03-23
GRF9104~WDS-004~2019-02-27
RAV4305~WDS-005~2019-03-04
RAV5901~WDS-006~2019-03-12
RAV5907~WDS-007~2019-03-19
RAV5904~WTW-001~2019-03-22
HUF7210~WTW-002~2019-03-14
RAV5908~WTW-003~2019-03-21
RAV4309~WTW-004~2019-03-14
GRF3706~WTW-005~2019-03-25
HUF7201~WTW-006~2019-03-18
RAV5906~WTW-007~2019-02-28
HUF7210~WTW-008~2019-02-25
RAV4302~WTW-009~2019-03-16
GRF9108~WTW-010~2019-03-01
HUF7201~WTW-011~2019-03-09
RAV4306~WTW-012~2019-03-04
RAV4307~WTW-013~2019-02-26
EndOfInput
2019-02-25~Angelina Johnson~PDM-011~Practical Defensive Magic and Its Use Against the Dark Arts
2019-02-25~B. Dunstan~STS-001~Saucy Tricks for Tricky Sorts
2019-02-25~Cho Chang~GTF-001~A Beginner's Guide to Transfiguration
2019-02-25~Cho Chang~ITF-003~Intermediate Transfiguration
2019-02-25~Daphne Greengrass~STS-004~Saucy Tricks for Tricky Sorts
2019-02-25~Davey Gudgeon~APM-004~Advanced Potion-Making
2019-02-25~Davey Gudgeon~HWH-003~Holidays With Hags
2019-02-25~Harold Potter~CYC-004~Charm Your Own Cheese
2019-02-25~Laura Madley~PDM-005~Practical Defensive Magic and Its Use Against the Dark Arts
2019-02-25~Mandy Brocklehurst~DMT-002~Defensive Magical Theory
2019-02-25~Mary Macdonald~WTW-008~Where There's a Wand, There's a Way
2019-02-25~Rubeus Hagrid~FBW-006~Fantastic Beasts and Where to Find Them
2019-02-25~Stewart Ackerley~SDS-003~Self-Defensive Spellwork
2019-02-25~Terry Boot~ATF-009~Guide to Advanced Transfiguration
2019-02-26~Angelina Johnson~PDM-001~Practical Defensive Magic and Its Use Against the Dark Arts
2019-02-26~Angelina Johnson~PDM-007~Practical Defensive Magic and Its Use Against the Dark Arts
2019-02-26~Dennis Creevey~WWW-006~Wanderings With Werewolves
2019-02-26~Geoffrey Hooper~WTW-013~Where There's a Wand, There's a Way
2019-02-26~Laverne de Montmorency~SDA-009~Secrets of the Darkest Art
2019-02-26~Rubeus Hagrid~DMT-003~Defensive Magical Theory
2019-02-26~S. Fawcett~MHF-005~One Thousand Magical Herbs and Fungi
2019-02-26~Seamus Finnigan~AIC-002~Achievements in Charming
2019-02-26~Seamus Finnigan~DKG-007~From Egg to Inferno, A Dragon Keeper's Guide
2019-02-26~Susan Bones~THH-004~The Healer's Helpmate
2019-02-26~Theodore Nott~SDS-004~Self-Defensive Spellwork
2019-02-27~Angelina Johnson~MMD-006~Important Modern Magical Discoveries
2019-02-27~Anthony Goldstein~WFT-005~Broken Balls: When Fortunes Turn Foul
2019-02-27~Bellatrix Lestrange~MME-001~Magical Me
2019-02-27~Davey Gudgeon~MDP-001~Magical Drafts and Potions
2019-02-27~Gwenog Jones~HWH-008~Holidays With Hags
2019-02-27~Harold Potter~DAO-002~The Dark Arts Outsmarted
2019-02-27~Lavender Brown~MMH-001~Modern Magical History
2019-02-27~Lavender Brown~SDS-013~Self-Defensive Spellwork
2019-02-27~Lily Moon~WDS-004~Weird Wizarding Dilemmas and Their Solutions
2019-02-27~Mandy Brocklehurst~ART-003~Ancient Runes Translation
2019-02-27~Marietta Edgecombe~DMT-005~Defensive Magical Theory
2019-02-27~Natalie McDonald~DMT-004~Defensive Magical Theory
2019-02-27~Oliver Wood~MDP-003~Magical Drafts and Potions
2019-02-27~S. Fawcett~THH-003~The Healer's Helpmate
2019-02-27~Terry Boot~ATF-005~Guide to Advanced Transfiguration
2019-02-27~Terry Boot~VWV-002~Voyages With Vampires
2019-02-27~Vincent Crabbe~THH-001~The Healer's Helpmate
2019-02-28~Anthony Goldstein~HBC-004~Handbook of Do-It-Yourself Broom Care
2019-02-28~Bellatrix Lestrange~ART-002~Ancient Runes Translation
2019-02-28~Bellatrix Lestrange~HBV-002~Basic Hexes for the Busy and Vexed
2019-02-28~Cho Chang~HOM-012~A History of Magic
2019-02-28~Draco Malfoy~WTW-007~Where There's a Wand, There's a Way
2019-02-28~Harold Potter~ART-007~Ancient Runes Translation
2019-02-28~Harold Potter~MKE-006~Magick Most Evile
2019-02-28~Harold Potter~MME-002~Magical Me
2019-02-28~Laura Madley~MKE-003~Magick Most Evile
2019-02-28~Laura Madley~VWV-010~Voyages With Vampires
2019-02-28~M. G. McGonagall~MKE-001~Magick Most Evile
2019-02-28~Mandy Brocklehurst~GHP-001~Gilderoy Lockhart's Guide to Household Pests
2019-02-28~Mandy Brocklehurst~SDS-006~Self-Defensive Spellwork
2019-02-28~Mary Macdonald~SPS-007~Spellman's Syllabary
2019-02-28~Oliver Wood~CCC-003~A Compendium of Common Curses and Their Counter-Actions
2019-02-28~Oliver Wood~SHG-003~Fowl or Foul? A Study of Hippogriff Brutality
2019-02-28~Padma Patil~ART-004~Ancient Runes Translation
2019-02-28~Theodore Nott~SDS-009~Self-Defensive Spellwork
2019-02-28~Vincent Crabbe~HBV-005~Basic Hexes for the Busy and Vexed
2019-03-01~Eddie Carmichael~MHF-004~One Thousand Magical Herbs and Fungi
2019-03-01~Ernest Macmillan~AMM-003~The Adventures of Martin Miggs, the Mad Muggle
2019-03-01~Harold Dingle~VWV-005~Voyages With Vampires
2019-03-01~Justin Finch-Fletchley~MNT-004~Notable Magical Names of Our Time
2019-03-01~Luna Lovegood~SDS-010~Self-Defensive Spellwork
2019-03-01~Oliver Wood~DGB-003~Dragon Species of Great Britain and Ireland
2019-03-01~Oliver Wood~SPS-004~Spellman's Syllabary
2019-03-01~Owen Cauldwell~EBA-003~Enchantment in Baking
2019-03-01~Pansy Parkinson~WTW-010~Where There's a Wand, There's a Way
2019-03-01~Seamus Finnigan~DGB-012~Dragon Species of Great Britain and Ireland
2019-03-01~Susan Bones~SHG-001~Fowl or Foul? A Study of Hippogriff Brutality
2019-03-01~Terry Boot~MKE-007~Magick Most Evile
2019-03-01~Viktor Krum~LAB-003~The Life and Lies of Albus Dumbledore
2019-03-02~Anthony Goldstein~HOM-008~A History of Magic
2019-03-02~Bellatrix Lestrange~AMM-007~The Adventures of Martin Miggs, the Mad Muggle
2019-03-02~Bertram Aubrey~ITF-004~Intermediate Transfiguration
2019-03-02~Gwenog Jones~MKE-002~Magick Most Evile
2019-03-02~Marcus Belby~MMD-009~Important Modern Magical Discoveries
2019-03-02~Marietta Edgecombe~STS-006~Saucy Tricks for Tricky Sorts
2019-03-02~Montgomery sisters~HBV-001~Basic Hexes for the Busy and Vexed
2019-03-02~Seamus Finnigan~MMD-003~Important Modern Magical Discoveries
2019-03-02~Susan Bones~MKE-005~Magick Most Evile
2019-03-02~Susan Bones~WET-006~Great Wizarding Events of the Twentieth Century
2019-03-02~Theodore Nott~AMM-001~The Adventures of Martin Miggs, the Mad Muggle
2019-03-03~Cho Chang~LAB-005~The Life and Lies of Albus Dumbledore
2019-03-03~Ciceron Harkiss~EBA-001~Enchantment in Baking
2019-03-03~Daphne Greengrass~PDM-009~Practical Defensive Magic and Its Use Against the Dark Arts
2019-03-03~Lily Moon~SHG-005~Fowl or Foul? A Study of Hippogriff Brutality
2019-03-03~M. G. McGonagall~HBC-003~Handbook of Do-It-Yourself Broom Care
2019-03-03~Marietta Edgecombe~GHP-008~Gilderoy Lockhart's Guide to Household Pests
2019-03-03~Mary Macdonald~MEE-004~An Appraisal of Magical Education in Europe
2019-03-03~Montgomery sisters~DKG-002~From Egg to Inferno, A Dragon Keeper's Guide
2019-03-04~Angelina Johnson~STS-005~Saucy Tricks for Tricky Sorts
2019-03-04~Anthony Goldstein~LAB-002~The Life and Lies of Albus Dumbledore
2019-03-04~Bertram Aubrey~LAB-006~The Life and Lies of Albus Dumbledore
2019-03-04~Ciceron Harkiss~MAA-006~Common Magical Ailments and Afflictions
2019-03-04~Ciceron Harkiss~WTW-012~Where There's a Wand, There's a Way
2019-03-04~Ernest Macmillan~SPS-005~Spellman's Syllabary
2019-03-04~Garrick Ollivander~ITF-010~Intermediate Transfiguration
2019-03-04~Garrick Ollivander~WET-008~Great Wizarding Events of the Twentieth Century
2019-03-04~Harold Dingle~GTF-005~A Beginner's Guide to Transfiguration
2019-03-04~Laura Madley~RDW-001~A Study of Recent Developments in Wizardry
2019-03-04~Mandy Brocklehurst~FBW-004~Fantastic Beasts and Where to Find Them
2019-03-04~Natalie McDonald~FBW-005~Fantastic Beasts and Where to Find Them
2019-03-04~Oliver Wood~AMM-006~The Adventures of Martin Miggs, the Mad Muggle
2019-03-04~Rubeus Hagrid~WDS-005~Weird Wizarding Dilemmas and Their Solutions
2019-03-04~Viktor Krum~DKG-003~From Egg to Inferno, A Dragon Keeper's Guide
2019-03-05~B. Dunstan~WWW-002~Wanderings With Werewolves
2019-03-05~Cho Chang~VWV-003~Voyages With Vampires
2019-03-05~Davey Gudgeon~AAV-001~Asiatic Anti-Venoms
2019-03-05~Draco Malfoy~WET-004~Great Wizarding Events of the Twentieth Century
2019-03-05~Euan Abercrombie~WFT-004~Broken Balls: When Fortunes Turn Foul
2019-03-05~Geoffrey Hooper~SPS-006~Spellman's Syllabary
2019-03-05~Gwenog Jones~CYC-003~Charm Your Own Cheese
2019-03-05~Laverne de Montmorency~RDW-006~A Study of Recent Developments in Wizardry
2019-03-05~Marcus Belby~MNT-006~Notable Magical Names of Our Time
2019-03-05~Montgomery sisters~MAA-003~Common Magical Ailments and Afflictions
2019-03-05~Montgomery sisters~MAA-008~Common Magical Ailments and Afflictions
2019-03-05~Natalie McDonald~MEE-001~An Appraisal of Magical Education in Europe
2019-03-05~Padma Patil~DAO-005~The Dark Arts Outsmarted
2019-03-05~Padma Patil~HBV-011~Basic Hexes for the Busy and Vexed
2019-03-05~Susan Bones~MNT-002~Notable Magical Names of Our Time
2019-03-05~Viktor Krum~DDA-002~The Essential Defence Against the Dark Arts
2019-03-06~Angelina Johnson~PDM-002~Practical Defensive Magic and Its Use Against the Dark Arts
2019-03-06~Avery~SDA-007~Secrets of the Darkest Art
2019-03-06~Davey Gudgeon~MBM-003~Monster Book of Monsters
2019-03-06~Eddie Carmichael~AMM-012~The Adventures of Martin Miggs, the Mad Muggle
2019-03-06~Garrick Ollivander~ART-005~Ancient Runes Translation
2019-03-06~Geoffrey Hooper~DDA-009~The Essential Defence Against the Dark Arts
2019-03-06~Harold Potter~PDM-008~Practical Defensive Magic and Its Use Against the Dark Arts
2019-03-06~Laura Madley~DKG-005~From Egg to Inferno, A Dragon Keeper's Guide
2019-03-06~Luna Lovegood~DGB-006~Dragon Species of Great Britain and Ireland
2019-03-06~Luna Lovegood~MME-003~Magical Me
2019-03-06~Mandy Brocklehurst~GTF-002~A Beginner's Guide to Transfiguration
2019-03-06~Owen Cauldwell~GHP-005~Gilderoy Lockhart's Guide to Household Pests
2019-03-06~Owen Cauldwell~THH-008~The Healer's Helpmate
2019-03-06~Pansy Parkinson~ATF-004~Guide to Advanced Transfiguration
2019-03-06~Roger Davies~HOM-005~A History of Magic
2019-03-06~Stewart Ackerley~SDA-002~Secrets of the Darkest Art
2019-03-06~Susan Bones~MME-006~Magical Me
2019-03-07~Colin Creevey~SDA-003~Secrets of the Darkest Art
2019-03-07~Eddie Carmichael~DDA-001~The Essential Defence Against the Dark Arts
2019-03-07~Harold Dingle~HBC-001~Handbook of Do-It-Yourself Broom Care
2019-03-07~Hermione Jean Granger~MMD-002~Important Modern Magical Discoveries
2019-03-07~Justin Finch-Fletchley~SDA-012~Secrets of the Darkest Art
2019-03-07~Lavender Brown~THH-007~The Healer's Helpmate
2019-03-07~Laverne de Montmorency~HWH-005~Holidays With Hags
2019-03-07~M. G. McGonagall~EBA-004~Enchantment in Baking
2019-03-07~S. Fawcett~SDS-007~Self-Defensive Spellwork
2019-03-07~Stewart Ackerley~AMM-004~The Adventures of Martin Miggs, the Mad Muggle
2019-03-07~Viktor Krum~GHP-002~Gilderoy Lockhart's Guide to Household Pests
2019-03-07~Vincent Crabbe~CCC-001~A Compendium of Common Curses and Their Counter-Actions
2019-03-07~Vincent Crabbe~MNT-003~Notable Magical Names of Our Time
2019-03-08~Avery~MAA-004~Common Magical Ailments and Afflictions
2019-03-08~Davey Gudgeon~ITF-009~Intermediate Transfiguration
2019-03-08~Harold Dingle~STS-002~Saucy Tricks for Tricky Sorts
2019-03-08~Hermione Jean Granger~DGB-008~Dragon Species of Great Britain and Ireland
2019-03-08~M. G. McGonagall~MBM-004~Monster Book of Monsters
2019-03-08~Marcus Belby~DKG-001~From Egg to Inferno, A Dragon Keeper's Guide
2019-03-08~Marietta Edgecombe~AAV-006~Asiatic Anti-Venoms
2019-03-08~Montgomery sisters~FBW-003~Fantastic Beasts and Where to Find Them
2019-03-08~Owen Cauldwell~CCC-007~A Compendium of Common Curses and Their Counter-Actions
2019-03-08~Stewart Ackerley~FET-005~Flesh-Eating Trees of the World
2019-03-08~Vincent Crabbe~CCC-005~A Compendium of Common Curses and Their Counter-Actions
2019-03-09~B. Dunstan~MMD-007~Important Modern Magical Discoveries
2019-03-09~B. Dunstan~WWW-005~Wanderings With Werewolves
2019-03-09~Bertram Aubrey~AIC-001~Achievements in Charming
2019-03-09~Ciceron Harkiss~DDA-004~The Essential Defence Against the Dark Arts
2019-03-09~Davey Gudgeon~HWH-002~Holidays With Hags
2019-03-09~Draco Malfoy~APM-002~Advanced Potion-Making
2019-03-09~Draco Malfoy~DMT-001~Defensive Magical Theory
2019-03-09~Ernest Macmillan~LAB-007~The Life and Lies of Albus Dumbledore
2019-03-09~Garrick Ollivander~PDM-010~Practical Defensive Magic and Its Use Against the Dark Arts
2019-03-09~Geoffrey Hooper~WET-007~Great Wizarding Events of the Twentieth Century
2019-03-09~Gwenog Jones~WTW-011~Where There's a Wand, There's a Way
2019-03-09~Justin Finch-Fletchley~EBA-002~Enchantment in Baking
2019-03-09~Laura Madley~HBV-004~Basic Hexes for the Busy and Vexed
2019-03-09~Montgomery sisters~HWH-001~Holidays With Hags
2019-03-09~Natalie McDonald~MTH-002~Magical Theory
2019-03-09~Rubeus Hagrid~ATF-011~Guide to Advanced Transfiguration
2019-03-10~Daphne Greengrass~RDW-002~A Study of Recent Developments in Wizardry
2019-03-10~Eddie Carmichael~WFT-003~Broken Balls: When Fortunes Turn Foul
2019-03-10~Garrick Ollivander~STS-008~Saucy Tricks for Tricky Sorts
2019-03-10~Justin Finch-Fletchley~THH-010~The Healer's Helpmate
2019-03-10~Lavender Brown~GHP-011~Gilderoy Lockhart's Guide to Household Pests
2019-03-10~Mandy Brocklehurst~MME-005~Magical Me
2019-03-10~Oliver Wood~ITF-005~Intermediate Transfiguration
2019-03-10~Seamus Finnigan~FBW-002~Fantastic Beasts and Where to Find Them
2019-03-11~Angelina Johnson~MAA-005~Common Magical Ailments and Afflictions
2019-03-11~Anthony Goldstein~WWW-009~Wanderings With Werewolves
2019-03-11~Avery~GHP-004~Gilderoy Lockhart's Guide to Household Pests
2019-03-11~Avery~MEE-002~An Appraisal of Magical Education in Europe
2019-03-11~Bellatrix Lestrange~AAV-007~Asiatic Anti-Venoms
2019-03-11~Cho Chang~HBV-003~Basic Hexes for the Busy and Vexed
2019-03-11~Cho Chang~MMD-004~Important Modern Magical Discoveries
2019-03-11~Ciceron Harkiss~AAV-010~Asiatic Anti-Venoms
2019-03-11~Dennis Creevey~CCC-006~A Compendium of Common Curses and Their Counter-Actions
2019-03-11~Euan Abercrombie~ATF-001~Guide to Advanced Transfiguration
2019-03-11~Lily Moon~MEE-003~An Appraisal of Magical Education in Europe
2019-03-11~Marcus Belby~STS-007~Saucy Tricks for Tricky Sorts
2019-03-11~Oliver Wood~HBV-008~Basic Hexes for the Busy and Vexed
2019-03-11~Pansy Parkinson~MKE-004~Magick Most Evile
2019-03-11~Susan Bones~MME-008~Magical Me
2019-03-11~Viktor Krum~THH-002~The Healer's Helpmate
2019-03-11~Vincent Crabbe~ITF-007~Intermediate Transfiguration
2019-03-12~Anthony Goldstein~WET-002~Great Wizarding Events of the Twentieth Century
2019-03-12~Anthony Goldstein~WFT-002~Broken Balls: When Fortunes Turn Foul
2019-03-12~Ciceron Harkiss~DGB-011~Dragon Species of Great Britain and Ireland
2019-03-12~Eddie Carmichael~MMD-001~Important Modern Magical Discoveries
2019-03-12~Garrick Ollivander~DKG-004~From Egg to Inferno, A Dragon Keeper's Guide
2019-03-12~Lavender Brown~MNT-005~Notable Magical Names of Our Time
2019-03-12~Lily Moon~MMH-002~Modern Magical History
2019-03-12~Marcus Belby~ITF-008~Intermediate Transfiguration
2019-03-12~Mary Macdonald~AMM-013~The Adventures of Martin Miggs, the Mad Muggle
2019-03-12~Oliver Wood~WDS-006~Weird Wizarding Dilemmas and Their Solutions
2019-03-12~Rubeus Hagrid~SPS-002~Spellman's Syllabary
2019-03-12~S. Fawcett~SPS-011~Spellman's Syllabary
2019-03-12~Susan Bones~DKG-008~From Egg to Inferno, A Dragon Keeper's Guide
2019-03-12~Vincent Crabbe~CCC-009~A Compendium of Common Curses and Their Counter-Actions
2019-03-13~Avery~HBC-002~Handbook of Do-It-Yourself Broom Care
2019-03-13~Bertram Aubrey~VWV-001~Voyages With Vampires
2019-03-13~Cho Chang~HBV-007~Basic Hexes for the Busy and Vexed
2019-03-13~Ciceron Harkiss~DGB-007~Dragon Species of Great Britain and Ireland
2019-03-13~Ciceron Harkiss~MFM-002~One Minute Feasts - It's Magic!
2019-03-13~Colin Creevey~ATF-003~Guide to Advanced Transfiguration
2019-03-13~Colin Creevey~SPS-008~Spellman's Syllabary
2019-03-13~Daphne Greengrass~CYC-002~Charm Your Own Cheese
2019-03-13~Eddie Carmichael~AAV-009~Asiatic Anti-Venoms
2019-03-13~Gwenog Jones~SPS-003~Spellman's Syllabary
2019-03-13~Harold Dingle~SDA-005~Secrets of the Darkest Art
2019-03-13~Lavender Brown~SPS-009~Spellman's Syllabary
2019-03-13~Natalie McDonald~MFM-001~One Minute Feasts - It's Magic!
2019-03-13~Natalie McDonald~THH-005~The Healer's Helpmate
2019-03-13~Roger Davies~SPS-012~Spellman's Syllabary
2019-03-13~Rubeus Hagrid~SDA-011~Secrets of the Darkest Art
2019-03-13~Seamus Finnigan~MTH-008~Magical Theory
2019-03-13~Stewart Ackerley~MNT-001~Notable Magical Names of Our Time
2019-03-14~Angelina Johnson~WTW-004~Where There's a Wand, There's a Way
2019-03-14~Avery~SDS-012~Self-Defensive Spellwork
2019-03-14~Daphne Greengrass~VWV-007~Voyages With Vampires
2019-03-14~Davey Gudgeon~AAV-013~Asiatic Anti-Venoms
2019-03-14~Dennis Creevey~MTH-003~Magical Theory
2019-03-14~Gwenog Jones~AMM-009~The Adventures of Martin Miggs, the Mad Muggle
2019-03-14~Justin Finch-Fletchley~ITF-001~Intermediate Transfiguration
2019-03-14~Laura Madley~MMH-003~Modern Magical History
2019-03-14~Laura Madley~WFT-010~Broken Balls: When Fortunes Turn Foul
2019-03-14~Luna Lovegood~DGB-009~Dragon Species of Great Britain and Ireland
2019-03-14~Mandy Brocklehurst~MBM-006~Monster Book of Monsters
2019-03-14~Marcus Belby~AMM-008~The Adventures of Martin Miggs, the Mad Muggle
2019-03-14~Mary Macdonald~FET-001~Flesh-Eating Trees of the World
2019-03-14~Mary Macdonald~WTW-002~Where There's a Wand, There's a Way
2019-03-14~Natalie McDonald~FBW-007~Fantastic Beasts and Where to Find Them
2019-03-14~Terry Boot~GHP-003~Gilderoy Lockhart's Guide to Household Pests
2019-03-15~Bellatrix Lestrange~ITF-006~Intermediate Transfiguration
2019-03-15~Cho Chang~SDA-010~Secrets of the Darkest Art
2019-03-15~Ciceron Harkiss~CCC-010~A Compendium of Common Curses and Their Counter-Actions
2019-03-15~Ciceron Harkiss~MHF-001~One Thousand Magical Herbs and Fungi
2019-03-15~Colin Creevey~RDW-003~A Study of Recent Developments in Wizardry
2019-03-15~Davey Gudgeon~ATF-010~Guide to Advanced Transfiguration
2019-03-15~Ernest Macmillan~GHP-006~Gilderoy Lockhart's Guide to Household Pests
2019-03-15~Geoffrey Hooper~VWV-009~Voyages With Vampires
2019-03-15~Harold Dingle~SPS-010~Spellman's Syllabary
2019-03-15~Lavender Brown~GHP-013~Gilderoy Lockhart's Guide to Household Pests
2019-03-15~Lily Moon~STS-003~Saucy Tricks for Tricky Sorts
2019-03-15~Luna Lovegood~AIC-005~Achievements in Charming
2019-03-15~Mandy Brocklehurst~MAA-002~Common Magical Ailments and Afflictions
2019-03-15~Mary Macdonald~DDA-007~The Essential Defence Against the Dark Arts
2019-03-15~Padma Patil~SDS-005~Self-Defensive Spellwork
2019-03-15~Terry Boot~SHG-006~Fowl or Foul? A Study of Hippogriff Brutality
2019-03-15~Viktor Krum~WFT-006~Broken Balls: When Fortunes Turn Foul
2019-03-16~Angelina Johnson~AAV-011~Asiatic Anti-Venoms
2019-03-16~Anthony Goldstein~MME-007~Magical Me
2019-03-16~Anthony Goldstein~MTH-005~Magical Theory
2019-03-16~Avery~DGB-002~Dragon Species of Great Britain and Ireland
2019-03-16~Bellatrix Lestrange~WDS-001~Weird Wizarding Dilemmas and Their Solutions
2019-03-16~Cho Chang~WFT-001~Broken Balls: When Fortunes Turn Foul
2019-03-16~Daphne Greengrass~WTW-009~Where There's a Wand, There's a Way
2019-03-16~Euan Abercrombie~MTH-001~Magical Theory
2019-03-16~Garrick Ollivander~HWH-007~Holidays With Hags
2019-03-16~Justin Finch-Fletchley~MKE-008~Magick Most Evile
2019-03-16~Marcus Belby~HOM-002~A History of Magic
2019-03-16~Marcus Belby~HWH-004~Holidays With Hags
2019-03-16~Marcus Belby~SDS-001~Self-Defensive Spellwork
2019-03-16~Marietta Edgecombe~CCC-008~A Compendium of Common Curses and Their Counter-Actions
2019-03-16~Padma Patil~THH-009~The Healer's Helpmate
2019-03-16~Roger Davies~RDW-004~A Study of Recent Developments in Wizardry
2019-03-16~S. Fawcett~MHF-006~One Thousand Magical Herbs and Fungi
2019-03-16~S. Fawcett~PDM-004~Practical Defensive Magic and Its Use Against the Dark Arts
2019-03-16~Terry Boot~DDA-008~The Essential Defence Against the Dark Arts
2019-03-17~Daphne Greengrass~SDA-008~Secrets of the Darkest Art
2019-03-17~Draco Malfoy~ATF-008~Guide to Advanced Transfiguration
2019-03-17~Draco Malfoy~WDS-002~Weird Wizarding Dilemmas and Their Solutions
2019-03-17~Garrick Ollivander~SDA-006~Secrets of the Darkest Art
2019-03-17~Garrick Ollivander~WET-003~Great Wizarding Events of the Twentieth Century
2019-03-17~Gwenog Jones~GTF-004~A Beginner's Guide to Transfiguration
2019-03-17~Hermione Jean Granger~DGB-001~Dragon Species of Great Britain and Ireland
2019-03-17~Justin Finch-Fletchley~MMD-005~Important Modern Magical Discoveries
2019-03-17~Mandy Brocklehurst~MMH-004~Modern Magical History
2019-03-17~Marietta Edgecombe~DGB-010~Dragon Species of Great Britain and Ireland
2019-03-17~Pansy Parkinson~MKE-009~Magick Most Evile
2019-03-17~Roger Davies~WWW-008~Wanderings With Werewolves
2019-03-17~S. Fawcett~GTF-003~A Beginner's Guide to Transfiguration
2019-03-17~Stewart Ackerley~WFT-008~Broken Balls: When Fortunes Turn Foul
2019-03-17~Viktor Krum~WFT-007~Broken Balls: When Fortunes Turn Foul
2019-03-18~Angelina Johnson~HOM-010~A History of Magic
2019-03-18~Ernest Macmillan~HBV-009~Basic Hexes for the Busy and Vexed
2019-03-18~Euan Abercrombie~LAB-004~The Life and Lies of Albus Dumbledore
2019-03-18~Gwenog Jones~WTW-006~Where There's a Wand, There's a Way
2019-03-18~Harold Potter~AAV-003~Asiatic Anti-Venoms
2019-03-18~Harold Potter~SDS-002~Self-Defensive Spellwork
2019-03-18~Laverne de Montmorency~MDP-005~Magical Drafts and Potions
2019-03-18~Marcus Belby~MHF-003~One Thousand Magical Herbs and Fungi
2019-03-18~Marcus Belby~SDS-008~Self-Defensive Spellwork
2019-03-18~Rubeus Hagrid~DKG-006~From Egg to Inferno, A Dragon Keeper's Guide
2019-03-18~Viktor Krum~GHP-007~Gilderoy Lockhart's Guide to Household Pests
2019-03-18~Viktor Krum~VWV-004~Voyages With Vampires
2019-03-19~Angelina Johnson~AIC-004~Achievements in Charming
2019-03-19~Colin Creevey~MTH-007~Magical Theory
2019-03-19~Daphne Greengrass~HOM-007~A History of Magic
2019-03-19~Draco Malfoy~ATF-002~Guide to Advanced Transfiguration
2019-03-19~Ernest Macmillan~DDA-010~The Essential Defence Against the Dark Arts
2019-03-19~Geoffrey Hooper~CYC-001~Charm Your Own Cheese
2019-03-19~Geoffrey Hooper~HOM-009~A History of Magic
2019-03-19~Harold Dingle~DAO-004~The Dark Arts Outsmarted
2019-03-19~Lily Moon~HBV-012~Basic Hexes for the Busy and Vexed
2019-03-19~Luna Lovegood~MFM-005~One Minute Feasts - It's Magic!
2019-03-19~Marietta Edgecombe~AMM-011~The Adventures of Martin Miggs, the Mad Muggle
2019-03-19~Montgomery sisters~ATF-007~Guide to Advanced Transfiguration
2019-03-19~Natalie McDonald~MMD-008~Important Modern Magical Discoveries
2019-03-19~Natalie McDonald~WDS-007~Weird Wizarding Dilemmas and Their Solutions
2019-03-19~Stewart Ackerley~FBW-001~Fantastic Beasts and Where to Find Them
2019-03-20~Anthony Goldstein~SHG-004~Fowl or Foul? A Study of Hippogriff Brutality
2019-03-20~Colin Creevey~AMM-002~The Adventures of Martin Miggs, the Mad Muggle
2019-03-20~Davey Gudgeon~DDA-003~The Essential Defence Against the Dark Arts
2019-03-20~Harold Potter~PDM-003~Practical Defensive Magic and Its Use Against the Dark Arts
2019-03-20~Lily Moon~MMH-006~Modern Magical History
2019-03-20~M. G. McGonagall~GHP-009~Gilderoy Lockhart's Guide to Household Pests
2019-03-20~Marietta Edgecombe~DAO-003~The Dark Arts Outsmarted
2019-03-20~Owen Cauldwell~MAA-001~Common Magical Ailments and Afflictions
2019-03-20~Roger Davies~LAB-001~The Life and Lies of Albus Dumbledore
2019-03-20~Stewart Ackerley~AAV-008~Asiatic Anti-Venoms
2019-03-20~Stewart Ackerley~MAA-007~Common Magical Ailments and Afflictions
2019-03-20~Terry Boot~AAV-002~Asiatic Anti-Venoms
2019-03-20~Terry Boot~CCC-002~A Compendium of Common Curses and Their Counter-Actions
2019-03-20~Terry Boot~DGB-004~Dragon Species of Great Britain and Ireland
2019-03-21~Cho Chang~HBV-006~Basic Hexes for the Busy and Vexed
2019-03-21~Colin Creevey~DDA-005~The Essential Defence Against the Dark Arts
2019-03-21~Daphne Greengrass~GHP-010~Gilderoy Lockhart's Guide to Household Pests
2019-03-21~Ernest Macmillan~HOM-006~A History of Magic
2019-03-21~Gwenog Jones~HOM-004~A History of Magic
2019-03-21~Laura Madley~PDM-006~Practical Defensive Magic and Its Use Against the Dark Arts
2019-03-21~Laura Madley~THH-006~The Healer's Helpmate
2019-03-21~Lavender Brown~WWW-003~Wanderings With Werewolves
2019-03-21~Laverne de Montmorency~APM-001~Advanced Potion-Making
2019-03-21~Luna Lovegood~MTH-004~Magical Theory
2019-03-21~M. G. McGonagall~WTW-003~Where There's a Wand, There's a Way
2019-03-21~Mandy Brocklehurst~AIC-003~Achievements in Charming
2019-03-21~Marcus Belby~SHG-002~Fowl or Foul? A Study of Hippogriff Brutality
2019-03-21~Marietta Edgecombe~FET-006~Flesh-Eating Trees of the World
2019-03-21~Rubeus Hagrid~SDA-001~Secrets of the Darkest Art
2019-03-21~S. Fawcett~MBM-001~Monster Book of Monsters
2019-03-21~Stewart Ackerley~SDA-004~Secrets of the Darkest Art
2019-03-21~Terry Boot~FET-004~Flesh-Eating Trees of the World
2019-03-22~Angelina Johnson~HOM-003~A History of Magic
2019-03-22~B. Dunstan~MFM-003~One Minute Feasts - It's Magic!
2019-03-22~Ciceron Harkiss~MDP-002~Magical Drafts and Potions
2019-03-22~Ernest Macmillan~MFM-004~One Minute Feasts - It's Magic!
2019-03-22~Ernest Macmillan~WTW-001~Where There's a Wand, There's a Way
2019-03-22~Euan Abercrombie~THH-011~The Healer's Helpmate
2019-03-22~Gwenog Jones~WWW-004~Wanderings With Werewolves
2019-03-22~Harold Dingle~MHF-002~One Thousand Magical Herbs and Fungi
2019-03-22~Hermione Jean Granger~WWW-007~Wanderings With Werewolves
2019-03-22~Marietta Edgecombe~VWV-008~Voyages With Vampires
2019-03-22~Marietta Edgecombe~WWW-001~Wanderings With Werewolves
2019-03-22~Vincent Crabbe~FET-002~Flesh-Eating Trees of the World
2019-03-23~Bertram Aubrey~VWV-006~Voyages With Vampires
2019-03-23~Cho Chang~SPS-001~Spellman's Syllabary
2019-03-23~Colin Creevey~MME-004~Magical Me
2019-03-23~Draco Malfoy~WFT-009~Broken Balls: When Fortunes Turn Foul
2019-03-23~Ernest Macmillan~WDS-003~Weird Wizarding Dilemmas and Their Solutions
2019-03-23~Lavender Brown~ATF-006~Guide to Advanced Transfiguration
2019-03-23~Marietta Edgecombe~HWH-006~Holidays With Hags
2019-03-23~Marietta Edgecombe~MBM-002~Monster Book of Monsters
2019-03-23~Mary Macdonald~DGB-005~Dragon Species of Great Britain and Ireland
2019-03-23~Mary Macdonald~RDW-005~A Study of Recent Developments in Wizardry
2019-03-23~Owen Cauldwell~HOM-011~A History of Magic
2019-03-24~Ciceron Harkiss~MMH-007~Modern Magical History
2019-03-24~Davey Gudgeon~MKE-010~Magick Most Evile
2019-03-24~Garrick Ollivander~AMM-010~The Adventures of Martin Miggs, the Mad Muggle
2019-03-24~Laura Madley~MTH-009~Magical Theory
2019-03-24~Mary Macdonald~AAV-005~Asiatic Anti-Venoms
2019-03-24~Oliver Wood~DAO-001~The Dark Arts Outsmarted
2019-03-24~Oliver Wood~HBV-010~Basic Hexes for the Busy and Vexed
2019-03-24~Stewart Ackerley~ART-006~Ancient Runes Translation
2019-03-24~Stewart Ackerley~DDA-006~The Essential Defence Against the Dark Arts
2019-03-24~Theodore Nott~MMD-010~Important Modern Magical Discoveries
2019-03-25~Avery~MBM-005~Monster Book of Monsters
2019-03-25~B. Dunstan~ART-001~Ancient Runes Translation
2019-03-25~B. Dunstan~HBV-013~Basic Hexes for the Busy and Vexed
2019-03-25~Bellatrix Lestrange~HOM-001~A History of Magic
2019-03-25~Euan Abercrombie~DGB-013~Dragon Species of Great Britain and Ireland
2019-03-25~Harold Dingle~WTW-005~Where There's a Wand, There's a Way
2019-03-25~Harold Potter~APM-003~Advanced Potion-Making
2019-03-25~Laverne de Montmorency~CCC-004~A Compendium of Common Curses and Their Counter-Actions
2019-03-25~Montgomery sisters~WET-005~Great Wizarding Events of the Twentieth Century
2019-03-25~Padma Patil~AAV-012~Asiatic Anti-Venoms
2019-03-25~Roger Davies~MMH-005~Modern Magical History
2019-03-25~Seamus Finnigan~MDP-004~Magical Drafts and Potions
2019-03-26~Angelina Johnson~SDS-011~Self-Defensive Spellwork
2019-03-26~Avery~WWW-010~Wanderings With Werewolves
2019-03-26~Colin Creevey~AMM-005~The Adventures of Martin Miggs, the Mad Muggle
2019-03-26~Draco Malfoy~AAV-004~Asiatic Anti-Venoms
2019-03-26~Euan Abercrombie~MTH-006~Magical Theory
2019-03-26~M. G. McGonagall~WET-001~Great Wizarding Events of the Twentieth Century
2019-03-26~Owen Cauldwell~GHP-012~Gilderoy Lockhart's Guide to Household Pests
2019-03-26~Roger Davies~ITF-002~Intermediate Transfiguration
2019-03-26~Theodore Nott~FET-003~Flesh-Eating Trees of the World
'''

#Program

def borrowers_input(b):
    x=input()
    while x!='Checkouts':
        x=x.split('~')
        b.append(x)
        x=input()

def checkouts_input(c):
    x=input()
    while x!='EndOfInput':
        x=x.split('~')
        c.append(x)
        x=input()

def output():
    global books,borrower,checkout
    date=[]
    uname=[]
    name=[]
    Anum=[]
    title=[]
    for i in range(0,len(checkout)):
        date.append(checkout[i][2])

    for i in range(0,len(checkout)):
        uname.append(checkout[i][0])

    for i in range(0,len(uname)):
        for j in range(0,len(borrower)):
            if(uname[i] == borrower[j][0]):
                name.append(borrower[j][1])

    for i in range(0,len(checkout)):
        Anum.append(checkout[i][1])

    for i in range(0,len(Anum)):
        for j in range(0,len(books)):
            if(Anum[i] == books[j][0]):
                title.append(books[j][1])

    final=[]
    for i in range(0,len(checkout)):
        final.append(date[i]+'~'+name[i]+'~'+Anum[i]+'~'+title[i])
    final.sort()
    for i in range(0,len(final)):
        print(final[i])


books=[]
borrower=[]
checkout=[]
x=input()
x=input()
while x!='Borrowers':
    x=x.split('~')
    books.append(x)
    x=input()
borrowers_input(borrower)
borrower.sort()
checkouts_input(checkout)
output()
