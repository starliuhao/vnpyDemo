# -*- encoding: utf-8 -*-
""""
@File    :   cutData.py    
@Contact :   liuhaobwjc@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019-01-21 13:19   liuhao      1.0         None
"""
import pandas as pd


data = pd.read_csv("tick_data.csv")
print data.shape
my_data = data[1:200000]
my_data.to_csv("tick_data_adf.csv", index=False)

