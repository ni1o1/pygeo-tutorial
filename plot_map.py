
import pandas as pd
import numpy as np

import math

import urllib
import io
from PIL import Image

def deg2num(lat_deg, lon_deg, zoom):
    lat_rad = math.radians(lat_deg)
    n = 2.0 ** zoom
    xtile = int((lon_deg + 180.0) / 360.0 * n)
    ytile = int((1.0 - math.log(math.tan(lat_rad) + (1 / math.cos(lat_rad))) / math.pi) / 2.0 * n)
    return (xtile, ytile)

def num2deg(xtile, ytile, zoom):
    n = 2.0 ** zoom
    lon_deg = xtile / n * 360.0 - 180.0
    lat_rad = math.atan(math.sinh(math.pi * (1 - 2 * ytile / n)))
    lat_deg = math.degrees(lat_rad)
    return (lat_deg, lon_deg)



def getImageCluster( lon_deg,lat_deg,   delta_long, delta_lat,zoom,style,printlog,imgsavepath,apikey = '',access_token = '',styleid = 'cjrewwj3l2dwt2tptkiu09scd'):
    '''
    apikey - openstreetmap token
    access_token - mapbox token
    '''
    if style == 1:
        smurl = r'https://a.tile.thunderforest.com/cycle/{0}/{1}/{2}.png?apikey='+apikey
    if style == 2:
        smurl = r'https://a.tile.thunderforest.com/transport/{0}/{1}/{2}.png?apikey='+apikey
    if style == 3:
        smurl = r'https://tile-b.openstreetmap.fr/hot/{0}/{1}/{2}.png'
    if style == 4:
        smurl = r'https://tiles.wmflabs.org/bw-mapnik/{0}/{1}/{2}.png'
    if style == 5:
        smurl = r'http://a.tile.stamen.com/toner/{0}/{1}/{2}.png'
    if style == 6:
        smurl = r'http://c.tile.stamen.com/watercolor/{0}/{1}/{2}.png'
    if style == 7:
        if styleid == 'dark':
            styleid = 'cjetnd20i1vbi2qqxbh0by7p8'
        if styleid == 'light':
            styleid = 'cjrewwj3l2dwt2tptkiu09scd'
        smurl = r'https://api.mapbox.com/styles/v1/ni1o1/'+styleid+r'/tiles/256/{0}/{1}/{2}?&access_token='+access_token
    else:
        styleid = ''
    xmin, ymax =deg2num(lat_deg, lon_deg, zoom)
    xmax, ymin =deg2num(lat_deg + delta_lat, lon_deg + delta_long, zoom)
    
    def get_img(smurl,zoom, xtile, ytile,imgsize,imgsavepath):
        import os
        
        filename = str(style)+str(styleid)+'-'+str(zoom)+'-'+str(xtile)+'-'+str(ytile)+'-'+str(imgsize)+'.png'
        def savefig(filename,tile):
            try:
                if 'tileimg' in os.listdir(imgsavepath):
                    if filename in os.listdir(imgsavepath+'tileimg'):
                        pass
                    else:
                        tile.save(imgsavepath+'tileimg\\'+filename)
                        print('figsaved:'+filename)
                else:
                    os.mkdir(imgsavepath+'tileimg')
            except:
                pass
        def loadfig(filename):
            try:
                if 'tileimg' in os.listdir(imgsavepath):
                    if filename in os.listdir(imgsavepath+'tileimg'):
                        tile = Image.open(imgsavepath+'tileimg\\'+filename)
                        return tile
                    else:
                        return None
                else:
                    os.mkdir(imgsavepath+'tileimg')
                    return None
            except:
                return None
        tile = loadfig(filename)
        if tile is None:
            try:
                t = 0
                while t<10:
                    try:
                        imgurl=smurl.format(zoom, xtile, ytile)
                        #print("Opening: " + imgurl)
                        imgstr = urllib.request.urlopen(imgurl,timeout = 6).read()
                        tile = Image.open(io.BytesIO(imgstr))
                        savefig(filename,tile)
                        Cluster.paste(tile, box=((xtile-xmin)*imgsize ,  (ytile-ymin)*imgsize))
                        t = 10
                    except:
                        if printlog:
                            print('Get map tile failed, retry ',t)
                        t += 1
            except: 
                print("Couldn't download image")
                tile = None
        else:
            Cluster.paste(tile, box=((xtile-xmin)*imgsize ,  (ytile-ymin)*imgsize))

    imgsize = 256
    import threading
    threads = []
    Cluster = Image.new('RGB',((xmax-xmin+1)*imgsize-1,(ymax-ymin+1)*imgsize-1)) 
    for xtile in range(xmin, xmax+1):
        for ytile in range(ymin,  ymax+1):
            threads.append(threading.Thread(target=get_img,args = (smurl,zoom, xtile, ytile,imgsize,imgsavepath)))
    for t in threads:
        t.setDaemon(True)
        t.start()
    for t in threads:
        t.join()
    threads.clear()
    
    return Cluster

    
def plot_map(plt,bounds,zoom,style,imgsavepath = 'C:\\',printlog = False,apikey = '',access_token = '',styleid = 'dark'):
    '''
    bounds -- Set your plotting boundary [lon1,lat1,lon2,lat2] (wgs1984)
    zoom -- The zoom level of the map
    style -- From 1 to 7 represent different map styles,1-6 is from openstreetmap and 7 is the mapbox
    styleid -- if style is set as 7(from mapbox), you can change the styleid here, "dark" or "light" or your own style
    imgsavepath -- Path to save the tile map so that you don't have to download again
    '''
    try:
        import os
        os.listdir(imgsavepath)
    except:
        print('imgsavepath do not exist, your tile map will not save')
    lon1= bounds[0]
    lat1 =  bounds[1]
    lon2 =  bounds[2]
    lat2 =  bounds[3]
    a = getImageCluster(lon1, lat1, lon2-lon1,  lat2-lat1, zoom,style,printlog = printlog,imgsavepath = imgsavepath,apikey = apikey,access_token = access_token, styleid = styleid)
    x1, y1 =deg2num(lat1, lon1, zoom)
    x2, y2 =deg2num(lat2, lon2, zoom)
    x1,y1 = num2deg(x1, y1+1, zoom)
    x2,y2 = num2deg(x2+1, y2, zoom)
    plt.imshow(np.asarray(a),extent = (y1,y2,x1+0.00,x2+0.00))

def plotscale(ax,bounds,textcolor = 'k',textsize = 8,compasssize = 1,accuracy = 'auto',rect=[0.1,0.1],unit = "KM",style = 1):
    
    #栅格化代码
    import math

    #划定栅格划分范围
    lon1 = bounds[0]
    lat1 = bounds[1]
    lon2 = bounds[2]
    lat2 = bounds[3]
    latStart = min(lat1, lat2);
    lonStart = min(lon1, lon2);
    if accuracy == 'auto':
        accuracy = (int((lon2-lon1)/0.0003/1000+0.5)*1000)
    a,c=rect
    b = 1-a
    d = 1-c
    alon,alat = (b*lon1+a*lon2)/(a+b),(d*lat1+c*lat2)/(c+d)

    #计算栅格的经纬度增加量大小▲Lon和▲Lat
    deltaLon = accuracy * 360 / (2 * math.pi * 6371004 * math.cos((lat1 + lat2) * math.pi / 360));
    
    #加比例尺
    
    from shapely.geometry import Polygon
    import geopandas as gpd
    if style == 1:
        scale = gpd.GeoDataFrame({'color':[(0,0,0),(1,1,1),(0,0,0),(1,1,1)],'geometry':
        [Polygon([(alon,alat),(alon+deltaLon,alat),(alon+deltaLon,alat+deltaLon*0.4),(alon,alat+deltaLon*0.4)]),
        Polygon([(alon+deltaLon,alat),(alon+2*deltaLon,alat),(alon+2*deltaLon,alat+deltaLon*0.4),(alon+deltaLon,alat+deltaLon*0.4)]),
        Polygon([(alon+2*deltaLon,alat),(alon+4*deltaLon,alat),(alon+4*deltaLon,alat+deltaLon*0.4),(alon+2*deltaLon,alat+deltaLon*0.4)]),
        Polygon([(alon+4*deltaLon,alat),(alon+8*deltaLon,alat),(alon+8*deltaLon,alat+deltaLon*0.4),(alon+4*deltaLon,alat+deltaLon*0.4)])
        ]})
        scale.plot(ax = ax,edgecolor= (0,0,0,1),facecolor = scale['color'],lw = 0.6)

        if (unit == 'KM')|(unit == 'km'):
            ax.annotate(str(int(accuracy/1000)),color = textcolor,size = textsize,xy=(alon+deltaLon,alat+deltaLon*0.2), xytext=(-textsize*3/5,textsize/1.5), textcoords='offset points')
            ax.annotate(str(int(2*accuracy/1000)),color = textcolor,size = textsize,xy=(alon+2*deltaLon,alat+deltaLon*0.2), xytext=(-textsize*3/5,textsize/1.5), textcoords='offset points')
            ax.annotate(str(int(4*accuracy/1000)),color = textcolor,size = textsize,xy=(alon+4*deltaLon,alat+deltaLon*0.2), xytext=(-textsize*3/5,textsize/1.5), textcoords='offset points')
            ax.annotate(str(int(8*accuracy/1000)),color = textcolor,size = textsize,xy=(alon+8*deltaLon,alat+deltaLon*0.2), xytext=(-textsize*3/5,textsize/1.5), textcoords='offset points')
            ax.annotate(unit,size = textsize,color = textcolor,xy=(alon+8*deltaLon,alat+deltaLon*0.1), xytext=(textsize*2/5,-textsize/5), textcoords='offset points')
        if (unit == 'M')|(unit == 'm'):
            ax.annotate(str(int(accuracy)),color = textcolor,size = textsize,xy=(alon+deltaLon,alat+deltaLon*0.2), xytext=(-textsize*3/5,textsize/1.5), textcoords='offset points')
            ax.annotate(str(int(2*accuracy)),color = textcolor,size = textsize,xy=(alon+2*deltaLon,alat+deltaLon*0.2), xytext=(-textsize*3/5,textsize/1.5), textcoords='offset points')
            ax.annotate(str(int(4*accuracy)),color = textcolor,size = textsize,xy=(alon+4*deltaLon,alat+deltaLon*0.2), xytext=(-textsize*3/5,textsize/1.5), textcoords='offset points')
            ax.annotate(str(int(8*accuracy)),color = textcolor,size = textsize,xy=(alon+8*deltaLon,alat+deltaLon*0.2), xytext=(-textsize*3/5,textsize/1.5), textcoords='offset points')
            ax.annotate(unit,size = textsize,color = textcolor,xy=(alon+8*deltaLon,alat+deltaLon*0.1), xytext=(textsize*2/5,-textsize/5), textcoords='offset points')
    if style == 2:
        scale = gpd.GeoDataFrame({'color':[(0,0,0),(1,1,1)],'geometry':
        [Polygon([(alon+deltaLon,alat),(alon+4*deltaLon,alat),(alon+4*deltaLon,alat+deltaLon*0.4),(alon+deltaLon,alat+deltaLon*0.4)]),
        Polygon([(alon+4*deltaLon,alat),(alon+8*deltaLon,alat),(alon+8*deltaLon,alat+deltaLon*0.4),(alon+4*deltaLon,alat+deltaLon*0.4)])
        ]})
        scale.plot(ax = ax,edgecolor= (0,0,0,1),facecolor = scale['color'],lw = 0.6)

        if (unit == 'KM')|(unit == 'km'):
            ax.annotate(str(int(4*accuracy/1000)),color = textcolor,size = textsize,xy=(alon+4*deltaLon,alat+deltaLon*0.2), xytext=(-textsize*3/5,textsize/1.5), textcoords='offset points')
            ax.annotate(str(int(8*accuracy/1000)),color = textcolor,size = textsize,xy=(alon+8*deltaLon,alat+deltaLon*0.2), xytext=(-textsize*3/5,textsize/1.5), textcoords='offset points')
            ax.annotate(unit,size = textsize,color = textcolor,xy=(alon+8*deltaLon,alat+deltaLon*0.1), xytext=(textsize*2/5,-textsize/5), textcoords='offset points')
        if (unit == 'M')|(unit == 'm'):
            ax.annotate(str(int(4*accuracy)),color = textcolor,size = textsize,xy=(alon+4*deltaLon,alat+deltaLon*0.2), xytext=(-textsize*3/5,textsize/1.5), textcoords='offset points')
            ax.annotate(str(int(8*accuracy)),color = textcolor,size = textsize,xy=(alon+8*deltaLon,alat+deltaLon*0.2), xytext=(-textsize*3/5,textsize/1.5), textcoords='offset points')
            ax.annotate(unit,size = textsize,color = textcolor,xy=(alon+8*deltaLon,alat+deltaLon*0.1), xytext=(textsize*2/5,-textsize/5), textcoords='offset points')

    #加指北针
    deltaLon = compasssize*deltaLon
    alon = alon-deltaLon
    compass = gpd.GeoDataFrame({'color':[(0,0,0),(1,1,1)],'geometry':
    [Polygon([[alon,alat],[alon,alat+deltaLon],[alon+1/2*deltaLon,alat-1/2*deltaLon]]),
    Polygon([[alon,alat],[alon,alat+deltaLon],[alon-1/2*deltaLon,alat-1/2*deltaLon]])]})
    compass.plot(ax= ax, edgecolor= (0,0,0,1),facecolor = compass['color'],lw = 0.6)
    ax.annotate('N',color = textcolor,size = textsize,xy=[alon,alat+deltaLon], xytext=(-textsize*2/5,textsize/2), textcoords='offset points')