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
The HTML validator was used on every html file in the project. It mainly returned Django related errors that were ignored. Some examples below:
![](readme-files/html-django.png)

This test also returned some other non Django related errors. These were all fixed accordingly.
![](readme-files/html-1.png)
![](readme-files/html-2.png)

### [CSS Validator](https://jigsaw.w3.org/css-validator/): 
The CSS validator was used on the following files:
- base.css
- checkout.css
- profile.css

The test returned no warnings in checkout.css and profile.css. However, the test returned two type of warnings in the base.css file:
- related to the buttons' colours and borders. These warnings were ignored since they were design choices and they don't affect any functionality of the code.
- related to browser cross-compatibility. These warnings were also ignored in order to have the content render properly on every browser.
![](readme-files/css-warnings.png)


The test returned no errors in any of the files
![](readme-files/css-error.png)

### [JSHint JavaScript Validator](https://jshint.com/):
The JavaScript validator was used on all .js files and JavaScript code snippets in the project. 
The test returned no errors, just a few recommendations about missing semicolons that were fixed.

### [PEP8 Python Validator](http://pep8online.com/): 
The PEP8 Python Validator along with the `python3 -m flake8` command were used on all .py files and some of those files returned a few formatting errors:
- line too long
- trailing whitespace
- no newline at end of file
- continuation line missing indentation or outdented

Most of these formatting errors were fixed successfully.

---

<span id="#2"></span>
## 2. Responsiveness
To test the responsiveness of the site I used [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools) and [Responsive Design Checker](https://www.responsivedesignchecker.com/).
I also asked some family members and friends to test it on their devices.

---

<span id="#3"></span>
## 3. Browser compatibility
![](readme-files/browser-comp.png)

---

<span id="#4"></span>
## 4. User Stories


---

<span id="#5"></span>
## 5. Bugs

- NoReverseMatch - When creating the edit blog functionality, a NoReverseMatch error was showing when attempting to go to the main blog page. 
    - Because I was using the same url in both the main blog page and the individual post page, I didn't realize that in the main blog page, the edit button was inside a for loop where the object was called 'post' and not 'blog' like it was called in the views.py file, so I just had to change 'blog' for 'post' and it worked properly.

- TypeError: 'AnonymousUser' object is not iterable - When a non logged in user tried to purchase an item (or many), they would get an error when clicking 'Complete order' in the checkout page. 
  - This was fixed by adding an if statement that would check if the user is authenticated just before saving the order's information in the views.py file in the checkout app.

- Modal deleting wrong product id.
To add security and avoid users (superusers) clicking the delete button by mistake, I decided to add a modal. This modal didn't delete the item I clicked on but it picked the first product 
  - With help from the CI tutors we found out that when a modal with a variable ID is used (meaning there are multiple products on the page), it tends to pick the first one. So to fix this we decided to make the ID dynamic and its match on the button

The same issue occurred with the modal I developed to delete a blog post in the blogs page, and this was fixed the same way

### Bugs to fix
A bug I couldn't fix before submission is the quantity button in the bag app that doesn't work properly in larger screen sizes. I used the same code snippet for both larger screen sizes and smaller screen sizes and while it works perfectly in the smaller versions, in the larger ones the user can press minus and go below zero. 
This isn't a huge issue for the proper functionality of the page because when the user updates the product to be minus, the product will be simply deleted from the shopping bag.

Another bug to fix in the future is the delivery info in the checkout app that saves even with the check button unmarked.

---

[Go back to README.md file](README.md).