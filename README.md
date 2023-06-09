# Wikidata
Wikidata is a cli program that compares wikipage contributions. You only
need to provide `wikidata` with the title of two Wikipedia pages, and it will
download information about the list contributions and contributors.

Wikidata can also pull different languages and compare them together.
you only have to pass it the abbriviation of the country in the case 
of a single language, or a set of lanaguages for multiple language analysis.

Wikidata will display 3 types of graphs:
1. Number of contributions by month for each page.
2. Number of contributions by type (anonymous or not) for each page.
3. The intersection between contributors from both pages.

![alt text](https://github.com/zeddo123/wikidata/blob/master/image.png?raw=true)

## Usage
```sh
usage: Wikidata [-h] [-c CONTRIBUTIONS]
                [-l LANGUAGES [LANGUAGES ...]] [-o OUTPUT]
                [--graphical | --no-graphical]
                [--csv-data | --no-csv-data]
                page1 page2

Extracts and compares data about wikipedia pages

positional arguments:
  page1                 Name of Wikipedia page
  page2                 Name of Wikipedia page

options:
  -h, --help            show this help message and exit
  -c CONTRIBUTIONS, --contributions CONTRIBUTIONS
                        Number of contributions to retrieve
  -l LANGUAGES [LANGUAGES ...], --languages LANGUAGES [LANGUAGES ...]
                        Set of language (default: en)
  -o OUTPUT, --output OUTPUT
                        Name of output file for the graphs
  --graphical, --no-graphical
                        Display data graphicly (default: True)
  --csv-data, --no-csv-data
                        Compile contributors information per page in
                        a csv file (default: False)
```
### Example
The simplest way to run `wikidata` is to just pass it the title name of the two pages.
```
python wikidata.py Mikhail_Bakunin Errico_Malatesta
```

The command below would compare the wikipedia pages (Albert_Camus, and David_Graeber) for the last 
100 revisions. No graphs will be shown (still going to be saved as png image), and csv
data of contributions for each data will be generated.
```sh 
python wikidata.py Albert_Camus David_Graeber -c 100 --no-graphical --csv-data
```

The command below would compare the wikipedia pages (Albert_Camus, and David_Graeber) for the last 
1000 revisions with 3 languages selected (en, fr, de).
```sh 
python wikidata.py Albert_Camus David_Graeber -c 1000 -l en fr de
```
#### Csv data structure
The csv file generated for each (meta)page has this format:
```csv
contributor, contributions, language
Fabienamnet,1,fr
Le sourcier de la colline,1,fr
Rita2008,27,de
Tsor,2,de
Invisigoth67,5,de
```

## Installation
To insall wikidata you only need to follow the instructions below.
```sh
// pull the git repository.
git clone https://github.com/zeddo123/wikidata
cd wikidata
// install the requirements.
poetry install // or pip install -r requirements.txt
```

### Dependencies
* beautifulsoup4: for web scrapping the wikipedia pages.
* matplotlib: for generating the plots from the data.
* matplotlib-venn: helper library used to generate the venn diagrams.
* aiohttp: async library used to speed up the pulling of the wikipedia pages.
* tqdm: used for progess bars.
* dateparser: used to parse the dates from any date format. Crucial to get the date objects from different languages.
