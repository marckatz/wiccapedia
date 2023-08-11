# Phase 4 PROJECT: Wiccapedia


## To Run The Application
- Clone the repository down to your machine.
- To run the api server
- From the top directory, run pipenv install & pipenv shell
- run python server/app.py
- To start the react app
- Open a second terminal
- From the top directory, run npm start --prefix client
- Then run npm install --prefix client
- Start interacting!

## User Stories:
- A user can sign up for an account or login if they are already signed up
- A user can create new Pages or edit existing pages if they are logged in
- A user can check the history of all the edits to the page to track and see what changes were made.
- A user can view their profile while logged in to see which pages they have edited and which they have authored
- A user can change their password from the user profile page
- A user can view pages on the site through the search feature
- A user can search by partial text and will be directed to the page if found or to a search results page if multiple pages match the search query
- A user who has logged in remains logged in until they have chosen to log out


## Routes:
- Navbar: Is shown on all pages to allow a user to search for a page, and to sign up or login, as well as to logout, create a new page, or view profile if logged in
- Home: "/" Base Route to the homepage includes information and some statistics about user edits & page edits
- Login: "/login" Routes to a form to ask the user to login with their username and password
- SignUp: "/signup" Routes to a form to ask the user to signup by providing a username and password
- Page: "/page/:pageId" Routes to the content of a Page as well as buttons to link to the editPage and the History
- ViewHistory: "/history/:pageId" Routes to the history of edits made to a page, as well as buttons to link to the Page and the editPage
- EditPage: "/edit/:pageId" Routes to a form that allows changes to be made to the text of the page and then submitted, as well as buttons to link to the Page and the History
- SearchResults: "/search/:query" Routes to the search results which lists links to all pages that come up from a search
- UserProfile: "/profile" Routes to the profile of the logged in user including past edits and created pages
- PostPage: "/post" Routes to page for creating a new page which requets a title and text for the content of the page
- NoutFound: "/notfound" Routes to generic 404 not found page for requests to pages that do not exist.

## Models:
Models are stored in seperate files in the models directory.  The models user a many-to-many relationship as diagramed below.

User>---Edit----<Page

`User` : Model has username and password both stored as a string

`Page` : Model has title, author, and text.  Text stores the content of the page as a string

`Edit` : Model has page_id, user_id, and diff.  Diff stores the changes made to page as a string