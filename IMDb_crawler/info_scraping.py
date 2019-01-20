#fetch('https://www.imdb.com/search/title?title_type=tv_series')

- Pour chaque film parsé sur la première page (classement popularité):
    - Entrer sur le lien de la page du film
    - Scraper les 12 div class="rec_item" (recommandés car semblables)
    - Les associer au film premièrement scrapé
- Passer à la seconde page



response.xpath('//*[@id="main"]/div/div[3]/div/div[1]/div[2]/a/img').css('::attr(data-tconst)')


response.xpath('//*[@id="title_recs"]/div[1]/div/div[2]/div[1]').css('.rec_item')
