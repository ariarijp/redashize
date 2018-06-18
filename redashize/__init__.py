def redashize(rows):
    return {
        'columns': [{'name': key, 'friendly_name': key} for key in rows[0].keys()],
        'rows': rows,
    }


def unredashize(result):
    return result['rows']
