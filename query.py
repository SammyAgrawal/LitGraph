import scholarly

def recent_publications(author_name, year_threshold=2021):
    # leap was founded in 2021 so publication must be at least after that
    pubs = {
        "Title" : [],
        "Publication Year" : [],
        "Type" : [], # journal article
        #"DOI" : [],
        "URL" : [], 

    }

    types_of_pubs = ["journal", "conference"]
    search_query = scholarly.search_author(author_name)
    author = scholarly.fill(next(search_query)) # dict
    for pub in author['publications']:
        pub = scholarly.fill(pub) 
        if(pub['bib']['pub_year'] >= 2021):
            try:
                pubs["Title"].append(pub['bib']['title'])
                pubs["Publication Year"].append(pub['bib']['pub_year'])
                
                for type in types_of_pubs:
                    if(type in pub['bib'].keys()):
                        pubs["Type"].append(type)
                
                pubs["URL"].append(pub['pub_url'])
            
            except KeyError:
                print("\nError accessing from these keys")
                print(pub['bib'].keys()) 
    
    return(pubs)       

author_pubs = recent_publications(sample_author)