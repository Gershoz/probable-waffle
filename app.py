from pytrends.request import TrendReq
import pandas as pd
from matplotlib import pyplot
import time

startTime = time.time()
pytrend = TrendReq(hl='en-US', tz=360)

keywords = ['Covid','Corona','China']
pytrend.build_payload(
     kw_list=keywords,
     cat=0,
     timeframe='2020-02-01 2023-09-01',
     geo='US',
     gprop='')
     
data = pytrend.interest_over_time()
data.plot(title="Google Search Trends")
pyplot.show()