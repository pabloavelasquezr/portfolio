import json

class Media:
    def __init__(self, email, cv, tooltipcv, github, likedin):
        self.email = email
        self.cv = cv
        self.tooltipcv = tooltipcv
        self.github = github
        self.likedin = likedin

class Skill:
    def __init__(self, skill):
        self.skill = skill

class Technology:
    def __init__(self, icon, name):
        self.icon = icon
        self.name = name

class Description:
    def __init__(self, item):
        self.item = item

class Experience:
    def __init__(self, icon, title, subtitle, description, date, place):
        self.icon = icon
        self.title = title
        self.subtitle = subtitle
        self.description = [Description(**item) for item in description]
        self.date = date
        self.place = place

class Project:
    def __init__(self, icon, title, description, technologies,tooltipurl,url,tooltipgithub,github,image):
        self.icon = icon
        self.title = title
        self.description = description
        self.technologies = [Technology(**tech) for tech in technologies]
        self.tooltipurl = tooltipurl
        self.url = url
        self.tooltipgithub = tooltipgithub
        self.github = github
        self.image = image

class Education:
    def __init__(self, icon, title, description, date, place):
        self.icon = icon
        self.title = title
        self.description = description
        self.date = date
        self.place = place

class Footer:
    def __init__(self, author, city, made):
        self.author = author
        self.city = city
        self.made = made

class Data:
    def __init__(
            self, 
            title, 
            description, 
            image, 
            avatar, 
            name, 
            skill, 
            location, 
            greeting,
            media, 
            abouttitle, 
            about, 
            skillstitle,
            skills,
            technologiestitle,
            technologies, 
            experiencetitle,
            experience,
            projectstitle,
            projects, 
            educationtitle,
            education,
            footer
        ):
        self.title = title
        self.description = description
        self.image = image
        self.avatar = avatar
        self.name = name
        self.skill = skill
        self.location = location
        self.greeting = greeting
        self.media = Media(**media)
        self.abouttitle = abouttitle
        self.about = about
        self.skillstitle = skillstitle
        self.skills = [Skill(**skill) for skill in skills]
        self.technologiestitle = technologiestitle
        self.technologies = [Technology(**tech) for tech in technologies]
        self.experiencetitle = experiencetitle
        self.experience = [Experience(**info) for info in experience]
        self.projectstitle = projectstitle
        self.projects = [Project(**info) for info in projects]
        self.educationtitle = educationtitle
        self.education = [Education(**info) for info in education]
        self.footer = Footer(**footer)

with open("assets/data/data-en.json", encoding="utf-8") as file:
    json_data = json.load(file)

data_en = Data(**json_data)



with open("assets/data/data-es.json", encoding="utf-8") as file:
    json_data = json.load(file)

data_es = Data(**json_data)
