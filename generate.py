import os
import datetime

"""
TODO:
 - Multiple images on post pages.
 - If any two images in one post share a resolution, show the second image when hovering over the post in the index.
 - Text posts.
 - Convert all loose images into post folders, and then remove support for loose images.
"""

rootDir = "./" #os.path.dirname(os.path.realpath(__file__))
postDir = "./posts/"

titleText = "Miscela Leone"
headerText = "Photographer from British Columbia, Canada. Takes pictures of trees and not people.<br>Celebrate the weird | Never lose hope"

print("Root Directory: " + os.path.realpath(rootDir))
print("Image Directory: " + os.path.realpath(postDir))

pageTop = """
<html>
<head>
	<title>Miscela Leone</title>
	<meta charset="UTF-8"/>
	<link rel="shortcut icon" type="image/jpg" href="avatar.jpg">
	<link rel="stylesheet" type="text/css" href="./main.css">
</head>

<body>
	<section id="pageContainer">
		<section id="header">
			<div id="headerImgContainer">
				<img id="headerImg" src="./headerSlightComp.webp">
			</div>
			<img id="logo" src="./avatar.jpg">
			<div id="headerText">{headerText}</div>
		</section>
		<section id="titleBar">
			<div id="titleText">{titleText}</div>
		</section>
		<section id="imageGrid">
""".format(titleText=titleText.upper(), headerText=headerText.upper())

pageBottom = """
		</section>
	</section>
	<section id="footer">
		<div id="footerText">© 2017-{currentYear} {titleText}</div>
	</section>

</body>
</html>
""".format(currentYear=datetime.datetime.now().year, titleText=titleText)

pageMiddle = ""


for root, dirs, files in os.walk(postDir):
	for dir in dirs:
		print("Post Found: " + dir)
		pageMiddle += "<a href=\"./" + dir + ".html\"><img src=\"./posts/" + dir + "/postThumb1.webp\"></a>\n"
		postTextFile = open("./posts/" + dir + "/postText", "r")
		postText = postTextFile.read()
		postTextFile.close()
		postDateFile = open("./posts/" + dir + "/postDate", "r")
		postDateStr = postDateFile.read()
		postDateFile.close()
		postDate = datetime.datetime.strptime(postDateStr[:10], "%m %d %Y")
		print(postDate)
		postDateDelta = datetime.datetime.now() - postDate
		if postDateDelta.days > 365:
			postDateAgo = "Posted " + str(round(postDateDelta.days / 365)) + " Years Ago"
		elif postDateDelta.days > 30:
			postDateAgo = "Posted " + str(round(postDateDelta.days / 30)) + " Months Ago"
		elif postDateDelta.days > 1:
			postDateAgo = "Posted " + postDateDelta.days + " Days Ago"
		elif postDateDelta.hours > 1:
			postDateAgo = "Posted " + postDateDelta.hours + " Hours Ago"
		elif postDateDelta.minutes > 1:
			postDateAgo = "Posted " + postDateDelta.minutes + " Minutes Ago"
		else:
			postDateAgo = postDateDelta.seconds + " Seconds Ago"
		postFile = open("./" + dir + ".html", "w")
		postFile.write("""
		<html>
			<head>
				<title>Miscela Leone</title>
				<meta charset="utf-8"/>
				<link rel="shortcut icon" type="image/jpg" href="avatar.jpg">
				<style>
					@font-face {{
						font-family: "mainFont";
						src: url("LiberationSans-Regular.ttf") format("truetype");
					}}

					html, body {{
						margin: 0px;
						height: 100%;
						background: #fafafa; /*#faeaf0;*/
						font-family: "mainFont";
					}}

					a:link, a:visited, a:hover, a:active {{
						text-decoration: none !important;
						color: black;
					}}

					#backImg {{
						width:30;
						height:30;
						position:absolute;
						top:15px;
						left:15px;
					}}

					#postContainer {{
						position: absolute;
						height: 95%;
						top: 50%;
						left: 50%;
						transform: translate(-50%, -50%);
						background: white;
					}}

					#postImage {{
						height: 85%;
					}}

					#postText {{
						padding: 15px 15px 5px 15px;
						font-size: small;
					}}
				</style>
			</head>
			<body>
				<a href="index.html"><img id="backImg" src="./avatar.jpg"></a>
				<section id="postContainer">
					<img id="postImage" src="./posts/{dir}/1.png">
					<section id="postText">
						{postText}<br><br>{postDateAgo}
					</section>
					<section id=postInfo>

					</section>
				</section>
			</body>
		</html>
		""".format(postText=postText, postDateAgo=postDateAgo, dir=dir))
		postFile.close()
	for file in files:
		#if file.lower().endswith(".png") \
		#or file.lower().endswith(".jpg") \
		#or file.lower().endswith(".jpeg"):
		if file.lower().endswith(".webp"):
			pageMiddle += "<a href=\"./posts/" + file + "\"><img src=\"./posts/" + file + "\"></a>\n"

pageMiddle += "<div>Fiddle-dee-dee, fiddle-dee-dum.</div>"

# Create the main file of the generated website.
htmlFile = open("./index.html", "w")
htmlFile.write(pageTop + pageMiddle + pageBottom)
htmlFile.close()
