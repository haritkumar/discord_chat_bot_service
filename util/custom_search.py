from googlesearch import search
from .dao.db_ops import *


def search_results_from_google(messege_content, author):
    print("Google search "+str(messege_content)+" "+str(author))
    query = messege_content.replace("!google", "")
    print(query);
    result_list = search(query, num_results=5);
    joined_string = "\n".join(result_list);
    add_history(author, query, joined_string)
    return result_list

def search_results_from_history(messege_content, author):
    print("Recent search " + str(messege_content) + " " + str(author))
    query = messege_content.replace("!recent", "")
    history_result = get_history(author, query)
    return history_result