class Song(object):
	def __init__(self, lyrics):
		self.words = lyrics
		#self.lyrics = lyrics
		#self.anything = lyrics

	def sing_me_a_song(self):
		for line in self.words:
			#if we used the self.lyrics in the __init__ we would need to update it here as 
			#for line in self.lyrics:
			print line 




happy_bday = Song(["Happy birthday to you",
					"I dont want to get sued",
					"So i'll stop right there"])

bulls_on_parade = Song(["they rally around the family",
						"With pockets full of shells"])



Nothing_Else_matters = Song(["So Close no matter how far",
								"couldnt be much more from the heart",
								"Forever trusting who we are",
								"And Nothing else matters"])



#happy_bday.sing_me_a_song()
#bulls_on_parade.sing_me_a_song()

Nothing_Else_matters.sing_me_a_song()
