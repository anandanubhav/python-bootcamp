playlist = {
			"name":"favorite",
			"author":"AA",
			"songs":[
			{"title":"song1", "artist":["queen","bbboys"], "duration":5},
			{"title":"song2", "artist":["queen1","bbboys1"], "duration":7},
			{"title":"meow", "artist":["garfield"], "duration":4}
			]
}

total_duration = 0
for song in playlist['songs']:
	print(song['title'])
	print(song['duration'])
	total_duration += song['duration']
	
	
print(f"Total duraion of songs in playlist is: {total_duration}")
			
