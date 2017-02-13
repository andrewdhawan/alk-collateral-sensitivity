#DN 06/02/2017
import numpy as np
import matplotlib.pyplot as plt

days = [0,1,3,7,14,21]

#The data for CertR
#Cerit resistant line
wtCriz = [163.6694, 92.7284, 138.9279, 81.1338, 160.382, 101.5383]
wtCrizErrors = [( 124.654001700344 , 216.212910546799 ), ( 46.6102205797559 , 178.244450403295 ), ( 75.9418940498425 , 250.67938875507 ), ( 33.2110842694353 , 184.623055793523 ), ( 113.457427878485 , 225.804754552824 ), ( 57.8401736438409 , 174.039947800208 )]
crizEC50s = [499.5046,   181.3725418, 475.7462702, 263.2175594, 241.7304768, 247.0166891]
crizErrors = [( 236.80546813747 , 1059.97950865926 ),    ( 56.4218623012538 , 569.250686401943 ), ( 176.597006907101 , 1201.29028715862 ), ( 174.205260124494 , 397.424788573334 ), ( 105.732834043354 , 539.494738264354 ), ( 123.852862593864 , 478.912278619393 )]

#Alec
wtAlec = [8.2665, 7.0297, 18.0028, 4.5254, 18.1501, 7.3704]
wtAlecErrors = [( 4.31552847346808 , 15.52989427972), ( 4.23330910148072 , 11.6234932364946 ), ( 12.6305368043434 , 25.7209071821998 ), ( 3.22712325632526 , 6.31017892302149 ), ( 10.6230442787539 , 31.5266562292566 ), ( 5.09844526944774 , 10.6992408310007 )]
alecEC50s = [100.6638,   44.72672699, 34.74855473, 32.19870356, 11.87045983, 16.90100291]
alecErrors = [( 38.243962939525 , 270.331360725386 ),    ( 13.0908125700331 , 153.9876004615 ),   ( 12.1428867560166 , 101.069781632563 ), ( 21.2419746358594 , 48.8228662533731 ), ( 6.95397013767778 , 20.3824337390243 ), ( 8.26699971963258 , 33.9491316182505 )] 

#Lorlatnib
wtLorl = [1.248, 2.034, 2.698, 1.6009, 3.805, 1.8568]
wtLorlErrors = [( 1.06701602558315 , 1.45729559093603 ), ( 1.34517999534078 , 3.03647943467069 ), ( 1.45080642323269 , 4.95871873504808 ), ( 1.16588595988726 , 2.19118501137926 ), ( 2.26350737759354 , 6.44442940127399 ), ( 1.1236949475959 , 3.0332863866961 )]
lorlEC50s = [5.7002, 0.3371,  3.6083129,   1.362019247, 3.086634421, 2.146583733]
lorlErrors = [( 3.07694989990502 , 10.6804269364993 ),   (0.3371, 0.3371),  ( 2.75400805951954 , 4.72425773120707 ), ( 0.771073022965494 , 2.40714630891569 ),    ( 2.08164825426629 , 4.58206641914434 ), ( 0.899834911374882 , 4.95426989733226 )]

#Cerit
wtCert = [6.3379, 0.4601, 13.0742, 15.7682, 8.6044, 2.412]
wtCertErrors = [( 3.52398167960523 , 11.1169089691941 ), ( 0.316483192662388 , 0.653153891892064 ), ( 7.83286875344515 , 21.8278217460877 ), ( 9.7169752120195 , 25.4612367208097 ), ( 5.74426718813696 , 12.844225572569 ), ( 1.53469730737552 , 3.81938461952842 )]
certEC50s = [206.8954,   17.02873889, 52.16913396, 23.66486155, 31.60143572, 55.88196409]
certErrors = [( 120.471260717367 , 350.414478459268 ),   ( 4.24204818204841 , 65.0335184641958 ), ( 26.9849683098921 , 100.280341803859 ), ( 14.1651720679449 , 39.3720193995115 ), ( 18.6981239402697 , 52.9395623487559 ), ( 23.4238503370672 , 132.177755340156 )]


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
    plt.title("LorlR under "+label)
    plt.ylabel("EC50")
    plt.yscale('log')
    plt.legend()
    # plt.show()
    plt.savefig("./Figs/LorlR_"+label+".pdf")

plot(wtCriz, wtCrizErrors, crizEC50s, crizErrors, aggCriz, aggCrizErrs, 'Criz')
plot(wtAlec, wtAlecErrors, alecEC50s, alecErrors, aggAlec, aggAlecErrs, 'Alec')
plot(wtLorl, wtLorlErrors, lorlEC50s, lorlErrors, aggLorl, aggLorlErrs, 'Lorl')
plot(wtCert, wtCertErrors, certEC50s, certErrors, aggCert, aggCertErrs, 'Cert')
