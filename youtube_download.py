from __future__ import unicode_literals
import pdb
import re
import os
import subprocess as sp

import youtube_dl

track_metadata = {
    "title": "title",
    "author": "author",
    "album_artist": "album_artist",
    "album": "album",
    "grouping": "grouping",
    "composer": "composer",
    "year": "year",
    "track": "track",
    "comment": "comment",
    "genre": "genre",
    "copyright": "copyright",
    "description": "description",
    "synopsis" : "synopsis",
    "show": "show",
    "episode_id": "episode_id",
    "network": "network",
    "lyrics": "lyrics",
}

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

track_regex = r"(?P<id>\d+)- (?P<title>.*?) (?P<timestamp>[0-9:]{5,})"

urls = [
		"https://www.youtube.com/watch?v=z6xW1jztwT0",
		"https://www.youtube.com/watch?v=HtlkUzA8gfc",
		"https://www.youtube.com/watch?v=sl27gJAPxXk",
		"https://www.youtube.com/watch?v=6Cvud0BGAQA",
		"https://www.youtube.com/watch?v=w1AMMep5qus",
		"https://www.youtube.com/watch?v=uL18GajdiR0",
	]
for url in urls[:5]:
	youtube_dl.YoutubeDL(ydl_opts).download([url])
	url_suffix = url.split("v=")[1]
	info = youtube_dl.YoutubeDL(ydl_opts).extract_info(url, download=False)
	folder = info['title']
	title  = folder + "-" + url_suffix + ".mp3"
	try:
		os.mkdir(folder)
	except:
		pass
	tracklist = info['description'].split("Tracklist:")[1].split("\n\n")[0].splitlines()[1:]
	tracklist.append("end")
	for i, track in enumerate(tracklist):
		print(track)
		current = re.match(track_regex, track)
		next    = re.match(track_regex, tracklist[i + 1])
		output  = os.path.join(folder, current["title"] + ".mp3")
		if next:
			command = 'ffmpeg -i "{}" -ss {} -to {} -metadata author="FFVII Remake OST" -metadata track="{}" -c copy "{}"'.format(title, current["timestamp"], next["timestamp"], i + 1, output)
			sp.run(command, shell=True, universal_newlines=True)#, stdout=sp.DEVNULL, stderr=sp.DEVNULL)
		else:
			command = 'ffmpeg -i "{}" -ss {} -metadata author="FFVII Remake OST" -metadata track="{}" -c copy "{}"'.format(title, current["timestamp"], i + 1, output)
			sp.run(command, shell=True, universal_newlines=True)#, stdout=sp.DEVNULL, stderr=sp.DEVNULL)
			break

"""
# get timestamps
youtube_dl.YoutubeDL(ydl_opts).extract_info("https://www.youtube.com/watch?v=w1AMMep5qus", download=False)['description'].split("Tracklist:")[1].split("\n\n")[0].splitlines()

Part 1
01- The Prelude ~ Reunion 00:00
02- Midgar, City of Mako (with sound effects) 07:02
03- Bombing Mission (Part 1) 11:29
04- Bombing Mission (Part 2) Tempo 17:53
05- Bombing Mission (Part 3) 20:03
06- Let the Battles Begin! - Ex-SOLDIER 26:25
07- Mako Reactor 1 (Part 1) 28:06
08- Mako Reactor 1 (Part 2) 31:55
09- Mako Reactor 1 - Battle Edit (Intro) 35:45
10- Mako Reactor 1 - Battle Edit 36:57
11- Scorpion Sentinel (Part 1) 40:47
12- Scorpion Sentinel (Part 2) 40:55
13- Scorpion Sentinel (Part 3) 44:09
14- Scorpion Sentinel (Part 4) 46:48
15- Scorpion Sentinel (Part 5) 49:50
16- Scorpion Sentinel (Part 6) 53:38
17- Getaway (Part 1) 54:19
18- Getaway (Part 2) 58:18
19- Getaway (Part 3) 59:17
20- Getaway (Part 4) 01:03:28
21- Getaway (Part 5) 01:08:05
22- Getaway (Part 6) 01:13:32
23- Shinra's Theme 01:14:28
24- Those Chosen by the Planet 01:21:58
25- The Promised Land - Cycle of Souls 01:27:13
26- Chance Meeting in Sector 8 01:31:05
27- Let the Battles Begin! - Break Through (Part 1) (With Intro) 01:34:32
28- Let the Battles Begin! - Break Through (Part 2) Bridge 01:37:11
29- Let the Battles Begin! - Break Through (Part 3) Field 01:37:19
30- Let the Battles Begin! - Break Through (Part 4) Up to the Rooftops 01:39:58
31- Let the Battles Begin! - Break Through (Part 5) Up to the Roofs Battle 01:43:38
32- Let the Battles Begin! - Break Through (Part 7) End 01:46:36
33- A Close Call 01:46:41
34- Shinra Creed 01:47:21
35- Shining Beacon of Civilization 01:52:23
36- Tifa's Theme - Seventh Heaven 01:54:24
37- Noises in the Night 02:00:49
38- Mako Poisoning 02:03:53
39- Main Theme of FFVII - Sector 7 Undercity 02:05:16

Part 2
01- Avalanche's Theme 00:00
02- Scrap Boulevard Cleanup Crew 10:59
03- Johnny's Theme 17:00
04- Let the Battles Begin! - A Merc's Job 21:20
05- On Our Way 24:02
06- The Star of Seventh Heaven 28:16
07- Lurking in the Darkness - Suspicious Man 31:16
08- Just Another Job 33:46
09- Lay Down Some Rubber - Let's Ride 38:56
10- Midnight Spiral 47:23
11- Speed Demon 50:27
12- The Red Zone 54:59
13- RUN RUN RUN (Bad) 56:46
14- RUN RUN RUN (Normal) 58:32
15- RUN RUN RUN 01:00:18
16- Jessie's Theme 01:01:55
17- Moonlight Thievery 01:04:52
18- A Tower, a Promise 01:13:10
19- S7-6 Annex Diversion (Part 1) 01:15:48
20- S7-6 Annex Diversion (Part 2) 01:18:45
21- S7-6 Annex Diversion (Part 3) 01:22:03
22- S7-6 Annex Diversion (Part 4) 01:25:40
23- Ignition Flame 01:29:12
24- Under Cover of Smoke 01:34:21
25- Main Theme of FFVII - Nightfall in the Undercity 01:42:46
26- Whispers' Theme 01:51:30
27- A New Operation 01:56:10


Part 3
01- Target Mako Reactor 5 00:00
02- Hurry! 05:49
03- Dogged Pursuit 08:33
04- Born Survivors - Section C 12:50
05- Born Survivors - Section E 14:19
06- Crab Warden (Part 1) 16:42
07- Crab Warden (Part 2) 19:42
08- Crab Warden (Part 3) 24:27
09- Crab Warden (Part 4) Finish + Cutscene 29:49
10- Undercity Suns 32:32
11- Tightrope 34:56
12- Maze of Scrap Metal 37:21
13- Critical Shot 41:38
14- Game Over 45:56
15- The Rendezvous Point 46:24
16- A Trap is Sprung (Part 6) 48:16
17- The Airbuster (Part 1) 51:03
18- The Airbuster (Part 2) 55:13
19- The Airbuster (Part 3) 57:54
20- The Airbuster (Part 4) 01:01:18
21- The Airbuster (Part 5) 01:05:23
22- Who Am I 01:05:41
23- The Turks' Theme ~ The Turks Reno 01:07:31
24- The Turks Reno Battle (Part 1) 01:12:54
25- The Turks Reno Battle (Part 2) 01:15:01
26- Flowers Blooming in the Church (Part 1) Intro 01:18:56
27- Flowers Blooming in the Church (Part 2) 01:20:29
28- Flowers Blooming in the Church (Part 3) Outro 01:25:56
29- Under the Rotting Pizza (Battle) 01:26:28
30- Under the Rotting Pizza 01:30:14
31- Anxiety 01:34:00
32- Aerith's Theme - Home Again (Part 1) Intro 01:38:04
33- Aerith's Theme - Home Again (Part 2) 01:40:50
34- Aerith's Theme - Home Again (Part 3) Alternate Version #1 01:45:22
35- Hollow Skies 01:49:53
36- Let the Battles Begin! - The Hideout 01:55:29
37- Whack-a-Box 01:58:10

Part 4
01- Midnight Rendezvous 00:00
02- Collapsed Expressway 06:17
03- High Five 10:54
04- The Oppressed - Beck's Badasses 15:32
05- Due Recompense 21:55
06- Due Recompense (Battle) 27:48
07- Wall Market - The Town That Never Sleeps 32:59
08- Wall Market - Chocobo Sam 37:09
09- Wall Market - Madam M 41:19
10- The Most Muscular 45:29
11- An Unforgettable Night 48:14
12- The Sweetest Honey 52:44
13- Luxury Massage 55:47
14- Tonight's Corneo Cup 57:31
15- Corneo Colosseum 58:40
16- Colosseum Death Match 01:02:09
17- Just Desserts 01:06:49
18- Electric Executioners 01:11:29
19- Hell House (Part 1) 01:17:23
20- Hell House (Part 2) 01:20:02
21- Hell House (Part 3) 01:23:46
22- Victory Fanfare 01:30:14
23- Certain Gaudiness (Best) 01:31:50
24- Let the Battles Begin! REMAKE 01:33:03
25- Stand Up 01:33:51
26- Funk with Me 01:35:57
27- Sync or Swim 01:36:48
28- Vibe Valentino 01:37:49
29- Stand Up - Reprise 01:38:38
30- Don of the Slums 01:40:24
31- The Audition 01:43:12
32- Smash 'Em, Rip 'Em 01:46:29

Part 5
01- Abzu (Part 1) Intro 00:00
02- Abzu (Part 2) 00:15
03- Rough Waters 03:20
04- Darkness Ahead 08:42
05- Any Last Words? 14:05
06- Ascension 19:27
07- Train Graveyard 22:48
08- Haunted 26:12
09- Come On, This Way 28:29
10- Ghoul (Part 1) 32:26
11- Ghoul (Part 2) 38:29
12- Ghoul (Part 3) 42:55
13- Alone 43:09
14- Black Wind 44:27
15- Waiting to Be Found 52:39
16- Eligor 54:13
17- Fight for Survival 59:48
18- Come Back to Us (Part 1) Intro 01:05:22
19- Come Back to Us (Part 2) 01:06:14
20- Cheap Play 01:11:37
21- Those in Need 01:13:52
22- Slums on Fire 01:18:03
23- Get to Safety! 01:24:27
24- Aerith and Marlene - A Familiar Flower 01:27:20
25- Limited Options 01:33:31
26- The Look on Her Face 01:38:05
27- Rematch atop the Pillar (Part 1) 01:45:51
28- Rematch atop the Pillar (Part 2) 01:51:59
29- Rematch atop the Pillar (Part 3) 01:57:32
30- Rematch atop the Pillar (Part 4) 02:01:16

Part 6
01- Return to the Planet 00:00
02- A Broken World 02:28
03- Daughter's Farewell 09:35
04- Infinity's End 12:42
05- Wild de Chocobo 18:41
06- Leslie's Theme 20:07
07- The Day Midgar Stood Still 28:10
08- Fires of Resistance 32:16
09- A Solemn Sunset 36:23
10- The Valkyrie (Part 1) Intro 43:24
11- The Valkyrie (Part 2) 45:17
12- The Valkyrie (Part 3) 51:11
13- The Valkyrie (Part 4) 54:33
14- The Valkyrie (Part 5) 59:02
15- The Shinra Building 01:00:47
16- Operation Save Aerith 01:08:21
17- All Quiet at the Gates 01:13:51
18- Hand over Hand 01:18:28
19- Scarlet's Theme 01:22:30
20- Stewards of the Planet (with sound effects) 01:37:37
21- Corporate Archives 01:41:34
22- Cultivating Madness 01:45:44
23- Another Day at Shinra HQ 01:47:44
24- The Turks' Theme - Office 01:51:03
25- Home Away from Home 01:52:47
26- Infiltrating Shinra HQ 01:56:06
27- The Drum 02:00:43
28- Catastrophe 02:04:56
29- Final Experiment 02:09:08
"""