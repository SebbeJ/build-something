import redis
import flask

def levenshteinRecursive(str1, str2, m, n):


      # str1 is empty
    if m == 0:
        return n
    # str2 is empty
    if n == 0:
        return m
    if str1[m - 1] == str2[n - 1]:
        return levenshteinRecursive(str1, str2, m - 1, n - 1)
    return 1 + min(
          # Insert     
        levenshteinRecursive(str1, str2, m, n - 1),
        min(
              # Remove
            levenshteinRecursive(str1, str2, m - 1, n),
          # Replace
            levenshteinRecursive(str1, str2, m - 1, n - 1))
    )

def closest_word(sentence, query):
    sentence_words = sentence.split(' ')
    min_distance = float('inf')
    closest = ""
    for s_word in sentence_words:

        distance = levenshteinRecursive(s_word.lower(), query.lower(), len(s_word), len(query))
        if distance < min_distance:
            min_distance = distance
            closest = s_word
    return {'word': closest, 'distance': min_distance}


# if __name__ == "__main__":
    #Register in service registry

    # while True:
        
    #     #Recieve sentence and query
    #     sentence = "This is a sample sentence."
    #     query = "sample"
    #     location = "0"

    #     #Find closest
    #     closest = closest_word(sentence, query)

    #     #Format
    #     formatted = {
    #         'text': sentence,
    #         'closest_word': closest['word'],
    #         'distance': closest['distance'],
    #         'place': int(location)
    #     }

    #     #return to book service

    #     #Register to service registry
