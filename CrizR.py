#DN 06/02/2017
import numpy as np
import matplotlib.pyplot as plt

days = [0,1,3,7,14,21]

#The data for CertR
#Cerit resistant line
wtCriz = [163.6694, 92.7284, 138.9279, 81.1338, 160.382, 101.5383]
wtCrizErrors = [( 124.654001700344 , 216.212910546799 ), ( 46.6102205797559 , 178.244450403295 ), ( 75.9418940498425 , 250.67938875507 ), ( 33.2110842694353 , 184.623055793523 ), ( 113.457427878485 , 225.804754552824 ), ( 57.8401736438409 , 174.039947800208 )]
crizEC50s = [322.0049,   165.0667679, 303.7944982, 309.4326217, 278.6938684, 163.7036668]
crizErrors = [( 123.31256861959 , 874.874788361958 ),    ( 78.0291605612335 , 341.578406363936 ), ( 85.1604728066104 , 1040.24626118083 ), ( 167.215824186662 , 576.132814704845 ), ( 127.262865931283 , 607.897896797238 ), ( 86.8207915056196 , 297.161043925319 )]

#Alec
wtAlec = [8.2665, 7.0297, 18.0028, 4.5254, 18.1501, 7.3704]
wtAlecErrors = [( 4.31552847346808 , 15.52989427972), ( 4.23330910148072 , 11.6234932364946 ), ( 12.6305368043434 , 25.7209071821998 ), ( 3.22712325632526 , 6.31017892302149 ), ( 10.6230442787539 , 31.5266562292566 ), ( 5.09844526944774 , 10.6992408310007 )]
alecEC50s = [65.6239,    12.52789654, 13.51981142, 14.00218039, 24.13247361, 6.886988133]
alecErrors = [( 16.2977267765845 , 215.66375110692 ),    ( 6.50601231614972 , 24.3689973046912 ), ( 3.66967535417408 , 53.2935096671514 ), ( 8.39447449771581 , 23.3386784672096 ), ( 13.740365298041 , 43.0508048593163 ),  ( 3.78342518158728 , 12.5059875813935 )] 

#Lorlatnib
wtLorl = [1.248, 2.034, 2.698, 1.6009, 3.805, 1.8568]
wtLorlErrors = [( 1.06701602558315 , 1.45729559093603 ), ( 1.34517999534078 , 3.03647943467069 ), ( 1.45080642323269 , 4.95871873504808 ), ( 1.16588595988726 , 2.19118501137926 ), ( 2.26350737759354 , 6.44442940127399 ), ( 1.1236949475959 , 3.0332863866961 )]
lorlEC50s = [5.1181, 3.005770319, 2.75248281,  1.733315502, 4.342305774, 1.770054215]
lorlErrors = [( 2.14276126491057 , 11.2981934377853 ),   ( 1.81926973376132 , 4.99959278044173 ), ( 0.98184829875003 , 8.14462068202647 ), ( 0.772045459521482 , 3.74367415939167 ),    ( 2.10665274938059 , 8.48549835145984 ), ( 1.22624596529548 , 2.54208624050678 )]

#Cerit
wtCert = [6.3379, 0.4601, 13.0742, 15.7682, 8.6044, 2.412]
wtCertErrors = [( 3.52398167960523 , 11.1169089691941 ), ( 0.316483192662388 , 0.653153891892064 ), ( 7.83286875344515 , 21.8278217460877 ), ( 9.7169752120195 , 25.4612367208097 ), ( 5.74426718813696 , 12.844225572569 ), ( 1.53469730737552 , 3.81938461952842 )]
certEC50s = [1569.33,    3.583473629, 58.16796215, 93.60545078, 12.62821562, 5.011109449]
certErrors = [( 910.394082499476 , 2654.38271761011 ),   ( 1.78985067827637 , 7.00641505828655 ), ( 21.2203613344561 , 161.894298771296 ), ( 41.2600661415578 , 213.231284958609 ), ( 7.60261819867219 , 21.0464052956147 ), ( 3.17019126164118 , 7.9320164316244 )]


#Aggregate WTs
aggCriz = 131.6273
aggCrizErrs = ( 87.5365206075413 , 195.966591751532 )

aggAlec = 10.3596
aggAlecErrs = ( 7.85465344599291 , 13.6708626254051 )

aggCert = 5.3833
aggCertErrs = ( 4.24417977191406 , 6.82502531943921 )

aggLorl = 2.577
aggLorlErrs = ( 1.7965598732221 , 3.67428153566039 )


def plot(wts, wterrs, ec50s, ec50serrors, agg, aggErrs, label=""):
    import matplotlib as mpl
    params = {
           'axes.labelsize': 14,
           'text.fontsize': 14,
           'axes.titlesize': 16,
           'legend.fontsize': 12,
           'xtick.labelsize': 12,
           'ytick.labelsize': 12,
           'text.usetex': False,
           'figure.subplot.bottom' : 0.15,
           'figure.subplot.wspace' : 0.3
           }
    mpl.rcParams.update(params)
    
    plt.clf()
    plt.figure()

    plt.plot(days, [agg for _ in days], c='g' , label = 'Avg WT '+label+' Sen', ls = '-')
    plt.plot(days, [aggErrs[0] for _ in days], c='g' , ls = '--', lw=0.3)
    plt.plot(days, [aggErrs[1] for _ in days], c='g' , ls = '--', lw=0.3)
    plt.fill_between(days, aggErrs[0], aggErrs[1], facecolor='g', alpha=0.25, interpolate=True)

    boterrs = [ec50s[k] - ec50serrors[k][0] for k in range(len(ec50s))]
    toperrs = [ec50serrors[k][1] - ec50s[k] for k in range(len(ec50s))]
    wtbots = [wts[k] - wterrs[k][0] for k in range(len(wts))]
    wttops = [wterrs[k][1] - wts[k] for k in range(len(wts))]

    (_, caps1, _) = plt.errorbar(days, ec50s, ls='', marker = 'o', yerr = [boterrs, toperrs], label = label+' Sen', capsize=5)
    (_, caps2, _) = plt.errorbar(days, wts, ls='', marker = 'o', yerr = [wtbots, wttops], label = 'WT' + label+' Sen', c='g', capsize=5) 
    for c in caps1:
        c.set_markeredgewidth(1)
    for c in caps2:
        c.set_markeredgewidth(1)


    #This may be an error.
    # plt.xlabel("Day")
    plt.xticks(days, ["Day 0", "Day 1", "Day 3", "Day 7", "Day 14", "Day 21"], rotation="vertical")
    plt.title("CrizR under "+label)
    plt.ylabel("EC50")
    plt.yscale('log')
    plt.legend()
    # plt.show()
    plt.savefig("./Figs/CrizR_"+label+".pdf")

plot(wtCriz, wtCrizErrors, crizEC50s, crizErrors, aggCriz, aggCrizErrs, 'Criz')
plot(wtAlec, wtAlecErrors, alecEC50s, alecErrors, aggAlec, aggAlecErrs, 'Alec')
plot(wtLorl, wtLorlErrors, lorlEC50s, lorlErrors, aggLorl, aggLorlErrs, 'Lorl')
plot(wtCert, wtCertErrors, certEC50s, certErrors, aggCert, aggCertErrs, 'Cert')