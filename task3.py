#3.Використовуючи бібліотеки RdfLib, SPARQLWrapper та відкритий endpoint написати Python-скрипт, який буде повертати акторів України та фільми, в яких вони зіграли головну роль.

from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper('https://dbpedia.org/sparql')

query = '''
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX dbc: <http://dbpedia.org/resource/Category:>

SELECT DISTINCT ?actorName (GROUP_CONCAT(DISTINCT ?title; SEPARATOR='; ') as ?filmsStarring)
WHERE {
  {
    ?actor dbo:wikiPageWikiLink dbc:Ukrainian_male_film_actors.
  }
  UNION
  {
    ?actor dbo:wikiPageWikiLink dbc:Ukrainian_film_actresses.
  }
  UNION
  {
    ?actor a dbo:Animal ;
      dbp:occupation "actor"@en ;
      dbo:birthPlace ?birthplace .
    ?birthplace dbo:country <http://dbpedia.org/resource/Ukraine> .
  }
  ?film a dbo:Film ;
    dbo:starring ?actor;
    dbp:name ?title .
  ?actor foaf:name ?actorName.

}

'''

sparql.setQuery(query)
sparql.setReturnFormat(JSON)
query_res = sparql.query().convert()

for value in query_res['results']['bindings']:
    actor  = value['actorName']['value']
    filmsStarring = value['filmsStarring']['value']
    print('Actor: ',actor, '| FilmsStarring: ', filmsStarring)
print('There is simply no field or other functionality (page of films with main actors) to select leading or main role of the film')
