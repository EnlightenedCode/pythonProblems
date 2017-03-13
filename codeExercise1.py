def twoArrays(current, target):
	deletions = list(set(current) - set(target))
	additions = list(set(target) - set(current))
	sorted (deletions, key=int, reverse=True)
	sorted (additions, key=int, reverse=True)
	print('additions: ' + '[' + ','.join(str(e) for e in sorted(additions)) + ']')
	print('deletions: ' + '[' + ','.join(str(e) for e in sorted(deletions)) + ']')


print('hello program')
twoArrays([1,3,5,6,8,9], [1,2,5,7,9])

