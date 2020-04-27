import pandas as pd
#import seaborn as sns
import scipy.stats as st
import matplotlib.pyplot as plt
import statsmodels.api as sm
#import sys

d2020= pd.read_csv("DraftResultsData/2020draft.csv")

#Create list to store players names for cleaning up
split_player = d2020["Player"]
#Split out and store the name of the player
players=[i.split("\\")[0] for i in split_player]
#Split out and store first and last names
fname = [i.split(maxsplit = 1)[0] for i in players]
lname = [i.split(maxsplit = 1)[1] for i in players]
#Add first and last name columns
d2020["First Name"]=fname
d2020["Last Name"]=lname

#Create new df in the format desired
d2020c = d2020[["Rnd","Pick","Tm","First Name","Last Name","Pos","Age","College/Univ"]]

#Import data from 2019 draft
d2019= pd.read_csv("DraftResultsData/2019Draft_Rank.csv")
#Create df that only includes players drafted
drafted2019 = d2019.dropna()
drafted2019.head()



#Generate Scatter Plot, Regression Line, r, r^2 of Rank vs Pick Overall
def linregsingle(df,x_values,y_values,ex,ey):
    #run linear regression and store key values
    slope, intercept, r_value, p_value, std_err = st.linregress(df[x_values],df[y_values])

    #generate predicted y values based on regression model
    regress_values = df[x_values] * slope + intercept

    #store linear regression equation and correlation coefficient
    line_eq = "ŷ = " + str(round(slope,4)) + "x + " + str(round(intercept,4))
    corr_coef = "r = " + str(round(r_value,4))
    r_2 = "r^2 = " + str(round(r_value**2,4))

    #plot regression line
    plt.plot(df[x_values], regress_values, "r-")

    #plot regression equation and correlation coefficient on the graph
    plt.annotate(line_eq, (ex,(ey)),fontsize = 12, color = 'red')
    plt.annotate(corr_coef,(ex,(ey-15)),fontsize = 12, color = 'red')
    plt.annotate(r_2,(ex,(ey-30)),fontsize = 12, color = 'red')
    #plt.annotate("New York", (20000000,14000),fontsize =12, color = 'red')
    #plt.annotate("California", (35000000,2000),fontsize =12, color = 'red')
    #plt.annotate("New Jersey", (5000000,6000),fontsize =12, color = 'red')

    #Create scatter plot and add title, x-labels, and y-labels
    plt.scatter(df[x_values], df[y_values])
    plt.title(f"{x_values} vs {y_values}")
    plt.xlabel(x_values)
    plt.ylabel(y_values)
    #plt.tight_layout()
    #plt.savefig(f"Graphics/{x_values}vs{y_values}.png")


#Generate Scatter Plot, Regression Line, r, r^2 of Rank vs Pick Overall
def linregcomp(df,x_values,y_values,r,c,ex,ey):
   
    class row:
        pass
    
    
    #run linear regression and store key values
    slope, intercept, r_value, p_value, std_err = st.linregress(df[x_values],df[y_values])

    #generate predicted y values based on regression model
    regress_values = df[x_values] * slope + intercept

    #store linear regression equation and correlation coefficient
    line_eq = "ŷ = " + str(round(slope,4)) + "x + " + str(round(intercept,4))
    corr_coef = "r = " + str(round(r_value,4))
    r_2 = "r^2 = " + str(round(r_value**2,4))

    #plot regression line
    axs[r,c].plot(df[x_values], regress_values, "r-")

    #plot regression equation and correlation coefficient on the graph
    #axs[r,c].annotate(line_eq, (ex,(ey)),fontsize = 12, color = 'red')
    #axs[r,c].annotate(corr_coef,(ex,(ey-15)),fontsize = 12, color = 'red')
    axs[r,c].annotate(r_2,(ex,(ey-30)),fontsize = 12, color = 'red')
    

    #Create scatter plot and add title, x-labels, and y-labels
    axs[r,c].scatter(df[x_values], df[y_values])
    #row.set_title(f"{x_values} vs {y_values}")
    #row.set_xlabel(x_values)
    #row.set_ylabel(y_values)
    #row.tight_layout()
    #plt.savefig(f"Graphics/{x_values}vs{y_values}.png")


f,(ax1,ax2) = plt.subplots(1,2,figsize = (10,5))

#linregcomp(drafted2019,"Rank","Pick Overall",ax1,150,50)
#linregcomp(drafted2019,"Grade","Pick Overall",ax2,30,50)
#plt.savefig("Graphics/ComparingRankGrade")
plt.show()


# Though it may be hard to tell at first glance these graphs tell the same story because the grade and rank are correlated.  I was curious which had a higher correlation with overall pick, so I ran a regression for both and found Grade to be a better predictor so I will observe grade moving forward.


x_values = drafted2019['Grade']
y_values = drafted2019['Pick Overall']
x_values = sm.add_constant(x_values)
# Note the difference in argument order
model = sm.OLS(y_values, x_values).fit()
predictions = model.predict(x_values) # make the predictions by the model

# Print out the statistics
model.summary()


positions = drafted2019["Position"].unique()

posdfs ={i:drafted2019[drafted2019["Position"]==i] for i in positions}

posdfs["WR"]

linregsingle(posdfs["QB"],"Grade","Pick Overall",40,50)

linregsingle(posdfs["WR"],"Grade","Pick Overall",40,50)

linregsingle(posdfs["DE"],"Grade","Pick Overall",40,50)


f,(axs) = plt.subplots(3,5,figsize = (15,12))
#(ax1,ax2,ax3,ax4,ax5),(ax6,ax7,ax8,ax9,ax10),(ax11,ax12,ax13,ax14,ax15)=axs

# linregcomp(posdfs["DE"],"Grade","Pick Overall",0,0,30,50)
# ax1.set_title("DE")
r=0
c=0
across = [0,1,2,3,5,6,7,8]
for i in range(len(positions)):
    
#     if (i == 0):
#         linregcomp(posdfs[positions[i]],"Grade","Pick Overall",r,c,50,50)
#         axs[r,c].set_title(positions[i])
#         c=c+1
        
#     else:
        if (i+1)%5 == 0:
            
            
            linregcomp(posdfs[positions[i]],"Grade","Pick Overall",r,c,50,50)
            axs[r,c].set_title(positions[i])
            r=r+1
            c=0
            
            
           
        else:
            linregcomp(posdfs[positions[i]],"Grade","Pick Overall",r,c,50,50)
            axs[r,c].set_title(positions[i])
            c=c+1
           

len(positions)

for i in range(len(positions)):
    print(i%5)


