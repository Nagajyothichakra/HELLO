import matplot.pyplot as plt
#pass the x and y cordinates of the bars to the function
#the label argument gives a label to the data
plt.bar([1,3,5,7,9],[5,2,7,8,2],label="data 1")
plt.legend()
#the growing commands add labels to out figure
plt.xlabel('xvalues')
plt.ylabel('height')
plt.title('vertical bar chart')
plt.show()