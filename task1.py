#Написати Python-скрипт, який на базі заданого графу повертає назви країн кожного континенту. Для країн також необхідно вказати назви пов’язаних мов і ранг мов.
from rdflib import Graph

g = Graph()
g.parse('countrues_info.ttl', format='ttl')

query = """
    SELECT ?continent_name ?country_name ?lang_name ?lang_rank
    WHERE {
      ?country rdf:type :Country;
      :country_name ?country_name ;
      :part_of_continent ?continent.
      
    ?continent :continent_name ?continent_name.
    
    ?lang rdf:type :Country_Language;
    :spoken_in ?country.

    ?lang :language_value ?lang_val;
    :rank ?lang_rank.
    
    ?lang_val :language_name ?lang_name.
    }
    ORDER BY ?continent_name
    """


results = g.query(query)
print(results)

for row in results:
    print(row['continent_name'], '| ', row['country_name'], '| ', row['lang_name'], '| ', row['lang_rank'])
