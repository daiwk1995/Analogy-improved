from utils.DBpediaCrawler import generate_graph
from pprint import pprint
with open("Food","w+") as f:
    f.write(generate_graph(["burger"],2000,debug=True).serialize())
