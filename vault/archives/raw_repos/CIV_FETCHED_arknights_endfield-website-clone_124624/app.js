const operatorImage = document.querySelector('.img-operator-0')
const imgOptions = document.querySelectorAll('.img-char-box')

const opName = document.querySelector('.op-name')
const opQuote = document.querySelector('.op-quote')
const opBio = document.querySelector('.op-bio-1')
const opBioTwo = document.querySelector('.op-bio-2')

for (let i = 0; i < imgOptions.length; i++) {
    imgOptions[i].addEventListener('click', function() {

        operatorImage.className = ''
        operatorImage.classList.add('img-operator')
        operatorImage.classList.add(`img-operator-${i}`)

        imgOptions.forEach((img) => {
            img.classList.remove('active')
            img.classList.add('inactive')
        })

        imgOptions[i].classList.remove('inactive')
        imgOptions[i].classList.add('active')

        //Descriptions of Characters

        if (operatorImage.classList.contains('img-operator-0') || operatorImage.classList.contains('img-operator-1')) { 
            opName.textContent = 'Endministrator';
            opQuote.textContent = 'The Endministrator of Endfield Industries'
            opBio.textContent = 'Rumors claim that the Endministrator showed up on multiple occasions whenever a crisis hits Endfield Industries or Talos-II, creating many legends and stories.'
        }

        if (operatorImage.classList.contains('img-operator-2')) { 
            opName.textContent = 'Perlica';
            opQuote.textContent = '"She is capable of responding to various crises in a calm and decisive manner."'
            opBio.textContent = 'Perlica is the Supervisor of Endfield Industries in charge of directing various operations according to the plans of the Endfield leadership.'
        }

        if (operatorImage.classList.contains('img-operator-3')) { 
            opName.textContent = 'Wulfgard';
            opQuote.textContent = '"I know that strength isn\'t\ everything, but in Talos-II, you can\'\t live without it."'
            opBio.textContent = 'As a young mercenary living in the fringes of civilization, Wulfgard is already very familiar with the darkest aspects of humanity.'
        }

        if (operatorImage.classList.contains('img-operator-4')) { 
            opName.textContent = 'Xaihi';
            opQuote.textContent = '"The angels I know definitely look nothing like this."'
            opBio.textContent = 'Very few people know anything about Xaihi\'\s past. They only heard that she came from an isolated and mysterious place where people have an odd reverence for technology.'
        }

         //Reliably Play Animation When Characters Swap
         if (operatorImage.style.animationName === 'slide-in') {
            operatorImage.style.animation = "slide-in-alt 1000ms"
        } else {
            operatorImage.style.animation = "slide-in 1000ms"
        }
    })
}