# -*- coding: utf-8 -*-
import numpy as np
import math
x_pi = 3.14159265358979324 * 3000.0 / 180.0
pi = 3.1415926535897932384626  # π
a = 6378245.0  # 长半轴
ee = 0.00669342162296594323  # 扁率
# WGS-84 转换为 GCJ-02 
def gcj02tobd09(lng, lat):
    """
    火星坐标系(GCJ-02)转百度坐标系(BD-09)
    谷歌、高德——>百度
    :param lng:火星坐标经度
    :param lat:火星坐标纬度
    :return:
    """
    z = np.sqrt(lng * lng + lat * lat) + 0.00002 * np.sin(lat * x_pi)
    theta = np.arctan2(lat, lng) + 0.000003 * np.cos(lng * x_pi)
    bd_lng = z * np.cos(theta) + 0.0065
    bd_lat = z * np.sin(theta) + 0.006
    return bd_lng, bd_lat


def bd09togcj02(bd_lon, bd_lat):
    """
    百度坐标系(BD-09)转火星坐标系(GCJ-02)
    百度——>谷歌、高德
    :param bd_lat:百度坐标纬度
    :param bd_lon:百度坐标经度
    :return:转换后的坐标列表形式
    """
    x = bd_lon - 0.0065
    y = bd_lat - 0.006
    z = np.sqrt(x * x + y * y) - 0.00002 * np.sin(y * x_pi)
    theta = np.arctan2(y, x) - 0.000003 * np.cos(x * x_pi)
    gg_lng = z * np.cos(theta)
    gg_lat = z * np.sin(theta)
    return gg_lng, gg_lat


def wgs84togcj02(lng, lat):
    """
    WGS84转GCJ02(火星坐标系)
    :param lng:WGS84坐标系的经度
    :param lat:WGS84坐标系的纬度
    :return:
    """

    dlat = transformlat(lng - 105.0, lat - 35.0)
    dlng = transformlng(lng - 105.0, lat - 35.0)
    radlat = lat / 180.0 * pi
    magic = np.sin(radlat)
    magic = 1 - ee * magic * magic
    sqrtmagic = np.sqrt(magic)
    dlat = (dlat * 180.0) / ((a * (1 - ee)) / (magic * sqrtmagic) * pi)
    dlng = (dlng * 180.0) / (a / sqrtmagic * np.cos(radlat) * pi)
    mglat = lat + dlat
    mglng = lng + dlng
    return mglng, mglat


def gcj02towgs84(lng, lat):
    """
    GCJ02(火星坐标系)转GPS84
    :param lng:火星坐标系的经度
    :param lat:火星坐标系纬度
    :return:
    """

    dlat = transformlat(lng - 105.0, lat - 35.0)
    dlng = transformlng(lng - 105.0, lat - 35.0)
    radlat = lat / 180.0 * pi
    magic = np.sin(radlat)
    magic = 1 - ee * magic * magic
    sqrtmagic = np.sqrt(magic)
    dlat = (dlat * 180.0) / ((a * (1 - ee)) / (magic * sqrtmagic) * pi)
    dlng = (dlng * 180.0) / (a / sqrtmagic * np.cos(radlat) * pi)
    mglat = lat + dlat
    mglng = lng + dlng
    return lng * 2 - mglng, lat * 2 - mglat

def wgs84tobd09(lon,lat):
    lon,lat = wgs84togcj02(lon,lat)
    lon,lat = gcj02tobd09(lon,lat)
    return lon,lat

def bd09towgs84(lon,lat):
    lon,lat = bd09togcj02(lon,lat)
    lon,lat = gcj02towgs84(lon,lat)
    return lon,lat

def transformlat(lng, lat):
    ret = -100.0 + 2.0 * lng + 3.0 * lat + 0.2 * lat * lat + \
        0.1 * lng * lat + 0.2 * np.sqrt(np.fabs(lng))
    ret += (20.0 * np.sin(6.0 * lng * pi) + 20.0 *
            np.sin(2.0 * lng * pi)) * 2.0 / 3.0
    ret += (20.0 * np.sin(lat * pi) + 40.0 *
            np.sin(lat / 3.0 * pi)) * 2.0 / 3.0
    ret += (160.0 * np.sin(lat / 12.0 * pi) + 320 *
            np.sin(lat * pi / 30.0)) * 2.0 / 3.0
    return ret


def transformlng(lng, lat):
    import numpy as np
    ret = 300.0 + lng + 2.0 * lat + 0.1 * lng * lng + \
        0.1 * lng * lat + 0.1 * np.sqrt(np.abs(lng))
    ret += (20.0 * np.sin(6.0 * lng * pi) + 20.0 *
            np.sin(2.0 * lng * pi)) * 2.0 / 3.0
    ret += (20.0 * np.sin(lng * pi) + 40.0 *
            np.sin(lng / 3.0 * pi)) * 2.0 / 3.0
    ret += (150.0 * np.sin(lng / 12.0 * pi) + 300.0 *
            np.sin(lng / 30.0 * pi)) * 2.0 / 3.0
    return ret

def getdistance(lon1, lat1, lon2, lat2): # 经度1，纬度1，经度2，纬度2 （十进制度数）输入为DataFrame的列
    # 将十进制度数转化为弧度
    lon1, lat1, lon2, lat2 = map(lambda r:r*pi/180, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = np.sin(dlat/2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2)**2
    c = 2 * np.arcsin(a**0.5) 
    r = 6371 # 地球平均半径，单位为公里
    return c * r * 1000