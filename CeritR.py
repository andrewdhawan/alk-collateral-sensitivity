#DN 06/02/2017
import numpy as np
import matplotlib.pyplot as plt
# import seaborn as sbn

days = [0,1,3,7,14,21]

#The data for CertR
#Cerit resistant line
wtCriz = [163.6694, 92.7284, 138.9279, 81.1338, 160.382, 101.5383]
wtCrizErrors = [( 124.654001700344 , 216.212910546799 ), ( 46.6102205797559 , 178.244450403295 ), ( 75.9418940498425 , 250.67938875507 ), ( 33.2110842694353 , 184.623055793523 ), ( 113.457427878485 , 225.804754552824 ), ( 57.8401736438409 , 174.039947800208 )]
crizEC50s = [523.0612, 126.3, 326.1499, 140.711, 164.7702, 231.7537]
crizErrors = [( 172.317247195642 , 2800.22338153986 ), ( 56.9381499873463 , 268.307700283064 ), ( 166.269332023094 , 623.668228337288 ), ( 84.9257014723923 , 229.455925445622 ), ( 104.544815745114 , 259.607589495227 ), ( 158.717976550163 , 336.210434706442 )]

#Alec
wtAlec = [8.2665, 7.0297, 18.0028, 4.5254, 18.1501, 7.3704]
wtAlecErrors = [( 4.31552847346808 , 15.52989427972), ( 4.23330910148072 , 11.6234932364946 ), ( 12.6305368043434 , 25.7209071821998 ), ( 3.22712325632526 , 6.31017892302149 ), ( 10.6230442787539 , 31.5266562292566 ), ( 5.09844526944774 , 10.6992408310007 )]
alecEC50s = [121.6785, 12.1896,22.4794, 11.5077, 12.7234, 14.601]
alecErrors = [( 31.2071852057391 , 527.408241330677 ), ( 6.95400615076317 , 21.2397523912124 ), ( 12.1531321877263 , 41.7990663677119 ), ( 7.02382063882062 , 18.8284336545373 ), ( 7.8933054273929 , 20.5094078901048 ), ( 9.54553696157696 , 22.334392304593 )] 

#Lorlatnib
wtLorl = [1.248, 2.034, 2.698, 1.6009, 3.805, 1.8568]
wtLorlErrors = [( 1.06701602558315 , 1.45729559093603 ), ( 1.34517999534078 , 3.03647943467069 ), ( 1.45080642323269 , 4.95871873504808 ), ( 1.16588595988726 , 2.19118501137926 ), ( 2.26350737759354 , 6.44442940127399 ), ( 1.1236949475959 , 3.0332863866961 )]
lorlEC50s = [2.143, 1.6568, 3.6065, 1.0247, 3.153, 2.3138]
lorlErrors = [(2.143, 2.143), ( 1.23591210814876 , 2.21224062401965 ), ( 1.86664438120957 , 6.77852105171989 ), ( 0.581477292956093 , 1.76227978775092 ), ( 1.91208101220748 , 5.05745676995825 ), ( 1.42655887852617 , 3.73552005374837 )]

#Cerit
wtCert = [6.3379, 0.4601, 13.0742, 15.7682, 8.6044, 2.412]
wtCertErrors = [( 3.52398167960523 , 11.1169089691941 ), ( 0.316483192662388 , 0.653153891892064 ), ( 7.83286875344515 , 21.8278217460877 ), ( 9.7169752120195 , 25.4612367208097 ), ( 5.74426718813696 , 12.844225572569 ), ( 1.53469730737552 , 3.81938461952842 )]
certEC50s = [2436.7521, 5.9218, 38.1682, 38.9731, 7.5344, 14.425,]
certErrors = [( 1324.48849029261 , 4332.67348041503 ), ( 4.38824682677574 , 7.96503848515285 ), ( 24.9914544427968 , 58.3367028031192 ), ( 14.1398457067346 , 104.443329137149 ), ( 3.71145624773181 , 14.8883182084386 ), ( 9.77647239339932 , 21.3215339482661 )]

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
    plt.title("CeritR under "+label)
    plt.ylabel("EC50")
    plt.yscale('log')
    plt.legend()
    # plt.show()
    plt.savefig("./Figs/CeritR_"+label+".pdf")

plot(wtCriz, wtCrizErrors, crizEC50s, crizErrors, aggCriz, aggCrizErrs, 'Criz')
plot(wtAlec, wtAlecErrors, alecEC50s, alecErrors, aggAlec, aggAlecErrs, 'Alec')
plot(wtLorl, wtLorlErrors, lorlEC50s, lorlErrors, aggLorl, aggLorlErrs, 'Lorl')
plot(wtCert, wtCertErrors, certEC50s, certErrors, aggCert, aggCertErrs, 'Cert')

