import pandas as ps
import streamlit as st
import plotly.express as ex
import plotly.graph_objects as go
from plotly.subplots import make_subplots as ms
raw_file = ps.read_csv(r"C:\Users\6327105\Downloads\Employee-Attrition - Employee-Attrition.csv")

st.set_page_config('Guvi project 3')
st.header("Hi user welcome to my site")
st.write('_This is all about the employee attrition and there details_')
Name = st.text_input('Hi user what is your name')
if Name:
    st.write(f'Hi {Name} how is your day! 😊')
    st.write('Let"s move on to the topic')
    st.write(f'\n')
    st.write(f'\n')
    st.write(f'\n')
    st.write(f'🔽')
    st.write(f'🔽')
    st.write(f'🔽')
    st.write(f'🔽')

#1
#Age
cols = ['EmployeeCount','Over18','StandardHours']
AA = raw_file.drop(columns=(cols),axis=1)
#print(AA.columns)
for i in AA.columns:
    if AA[i].dtype == 'object':
        AA[i] = ps.factorize(AA[i])[0]+1

#use to calculate the age distribution and its correlation with other factors like job satisfaction, attrition, or performance
col1 = ['Age','JobSatisfaction','PerformanceRating','Attrition']
#print(AA[col].corr())

#print(raw_file['Attrition'].value_counts(normalize=True))
if Name:
    age_filter = AA['Age'].unique().tolist()
    select_age = st.multiselect(f'select the age from the list so view the correlation of employee',age_filter)
    if select_age:
        filters = AA[AA['Age'].isin(select_age)]
        st.write(filters)
        st.write('Correlation for the age')
        st.write(filters[col1].corr())


#2
#Attrition
#Whether the employee left the company (1) or stayed (0).
#print(raw_file['Attrition'].value_counts())
#print(raw_file.columns)

BB = raw_file.copy()

for j in BB.columns:
    if BB[j].dtype == 'object':
        BB[j] = ps.factorize(BB[j])[0]+1
#This is used to calculate the factors influencing attrition
#print(BB.corr()['Attrition'].sort_values(ascending=False).head(5))

if Name:
    col2 = BB.columns
    select_attrition = st.multiselect(f'Kindly select the column you want to see the corr',col2)
    if select_attrition:
        st.write('Correlation for the attrition in all the columns')
        filter_attrition = BB[BB['Attrition'].isin(select_attrition)]
        st.write(filter_attrition[col2].corr())

    
#3
CC = raw_file.copy()
#this is used to show the number of person used to travel or not
#print(CC['BusinessTravel'].value_counts())

#this is used to calculate the travel pattern the impact in the work daily life
for k in CC.columns:
    if CC[k].dtype == 'object':
        CC[k] = ps.factorize(CC[k])[0]+1
col3 = ['WorkLifeBalance','PerformanceRating','JobSatisfaction']

valid_col = [c for c in col3 if c in CC.columns]
#print(CC[valid_col].corr())
if Name :
    filter_travel = CC['BusinessTravel'].unique().tolist()
    select_travel = st.multiselect(f'select the option so see the corr of business travel',filter_travel)
    if select_travel:
        filters3 = CC[CC['BusinessTravel'].isin(select_travel)]
        st.write(filters3[col3].corr())

#4
#daily rate of pay
DD = raw_file.copy()
#pay scale and its relationship with other factors like job satisfaction, performance, or attrition.

col4= ['JobSatisfaction','PerformanceRating','Attrition']

for l in DD.columns:
    if DD[l].dtype == 'object':
        DD[l] = ps.factorize(DD[l])[0]+1

valid_col1 = [d for d in DD if d in DD.columns]
#print(DD.corr()['DailyRate'][['JobSatisfaction','PerformanceRating','Attrition']])
if Name:
    filter_Dailyrate = DD['DailyRate'].unique().tolist()
    select_dailyRate = st.multiselect(f'select the rate to check the corr of jobsatis , perf , attrition',filter_Dailyrate)

    if select_dailyRate:
        filter_dailyrate = DD[DD['DailyRate'].isin(select_dailyRate)]
        st.write(filter_dailyrate[col4].corr())

#5
#department
EE = raw_file.copy()

EE['Attrition'] = EE['Attrition'].map({'Yes' :1,'No' :0})
EE['Department'] = EE['Department'].map({'Sales':1,'Research & Development':2,'Human Resources':3})
attrition_dept = EE.groupby('Department')['Attrition'].mean().reset_index()

#print(attrition_dept)

col5 = ['Attrition','JobSatisfaction']

#print(EE.corr()['Department'][['Attrition','JobSatisfaction']])
if Name:
    depart = EE['Department'].unique().tolist()
    select_depart = st.multiselect(f'select to view the corr of department field',depart)

    if select_depart:
        filter_depart = EE[EE['Department'].isin(select_depart)]
        st.write(filter_depart[col5].corr())
    
#6
#Distance from home
FF = raw_file.copy()

for f in FF.columns:
    if FF[f].dtype == 'object':
        FF[f] = ps.factorize(FF[f])[0]+1

#print(FF[['Attrition','JobSatisfaction','WorkLifeBalance','DistanceFromHome']].corr()['DistanceFromHome'])

col6 = ['Attrition','JobSatisfaction','WorkLifeBalance','DistanceFromHome']
if Name:
    Distancefromhome = FF['DistanceFromHome'].unique().tolist()
    Select_Distancehome = st.multiselect('If you want to check the corr related of distance from home',Distancefromhome)

    if Select_Distancehome:
        filter_distance = FF[FF['DistanceFromHome'].isin(Select_Distancehome)]
        st.write(filter_distance[col6].corr())

#7
#education 
GG = raw_file.copy()

for g in GG.columns:
    if GG[g].dtype == 'object':
        GG[g] = ps.factorize(GG[g])[0]+1

#print(GG[['JobSatisfaction','PerformanceRating','Education']].corr()['Education'])

col7 = ['JobSatisfaction','PerformanceRating','Education']
if Name:
    Education = GG['Education'].unique().tolist()
    select_education = st.multiselect('select the education to check the corr of it',Education)

    if select_education:
        filter_education = GG[GG['Education'].isin(select_education)]
        st.write(filter_education[col7].corr())

#8
#Educationfield
HH = raw_file.copy()

for h in HH.columns:
    if HH[h].dtype == 'object':
        HH[h] = ps.factorize(HH[h])[0]+1

#print(HH[['EducationField','PerformanceRating','JobSatisfaction']].corr()['EducationField'])

col8 = ['EducationField','PerformanceRating','JobSatisfaction']
if Name:
    educationfield = HH['EducationField'].unique().tolist()
    select_educationfield = st.multiselect('select the education field to check the corr of it',educationfield)

    if select_educationfield:
        filter_educationfield = HH[HH['EducationField'].isin(select_educationfield)]
        st.write(filter_educationfield[col8].corr())

#9
#emplooye count
II = raw_file.copy()
#employesscount and employees_constant 
#print(II['EmployeeNumber'].drop_duplicates().count())
#print(II['EmployeeNumber'].unique())

#10
#employee number
JJ = raw_file.copy()
#Unique identifier for each employee
#print(JJ['EmployeeNumber'].unique()) == len(JJ)

#11
#EnvironmentSatisfaction 
KK = raw_file.copy()

for k in KK.columns:
    if KK[k].dtype == 'object':
        KK[k] = ps.factorize(KK[k])[0]+1

#print(KK[['EnvironmentSatisfaction','JobSatisfaction']].corr()['EnvironmentSatisfaction'])

col11 = ['EnvironmentSatisfaction','JobSatisfaction']
if Name:
    environment = KK['EnvironmentSatisfaction'].unique().tolist()
    select_environmentstat = st.multiselect('if you want to check the environmentstat correlation select here',environment)

    if select_environmentstat:
        filter_environment = KK[KK['EnvironmentSatisfaction'].isin(select_environmentstat)]
        st.write(filter_environment[col11].corr())

#12
#Gender
LL = raw_file.copy()

for l in LL.columns:
    if LL[l].dtype == 'object':
        LL[l] = ps.factorize(LL[l])[0]+1

#Used to study gender-based differences in satisfaction, pay, and attrition.
#print(LL[['Gender','JobSatisfaction','MonthlyIncome','Attrition']].corr()['Gender'])

col12 = ['Gender','JobSatisfaction','MonthlyIncome','Attrition']
if Name:
    gender = LL['Gender'].unique().tolist()
    select_gender = st.multiselect('select the gender to view the corr of it',gender)

    if select_gender:
        filter_gender = LL[LL['Gender'].isin(select_gender)]
        st.write(filter_gender[col12].corr())

#13
#Jobinvolvement
MM = raw_file.copy()

for m in MM.columns:
    if MM[m].dtype == 'object':
        MM[m] = ps.factorize(MM[m])[0]+1
# Used to study how job involvement correlates with performance, satisfaction, and attrition.
#print(MM[['HourlyRate','Attrition','JobSatisfaction']].corr()['HourlyRate'])

col13 = ['HourlyRate','Attrition','JobSatisfaction']
if Name:
    hourlyrate = MM['HourlyRate'].unique().tolist()
    select_hourly = st.multiselect('select the hourlyrate to check the corr of it ',hourlyrate)

    if select_hourly:
        filter_hourly = MM[MM['HourlyRate'].isin(select_hourly)]
        st.write(filter_hourly[col13].corr())

#14
#jobinvolvement

NN = raw_file.copy()

for n in NN.columns:
    if NN[n].dtype == 'object':
        NN[n] = ps.factorize(NN[n])[0]+1
#Used to study how job involvement correlates with performance, satisfaction, and attrition.
#print(NN[['JobInvolvement','JobSatisfaction','PerformanceRating','Attrition']].corr()['JobInvolvement'])
if Name:
    col14 = ['JobInvolvement','JobSatisfaction','PerformanceRating','Attrition']
    jobinvolvement = NN['JobInvolvement'].unique().tolist()
    select_jobinvolvement = st.multiselect('select the jobinvolvement to see the corr',jobinvolvement)

    if select_jobinvolvement:
        filter_jobinvolvement = NN[NN['JobInvolvement'].isin(select_jobinvolvement)]
        st.write(filter_jobinvolvement[col14].corr())

#15
#joblevel

OO = raw_file.copy()

for o in OO.columns:
    if OO[o].dtype == 'object':
        OO[o] = ps.factorize(OO[o])[0]+1
# help analyze the relationship between job level and performance, satisfaction.
#print(OO[['JobLevel','PerformanceRating','JobSatisfaction']].corr()['JobLevel'])
if Name:
    col15 = ['JobLevel','PerformanceRating','JobSatisfaction']
    joblevel = OO['JobLevel'].unique().tolist()
    select_joblevel = st.multiselect('select the jobrole to check the corr ',joblevel)

    if select_joblevel:
        filter_joblevel = OO[OO['JobLevel'].isin(select_joblevel)]
        st.write(filter_joblevel[col15].corr())

#16
#jobrole
PP = raw_file.copy()

for p in PP.columns:
    if PP[p].dtype == 'object':
        PP[p] = ps.factorize(PP[p])[0]+1

#sales executive
#print(PP.loc[PP['JobRole']==1,['Attrition','JobSatisfaction','PerformanceRating']].corr())
#Research Scientist
#print(PP.loc[PP['JobRole']==2,['Attrition','JobSatisfaction','PerformanceRating']].corr())

col16 = ['Attrition','JobSatisfaction','PerformanceRating']
if Name:
    jobrole = PP['JobRole'].unique().tolist()
    select_jobrole = st.multiselect('Kindly select the jobrole to view the corr',jobrole)

    if select_jobrole:
        filter_jobrole = PP[PP['JobRole'].isin(select_jobrole)]
        st.write(filter_jobrole[col16].corr())

#17
#jobstatisfaction
QQ = raw_file.copy()

for q in QQ.columns:
    if QQ[q].dtype == 'object':
        QQ[q] = ps.factorize(QQ[q])[0]+1
#jobsatisfaction 1        
#print(QQ.loc[QQ['JobSatisfaction']==1,['Attrition','PerformanceRating','MonthlyIncome']].corr())
#jobsatisfaction 2
#print(QQ.loc[QQ['JobSatisfaction']==2,['Attrition','PerformanceRating','MonthlyIncome']].corr())
#jobsatisfaction 3
#print(QQ.loc[QQ['JobSatisfaction']==3,['Attrition','PerformanceRating','MonthlyIncome']].corr())
#jobsatisfaction 4
#print(QQ.loc[QQ['JobSatisfaction']==4,['Attrition','PerformanceRating','MonthlyIncome']].corr())

col17 = ['Attrition','PerformanceRating','MonthlyIncome']

job_statis = QQ['JobSatisfaction'].unique().tolist()
if Name:
    select_jobstatis = st.multiselect(f'select the job stats to check the correlation of it',job_statis)

    if select_jobstatis:
        filter_job_stat = QQ[QQ['JobSatisfaction'].isin(select_jobstatis)]
        st.write(filter_job_stat[col17].corr())

#18
#maritalstatus
RR = raw_file.copy()

for r in RR.columns:
    if RR[r].dtype == 'object':
        RR[r] = ps.factorize(RR[r])[0]+1

#employess = single
#print(RR.loc[RR['MaritalStatus']==1,['JobSatisfaction','PerformanceRating','Attrition']].corr())
#employess = Married
#print(RR.loc[RR['MaritalStatus']==2,['JobSatisfaction','PerformanceRating','Attrition']].corr())
#employess = Divorced
#print(RR.loc[RR['MaritalStatus']==3,['JobSatisfaction','PerformanceRating','Attrition']].corr())

col18 = ['JobSatisfaction','PerformanceRating','Attrition']
martialstatus = RR['MaritalStatus'].unique().tolist()
if Name:
    select_martialstatus = st.multiselect('select the martial status to check the corr',martialstatus)

    if select_martialstatus:
        filter_martialstatus = RR[RR['MaritalStatus'].isin(select_martialstatus)]
        st.write(filter_martialstatus[col18].corr())

#19
#montlyincome
SS = raw_file.copy()

SS['Attrition'] = SS['Attrition'].replace({'Yes': 1, 'No': 0})

for s in SS.columns:
    if SS[s].dtype == 'object' and s!= 'Attrition':
        SS[s] = ps.factorize(SS[s])[0]+1

#print(SS.corr()['MonthlyIncome'][['JobSatisfaction','PerformanceRating','Attrition']])

col19 = ['JobSatisfaction','PerformanceRating','Attrition']
montlyincome = RR['MonthlyIncome'].unique().tolist()
if Name:
    select_monthlyincome = st.multiselect('select the montly income to check the corr',montlyincome)

    if select_monthlyincome:
        filter_monthlyincome = RR[RR['MaritalStatus'].isin(select_monthlyincome)]
        st.write(filter_monthlyincome[col18].corr())

#20
#montlyrate
TT = raw_file.copy()

for t in TT.columns:
    if TT[t].dtype == 'object':
        TT[t] = ps.factorize(TT[t])[0]+1

#print(TT.corr()['MonthlyRate'][['Attrition','PerformanceRating','JobSatisfaction']])
col20 = ['Attrition','PerformanceRating','JobSatisfaction']
montlyrate = TT['MonthlyRate'].unique().tolist()
if Name:
    select_montlyrate = st.multiselect('select the monthly rate amount to see the correl',montlyrate)

    if select_montlyrate:
        filter_montlyrate = TT[TT['MonthlyRate'].isin(select_montlyrate)]
        st.write(filter_montlyrate[col20].corr())

#21
#numcompaniesworked
UU = raw_file.copy()

for u in UU.columns:
    if UU[u].dtype == 'object':
        UU[u] = ps.factorize(UU[u])[0]+1

#print(UU.corr()['NumCompaniesWorked'][['JobSatisfaction','PerformanceRating','Attrition']])

col21 = ['JobSatisfaction','PerformanceRating','Attrition']
numcompanieswork = UU['NumCompaniesWorked'].unique().tolist()
if Name:
    select_numofcompanies = st.multiselect('select the option to check the num of companies work and its corr',numcompanieswork)

    if select_numofcompanies:
        filter_numofcompanies = UU[UU['NumCompaniesWorked'].isin(select_numofcompanies)]
        st.write(filter_numofcompanies[col21].corr())

#22
#this is used to check the all the employees are over 18
VV = raw_file.copy()

for v in VV.columns:
    if VV[v].dtype == 'object':
        VV[v] = ps.factorize(VV[v])[0]+1

#if VV['Over18'].nunique() == 1 and (VV['Over18'] ==1).all() :
#    print(VV['Over18'].head())
#    print('Every one is over 18')
#    print(sum(VV['Over18']))
#else:
#    print('no this person is not over 18')


#23
#This is used to check the employees or over-time working and job satisfication
WW = raw_file.copy()

for w in WW.columns:
    if WW[w].dtype == 'object':
        WW[w] = ps.factorize(WW[w])[0] 

#print(WW.corr()['OverTime'][['JobSatisfaction','PerformanceRating','Attrition']])

col23 = ['JobSatisfaction','PerformanceRating','Attrition']

over_time = WW['OverTime'].unique().tolist()
if Name:
    select_overtime = st.multiselect('select the value to check the correlation of it',over_time)

    if select_overtime:
        filter_overtime = WW[WW['OverTime'].isin(select_overtime)]
        st.write(filter_overtime[col23].corr())

#24
#percentsalaryhike

ZZ = raw_file.copy() 

for z in ZZ.columns:
    if ZZ[z].dtype == 'object':
        ZZ[z] = ps.factorize(ZZ[z])[0]+1

#print(ZZ.corr()['PercentSalaryHike'][['JobSatisfaction','Attrition','PerformanceRating']])
col24 = ['JobSatisfaction','Attrition','PerformanceRating']
salaryhike = ZZ['PercentSalaryHike'].unique().tolist()
if Name:
    select_salaryhike = st.multiselect('select the option of the salaryhike to view the correlation',salaryhike)

    if select_salaryhike:
        filter_salaryhike = ZZ[ZZ['PercentSalaryHike'].isin(select_salaryhike)]
        st.write(filter_salaryhike[col24].corr())

#25
#performance Rating

AA1 = raw_file.copy()

for A1 in AA1.columns:
    if AA1[A1].dtype == 'object':
        AA1[A1] = ps.factorize(AA1[A1])[0]+1

#print(AA1.corr()['PerformanceRating'][['Attrition','JobInvolvement','JobSatisfaction','MonthlyIncome','JobInvolvement','OverTime','YearsAtCompany']])

col25 = ['Attrition','JobInvolvement','JobSatisfaction','MonthlyIncome','JobInvolvement','OverTime','YearsAtCompany']
performancerating = AA1['PerformanceRating'].unique().tolist()
if Name:
    select_perfomancerating = st.multiselect('select the option to view the correlation of it',performancerating)

    if select_perfomancerating:
        filter_performancerating = AA1[AA1['PerformanceRating'].isin(select_perfomancerating)]
        st.write(filter_performancerating[col25].corr())

#26
#relationship satisfication
AA2 =raw_file.copy() 

for A2 in AA2.columns:
    if AA2[A2].dtype == 'object':
        AA2[A2] = ps.factorize(AA2[A2])[0]+1

#print(AA2.corr()['RelationshipSatisfaction'][['JobSatisfaction','Attrition']])

col26 = ['JobSatisfaction','Attrition']
relationship = AA2['RelationshipSatisfaction'].unique().tolist()
if Name:
    select_relationship = st.multiselect('select the option to view the correlation of it',relationship)

    if select_relationship:
        filter_relationship = AA2[AA2['RelationshipSatisfaction'].isin(select_relationship)]    
        st.write(filter_relationship[col26].corr())

#27
#standard Hours

AA3 = raw_file.copy()

#if (AA3['StandardHours'] == 80).all():
#    print("yes the standard hours for all the employee is 80")
#else:
#    print('No not for all the employee')

#28
#Stock option level

AA4 = raw_file.copy()

for A4 in AA4.columns:
    if AA4[A4].dtype == 'object':
        AA4[A4] = ps.factorize(AA4[A4])[0]+1

#print(AA4.corr()['StockOptionLevel'][['JobSatisfaction','Attrition','PerformanceRating']])

col28 = ['JobSatisfaction','Attrition','PerformanceRating']
stockoption = AA4['StockOptionLevel'].unique().tolist()
if Name:
    select_stockoption = st.multiselect('select the option of stock option to view the corr of it',stockoption)

    if select_stockoption:
        filter_stockoption = AA4[AA4['StockOptionLevel'].isin(select_stockoption)]
        st.write(filter_stockoption[col28].corr())
    

#29
#Total working years

AA5 = raw_file.copy()

for A5 in AA5.columns:
    if AA5[A5].dtype == 'object':
        AA5[A5] = ps.factorize(AA5[A5])[0]+1

#print(AA5.corr()['TotalWorkingYears'][['PerformanceRating','Attrition']])
col29 = ['PerformanceRating','Attrition']
totalworking = AA5['TotalWorkingYears'].unique().tolist()
if Name:
    select_totalworking = st.multiselect('select the option to view the corr of totalworkingyears',totalworking)

    if select_totalworking:
        filter_totalworking = AA5[AA5['TotalWorkingYears'].isin(select_totalworking)]
        st.write(filter_totalworking[col29].corr())

#30
#Traning times last year

AA6 = raw_file.copy()

for A6 in AA6.columns:
    if AA6[A6].dtype == 'object':
        AA6[A6] = ps.factorize(AA6[A6])[0]+1

#print(AA6.corr()['TrainingTimesLastYear'][['PerformanceRating','Attrition','PerformanceRating']])

col30 = ['PerformanceRating','Attrition','PerformanceRating']

training_time = AA6['TrainingTimesLastYear'].unique().tolist()
if Name:
    select_training_time = st.multiselect('select the option to view the corr of training time ',training_time)

    if select_training_time:
        filter_training_time = AA6[AA6['TrainingTimesLastYear'].isin(select_training_time)]
        st.write(filter_training_time[col30].corr())

#31
#worklifebalancce

AA7 = raw_file.copy()

for A7 in AA7.columns:
    if AA7[A7].dtype == 'object':
        AA7[A7] = ps.factorize(AA7[A7])[0]+1

#print(AA7.corr()['WorkLifeBalance'][['PerformanceRating','JobSatisfaction','Attrition']])

col31= ['PerformanceRating','JobSatisfaction','Attrition']

worklifebal = AA7['WorkLifeBalance'].unique().tolist()
if Name:
    select_worklifebal = st.multiselect('Select the option to check the corr of worklifebal',worklifebal)

    if select_worklifebal:
        filter_worklifebal = AA7[AA7['WorkLifeBalance'].isin(select_worklifebal)]
        st.write(filter_worklifebal[select_worklifebal].corr())

#32
#Yearatcompany
AA8 = raw_file.copy()

for A8 in AA8.columns:
    if AA8[A8].dtype == 'object':
        AA8[A8] = ps.factorize(AA8[A8])[0]+1

#print(AA8.corr()['YearsAtCompany'][['PerformanceRating','JobSatisfaction','Attrition']])

col32 = ['PerformanceRating','JobSatisfaction','Attrition']

yearatcompany = AA8['YearsAtCompany'].unique().tolist()
if Name:
    select_yearatcompany = st.multiselect('select the option to view the corr of yearatcompany',yearatcompany)

    if select_yearatcompany:
        filter_yearatcompany = AA8[AA8['YearsAtCompany'].isna(select_yearatcompany)]
        st.write(filter_yearatcompany[col32].corr())

#33
#Yearincurrentrole

AA9 = raw_file.copy()

for A9 in AA9.columns:
    if AA9[A9].dtype == 'object':
        AA9[A9] = ps.factorize(AA9[A9])[0]+1

#print(AA9.corr()['YearsInCurrentRole'][['JobSatisfaction','Attrition']])

col33 = ['JobSatisfaction','Attrition']

yearincurrentrole = AA9['YearsInCurrentRole'].unique().tolist()
if Name:
    select_yearsinrole = st.multiselect('select the option to view the corr of years at same role',yearincurrentrole)

    if select_yearsinrole:
        filter_yearinrole = AA9[AA9['YearsInCurrentRole'].isin(select_yearsinrole)]
        st.write(filter_yearinrole[col33].corr())

#34
#Yearsincelast promotion

AA10 = raw_file.copy()

for A10 in AA10.columns:
    if AA10[A10].dtype == 'object':
        AA10[A10] = ps.factorize(AA10[A10])[0]+1

#print(AA10.corr()['YearsSinceLastPromotion'][['EnvironmentSatisfaction','Attrition']])

col34 = ['EnvironmentSatisfaction','Attrition']

yearsincepromotion = AA10['YearsSinceLastPromotion'].unique().tolist()
if Name:
    select_yearsincepromotion = st.multiselect('select the option to view the corr of yearsincepromotion',yearsincepromotion)

    if select_yearsincepromotion:
        filter_yearsincepromotion = AA10[AA10['YearsSinceLastPromotion'].isin(select_yearsincepromotion)]
        st.write(filter_yearsincepromotion[col34].corr())

#35
#yearwithcurrmanager

AA11 = raw_file.copy()

for A11 in AA11.columns:
    if AA11[A11].dtype == 'object':
        AA11[A11] = ps.factorize(AA11[A11])[0]+1

#print(AA11.corr()['YearsWithCurrManager'][['EnvironmentSatisfaction','Attrition']])

col35 = ['EnvironmentSatisfaction','Attrition']
yearwithcurrentmanager = AA11['YearsWithCurrManager'].unique().tolist()
if Name:
    select_current_manager = st.multiselect('select the option to check the corr of current manager ',yearwithcurrentmanager)

    if select_current_manager:
        filter_currentmanager = AA11[AA11['YearsWithCurrManager'].isin(select_current_manager)]
        st.write(filter_currentmanager[col35])

#Attrition prediction 1

AAA = raw_file.copy()

AAA1 = raw_file.drop(columns=['EmployeeCount','Over18','StandardHours'],axis=1)

#print(AAA1.info())
#print(AAA1.isna().count())

coly = ['Attrition','BusinessTravel','Department','EducationField','Gender','JobRole','MaritalStatus','OverTime']

for ii in AAA1[coly]:
    if AAA1[ii].dtype == 'object':
        AAA1[ii] = ps.factorize(AAA1[ii])[0]

x = AAA1.drop(columns=['Attrition'],axis=1)
y = AAA1['Attrition']

from sklearn.model_selection import train_test_split

x_train , x_test , y_train , y_test = train_test_split(x,y,test_size=0.25,random_state=42)

#print(f'x train {x_train.shape}')
#print(f'x test {x_test.shape}')

#print(AAA1.corr()[['Attrition']].sort_values(ascending=False))

import matplotlib.pyplot as plt
import plotly as ply
import seaborn as sbn

#plt.figure(figsize=(15, 10))
#sbn.heatmap(data=AAA1.corr(),cmap='coolwarm',annot=True)
#plt.show()

from sklearn.utils.class_weight import compute_class_weight
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB

dlt = DecisionTreeClassifier()
dlt.fit(x_train,y_train)
k = dlt.predict(x_test)

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix

model = []

model.append((f'kkk',KNeighborsClassifier()))
model.append((f'decision',DecisionTreeClassifier()))
model.append((f'gaussian',GaussianNB()))
model.append((f'random',RandomForestClassifier(class_weight='balanced')))

for name , models in model:
#    print(models)
#    print(f'\n')
    models.fit(x_train,y_train)
    y_pred = models.predict(x_test)
    y_proba = models.predict_proba(x_test)[:, 1] if hasattr(model, "predict_proba") else None
#    print(f'accuracy',accuracy_score(y_test, y_pred))
#    print(f'\n')
#    print(f'precision',precision_score(y_test, y_pred))
#    print(f'\n')
#    print(f'recall',recall_score(y_test, y_pred))
#    print(f'\n')
#    print(f'confusion',f1_score(y_test, y_pred))
#    if y_proba is not None:
#        print(f"AUC-ROC  : {roc_auc_score(y_test, y_proba):.4f}")
#    print("Confusion Matrix:")
#    print(confusion_matrix(y_test, y_pred))

#PerformanceRating prediction 1

BBB1= raw_file.copy()

for jj in BBB1:
    if BBB1[jj].dtype == 'object':
        BBB1[jj] = ps.factorize(BBB1[jj])[0]+1

clean_BBB1 = BBB1.drop(columns=['EmployeeCount','Over18','StandardHours'],axis=1)

#this is used to check the correlation using the heatmap
plt.figure(figsize=(10,15))
sbn.heatmap(data=clean_BBB1.corr()[['PerformanceRating']],annot=True,cmap='coolwarm')
#plt.show()
#This is used to check the performancerating correlation with other fators
#print(clean_BBB1.corr()['PerformanceRating'].sort_values(ascending=False))

from sklearn.model_selection import train_test_split

xx = clean_BBB1.drop(columns=['PerformanceRating'],axis=1)
yy = clean_BBB1['PerformanceRating']

xx_train , xx_test ,yy_train , yy_test = train_test_split(xx,yy,test_size=0.25,random_state=42)

#This use us to see the shape of the train function
#print(f'xx train {xx_train.shape}')
#print(f'xx testn {xx_test.shape}')


from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
modelB = []
modelB.append((f'decision',DecisionTreeRegressor()))
modelB.append(('random',RandomForestRegressor()))
modelB.append(('linear',LinearRegression()))

from sklearn.metrics import mean_absolute_error , median_absolute_error , r2_score

for nameB , models_B in modelB:
#    print(models_B)
#    print(f'\n')
    models_B.fit(xx_train,yy_train)
    y_predB = models_B.predict(xx_test)
#    print(f'mean metric{mean_absolute_error(yy_test,y_predB)}')
#    print(f'\n')
#    print(f'median {median_absolute_error(yy_test,y_predB)}')
#    print(f'\n')
#    print(f'r2 score {r2_score(yy_test,y_predB)}')
#    print(f'\n')

# YearsSinceLastPromotion 2
CCC1 = raw_file.copy()

for kk in CCC1.columns:
    if CCC1[kk].dtype == 'object':
        CCC1[kk] = ps.factorize(CCC1[kk])[0]+1

colx = ['EmployeeCount','Over18','StandardHours']

clean_CCC1 = CCC1.drop(columns=(colx))

#This is used to check the correlence for the performancerating
#print(clean_CCC1.corr()['PerformanceRating'].sort_values(ascending=False))

#this is used to check the correlence using the plot map
plt.figure(figsize=(10,14))
sbn.heatmap(clean_CCC1.corr()[['YearsSinceLastPromotion']])
#plt.show()

xxx = clean_CCC1.drop(columns=['YearsSinceLastPromotion'])
yyy = clean_CCC1['YearsSinceLastPromotion']

from sklearn.model_selection import train_test_split

xxx_train , xxx_test , yyy_train , yyy_test = train_test_split(xxx,yyy,test_size=0.25,random_state=42)

#This is used to check the shape of the train and test field
#print(f'xxx train {xxx_train.shape}')
#print(f'xxx test {xxx_test.shape}')

from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression

model2 = []

model2.append(('randomforest',RandomForestRegressor()))
model2.append(('decision',DecisionTreeRegressor()))
model2.append(('Linear',LinearRegression()))

from sklearn.metrics import mean_absolute_error , r2_score , median_absolute_error

for name_C, model_C in model2:
#    print(name_C)
    model_C.fit(xxx_train,yyy_train)
    train_prec_C = model_C.predict(xxx_train)
#    print(f'mean {mean_absolute_error(yyy_train,train_prec_C)}')
#    print(f'\n')
#    print(f'r2  {r2_score(yyy_train,train_prec_C)}')
#    print(f'\n')
#    print(f'median {median_absolute_error(yyy_train,train_prec_C)}')
    
    Test_prec_C = model_C.predict(xxx_test)
#    print(f'mean {mean_absolute_error(yyy_test,Test_prec_C)}')
#    print(f'\n')
#    print(f'r2  {r2_score(yyy_test,Test_prec_C)}')
#    print(f'\n')
#    print(f'median {median_absolute_error(yyy_test,Test_prec_C)}')

options = AA.columns
select_option = st.multiselect('if you want to see the correlation of you own select',options)

if select_option:
    filter_option = AA[select_option]
    st.write(filter_option.corr())

