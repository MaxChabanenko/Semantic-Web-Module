#2.Використовуючи відкритий SPARQL endpoint http://dbpedia.org/sparql, напишіть SPARQL запит для визначення назви найбільшого за кількістю населення міста України.

from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper('https://dbpedia.org/sparql')

query = '''
    SELECT ?name ?population
    WHERE  {
           ?city a dbo:City ;
            dbo:country <http://dbpedia.org/resource/Ukraine> ;
            dbo:originalName ?name ;
            dbo:populationTotal ?population .
    }
    ORDER BY DESC(?population)
    LIMIT 1
'''

sparql.setQuery(query)
sparql.setReturnFormat(JSON)
query_res = sparql.query().convert()

for value in query_res['results']['bindings']:
    city = value['name']['value']
    population = value['population']['value']
    print('City = ',city, ', Population', population)
