# Testing

- <a href="#1">1. Code Validators</a>
- <a href="#2">2. Responsiveness</a>
- <a href="#3">3. Browser Compatibility</a>
- <a href="#4">4. User Stories</a>
- <a href="#5">5. Bugs</a>

---

<span id="#1"></span>
## 1. Code validators

### [HTML Validator](https://validator.w3.org/): 



### [CSS Validator](https://jigsaw.w3.org/css-validator/): 


### [JSHint JavaScript Validator](https://jshint.com/):


### [PEP8 Python Validator](http://pep8online.com/): 


---

<span id="#2"></span>
## 2. Responsiveness
To test the responsiveness of the site I used [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools) and [Responsive Design Checker](https://www.responsivedesignchecker.com/).
I also asked some family members and friends to test it on their devices.

---

<span id="#3"></span>
## 3. Browser compatibility

---

<span id="#4"></span>
## 4. User Stories


---

<span id="#5"></span>
## 5. Bugs

- NoReverseMatch - When creating the edit blog functionality, a NoReverseMatch error was showing when attempting to go to the main blog page. 
    - Because I was using the same url in both the main blog page and the individual post page, I didn't realize that in the main blog page, the edit button was inside a for loop where the object was called 'post' and not 'blog' like it was called in the views.py file, so I just had to change 'blog' for 'post' and it worked properly.

- TypeError: 'AnonymousUser' object is not iterable - When a non logged in user tried to purchase an item (or many), they would get an error when clicking 'Complete order' in the checkout page. 
  - This was fixed adding an if statement that would check if hte user is authenticated just before saving the order's information in the views.py file in the checkout app.

- Modal deleting wrong product id.
To add security and avoid users (superusers) clicking the delete button by mistake, I decided to add a modal. This modal didn't delete the item I clicked on but it picked the first product 
- With help from the CI tutors we found out that when a modal with a variable ID is used (meaning there are multiple products on the page), it tends to pick the first one. So to fix this we decided to make the ID dynamic and its match on the button

* The same issue occured with the modal I developed to delete a blog post in the blogs page, and this was fixed the same way

---

[Go back to README.md file](README.md).