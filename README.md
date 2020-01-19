# 教程目录

>[1-出租车数据的基础处理，由gps生成OD（pandas）](1-taxigps_to_od(pandas).ipynb)  
[2-出租车数据的地理信息处理（geopandas）](2-taxigps_data_geo_processing(geopandas).ipynb)  
[3-基于出租车GPS的OD期望线绘制与底图添加（plot_map）](3-taxigps_data_OD_plot.ipynb)  
[4-绘制数据分布的散点图和热力图（contourf）](4-scatterplot-contourfplot.ipynb)  
[5-爬虫爬API抓取行政区划](5-api_get_xzqh.ipynb)  
[6-基于folium的可交互地图可视化(folium)](6-folium.ipynb)  
[7-结构化数据的存储及处理的思维训练(理论课)](7-structure.ipynb)  
[8-实战项目：怎么当一个优秀的出租车手](8-project.ipynb)  

# 教程说明
大数据时代到来，随着数据的逐步开放，数据工作者们或多或少都要接触到时空数据。  
在处理时空数据的时候，你不仅要数据处理，还需要会GIS，最重要的是要出很好看的GIS图。  
  
以前，我要用sql数据库处理数据，导出到excel画图表，再导出到arcgis出图，一套流程下来得开好几个软件，工作效率极低。  

>上次老师跟我说：小旭啊，我们这个项目你给我出800张图吧，我这周五就要。这个其实画出来也没什么用，主要是想放我们项目文本的附录里显示我们的工作量  
我当场把桌子掀起来，画你妹！老子这博不读了  
不，以上是做梦，现实情况是: 我微笑着说，好的老师，我通宵画  


现在，python出现了，有了python里面的pandas，geopandas，matplotlib包，只需要用python就能实现数据的批量计算，批量出gis图等等。  
  
哇！太棒了！简直是读研、读博、设计院画图、数据分析、闲着没事、居家旅行时候都必须会的技能，别说800张图了，电脑空间有多少我就能生成多少图，包您满意

通过本教程，你将会学会怎么对时空数据处理，用python的matplotlib包绘制下面的GIS图  
<img src="resource/map-example.png" style="width:600px">
<img src="resource/heatmap-example.png" style="width:600px">

# 学习本教程需要的基础
在学习本教程之前，强烈建议各位已经掌握了python的最基础的编程语法。如果你还没有掌握，下面建议你完成：

[小甲鱼的python入门视频（看到35P）](https://www.bilibili.com/video/av27789609?from=search&seid=5111701058031824734)  


# 使用数据
用python分析时空数据的教程
数据来源：  
[深圳出租车数据](https://www.cs.rutgers.edu/~dz220/data.html)  
Urban Data Release V2  
Taxi GPS Data Format: 22223,2013-10-22 08:49:25,114.116631,22.582466,0  
Taxi ID, Time, Latitude, Longitude, Occupancy Status, Speed; Occupancy Status: 1-with passengers & 0-with passengers;  
    

