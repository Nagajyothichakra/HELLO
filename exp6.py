#1.character vector
color=c('red','green','yello')
class(color)



#2.numeric vector
year=c(2010,2011,2012)
class(year)



#3.create dataframe
a=c(1,2,3,4)
b=c("book","pen","text_book","pencil")
c=c(TRUE,FALSE,TRUE,FALSE)
d=c(2.5,8,7,10)
df=data.frame(a,b,c,d)
df



#4.create existing dataframe quantity
quantity=c(10,35,40,5)
df$quantity=quantity
df



#5.create ordinal
day=c('morning','afternoon','evening','night','midnight')
factor_day=factor(day,order=TRUE,levels=c('morning','afternoon','evening','night','midnight'))
summary(factor_day)



#6.combine three integer vectors to 3x3 matrix
a=c(1,2,3)
b=c(4,5,6)
c=c(7,8,9)
m=cbind(a,b,c)
print("content of side matrix:")
print(m)


#7.to find sum,mean and product
num=c(10,20,30)
print("original vector")
print(num)
print(paste("sum of vector elements:",sum(num)))
print(paste("mean of vector elements:",mean(num)))
print(paste("product of vector elements:",prod(num)))




#8.to find max and min value of a given vector
num=c(10,20,30,40,50,60,70,80,90)
print('original vector')
print(num)
print(paste("maximum value of given vector is:",max(num)))
print(paste("minimum value of given vector is:",min(num)))





#9.print upper and lower case letters
print("first 13 letters in upper case: ")
t=head(LETTERS,13)
print(t)
print("last 13 letters in lower case: ")
t=tail(letters,13)
print(t)




#10.to display 10 random integer values between -50 to +50
v=sample(-50:+50,10,replace=TRUE)
print('content of the vector:')
print("10 random integer values between -50 to  +50")
print(v)



#11. to get the lenght of first three factors of a given list
list1=list(g1=1:10,g2="R programming",g3="HTML")
print("original list")
print(list1)
print("lenght of vector 'g1','g2' and 'g3' of the given list")
print(length(list1$g1))
print(length(list1$g2))
print(length(list1$g3))



#12.to find sequence,mean and sum of numbers from 20 to 50
print("sequence of numbers from 20 to 50:")
print(seq(20,50))
print("mean of numbers from 20 to 50:")
print(mean(20:50))
print("sum of numbers from 20 to 50:")
print(sum(20:50))



#13.to find factors of a given number
print_factors=function(x)
{
print(paste("the factors of",x,"are:"))
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




