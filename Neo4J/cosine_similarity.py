from sklearn.metrics.pairwise import cosine_similarity

one = [1,1,0]
two = [0,1,1]

array = cosine_similarity([one, two])

print array