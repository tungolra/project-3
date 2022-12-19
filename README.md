# [Culinarian](https://culinarian-sei55.herokuapp.com/)



### Introduction

_In Canada people waste an estimated [$30 billion](https://www.cbc.ca/news/business/canada-food-waste-1.3813965) of food every year._

_The average Canadian spends almost [$3,000](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1110012501) every year on dining out._

Culinarian keeps cooking simple.

Using a Django, Python, and PostgreSQL as our solutions-stack, our team of 4 software developers launched a recipe-based website that aims to streamline decision-making in the kitchen and mitigate food waste. Users have access to a large database of recipes that suggests popular recipes and exact portions of ingredients for their next grocery run.

### About the Project
This project was built in 7 days. Working within a team of 4, along with two UX Designers, Nick Collett and Karishma Jani, we organized our project by first creating a [wireframe](https://www.figma.com/file/KmUPhWQxVPztGLhFxzJMVN/Collabathon?node-id=167%3A813), mapping an [ERD](https://lucid.app/lucidchart/78f5650d-cdb2-45c6-a92a-3285be5d8009/edit?viewport_loc=-1706%2C-645%2C2493%2C1122%2C0_0&invitationId=inv_b0952405-cfc6-4620-8334-bb4c4707eb1a), and organizing our tasks for the minimum viable product (MVP) using [Notion](https://www.notion.so/f802231124e345e38edb4db5b1e4b008?v=12e1bfb756a147a88750053b30b02be1). Following an Agile workflow, our team met daily during project week to touch base on task progress, issues faced, and mapping out next steps.   

### Responsibilities

For the UI/UX, we took a mobile-first approach to create a responsive website using HTML, CSS, and Materialize’s styling framework. I was responsible for creating AJAX calls to our database and populating the data within Django's templates. 

I was tasked with creating RESTful APIs so users can collect recipes into their "My Recipes" page, create meal plans in their "My Meal Plans" page, and generate grocery lists from their collections.

Following Django’s MVT architecture, I established the routing and CRUD functions to make API calls to the app’s PostgreSQL database and TastyCO’s API. 

Lastly, I was responsible for implementing Django’s session-based authorization to validate user credentials.


### Home Page
Upon sign in, users are taken to the homepage where they will first see a Featured Recipe. Below is the option to Explore by cuisine-type. Lastly, we generate a list of featured recipes. 

<img src="https://i.imgur.com/bu8ZXid.gif">
<img src="https://i.imgur.com/OOrGzJ0.png">

### Explore Page

Featuring a carousel to browse through a number of cuisine-types from around the world, users can click into a particular cuisine. They will be redirected to another page of recipes. 
<img src="https://i.imgur.com/gmJyfdy.gif">

### Nav Bar

We've created a responsive nav bar to reduce empty space for larger screens or maximize content-space in smaller screens. 
<img alt="navbar" src="https://i.imgur.com/eE7p9Ul.gif">

### My Recipes Page

When a user views the details for a recipe, they can click the Like icon to save to their recipes. Their newly saved recipe will show in the My Recipes Page. 
<img alt="myrecipes" src="https://i.imgur.com/xLZ0Nbm.gif">

### Recipe Details Page

The Recipe Details page resembles a modern website highlighting helpful details related to a single recipe. Users will find out the cooktime, recipe rating, number of servings, and calorie content in the summary details. They have the option to jump to any section of the page - Directions, Nutrition content, instructional videos, and reviews. 
<img src="https://i.imgur.com/Wzykr4U.gif">

### My Meal Plans Page

On the Meal Plans Page, users can view all their customizable meal plans. Here, they can create new meal plans or view all the recipes collected for a particular meal plan.
<img alt="mealplanspage" src="https://i.imgur.com/qgkhZ1C.png">

### Adding Recipes to Meal Plan

Through the recipe details page, users can also directly add a recipe to a particular meal plan. This recipe will be available when going into their selected meal plan. 
<img alt="mealplanspage" src="https://i.imgur.com/oTplFje.gif">

### Creating New Meal Plans

Creating a new meal plan is as easy as inputting a name for their collection. 
<img alt="mealplanscreate/update" src="https://i.imgur.com/ZqHE0J4.png">

### Grocery Page

Finally, once users have collected a list of recipes for their meal plan, they can generate a grocery list which compiles the quantities for all unique grocery items. 
<img src="https://i.imgur.com/hVQQQzV.png">

### Registration Pages
Using Django's session-based authorization, users can create a new account to begin their culinary journey. 

#### Log in Page
<img src="https://i.imgur.com/lBQ4uhW.png">

#### Sign up Page
<img src="https://i.imgur.com/iZOOcYy.png">

### Technologies Used:
- Python
- Django
- PostgreSQL
- [Tasty API](https://rapidapi.com/apidojo/api/tasty/)
- HTML
- CSS/Materialize


### Icebox

- A search option where you can query by diet, ingredients, cuisine etc.
- The ability to create recipes.
- A functional share button to pass recipes along to others. 

### Team Members
- Ralph Tungol
- Saad Khan
- Lucas Friedmann
- Kendra Yoshizawa
- Karishma Jani
- Nick Collett


Ralph Tungol
Email: rarttungol@gmail.com
Project Repo: [Repo](https://github.com/tungolra/project-3/tree/development)
Project Site: [Site - _offline_]()

