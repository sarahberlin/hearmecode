bottles = 99

while bottles > 1:
	for bottle in range(99):
		print "{0} bottles of beer on the wall, {0} bottles of beer...".format(bottles)
		bottles = bottles - 1
		print "If one of those bottles should happen to fall, {0} bottles of beer on the wall".format(bottles)
