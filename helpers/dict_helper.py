
def dict_merge(dict1, dict2):
    return {**dict1, **dict2}


def dict_to_query(query):
    if isinstance(query, dict) and query:
        conditions = []
        for key, value in query.items():
            if key == 'initial_date':
                conditions.append(f"purchaseDate >= '{value}'")
            elif key == 'final_date':
                conditions.append(f"purchaseDate <= '{value}'")
            else:
                conditions.append(f"{key}='{value}'")
        resolved_query = " AND ".join(conditions)
        return f" WHERE {resolved_query}"
