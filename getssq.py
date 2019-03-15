# -*- coding: utf-8 -*-
import scrapy
from caipiao.items import CaipiaoItem

class GetssqSpider(scrapy.Spider):
	name = 'getssq'
	allowed_domains = ['zhcw.com']
	start_urls = ['http://kaijiang.zhcw.com/zhcw/html/ssq/list_%d.html' % i for i in xrange(1,115)]

	def parse(self, response):
		for sel in response.css('.wqhgt tr'):
			if sel.css('td:nth-child(2)::text').extract() == []:
				continue
			i = CaipiaoItem()
			i['num'] = sel.css('td:nth-child(2)::text').extract()
			i['qiuH1'] = sel.css('td em:nth-child(1)::text').extract()
			i['qiuH2'] = sel.css('td em:nth-child(2)::text').extract()
			i['qiuH3'] = sel.css('td em:nth-child(3)::text').extract()
			i['qiuH4'] = sel.css('td em:nth-child(4)::text').extract()
			i['qiuH5'] = sel.css('td em:nth-child(5)::text').extract()
			i['qiuH6'] = sel.css('td em:nth-child(6)::text').extract()
			i['qiuL'] = sel.css('td em:nth-child(7)::text').extract()
			yield i
		pass
