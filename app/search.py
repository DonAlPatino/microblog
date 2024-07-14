from flask import current_app

def add_to_index(index, model):
    if not current_app.elasticsearch:
        return
    payload = {}
    for field in model.__searchable__:
        payload[field] = getattr(model, field)
        print (payload[field])
    current_app.elasticsearch.index(index=index, id=model.id, document=payload)

def remove_from_index(index, model):
    if not current_app.elasticsearch:
        return
    current_app.elasticsearch.delete(index=index, id=model.id)

def query_index(index, query, page, per_page):
    if not current_app.elasticsearch:
        return [], 0
    search = current_app.elasticsearch.search(
        index=index,
        query={'multi_match': {'query': query, 'fields': ['*']}},
        from_=(page - 1) * per_page,
        size=per_page)
    #print(search)
    ids = [int(hit['_id']) for hit in search['hits']['hits']]
#>>> query_index('post', 'one two three four five', 1, 100) - получить json, который потом надо разобрать
#{'took': 2, 'timed_out': False, '_shards': {'total': 1, 'successful': 1, 'skipped': 0, 'failed': 0}, 
# 'hits': {'total': {'value': 5, 'relation': 'eq'}, 'max_score': 1.3862942, 
# 'hits': [{'_index': 'post', '_id': '1', '_score': 1.3862942, '_source': {'body': 'one'}}, 
# {'_index': 'post', '_id': '2', '_score': 1.3862942, '_source': {'body': 'two'}}, 
# {'_index': 'post', '_id': '3', '_score': 1.3862942, '_source': {'body': 'three'}}, 
# {'_index': 'post', '_id': '4', '_score': 1.3862942, '_source': {'body': 'four'}}, 
# {'_index': 'post', '_id': '5', '_score': 1.3862942, '_source': {'body': 'five'}}]}}
#([1, 2, 3, 4, 5], 5)


    return ids, search['hits']['total']['value']