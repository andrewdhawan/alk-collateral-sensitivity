#DN 06/02/2017
import numpy as np
import matplotlib.pyplot as plt

days = [0,1,3,7,14,21]

#The data for AlecR
#Cerit resistant line
wtCriz = [163.6694, 92.7284, 138.9279, 81.1338, 160.382, 101.5383]
wtCrizErrors = [( 124.654001700344 , 216.212910546799 ), ( 46.6102205797559 , 178.244450403295 ), ( 75.9418940498425 , 250.67938875507 ), ( 33.2110842694353 , 184.623055793523 ), ( 113.457427878485 , 225.804754552824 ), ( 57.8401736438409 , 174.039947800208 )]
crizEC50s = [471.957, 516.4646827, 297.8239999, 431.0470205, 79.91290722, 59.245402]
crizErrors = [( 258.42346457038 , 849.625840563997 ), ( 252.454243979907 , 1026.13895848501 ), ( 154.2619619137 , 565.261576417216 ), ( 265.515281690513 , 701.769034452273 ), ( 46.4625782085581 , 136.611954081815 ), ( 35.4495732989903 , 98.5541638300203 )]

#Alec
wtAlec = [8.2665, 7.0297, 18.0028, 4.5254, 18.1501, 7.3704]
wtAlecErrors = [( 4.31552847346808 , 15.52989427972), ( 4.23330910148072 , 11.6234932364946 ), ( 12.6305368043434 , 25.7209071821998 ), ( 3.22712325632526 , 6.31017892302149 ), ( 10.6230442787539 , 31.5266562292566 ), ( 5.09844526944774 , 10.6992408310007 )]
alecEC50s = [77.135, 254.4327, 74.518, 7.706, 7.4835, 8.9785]
alecErrors = [( 39.9981711410486 , 147.250934807652 ),   ( 77.2810847882097 , 1656.20277491005 ), ( 27.0391907712907 , 212.330378049052 ), ( 3.47528751628521 , 17.0237943815893 ), ( 5.53541507414172 , 10.086175737215 ),  ( 4.50895716380355 , 18.1639132689427 )] 

#Lorlatnib
wtLorl = [1.248, 2.034, 2.698, 1.6009, 3.805, 1.8568]
wtLorlErrors = [( 1.06701602558315 , 1.45729559093603 ), ( 1.34517999534078 , 3.03647943467069 ), ( 1.45080642323269 , 4.95871873504808 ), ( 1.16588595988726 , 2.19118501137926 ), ( 2.26350737759354 , 6.44442940127399 ), ( 1.1236949475959 , 3.0332863866961 )]
lorlEC50s = [1.5081, 1.1193,  0.5609,  0.871,   1.8716,  2.443]
lorlErrors = [( 0.69600575674979 , 3.12311431136647 ),   ( 0.364569101433697 , 4.15607208609406 ),    ( 0.169862375048698 , 1.70544578669749 ),    ( 0.332528807050575 , 2.20723288640412 ),    ( 1.26576864212218 , 2.72584538869469 ), ( 1.28616049764845 , 4.76427091451931 )]

#Cerit
wtCert = [6.3379, 0.4601, 13.0742, 15.7682, 8.6044, 2.412]
wtCertErrors = [( 3.52398167960523 , 11.1169089691941 ), ( 0.316483192662388 , 0.653153891892064 ), ( 7.83286875344515 , 21.8278217460877 ), ( 9.7169752120195 , 25.4612367208097 ), ( 5.74426718813696 , 12.844225572569 ), ( 1.53469730737552 , 3.81938461952842 )]
certEC50s = [767.0423,   26.21045334, 7.512498102, 21.33592542, 0.33345152,  9.350635203]
certErrors = [( 378.992722566744 , 1491.16821465153 ) ,  ( 6.89625263334754 , 94.0136554801832 ), ( 2.95707599648871 , 18.0842298512248 ), ( 11.8179726595732 , 38.1203898392767 ), ( 0.0593088068141017 , 1.2541892207588 ),    ( 4.1279299583902 , 21.1686579941441 )]


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
    plt.title("AlecR under "+label)
    plt.ylabel("EC50")
    plt.yscale('log')
    plt.legend()
    # plt.show()
    plt.savefig("./Figs/AlecR_"+label+".pdf")

plot(wtCriz, wtCrizErrors, crizEC50s, crizErrors, aggCriz, aggCrizErrs, 'Criz')
plot(wtAlec, wtAlecErrors, alecEC50s, alecErrors, aggAlec, aggAlecErrs, 'Alec')
plot(wtLorl, wtLorlErrors, lorlEC50s, lorlErrors, aggLorl, aggLorlErrs, 'Lorl')
plot(wtCert, wtCertErrors, certEC50s, certErrors, aggCert, aggCertErrs, 'Cert')
