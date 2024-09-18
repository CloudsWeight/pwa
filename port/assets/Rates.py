'''
################################################################################################################################
#                                                                                                                              # 
#                                                                                   :                                          #
#           .                             ,;                                       t#,     L.                     ,;           #
#          ;W          j.               f#i                                       ;##W.    EW:        ,ft       f#i            #
#         f#E GEEEEEEELEW,            .E#t             ..           ..       :   :#L:WE    E##;       t#E     .E#t  f.     ;WE.#
#       .E#f  ,;;L#K;;.E##j          i#W,             ;W,          ,W,     .Et  .KG  ,#D   E###t      t#E    i#W,   E#,   i#G  #
#      iWW;      t#E   E###D.       L#D.             j##,         t##,    ,W#t  EE    ;#f  E#fE#f     t#E   L#D.    E#t  f#f   #
#     L##Lffi    t#E   E#jG#W;    :K#Wfff;          G###,        L###,   j###t f#.     t#i E#t D#G    t#E :K#Wfff;  E#t G#i    #
#    tLLG##L     t#E   E#t t##f   i##WLLLLt       :E####,      .E#j##,  G#fE#t :#G     GK  E#t  f#E.  t#E i##WLLLLt E#jEW,     #
#      ,W#i      t#E   E#t  :K#E:  .E#L          ;W#DG##,     ;WW; ##,:K#i E#t  ;#L   LW.  E#t   t#K: t#E  .E#L     E##E.      #
#     j#E.       t#E   E#KDDDD###i   f#E:       j###DW##,    j#E.  ##f#W,  E#t   t#f f#:   E#t    ;#W,t#E    f#E:   E#G        #
#   .D#j         t#E   E#f,t#Wi,,,    ,WW;     G##i,,G##,  .D#L    ###K:   E#t    f#D#;    E#t     :K#D#E     ,WW;  E#t        #
#  ,WK,          t#E   E#t  ;#W:       .D#;  :K#K:   L##, :K#t     ##D.    E#t     G#t     E#t      .E##E      .D#; E#t        #
#  EG.            fE   DWi   ,KK:        tt ;##D.    L##, ...      #G      ..       t      ..         G#E        tt EE.        #
#  ,               :                        ,,,      .,,           j                                   fE           t          #
#                                                                                                       ,                      #
################################################################################################################################
'''
import requests
import json 
import csv
from accts import accts
#from secret import SECRET 
import argparse
from datetime import datetime 

class OandaApp():
  '''
  A class to create an Oanda Stream for Rates
  '''
	def __init__(self, token=None, account=None):
		self.BASE_URL ='https://api-fxtrade.oanda.com'
		if account is not None:
			self.account = {
					'URL':f'{self.BASE_URL}/v3/accounts', # Accounts Endpoint
					'acctId': account,
					'current':f'{account}'
					}
		self.account = {
					'URL':f'{self.BASE_URL}/v3/accounts', # Accounts Endpoint
					'acctId': accts,
					'current':f'{accts[0]}'
						}
		#if token is None:
			#self.token = SECRET
		self.token = token
		self.HEADER = { # Headers and Auth
					'Authorization': 'Bearer {}'.format('13371337133713371337'),
				} 
		self.ENDPOINT = { 
						'instruments':f'{self.BASE_URL}/v3/instruments/',
						'candles': f'{self.BASE_URL}/candles?',
						}
		self.instruments = {
					# CURRENCY PAIRS
					'URL':f'{self.BASE_URL}/v3/instruments/', 
					'current':'USD_JPY',
					'eurusd':'EUR_USD', 
					'usdjpy':'USD_JPY', 
					'usdchf':'USD_CHF', 
					}
		self.count = {
						'URL':'count=',
						'current':'3' # [default=500, maximum=5000] dont use with "FROM and TO"
						}
		self.candles = {'URL':'/candles?',
						'granularity':{
						'current':'&granularity=H4',
						'5s':'&granularity=S5',
						'5m':'&granularity=M5',
						'15m':'&granularity=M15',
						'1h':'&granularity=H1', 
						'4h':'&granularity=H4',
						'd':'&granularity=D',
						'w':'&granularity=W',
						'M':'&granularity=M',
						 },
					}
		self.current_url = (
			 f"{self.instruments['URL']}{self.instruments['current']}"
			 f"{self.candles['URL']}"
			 f"{self.count['URL']}{self.count['current']}"
			 f"{self.candles['granularity']['current']}"
			 				) # As Above So Below
	# Example:	https://api-fxtrade.oanda.com/v3/instruments/EUR_USD/candles?count=6&price=M&granularity=S5
	######################## methods, man
	def query_accounts(self, url=None, header=None):
		if header is None:
			header = self.HEADER
		if url is None:
			url = f"{self.account['URL']}"
		r = requests.get(url=url, headers=header)
		print(f"{r.status_code}, /n {r.content}")

	def query_account(self, url=None, header=None):
		if header is None:
			header = self.HEADER
		if url is None:
			url = f"{self.account['URL']}/{self.account['current']}"
			print(url)
		r = requests.get(url=url, headers=header)
		print(f"{r.status_code}")

	def query_rate(self, url=None, header=None):
		if header is None:
			header = self.HEADER
		if url is None:
			url = self.current_url
		#print(f"\nURL: {self.current_url}")
		r = requests.get(url=url, headers=header)
		#print(r.status_code)
		#print(r.content)
		json_content = r.content.decode('utf-8')
		return(json_content)

	def deserialize(self, bin_data=None):
		if json is None:
			print("must provide binary data")
		else:
			json_string = bin_data.decode('utf-8')
			json_data = json.loads(json_string)
			#print(json.dumps(json_data, indent=2))
		return json_data

	def update_current_url(self): # if you make changes then update with this method 
		self.current_url = (
					 f"{self.instruments['URL']}{self.instruments['current']}"
					 f"{self.candles['URL']}"
					 f"{self.count['URL']}{self.count['current']}"
					 f"{self.candles['granularity']['current']}"
					 )

	def set_rate(self, rate=None):
		if rate is None:
			print("No rate set no change made")
		rate = rate.lower()
		self.instruments['current'] = self.instruments[rate]
		print(f"new rate {self.instruments['current']}\n ")     
		self.update_current_url()

	def test_query(self):
		rates = self.query_rate()
		return rates

################## Enter the dragon
if __name__ == '__main__':
	#print("Null stuff")
	trade = OandaApp()
	try:
		rates = trade.test_query()
	except:
		pass
	print(rates)


	

