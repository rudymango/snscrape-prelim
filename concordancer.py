import json
from concordancer.demo import download_demo_corpus
from concordancer.concordancer import Concordancer
from concordancer import server

# Load demo corpus
fp = download_demo_corpus(to="~/Desktop")
with open(fp, encoding="utf-8") as f:
	corpus = [json.loads(l) for l in f]

# Index and initiate the corpus as a concordancer object
C = concordancer(corpus)
C.set_cql_parameters(default_attr="word", max_quant=3)

serer.run(C)	