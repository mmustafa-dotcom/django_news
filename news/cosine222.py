from scipy.spatial.distance import cosine
A=[4,10,16]
B=[12,18,24]
similarity= 1- cosine(A,B)
print(similarity)