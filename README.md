# DRIO4302C - Data Engineering

- Course : DRIO-4302C Data Engineering
- Students : Vincent Barbosa Vaz, William Cardoso
- Teacher : Daniel Courivaud, Raphaël Courivaud

- recueil de données (scraping ou DB Open Data)
- stockage MongoDB
- interface Flask d'interrogation de la DB

## The project

Crawling/scraping of [IMDb](https://www.imdb.com/) for series, with Scrapy.

Save data into MongoDB database.

Create a Flask web-app to display the data.

The user likes series he loves (through Elasticsearch), the app match the bests series to watch.

# Run the project

Clone it :

```bash
git clone https://github.com/v-barbosavaz/DRIO4302C
```

Then :

```bash
docker-compose up -d
```