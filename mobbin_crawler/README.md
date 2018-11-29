# Mobbin Crawler

> https://mobbin.design/


Scrapy project


## Run this spider

> cd ./mobbin_crawler/moibbin_scrapy/

> scrapy crawl mobbin_images_spider


# Approach

*A*

infinite scroll with selenium, save html as file
<br>
from HTML file saved, crawl the data required.

*B*

Crawl available, scroll down when completed

## how to?

*For Approach B*

```
n = 0
while true:
    n += 1
    //div/[n]
```


0~10
<br>
scroll : new items
<br>
10~20
<br>
scroll : new items
<br>
20~30



