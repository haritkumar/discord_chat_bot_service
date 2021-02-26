from googlesearch import search

def search_results_from_google(messege_content):
    query = messege_content.replace("!google", "")
    print(query);
    result_list = search(query, num_results=5);
    joined_string = "\n".join(result_list);
    return joined_string
