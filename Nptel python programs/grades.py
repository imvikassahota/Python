'''
The academic office at the Hogwarts School of Witchcraft and Wizardry has compiled data about students' grades. The data is provided as text from standard input in three parts: information about courses, information about students and information about grades. Each part has a specific line format, described below..

Information about courses
Line format: Course Code~Course Name~Semester~Year~Instructor
Information about students
Line format: Roll Number~Full Name
Information about grades
Line format: Course Code~Semester~Year~Roll Number~Grade
The possible grades are A, AB, B, BC, C, CD, D with corresponding grade points 10, 9, 8, 7, 6, 5 and 4. The grade point average of a student is the sum of his/her grade points divided by the number of courses. For instance, if a student has taken two courses with grades A and C, the grade point average is 8 = (10+6)÷2. If a student has not completed any courses, the grade point average is defined to be 0.

You may assume that the data is internally consistent. For every grade, there is a corresponding course code and roll number in the input data.

Each section of the input starts with a line containing a single keyword. The first section begins with a line containing Courses. The second section begins with a line containing Students. The third section begins with a line containing Grades. The end of the input is marked by a line containing EndOfInput.

Write a Python program to read the data as described above and print out a line listing the grade point average for each student in the following format:

Roll Number~Full Name~Grade Point Average
Your output should be sorted by Roll Number. The grade point average should be rounded off to 2 digits after the decimal point. Use the built-in function round().

Here is a sample input and its corresponding output.

Sample Input

Courses
TRAN~Transfiguration~1~2011-2012~Minerva McGonagall
CHAR~Charms~1~2011-2012~Filius Flitwick
Students
SLY2301~Hannah Abbott
SLY2302~Euan Abercrombie
SLY2303~Stewart Ackerley
SLY2304~Bertram Aubrey
SLY2305~Avery
SLY2306~Malcolm Baddock
SLY2307~Marcus Belby
SLY2308~Katie Bell
SLY2309~Sirius Orion Black
Grades
TRAN~1~2011-2012~SLY2301~AB
TRAN~1~2011-2012~SLY2302~B
TRAN~1~2011-2012~SLY2303~B
TRAN~1~2011-2012~SLY2305~A
TRAN~1~2011-2012~SLY2306~BC
TRAN~1~2011-2012~SLY2308~A
TRAN~1~2011-2012~SLY2309~AB
CHAR~1~2011-2012~SLY2301~A
CHAR~1~2011-2012~SLY2302~BC
CHAR~1~2011-2012~SLY2303~B
CHAR~1~2011-2012~SLY2305~BC
CHAR~1~2011-2012~SLY2306~C
CHAR~1~2011-2012~SLY2307~B
CHAR~1~2011-2012~SLY2308~AB
EndOfInput
Sample Input

SLY2301~Hannah Abbott~9.5
SLY2302~Euan Abercrombie~7.5
SLY2303~Stewart Ackerley~8.0
SLY2304~Bertram Aubrey~0
SLY2305~Avery~8.5
SLY2306~Malcolm Baddock~6.5
SLY2307~Marcus Belby~8.0
SLY2308~Katie Bell~9.5
SLY2309~Sirius Orion Black~9.0
Sample Test Cases
Input	Output
Test Case 1	
Courses
TRAN~Transfiguration~1~2011-2012~Minerva McGonagall
CHAR~Charms~1~2011-2012~Filius Flitwick
Students
SLY2301~Hannah Abbott
SLY2302~Euan Abercrombie
SLY2303~Stewart Ackerley
SLY2304~Bertram Aubrey
SLY2305~Avery
SLY2306~Malcolm Baddock
SLY2307~Marcus Belby
SLY2308~Katie Bell
SLY2309~Sirius Orion Black
Grades
TRAN~1~2011-2012~SLY2301~AB
TRAN~1~2011-2012~SLY2302~B
TRAN~1~2011-2012~SLY2303~B
TRAN~1~2011-2012~SLY2305~A
TRAN~1~2011-2012~SLY2306~BC
TRAN~1~2011-2012~SLY2308~A
TRAN~1~2011-2012~SLY2309~AB
CHAR~1~2011-2012~SLY2301~A
CHAR~1~2011-2012~SLY2302~BC
CHAR~1~2011-2012~SLY2303~B
CHAR~1~2011-2012~SLY2305~BC
CHAR~1~2011-2012~SLY2306~C
CHAR~1~2011-2012~SLY2307~B
CHAR~1~2011-2012~SLY2308~AB
EndOfInput
SLY2301~Hannah Abbott~9.5
SLY2302~Euan Abercrombie~7.5
SLY2303~Stewart Ackerley~8.0
SLY2304~Bertram Aubrey~0
SLY2305~Avery~8.5
SLY2306~Malcolm Baddock~6.5
SLY2307~Marcus Belby~8.0
SLY2308~Katie Bell~9.5
SLY2309~Sirius Orion Black~9.0
Test Case 2	
Courses
POT~Potions~1~2011-2012~Severus Snape
DADA~Defence Against the Dark ARTS~1~2011-2012~Gilderoy Lockhart 
Students
RAV4309~Angelina Johnson
HUF7201~Gwenog Jones
GRF9110~Parvati Patil
RAV4308~Olive Hornby
Grades
POT~1~2011-2012~RAV4308~C
POT~1~2011-2012~RAV4309~B
POT~1~2011-2012~GRF9110~A
EndOfInput
GRF9110~Parvati Patil~10.0
HUF7201~Gwenog Jones~0
RAV4308~Olive Hornby~6.0
RAV4309~Angelina Johnson~8.0
Test Case 3	
Courses
TRAN~Transfiguration~1~2011-2012~Minerva McGonagall
CHAR~Charms~1~2011-2012~Filius Flitwick
Students
SLY2301~Hannah Abbott
SLY2302~Euan Abercrombie
SLY2303~Stewart Ackerley
SLY2304~Bertram Aubrey
SLY2305~Avery
SLY2306~Malcolm Baddock
SLY2307~Marcus Belby
SLY2308~Katie Bell
SLY2309~Sirius Orion Black
Grades
TRAN~1~2011-2012~SLY2301~AB
TRAN~1~2011-2012~SLY2302~B
TRAN~1~2011-2012~SLY2303~B
TRAN~1~2011-2012~SLY2305~A
TRAN~1~2011-2012~SLY2306~BC
TRAN~1~2011-2012~SLY2308~A
TRAN~1~2011-2012~SLY2309~AB
CHAR~1~2011-2012~SLY2301~A
CHAR~1~2011-2012~SLY2302~BC
CHAR~1~2011-2012~SLY2303~B
CHAR~1~2011-2012~SLY2305~BC
CHAR~1~2011-2012~SLY2306~C
CHAR~1~2011-2012~SLY2307~B
CHAR~1~2011-2012~SLY2308~AB
EndOfInput
SLY2301~Hannah Abbott~9.5
SLY2302~Euan Abercrombie~7.5
SLY2303~Stewart Ackerley~8.0
SLY2304~Bertram Aubrey~0
SLY2305~Avery~8.5
SLY2306~Malcolm Baddock~6.5
SLY2307~Marcus Belby~8.0
SLY2308~Katie Bell~9.5
SLY2309~Sirius Orion Black~9.0
Test Case 4	
Courses
POT~Potions~1~2011-2012~Severus Snape
DADA~Defence Against the Dark ARTS~1~2011-2012~Gilderoy Lockhart 
Students
RAV4309~Angelina Johnson
HUF7201~Gwenog Jones
GRF9110~Parvati Patil
RAV4308~Olive Hornby
Grades
POT~1~2011-2012~RAV4308~C
POT~1~2011-2012~RAV4309~B
POT~1~2011-2012~GRF9110~A
EndOfInput
GRF9110~Parvati Patil~10.0
HUF7201~Gwenog Jones~0
RAV4308~Olive Hornby~6.0
RAV4309~Angelina Johnson~8.0
Test Case 5	
Courses
DADA~Defence Against the Dark ARTS~1~2011-2012~Gilderoy Lockhart 
HOM~History of Magic~1~2011-2012~Cuthbert Binns
ARTH~Arithmancy~1~2011-2012~Septima Vector
Students
SLY2301~Hannah Abbott
SLY2302~Euan Abercrombie
SLY2303~Stewart Ackerley
SLY2304~Bertram Aubrey
SLY2305~Avery
SLY2306~Malcolm Baddock
SLY2307~Marcus Belby
SLY2308~Katie Bell
SLY2309~Sirius Orion Black
SLY2310~Melinda Bobbin
SLY2311~Susan Bones
SLY2312~Terry Boot
SLY2313~Eleanor Branstone
SLY2315~Mandy Brocklehurst
SLY2316~Lavender Brown
SLY2317~Millicent Bulstrode
SLY2318~S. Capper
SLY2319~Eddie Carmichael
SLY2320~Owen Cauldwell
SLY2321~Cho Chang
SLY2323~Michael Corner
GRF3701~Vincent Crabbe
GRF3702~Colin Creevey
GRF3703~Dennis Creevey
GRF3704~Roger Davies
GRF3705~Cedric Diggory
GRF3706~Harold Dingle
GRF3707~Emma Dobbs
GRF3708~J. Dorny
GRF3709~B. Dunstan
GRF3710~Marietta Edgecombe
GRF3711~S. Fawcett
GRF3712~Justin Finch-Fletchley
GRF3713~Seamus Finnigan
GRF3714~Vicky Frobisher
GRF3715~Basil Fronsac
GRF3716~Anthony Goldstein
GRF3717~Gregory Goyle
RAV4301~Hermione Jean Granger
RAV4302~Daphne Greengrass
RAV4303~Gellert Grindelwald
RAV4304~Davey Gudgeon
RAV4305~Rubeus Hagrid
RAV4306~Ciceron Harkiss
RAV4307~Geoffrey Hooper
RAV4308~Olive Hornby
RAV4309~Angelina Johnson
HUF7201~Gwenog Jones
HUF7202~Lee Jordan
HUF7203~Bertha Jorkins
HUF7204~Viktor Krum
HUF7206~Bellatrix Lestrange
HUF7207~Neville Longbottom
HUF7208~Luna Lovegood
HUF7209~Remus John Lupin
HUF7210~Mary Macdonald
RAV5901~Oliver Wood
RAV5902~Isobel MacDougal
RAV5903~Morag MacDougal
RAV5904~Ernest Macmillan
RAV5905~Laura Madley
RAV5906~Draco Malfoy
RAV5907~Natalie McDonald
RAV5908~M. G. McGonagall
GRF9101~Eloise Midgen
GRF9102~Laverne de Montmorency
GRF9103~Montgomery sisters
GRF9104~Lily Moon
GRF9105~Harold Potter
GRF9106~Theodore Nott
GRF9107~Garrick Ollivander
GRF9108~Pansy Parkinson
GRF9109~Padma Patil
GRF9110~Parvati Patil
Grades
HOM~1~2011-2012~SLY2301~AB
HOM~1~2011-2012~SLY2302~C
HOM~1~2011-2012~SLY2303~AB
HOM~1~2011-2012~SLY2304~BC
HOM~1~2011-2012~SLY2305~CD
HOM~1~2011-2012~SLY2306~BC
HOM~1~2011-2012~SLY2307~A
HOM~1~2011-2012~SLY2308~BC
HOM~1~2011-2012~SLY2309~AB
HOM~1~2011-2012~SLY2310~A
HOM~1~2011-2012~SLY2311~BC
HOM~1~2011-2012~SLY2312~CD
HOM~1~2011-2012~SLY2313~C
HOM~1~2011-2012~SLY2315~BC
HOM~1~2011-2012~SLY2316~BC
DADA~1~2011-2012~SLY2319~BC
DADA~1~2011-2012~SLY2320~B
DADA~1~2011-2012~SLY2321~C
DADA~1~2011-2012~SLY2323~D
HOM~1~2011-2012~SLY2317~D
HOM~1~2011-2012~SLY2323~A
HOM~1~2011-2012~RAV4301~AB
HOM~1~2011-2012~RAV4302~BC
HOM~1~2011-2012~RAV4303~AB
HOM~1~2011-2012~RAV4304~AB
HOM~1~2011-2012~RAV4305~BC
HOM~1~2011-2012~RAV4306~BC
HOM~1~2011-2012~RAV4307~AB
HOM~1~2011-2012~RAV4308~C
HOM~1~2011-2012~RAV4309~BC
HOM~1~2011-2012~GRF3717~CD
ARTH~1~2011-2012~RAV4301~B
ARTH~1~2011-2012~RAV4302~AB
ARTH~1~2011-2012~RAV4303~A
ARTH~1~2011-2012~RAV4304~AB
HOM~1~2011-2012~SLY2318~CD
HOM~1~2011-2012~SLY2319~CD
HOM~1~2011-2012~SLY2320~AB
HOM~1~2011-2012~SLY2321~AB
ARTH~1~2011-2012~RAV4305~BC
ARTH~1~2011-2012~RAV4306~B
ARTH~1~2011-2012~RAV4307~B
DADA~1~2011-2012~SLY2301~B
DADA~1~2011-2012~SLY2302~AB
DADA~1~2011-2012~SLY2303~C
DADA~1~2011-2012~SLY2304~BC
DADA~1~2011-2012~SLY2305~A
DADA~1~2011-2012~SLY2306~BC
DADA~1~2011-2012~SLY2307~C
DADA~1~2011-2012~SLY2308~CD
DADA~1~2011-2012~SLY2309~B
DADA~1~2011-2012~SLY2310~AB
DADA~1~2011-2012~SLY2311~A
DADA~1~2011-2012~SLY2312~BC
DADA~1~2011-2012~SLY2313~B
DADA~1~2011-2012~SLY2315~C
DADA~1~2011-2012~SLY2316~CD
DADA~1~2011-2012~SLY2317~B
DADA~1~2011-2012~SLY2318~AB
ARTH~1~2011-2012~RAV4308~B
ARTH~1~2011-2012~RAV4309~B
EndOfInput
GRF3701~Vincent Crabbe~0
GRF3702~Colin Creevey~0
GRF3703~Dennis Creevey~0
GRF3704~Roger Davies~0
GRF3705~Cedric Diggory~0
GRF3706~Harold Dingle~0
GRF3707~Emma Dobbs~0
GRF3708~J. Dorny~0
GRF3709~B. Dunstan~0
GRF3710~Marietta Edgecombe~0
GRF3711~S. Fawcett~0
GRF3712~Justin Finch-Fletchley~0
GRF3713~Seamus Finnigan~0
GRF3714~Vicky Frobisher~0
GRF3715~Basil Fronsac~0
GRF3716~Anthony Goldstein~0
GRF3717~Gregory Goyle~5.0
GRF9101~Eloise Midgen~0
GRF9102~Laverne de Montmorency~0
GRF9103~Montgomery sisters~0
GRF9104~Lily Moon~0
GRF9105~Harold Potter~0
GRF9106~Theodore Nott~0
GRF9107~Garrick Ollivander~0
GRF9108~Pansy Parkinson~0
GRF9109~Padma Patil~0
GRF9110~Parvati Patil~0
HUF7201~Gwenog Jones~0
HUF7202~Lee Jordan~0
HUF7203~Bertha Jorkins~0
HUF7204~Viktor Krum~0
HUF7206~Bellatrix Lestrange~0
HUF7207~Neville Longbottom~0
HUF7208~Luna Lovegood~0
HUF7209~Remus John Lupin~0
HUF7210~Mary Macdonald~0
RAV4301~Hermione Jean Granger~8.5
RAV4302~Daphne Greengrass~8.0
RAV4303~Gellert Grindelwald~9.5
RAV4304~Davey Gudgeon~9.0
RAV4305~Rubeus Hagrid~7.0
RAV4306~Ciceron Harkiss~7.5
RAV4307~Geoffrey Hooper~8.5
RAV4308~Olive Hornby~7.0
RAV4309~Angelina Johnson~7.5
RAV5901~Oliver Wood~0
RAV5902~Isobel MacDougal~0
RAV5903~Morag MacDougal~0
RAV5904~Ernest Macmillan~0
RAV5905~Laura Madley~0
RAV5906~Draco Malfoy~0
RAV5907~Natalie McDonald~0
RAV5908~M. G. McGonagall~0
SLY2301~Hannah Abbott~8.5
SLY2302~Euan Abercrombie~7.5
SLY2303~Stewart Ackerley~7.5
SLY2304~Bertram Aubrey~7.0
SLY2305~Avery~7.5
SLY2306~Malcolm Baddock~7.0
SLY2307~Marcus Belby~8.0
SLY2308~Katie Bell~6.0
SLY2309~Sirius Orion Black~8.5
SLY2310~Melinda Bobbin~9.5
SLY2311~Susan Bones~8.5
SLY2312~Terry Boot~6.0
SLY2313~Eleanor Branstone~7.0
SLY2315~Mandy Brocklehurst~6.5
SLY2316~Lavender Brown~6.0
SLY2317~Millicent Bulstrode~6.0
SLY2318~S. Capper~7.0
SLY2319~Eddie Carmichael~6.0
SLY2320~Owen Cauldwell~8.5
SLY2321~Cho Chang~7.5
SLY2323~Michael Corner~7.0
'''

#Program

def stu_input(l):
    x=input()
    while x!='Grades':
        x=x.split('~')
        x.append(0)   # appending 0 as the grade marks 
        l.append(x)
        x=input()
# function to take the grades of the students
def inp_grade(grade):
    x=input()
    while x!='EndOfInput':
        x=x.split('~')
        x=x[len(x)-2:]
        grade.append(x)
        x=input()
def com(x):
    if x=='A':
        return 10
    elif x=='AB':
        return 9
    elif x=='B':
        return 8
    elif x=='BC':
        return 7
    elif x=='C':
        return 6
    elif x=='CD':
        return 5
    else:
        return 4
def cal():
    global li,grade
    for i in li:   # i is a list containg the name and roll of a student
        j=0
        sum=0
        while j<len(grade):
            if i[0]==grade[j][0] :     # if the roll matchs
                sum=sum+com(grade[j][1])
                grade.pop(j)
                i[2]+=1
            else :
                j+=1
        if sum!=0 :
            i[2]=round(sum/i[2],2)
        print(i[0]+'~'+i[1]+'~',i[2],sep='')
# main function starts here
li=[]              # the list where the answer will be stored 
grade=[]
x=input()
while x!='Students':           # first inputs are not required
    x=input()
stu_input(li)
li.sort()
inp_grade(grade)
cal()
