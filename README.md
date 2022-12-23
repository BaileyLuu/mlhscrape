# mlhscrape

# Purpose

To download the images of hackathons from MLH website and store in MongoDB

# Tools Used

Python, MongoDB, BeautifulSoup, and Requests

# What I learned

1. Created a virtual environment 
2. Implemented <strong>BeautifulSoup</strong> to scrape the data
3. Integrated with <strong>MongoDB</strong> to store the scraped data
4. Installed <strong>python-dotenv</strong> to store the environment variables
5. Used <strong>os.getcwd()</strong> function to get the path of the project and automatically create a directory inside the project to store the images
6. Added .gitignore and clear Git's cache
7. Added requirements.txt to store the required packages and its version

# Challenges

At first, I used wget to download images into a folder. However, I encountered HTTP 403 Error. Thus, I used urllib.request.urlretrieve() function. I realized that one of its parameters only accept a file, not director. Thus, I scraped the name of the hackathon and save the image according to its name and extension type. 

# Resources for Learning 

1. https://www.mongodb.com/languages/python
2. https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/
3. https://stackoverflow.com/questions/1139762/ignore-files-that-have-already-been-committed-to-a-git-repository/1139797#1139797
4. https://www.digitalocean.com/community/tutorials/how-to-push-an-existing-project-to-github
