import QUANTAXIS as QA
import sys
QA.QA_util_log_info('='*10)
QA.QA_util_log_info('日线数据')
QA.QA_util_log_info('不复权')  
data=QA.QAFetch.QATdx.QA_fetch_get_stock_day('00001','2017-01-01','2017-01-31')
QA.QA_util_log_info(data)
QA.QA_util_log_info(QA.QA_util_to_json_from_pandas(data.head(1)))
QA.QA_util_log_info('前复权')
data=QA.QAFetch.QATdx.QA_fetch_get_stock_day('00001','2017-01-01','2017-01-31','01')
QA.QA_util_log_info(data)
QA.QA_util_log_info(QA.QA_util_to_json_from_pandas(data.head(1)))
QA.QA_util_log_info('后复权')
data=QA.QAFetch.QATdx.QA_fetch_get_stock_day('00001','2017-01-01','2017-01-31','02')
QA.QA_util_log_info(data)
QA.QA_util_log_info(QA.QA_util_to_json_from_pandas(data.head(1)))
QA.QA_util_log_info('定点前复权')
data=QA.QAFetch.QATdx.QA_fetch_get_stock_day('00001','2017-01-01','2017-01-31','03')
QA.QA_util_log_info(data)
QA.QA_util_log_info(QA.QA_util_to_json_from_pandas(data.head(1)))
QA.QA_util_log_info('定点后复权')
data=QA.QAFetch.QATdx.QA_fetch_get_stock_day('00001','2017-01-01','2017-01-31','04')
QA.QA_util_log_info(data)
QA.QA_util_log_info(QA.QA_util_to_json_from_pandas(data.head(1)))
QA.QA_util_log_info('='*10)
QA.QA_util_log_info('='*10)
QA.QA_util_log_info('分钟线')
QA.QA_util_log_info('1min')
data=QA.QAFetch.QATdx.QA_fetch_get_stock_min('000001','2017-07-01','2017-08-01','1min')
QA.QA_util_log_info(data)
QA.QA_util_log_info(QA.QA_util_to_json_from_pandas(data.head(1)))
QA.QA_util_log_info('5min')
data=QA.QAFetch.QATdx.QA_fetch_get_stock_min('000001','2017-07-01','2017-08-01','5min')
QA.QA_util_log_info(data)
QA.QA_util_log_info(QA.QA_util_to_json_from_pandas(data.head(1)))
QA.QA_util_log_info('15min')
data=QA.QAFetch.QATdx.QA_fetch_get_stock_min('000001','2017-07-01','2017-08-01','15min')
QA.QA_util_log_info(data)
QA.QA_util_log_info(QA.QA_util_to_json_from_pandas(data.head(1)))
QA.QA_util_log_info('='*10)
QA.QA_util_log_info('='*10)
QA.QA_util_log_info('除权除息')
data=QA.QAFetch.QATdx.QA_fetch_get_stock_xdxr('00001')
QA.QA_util_log_info(data)
QA.QA_util_log_info(QA.QA_util_to_json_from_pandas(data.head(1)))
QA.QA_util_log_info('='*10)
QA.QA_util_log_info('='*10)
QA.QA_util_log_info('股票列表')
data=QA.QAFetch.QATdx.QA_fetch_get_stock_list('stock')
QA.QA_util_log_info(data)
QA.QA_util_log_info(QA.QA_util_to_json_from_pandas(data.head(1)))
QA.QA_util_log_info('指数列表')
data=QA.QAFetch.QATdx.QA_fetch_get_stock_list('index')
QA.QA_util_log_info(data)
QA.QA_util_log_info(QA.QA_util_to_json_from_pandas(data.head(1)))
QA.QA_util_log_info('全部列表')
data=QA.QAFetch.QATdx.QA_fetch_get_stock_list('all')
QA.QA_util_log_info(data)
QA.QA_util_log_info(QA.QA_util_to_json_from_pandas(data.head(1)))
QA.QA_util_log_info('='*10)
QA.QA_util_log_info('='*10)
QA.QA_util_log_info('指数日线')
data=QA.QAFetch.QATdx.QA_fetch_get_index_day('000001','2017-01-01','2017-09-01')
QA.QA_util_log_info(data)
QA.QA_util_log_info(QA.QA_util_to_json_from_pandas(data.head(1)))
QA.QA_util_log_info('='*10)
QA.QA_util_log_info('='*10)
QA.QA_util_log_info('指数分钟线')
QA.QA_util_log_info('1min')
data=QA.QAFetch.QATdx.QA_fetch_get_index_min('000001','2017-07-01','2017-08-01','1min')
QA.QA_util_log_info(data)
QA.QA_util_log_info(QA.QA_util_to_json_from_pandas(data.head(1)))
QA.QA_util_log_info('5min')
data=QA.QAFetch.QATdx.QA_fetch_get_index_min('000001','2017-07-01','2017-08-01','5min')
QA.QA_util_log_info(data)
QA.QA_util_log_info(QA.QA_util_to_json_from_pandas(data.head(1)))
QA.QA_util_log_info('15min')
data=QA.QAFetch.QATdx.QA_fetch_get_index_min('000001','2017-07-01','2017-08-01','15min')
QA.QA_util_log_info(data)
QA.QA_util_log_info(QA.QA_util_to_json_from_pandas(data.head(1)))
QA.QA_util_log_info('='*10)
QA.QA_util_log_info('='*10)
QA.QA_util_log_info('最后一次交易价格')
QA.QA_util_log_info('参数为列表')
data=QA.QAFetch.QATdx.QA_fetch_get_stock_latest(['000001','000002'])
QA.QA_util_log_info(data)
QA.QA_util_log_info(QA.QA_util_to_json_from_pandas(data.head(1)))
QA.QA_util_log_info('参数为一只股票')
data=QA.QAFetch.QATdx.QA_fetch_get_stock_latest('000001')
QA.QA_util_log_info(data)
QA.QA_util_log_info(QA.QA_util_to_json_from_pandas(data.head(1)))
QA.QA_util_log_info('='*10)
QA.QA_util_log_info('='*10)
QA.QA_util_log_info('实时价格')
data=QA.QAFetch.QATdx.QA_fetch_get_stock_realtime(['000001','000002'])
QA.QA_util_log_info(data)
QA.QA_util_log_info(QA.QA_util_to_json_from_pandas(data.head(1)))
QA.QA_util_log_info('='*10)
QA.QA_util_log_info('='*10)
QA.QA_util_log_info('分笔成交')
data=QA.QAFetch.QATdx.QA_fetch_get_stock_transaction('000001','2001-01-01','2001-01-15')
QA.QA_util_log_info(data)
QA.QA_util_log_info(QA.QA_util_to_json_from_pandas(data.head(1)))
QA.QA_util_log_info('='*10)
QA.QA_util_log_info('='*10)