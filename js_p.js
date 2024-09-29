// 1, Basic structures


document.addEventListener('DOMContentLoaded', () => {
    // Some code here
});

array.forEach(function(element, index, array) {
    // Code to execute for each element
});

document.querySelector('h1')


const li = document.createElement('li');
document.querySelector('#tasks').append(li);


setInterval(count, 1000);

localStorage.getItem(key)
localStorage.setItem(key, value)
 

history.pushState({section: section}, "", `section${section}`);

// When back arrow is clicked, show previous section
window.onpopstate = function(event) {
    console.log(event.state.section);
    showSection(event.state.section);
}

window.onscroll = () => {
    if (window.innerHeight + window.scrollY >= document.body.offsetHeight) {
        load();
    }
};


// 2, some basics

let counter = 0;
function count() {
    counter++;
    document.querySelector('h1').innerHTML = counter;
    
    if (counter % 10 === 0) {
        alert(`Count is now ${counter}`)
    }
}


button.onclick = function() {
    showPage(this.dataset.page);
}


document.querySelector('form').onsubmit = function() {
    const button = document.querySelector('button');
    const head = document.querySelector('#hello');
    head.style.color = button.dataset.color;

    const name = document.querySelector('#name').value;
    alert(`Hello, ${name}`);
};


document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('select').onchange = function() {
        document.querySelector('#hello').style.color = this.value;
    }
});


document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('select').onchange = (event) => {
        document.querySelector('#hello').style.color = event.target.value;
    }
});

document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('form').onsubmit = function() {

        // Send a GET request to the URL
        fetch('https://api.exchangeratesapi.io/latest?base=USD')
        // Put response into json form
        .then(response => response.json())
        .then(data => {
            // Get currency from user input and convert to upper case
            const currency = document.querySelector('#currency').value.toUpperCase();

            // Get rate from data
            const rate = data.rates[currency];

            // Check if currency is valid:
            if (rate !== undefined) {
                // Display exchange on the screen
                document.querySelector('#result').innerHTML = `1 USD is equal to ${rate.toFixed(3)} ${currency}.`;
            }
            else {
                // Display error on the screen
                document.querySelector('#result').innerHTML = 'Invalid Currency.';
            }
        })
        // Catch any errors and log them to the console
        .catch(error => {
            console.log('Error:', error);
        });
        // Prevent default submission
        return false;
    }
});

function showSection(section) {
                
    // Find section text from server
    fetch(`/sections/${section}`)
    .then(response => response.text())
    .then(text => {
        // Log text and display on page
        console.log(text);
        document.querySelector('#content').innerHTML = text;
    });
}




// 3, events

onsubmit
onclick
onmouseover
onkeydown
onload
onblur
onchange 
onscroll

animationend

// 4, properties and methods

.value
.value.length
.innerHTML
.className
.style.color
.style.display
.style.background
.style.animationPlayState
.dataset.color
.state.
.target
.parentElement


// 5,

// Use regular functions when you need this to be dynamically bound based on how the function is called.
// Use arrow functions when you want this to be lexically bound (i.e., inherit from the surrounding scope).


texts = ["Text 1", "Text 2", "Text 3"]

def section(request, num):
    if 1 <= num <= 3:
        return HttpResponse(texts[num - 1])
    else:
        raise Http404("No such section")