import datasets
def process_docs(dataset: datasets.Dataset):
    def _helper(doc):
        doc["rating"] = "pozitivă" if doc["starRating"] > 3 else "negativă" 
        return doc

    return dataset.map(_helper) # returns back a datasets.Dataset object

def doc_to_target_bc(doc):
    if doc["rating"] == "pozitivă":
        return 1
    return 0

def doc_to_target_mc(doc):
    return [1, 2, 4, 5].index(doc["starRating"])