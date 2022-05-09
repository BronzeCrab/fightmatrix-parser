What is it?

It's python and Scrapy based parser of mma fighters from fightmatrix.com

What I've done to init the project:

	pip install scrapy
	scrapy startproject fightmatrix
	cd fightmatrix/
	scrapy genspider fightmatrix fightmatrix.com
	scrapy crawl fightmatrix_spider
	scrapy crawl fightmatrix_spider -o output.csv -t csv
	
How to use this parser:

    pip install scrapy
    cd fightmatrix/
    scrapy crawl fightmatrix_spider -o output.csv -t csv