# Plantas&co. Shop
![Plantas&co. Shop]()
Plantas&co. is a fictitious online shop that sells all kinds of indoor plants, but also dry flowers bouquets. 
Besides shopping, users of Plantas&co. will find a blog where both beginners and expers can find some useful tips on how to take care of their plants.

---
#### CONTENT
- <a href="#1-UX">1. UX</a>
  - <a href="#1-UX-1">1.1 Project Goals</a>
  - <a href="#1-UX-2">1.2 User Stories</a>
  - <a href="#1-UX-3">1.3 Design Choices</a>
  - <a href="#1-UX-4">1.4 Database Design</a>
  - <a href="#1-UX-5">1.5 Wireframes</a>
- <a href="#2-FEAT">2. Features</a>
  - <a href="#2-FEAT-1">2.1 Existing Features</a>
  - <a href="#2-FEAT-2">2.2 Potential Features</a>
- <a href="#3-TECH">3. Technologies Used</a>
- <a href="#4-TEST">4. Testing</a>
- <a href="#5-DEPL">5. Deployment</a>
- <a href="#6-CRED">6. Credits</a>

---
 
<span id="1-UX"></span>
## 1. UX

<span id="1-UX-1"></span>
### 1.1 Project Goals
The primary goal of Plantas&co. shop is to provide a clean, intuitive online shop where the user can browse and purchase different types of plants easily. 

Another main goal is to provide the users with a blog to keep them informed with advice to take care of their plants at home.

<span id="1-UX-2"></span>
### 1.2 User Stories

##### Viewing and Navigation
- As a shopper, I want to be able to view a list of products so that I can select some to purchase
- As a shopper, I want to be able to view individual product details so that I can identify the price, description and product image
- As a shopper, I want to be able to quickly identify special offers so that I can take advantage of special savings on products I'd like to purchase
- As a shopper, I want to be able to easily view the total of my purchases at anytime so that I can avoid spending too much

##### Registration and User Account
- As a site user, I want to be able to easily register for an account so that I can have a personal account and be able to view my profile
- As a site user, I want to be able to easily login or logout so that I can access my personal account information
- As a site user, I want to be able to easily recover my password in case I forget it so that I can recover access to my account
- As a site user, I want to be able to receive an email confirmation after registering so that I can verify that my account registration was successful
- As a site user, I want to be able to have a personalized user profile so that I can view my personal order history and order confirmation, save my payment information and see the products I saved in my favourites listx

##### Sorting and Searching
- As a shopper, I want to be able to sort the list of available products so that I can easily identify the best priced and categorically sorted products
- As a shopper, I want to be able to sort a specific category of product so that I can find the best-priced product in a specific category, or sort the products in that category by name
- As a shopper, I want to be able to sort multiple categories of products simultaneously so that I can find the best-priced products across broad categories, such as "indoor plants" or "dry flowers"
- As a shopper, I want to be able to search for a product by name or description so that I can find a specific product I'd like to purchase
- As a shopper, I want to be able to easily see what I've searched for and the number of results so that I can quickly decide whether the product I want is available

##### Purchasing and Checkout
- As a shopper, I want to be able to easily select the quantity of a product when purchasing it so that I can ensure I don't accidentally select the wrong product or quantity
- As a shopper, I want to be able to view items in  my bag to be purchased so that I can identify the total cost of my purchase and all items I will receive
- As a shopper, I want to be able to adjust the quantity of individual items in my bag so that I can easily make changes to my purchase before checkout
- As a shopper, I want to be able to easily enter my payment information so that I can check out quickly and with no hassles
- As a shopper, I want to be able to feel my personal and payment information is safe and secure so that I can confidently provide the needed information to make a purchase
- As a shopper, I want to be able to view an order confirmation after checkout so that I can verify that I haven't made any mistakes
- As a shopper, I want to be able to receive an email confirmation after checking out so that I can keep the confirmation of what I've purchased for my records

##### Admin and Store Management
- As a shopper, I want to be able to add a product so that I can add new items to my store
- As a shopper, I want to be able to edit/update a product so that I can change product prices, descriptions, images and other product criteria
- As a shopper, I want to be able to delete a product so that I can remove items that are no longer for sale


<span id="1-UX-3"></span>
### 1.3 Design Choices

**Fonts**: 
- The main font Raleway was chosen for being a clear, aesthetic and readable font.
- The secondary font Playfair Display was used to create the logo for having an elegant feeling.

Both fonts were imported from [Google Fonts](https://fonts.google.com/)

**Colors**:
To give the project a clean look, the main colors chosen were off-black and off-white, with two shades of blue-green to emphasize some areas like the shop now button.

**Images**:

<span id="1-UX-4"></span>
### 1.4 Database Design

<span id="1-UX-5"></span>
### 1.5 Wireframes


---

<span id="2-FEAT"></span>
## 2. Features

<span id="2-FEAT-1"></span>
### 2.1 Existing Features
 
**Site wide**:
- **Navbar**: gives consistency and allow users to navigate the site in an easy and intuitive way. There are two versions of it: one for larger screen sizes and one for smaller screen sizes. Both of them include the same features:

  - **Home Button**: allows users to go back to the Home page from any part of the page
  - **Shop Button**: opens a side menu in larger screen sizes and a dropdown in mobile that allows users to go to the 'All Products' page and to the main categories: Indoor Greenery, Cacti and Dry Flowers
  - **Plants Tips Button**: allows users to go to the Blog
  - **Logo**: allows users to identify where they are and to go back to the Home page from any part of the page.
  - **Search Icon Button**: in larger screen sizes opens a side nav menu that allow users to search for any product in the shop
  - **Bag Icon Button**: allows users to access the Shopping Bag page from any part of the site
  - **Account Button**: opens a side menu in larger screen sizes and a dropdown in mobile that shows different features depending on the user type:
    - Anonymous users can see a ‘Register’ and a ‘Login’ link
    Registered users can see a ‘My Profile’, ‘My Wishlist’ and ‘logout’ links
    Superusers can see the same ‘My Profile’, ‘My Wishlist’ and ‘Logout’ links and also ‘Product Management - Add Product’ and ‘Product Management - Add Blog Post’ 

- **Footer**:
  - **Contact Us**: informs users of the shop's (fake) contact details
  - **Logo**: reminds users where they are and to go back to the Home page from any part of the page.
  - **Follow Us**: allows users to view the shop's (fake) social accounts

- **Home Page**: 
  - **Jumbotron**: works as a call to action and includes a button for the users to go directly to the All Products page
  - **Links to main categories**: allows users to access directly the category they are searching for: Indoor Plants, Dry Flowers and Cacti
  - **Blog Link**: informs the user that the shop also offers advice about plants and encourage them to visit the blog
  - **Shop values**: gives the users a quick glance about the shop's values

- **Products Page**

- **Product Detail Page**

- **Bag Page**

- **Checkout Page**

- **Checkout Success Page**

- **Profile Page**

- **Wishlist Page**

- **Blog Page**

- **Blog Post Page**

- **Register Page**

- **Log In Page**

- **Log Out Page**


Restricted to Superusers

- **Add Product Page**

- **Edit Product Page**

- **Add Blog Post Page**

- **Edit Blog Post Page**





 
<span id="2-FEAT-2"></span>
### 2.2 Potential Features


---

<span id="3-TECH"></span>
## 3. Technologies Used

---
 
<span id="4-TEST"></span>
## 4. Testing

BUGS

- NoReverseMatch - When creating the edit blog functionality, a NoReverseMatch error was showing when attempting to go to the main blog page. 
    - Because I was using the same url in both the main blog page and the individual post page, I didn't realize that in the main blog page, the edit button was inside a for loop where the object was called 'post' and not 'blog' like it was called in the views.py file, so I just had to change 'blog' for 'post' and it worked properly.

- TypeError: 'AnonymousUser' object is not iterable - When a non logged in user tried to purchase an item (or many), they would get an error when clicking 'Complete order' in the checkout page. 
  - This was fixed adding an if statement that would check if hte user is authenticated just before saving the order's information in the views.py file in the checkout app.


 
---
 
<span id="5-DEPL"></span>
## 5. Deployment
 
### 5.1 Heroku deployment

### 5.2 Running This Project Locally


---
 
<span id="6-CRED"></span>
## 6. Credits
 
### 6.1 Code

- This project was developed following the Boutique Ado project tutorial from [Code Institute](https://codeinstitute.net/). The code was adapted to fit the purpose of this project.
- The code to create the side navbar menu functionality is from [W3Schools](https://www.w3schools.com/howto/howto_js_sidenav.asp)
- The code to style the blog posts is from [W3Schools](https://www.w3schools.com/howto/howto_css_image_text.asp)
- I got inspiration from [KeisGSmit](https://github.com/KeisGSmit/Gymshop) to create the Wishlist app

### 6.2 Content

- The posts in the blog app are originally from this article in [modsy.com](https://blog.modsy.com/home-design-tips-guides/tips-guides/indoor-plants-care/) and also from [hunker.com](https://www.hunker.com/13411862/how-to-care-for-dried-flowers)
- The text talking about the company values in the home page is originally from [thesill.com](https://www.thesill.com/)
- The information about the plants and how to take care of them was obtained from the following sources:
    - https://gardeningit.com/
    - https://www.thespruce.com/
    - https://www.houseplantsexpert.com/
    - https://www.evergreenseeds.com/
    - https://feey.ch/
    - https://www.leafyplace.com/
    - https://succulentcareguide.com/
    - https://theyardandgarden.com/
    - https://sproutingindoors.com/
DISCLAIMER:
Although deep research has been made to provide an accourate description and real useful information about the type of plants and how to take care of them, this could still not be 100% true in some cases.

### 6.3 Media

- The images used for the main page, blog and background belong to [Ceyda Çiftci](https://unsplash.com/@ceydaciftci) in [Unsplash](https://unsplash.com/)
- The images used as product images belong to [Severin Candrian](https://unsplash.com/@feeypflanzen) in [Unsplash](https://unsplash.com/)

### 6.4 Acknowledgments