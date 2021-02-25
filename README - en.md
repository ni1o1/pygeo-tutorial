
[中文](README.md)

# How to use this tutorial
This tutorial is written on the jupyter notebook of Python. Some basic environments of Python need to be configured:
1. Python environment: Python 3.6 / 3.7 can be used. It is recommended to install an Anaconda here. Click [this link](https://www.anaconda.com/distribution/) to download and install (Python is a programming language, anaconda is a python platform that packs common functions of data analysis. Installing Anaconda already include Python)
See [this link](https://blog.csdn.net/m0_37438418/article/details/80620190) for how to use Anaconda's jupyter notebook
2. Download this tutorial to local, click clone or download in the upper right corner of this page, and use git clone or download zip to download to local.
3. Install the core package of this tutorial: Python's geopandas package. Click [this link](https://geopandas.readthedocs.io/en/latest/install.html#installing-from-source) to install a (actually, I recommend the installation from source method).
4. Open the tutorial, enjoy!

# Catalog

[1 Basic processing of taxi GPS data: generating OD for trips - pandas](1-taxigps_to_od_en.ipynb)   
[2 Plotting figures of data aggregation- matplotlib](2-plot_figures_by_matplotlib_and_seaborn_en.ipynb)   
[3 Gis processing of taxi GPS data - geopandas](3-taxigps_data_geo_processing_en.ipynb)    
[4 Match grid OD to administrative units and plot map background - plot_map](4-taxigps_data_OD_plot_en.ipynb)    
[5 The scatter and heatmap plot of data distribution - contourf](5-scatterplot-contourfplot_en.ipynb)    
[6 How to deal with a complicate data processing tasks? - theoretical](6-structure_en.ipynb)    
[7 Use folium to visualize map - folium](8-folium_en.ipynb)    

# About this tutorial
With the coming of the era of big data and with the gradual opening of data, data workers are more or less facing spatiotemporal data.
>Xiaoxu once said：The data is data since it's data.  

Yes! Data processing is an art! When dealing with spatiotemporal data, you need not only the skill of data processing, but also GIS. The most important thing is that it's an art. You need to use your aesthetics and produce beautiful figures!
  
Before I learn how to use python, I used to use SQL database to process data, export it to Excel to draw charts, and then export it to ArcGIS to draw maps. A set of process has several software, and the work efficiency is very low.

>Last time, the teacher said to me: Xiao Xu, please give me 800 figures for this project. I need them this Friday. In fact, it's useless to draw this. It's mainly to show our workload in the appendix of our project text.  
I flipped the table and said: Draw these by yourself, I quit!  
No, it's a dream. The reality is: I smile and say, ok, I will draw all night  


Now, we have python. With the pandas, geopandas, and Matplotlib packages in Python, you use Python to realize batch calculation of data, batch production of GIS maps, and so on. 
  
WOW! That is great! You definitely need necessary skill if you are a student in graduate school and eager for data analysis. Let alone 800 figures. I can generate as many figures as there is in the computer space!

Through this tutorial, you will learn some processing skills of spatiotemporal data from the beginning, such as data cleaning, data collection, data integration and visualization with Python! After that, this tutorial introduces several commonly used Python visualization packages, and finally the actual project
  
Demos(all plotted by python):  
<img src="resource/map-example.png" style="width:600px">
<img src="resource/heatmap-example.png" style="width:600px">

# Data
Data sources for this tutorial (open datasets can be downloaded directly): 
[Taxi data in Shenzhen](https://www.cs.rutgers.edu/~dz220/data.html)  
Urban Data Release V2  
Taxi GPS Data Format: 22223,2013-10-22 08:49:25,114.116631,22.582466,0  
Taxi ID, Time, Latitude, Longitude, Occupancy Status, Speed; Occupancy Status: 1-with passengers & 0-with passengers;  
    
# Basics skills you need for this tutorial
Before learning this tutorial, it is strongly recommended that you have learn the most basic programming skill of Python. If you haven't, here are some suggestions:

[小甲鱼的python入门视频（看到35P）(in Chinese)](https://www.bilibili.com/video/av27789609?from=search&seid=5111701058031824734)  

In addition, some recommended courses:

1. [imooc的Python数据分析-基础技术篇教程(in Chinese)](https://www.imooc.com/learn/843)
2. [python data analysis in udacity(in English)](https://classroom.udacity.com/courses/ud170/)
3. [machine learning in coursera(in English)](https://www.coursera.org/learn/machine-learning)
4. [莫烦PYTHON的pytorch动态神经网络课程(in Chinese)](https://morvanzhou.github.io/tutorials/machine-learning/torch/)
