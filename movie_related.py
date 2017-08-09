class Movie:

	def __init__(self, title, rating):
		self.title = title
		self.rating = rating
		self.related = []

		
def print_all(m):
	print '%s %s' % (m.title, m.rating)
	
	for sm in m.related:
		print_all(sm)
	
def find_movie_with_ratings(m, rating, result):
	if m.rating >= rating:
		result.append(m)

	for sm in m.related:
		find_movie_with_ratings(sm, rating, result)

	return result

def main():
	m = Movie('Avengers', 9)
	m2 = Movie('Captain America', 6)
	m3 = Movie('Ironman', 7)
	m4 = Movie('Ironman-2', 8)
	m5 = Movie('Ironman-3', 3)
	
	m3.related.append(m4)
	m3.related.append(m5)
	m.related.append(m2)
	m.related.append(m3)
	
	# print_all(m)
	result = find_movie_with_ratings(m, 8, [])
	for x in result:
		print x.title, x.rating
	
if __name__ == '__main__':
	main()
