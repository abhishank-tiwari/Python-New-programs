import pandas as pd
import matplotlib.pyplot as plt
import os 
os.getcwd()           
#get current working directory
dataa = pd.read_csv(".\csv\exms.csv")
dataa
#Find the name of column whose variance is to be found
print(dataa["age"].var())