
![Cocktail Bible](/Readme-images/responsive.png)
# Cocktail Bible

The aim of this site is to share not only with cocktail lovers, but any person interested in cocktails, the best cocktail recipes from all around  the world. 
Here users have the chance to find, read, add,  and edit their own cocktail recipes. 
Therefore, through this website we want to promote the cocktail culuture to help people find new flavors and make of cocktail drinking and making a unique experience. 

- [Visite Site ](https://flask-cocktail-bible.herokuapp.com/get_cocktails)

## Index 

- <a href="#ux">1. User experience (UX)</a>
  - <a href="#Project">1.1. Project goals</a>
  - <a href="#User-story">1.2 User stories</a>
  - <a href="#Wireframes">1.3 Wireframes</a>
  - <a href="#Design">1.4 Design</a>
- <a href="#Features">2. Features</a>
- <a href="#Technologies">3. Technologies used</a>
- <a href="#Testing">4. Testing</a>
- <a href="#Deployment">5. Deployment</a>
- <a href="#Credits">6. Credits</a>
- <a href="#Media">7. Media</a>
- <a href="#Acknowledgements">8. Acknowledgements</a>
- <a href="#Github">9. 9. Github</a>
<span id="ux"></span>
##  1. UX
<span id="Project"></span>
### 1.1 Project goals
- This website is specially addressed to cocktail lovers and any person who want to learn to make good cocktails.
- Be intuitive for users and easy to navigate.  
- Be Interactive, so users can read, add, edit, search and delete their recipes.
- promote the cocktail culture.


## 1.2 User Story: 
<span id="User-story"></span>
### As a user I want to:

- Have access to all recipes displayed in the website

- See the ingredients and preparation of the cocktails

- Find easily the different recipes

- Add my own recipes  

- Edit my own recipes

- Delete my own recipes if needed

- To move easly and intutively

- Register and login to have my personalized profile



## 1. 3  [Wireframes ](/wireframes-images/wireframes.jpg)
[See Wireframes ](/wireframes-images/wireframes.jpg)
<span id="Wireframes"></span>
 
These wireframes where designed  with [Figma](https://www.figma.com/file/x4m6WQpYOvB8l1EB9EikFm/Untitled?node-id=0%3A1)
which is a very instuitive prototyping tool that focuses in the user interface and user experience design.

<span id="Design"></span>
## 1.4. Design

This website was designed using [Heroic Features](https://startbootstrap.com/template/heroic-features)
A basic Bootstrap home page template from [startboostrap](https://startbootstrap.com/).
this template was chosen thinking on a minimalist 
concept which transmits serenity and tranquillity. Therefore, all pages are diaphanous but functional, avoiding the overuse of colors which could be stressful  and overwhelming for the users.
Hence, black and  white are the predominant colors. There are also some other colors such as yellow, green, red and blue in puntual elements as bottoms and icons. 

**Colors**
- Black #000000: used for the page body, collapsible body, and font on the collapsible headers.
- White #ffffff: used for the Font and collapsible headers background 
- Black #212121: used for buttons in log in, register pages
- Green #26a69a: edit buttons in profile page
- Green #45be74: used for refresh 
button in the search box.
- Red #f44336: user for the delete button in the edit form. 
- yellow #f44336: user for the confirmation button in the modal window



**Font**
- The Fonts used was the ones preset in the template.
 
**Font-sans-serif:**  system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", "Liberation Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";

**Font-monospace:** SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
    
**Input format**
All the forms in the page count with some security features to guide the user to introduce the data in a secured and correct way. Therefore, in the **log in** and **resgiter** forms are required to enter a user and passwords with a length of max-15 and min-5 characters. These characters have to be numbers and upper and lower case letters. 

For **Adding and Editing a coktail** users have a max-400 and min-5 characters per filling box. lower and upper cases are allowed as well as special characters. 
For the Url. users need to add a valid "http//:" url in order to fill the box. 

There were
<span id="Features"></span>
## 2. Features
### 2.1. Existing features


 

### 2.1.1 Home:

This feature is the main page of the site.
Here users will come across with all the recipes sorted out by the different types of alcohol each cocktail uses. Besides user can find in the navigation-bar the option to register and login in order to have access to more features. Moreover, Users can also use the search-bar to speed up the search of a recipe. 



### 2.1.2 Navigation bar:  
This website has a navigation bar that displays different features depending on the actions te user takes. If a user registers and logs in, then the features from the navigation bar will be different from those who do not do it. A first time visitor will only find in the Nabvar the chance to register and login. And if they create an account the Navbar will display also the options to add a recipe, log out or user profile. 
        


### 2.1.3 Register:
On this feature users can create an account adding a user name and a password 

### 2.1.4 Log In: 
Through this feature user access to the content reserved to those who have an account. Thus, the members can add, edit and delete their own recipes.

### 2.1.5 Profile: 
Is a page with some information from the user. Here the user finds a list with the cocktails added by him/her. is in this part of the site where users have the option to edit, or delete their own cocktails.   

### 2.1.6 log Out:
 When cliking on this option the user leaves his/her account, having access only to the home page. It means they are not allowed to add, edit or erase any recipe.   

 ### 2.1.7 Add a Cocktail:
All registered users have the chance to add new cocktails to the page through a form linked to the dababase in order to keep it updated. 

 ### 2.1.8 Search bar:
In order to help users to easily find  a recipe or just an ingrediente amongst all recipes there is a search bar located in the header of the home page in which they can type the term needed and  it will be filtered and displayed in  the screen.
 ### 2.1.9 Edit Cockatil:
Users have the chance to edit the cocktails they added thought a edit button located in their profile page. This edit button will lead the user to a prefilled form which can be easily updated.
### 2.2 Features left to implement in the future
 - In the future, I would like to add a section where visitors can leave reviews of the cocktails.  
- I would also like the to let user upload their own pictures 


<span id="Technologies"></span>
## 3. Technologies Used

This website was built using:
- [HTML](https://html.com) **HTML**is used to create pages and make them functional.
- [CSS](https://css3.com) **Css** is used to style the page
- [Boostrap](https://Boostrap.com) **Boostrap** is used also to style the page
- [Fontawesome](https://fontawesome.com/) **Fontawesome** used to add icons
- [Googlefont](https://fonts.google.com/) **Googlefont** used to set the font
- [Gitpot](http://gitpod.io/) **Gitpod** use to edit and built the page
- [Github](http://github.com/) **Github** use to storage the page 
- [Figma](http://figma.com/) **Figma** used to creat a wireframe or mock-up 
- [Photoshop](http://photoshop.com/) **Photoshop** used to edit the images used in the page. 
- [Responsivedesign](http://ami.responsivedesign.is/) **Responsive Design** to show how it looks in defferent devices. 
- [Startbootstrap](https://startbootstrap.com/template/heroic-features) **Startbootstrap** html and css template used to build the front-end
 - [materializecss](https://materializecss.com/) **Materialized** A modern responsive front-end framework based on Material Design
 - [Flask](https://flask.palletsprojects.com/en/2.0.x/) **Flask** 
 is a web framework. tahts provides tools, libraries and technologies that allows to build a web application. 
 - [Python](https://www.python.org/) **Python** is a computer programming language used to build websites and software, automate tasks, and conduct data analysis.
 - [JavaScript](https://www.javascript.com/) **JavaScript** is a text-based programming language used both on the client-side and server-side that allows you to make web pages interactive 
- [Heroku](https://www.heroku.com/) **Heroku** is use to deploy, manage, and scale modern apps.
- [Mongodb](https://www.mongodb.com/)**MongoDB** is a cloud database

 <span id="Testing"></span>
## 4. Testing

  - [Results Here](testing.md)
 

  
<span id="Deployment"></span>
## 5. Deployment

### **5.1 Github deployment and cloning**
- **Open github**
![Github.com](/Readme-images/github.png)

- **Open juliandavid-garcia/MS3_Cocktails**
![Repository](/Readme-images/respository.png)

- **Go to settings.**
![setting](/Readme-images/settings.png)

- **Open setting and scrolled down until Github Pages and ckicl on "Check it out here!"**
![pages](/Readme-images/pages.png)


- **Click on the None dropdowmenu and select the branch to publish : main**
![pages](/Readme-images/main.png)


-  **Click save**
![Save](/Readme-images/save.png)

- **The website is now deployed.**
![Save](/Readme-images/deployed.png)

- [Deployed site address](https://juliandavid-garcia.github.io/MS3_Cocktails/)

## 5.2. To clon the repository using GitHub Desktop
- **Download and install GitHub Desktop**

 [Download GitHub Desktop](https://desktop.github.com/)

- **Open github**
![Github.com](/Readme-images/github.png)

- **Open juliandavid-garcia/MS3_Cocktails**
![Repository](/Readme-images/respository.png)

- **Click on the button "Code"**
![code](/Readme-images/code.png)

- **Select "Open with GitHub Desktop" to clone
 and open the respository with GitHub Desktop.**
![Desktop](/Readme-images/desktop.png)

- **Allow Github desktop to open the file you want to clone**
![Allow](/Readme-images/allow.png)

- **Choose where you want to save your cloned file**
![path](/Readme-images/path.png)

- **Give a name to your cloned file.**
![folder name](/Readme-images/destination.png)

- **Go to the archive where you decided to save your cloned document and you will have your cloned document there..**
![Cloned](/Readme-images/cloned.png)

### 5.3 **Heroku deployment**
- **Go to Heroku.com, log in and choose the project you want to deploy**
![folder name](/Readme-images/Projecto.png)

- **Go to deploy**
![folder name](/Readme-images/deply.png)

 - **As a deployment method select GitHub "Connect to GitHub**
![folder name](/Readme-images/deplo_heroku.png)

 - **Search your github account and select the repository you want to conect**
![folder name](/Readme-images/repository_name.png)

- **Click on "Conect"**
![folder name](/Readme-images/conect.png)

- **Go to settings and scrolldown until "Config Vars" section and  click on the "Reveal Config Vars" button**
![folder name](/Readme-images/reveal.png)

- **Fill in the form with the date from the env.py file you have in your repository**
![folder name](/Readme-images/fill_in.png)

- **Return to the deploy section, selecte the branch main and enable automatic deploys**
![folder name](/Readme-images/automatic_deploy.png)

- **Finally clock on the "Deploy Branch" to deploy the site**
![folder name](/Readme-images/deploy_branch.png)

- [Deployed site address](https://flask-cocktail-bible.herokuapp.com/)



<span id="Credits"></span>
## 6. Credits:
The front-end of this website was built based on the template Heroic Features from [startbootstrap](https://startbootstrap.com/template/heroic-features)

- [Html and css Template](https://startbootstrap.com/template/heroic-features)

The forms used to add and edit the recipes were built using features from materialized [materializecss](https://materializecss.com/select.html) :

- [Form](https://materializecss.com/select.html)

The icons where taken from:
- [Font awesome](https://fontawesome.com/icons)

In order to display the recipes collapsible boxes taken from materializedcss: 
 - [Materializecss](https://materializecss.com/collapsible.html)

 The data base used fot his porject was mongodb :
 - [Mongodb](https://www.mongodb.com/)

 The search bar was built using materializedcss form :
 - [Search bar](https://materializecss.com/text-inputs.html)

<span id="Media"></span>
## 7. Media
The photo used in this site as hero image was obtained from :
- [Unsplash](https://unsplash.com/photos/MzsWrM8DSCU)

Pictures used in the recipes were obtained from the following websites:
- [**Mojito**: la-cucina.be](https://www.la-cucina.be/sites/default/files/styles/recept-afbeelding/public/mojito.jpg?itok=Lg9_TYKk)

- [**Whiskey sour**: bonappetit.com](https://assets.bonappetit.com/photos/57acc14e53e63daf11a4d9b6/1:1/w_2560%2Cc_limit/whiskey-sour.jpg)

- [**Old Fashioned**: thespruceeats.com](https://www.thespruceeats.com/thmb/fShdgWfPHQDDiytQJo7MGcTmG0s=/960x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/old-fashioned-cocktail-recipe-and-history-759328-hero-01-c9002b3aa6d24a3781befa19dc69eb0e.jpg)

- [**Mint julep**: diffords.com](https://cdn.diffords.com/contrib/stock-images/2020/07/5f0ec1c93c570.jpg)

- [**Smoked & Salted**: diffords.com](https://cdn.diffords.com/contrib/stock-images/2018/05/5af313a25d7fc.jpg)

- [**Piña Colada**: kookmutsjes.com](https://adminwp.kookmutsjes.com/wp-content/uploads/2020/05/Pina-colada-Kookmutsjes.jpg)

- [**Dark-n-Stormy**: nyt.com](https://static01.nyt.com/images/2014/04/23/dining/Dark-n-Stormy/Dark-n-Stormy-articleLarge.jpg)

- [**swizzle**: liquor.com](https://www.liquor.com/thmb/lAIEy2Og_85HpD0oSs0MlG85w0k=/960x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/bermuda-rum-swizzle-720x720-primary-ab9d5694a0924c45ba495ba10c0aea3a.jpg)

- [**Skinny-Bitch**: ketovoorbeginners.com](https://ketovoorbeginners.com/wp-content/uploads/2019/08/Skinny-Bitch.jpg)

- [**Moscow Mule**: hearstapps.com](https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/tanbackground-1553877785.jpg)

- [**Gimlet**: liquor.com](https://www.liquor.com/thmb/0sYe7S3WyK8FK6HfwuJGDzeU3uc=/735x0/__opt__aboutcom__coeus__resources__content_migration__liquor__2019__01__10072454__gimlet-720x720-recipe-a0d317f2ce7b4818a0fdbd2bbaaaf2c9.jpg)

- [**Cosmopolitan**: wikimedia.org](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c0/Cosmopolitan_%285076906532%29.jpg/220px-Cosmopolitan_%285076906532%29.jpg)

- [**Sidecar**: liquor.com](https://www.liquor.com/thmb/4KGXdt5wcHTEE3azDlWUaOTCYnE=/735x0/__opt__aboutcom__coeus__resources__content_migration__liquor__2019__05__22111906__sidecar-720x720-recipe-4758380fb7ef4adfaafa21c3f4eed264.jpg)


- [**Banana Bliss** cocktailmag.fr](https://www.cocktailmag.fr/media/k2/items/cache/51a3864ed3ad604d2340c3f8fe249f94_M.jpg)

- [**Tequila-Sunrise** acouplecooks.com](https://www.acouplecooks.com/wp-content/uploads/2020/04/Tequila-Sunrise-003s.jpg)

- [**TPORNSTAR 43** licor43.com](https://www.licor43.com/nl-nl/wp-content/uploads/sites/3/2019/10/l43-recipe-square--0011-porn-star-43-500x500.jpg)






## 8. Acknowledgements
<span id="Acknowledgements"></span>
- I received inspiration for this project from the previous miniproject(task-manager) covered in the previous unit.

- Thanks to Precious Ijege for his mentoring while developing this project. His advices, patience and support were of high relevance to carry out this project. 


- ## 9. Github
<span id="Github"></span>
You can find this project on 
[My Github](https://github.com/juliandavid-garcia)
