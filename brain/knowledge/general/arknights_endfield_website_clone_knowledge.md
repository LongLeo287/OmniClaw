# Knowledge Dump for arknights_endfield_website_clone

## File: DEEP_KNOWLEDGE.md
```
# Deep Matrix Profile: CIV_FETCHED_arknights_endfield-website-clone_124624

# Deep Knowledge Report for Arknight Endfield Website Clone

## Overview
The `app.js` file in this repository is responsible for handling the dynamic interactions of character images on a website clone of the Arknight Endfield game. The script uses event listeners and class manipulation to update content based on user interaction, ensuring that the layout remains responsive and engaging.

## Architectural Patterns

### Event-Driven Architecture
The primary mechanism used in `app.js` is an event-driven architecture where each character image has a click event listener attached to it. This pattern allows for modular code where individual components (in this case, images) can trigger specific actions without needing to know the details of how those actions are implemented.

### Class Manipulation
The script heavily relies on class manipulation to update the state of elements. By adding and removing classes like `active` and `inactive`, it dynamically changes the appearance and behavior of UI components. This approach is efficient as it leverages CSS for styling, reducing the need for complex JavaScript logic.

## Core Algorithms

### Character Image Selection
The script iterates over a collection of image options using a `for` loop to attach event listeners. Each listener updates the main character image (`operatorImage`) and its associated content (name, quote, bio) based on which image was clicked. This ensures that only one character can be active at any given time.

### Animation Management
The script manages animations by checking the current animation name of `operatorImage` and switching between two possible animations: `slide-in` and `slide-in-alt`. This is done to provide a smooth transition when swapping characters, enhancing user experience with visual feedback.

## Primary Mechanisms

### Dynamic Content Updates
- **Character Name**: The `opName.textContent` property updates the text content of the character name based on which image was clicked.
- **Character Quote**: The `opQuote.textContent` property updates the quote associated with the selected character.
- **Character Bio**: The `opBio.textContent` and `opBioTwo.textContent` properties update the biographical information for the character.

### State Management
The script uses class manipulation to manage state. For example:
- `.active` and `.inactive` classes are used to toggle between active and inactive states of the image options.
- The main character image (`operatorImage`) has specific classes added or removed based on which image is clicked, affecting its appearance and animations.

### Animation Logic
The script checks if `operatorImage` currently has a specific animation name (e.g., `slide-in`). If it does, it switches to the alternative animation (`slide-in-alt`), ensuring smooth transitions between character images. This logic is encapsulated within an `if-else` statement for clarity and maintainability.

## Conclusion
The `app.js` script effectively manages dynamic content updates and state changes using event listeners and class manipulation. It ensures that user interactions are smooth and engaging, providing a seamless experience as users explore different characters in the Arknight Endfield game clone. The use of animations enhances visual feedback, making the interaction more enjoyable.

This approach is both efficient and maintainable, leveraging modern web development practices to create an interactive and responsive UI.
```

## File: README.md
```
# Arknights Endfield Website Clone

**OmniClaw Operator Skill**

Assimilated OmniClaw Skill for arknights_endfield_website_clone.

## Internal Resources
- Schema Definition: schema.json
- Context Execution: SKILL.md

```

## File: schema.json
```
{
    "name": "Arknights Endfield Website Clone",
    "description": "Assimilated OmniClaw Skill for arknights_endfield_website_clone.",
    "domain": "frontend",
    "tier": 3,
    "type": "assimilated_repo_skill",
    "parameters": {}
}
```

## File: SKILL.md
```
---
id: arknights_endfield_website_clone
name: Arknights Endfield Website Clone
version: 1.0.0
tier: 3
status: active
author: OmniClaw Assimilation Daemon
updated: 2026-04-09
domain: frontend
---

# Arknights Endfield Website Clone

This skill was assimilated from an external raw repository.
Reference README.md or DEEP_KNOWLEDGE.md for specific technical payload.

```

## File: _DIR_IDENTITY.md
```
---
id: arknights_endfield_website_clone
type: skill
owner: OA
registered_at: 2026-04-08T13:20:54.282838
tags: ["auto-cloned", "CSS Grid", "Website Clone", "Animation", "oa-assimilated", "premium-repo"]
---

# CIV_FETCHED_arknights_endfield-website-clone_124624

## Assimilation Report
This repository contains the code for a website clone of the Arknight Endfield game. The project uses CSS Grid to handle layout and overlapping content, which is described as making the layout more maintainable. It also includes hover effects, animations, pseudo-elements, and gradient patterns.

## Application for OmniClaw
EMERGENCY FALLBACK: LLM failed to analyze. However, because this is a CIV-Approved Repo, OA forces assimilation. Please manually review and integrate.

```

## File: payload\app.js
```
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
```

## File: payload\DEEP_KNOWLEDGE.md
```
# Deep Matrix Profile: CIV_FETCHED_arknights_endfield-website-clone_124624

# Deep Knowledge Report for Arknight Endfield Website Clone

## Overview
The `app.js` file in this repository is responsible for handling the dynamic interactions of character images on a website clone of the Arknight Endfield game. The script uses event listeners and class manipulation to update content based on user interaction, ensuring that the layout remains responsive and engaging.

## Architectural Patterns

### Event-Driven Architecture
The primary mechanism used in `app.js` is an event-driven architecture where each character image has a click event listener attached to it. This pattern allows for modular code where individual components (in this case, images) can trigger specific actions without needing to know the details of how those actions are implemented.

### Class Manipulation
The script heavily relies on class manipulation to update the state of elements. By adding and removing classes like `active` and `inactive`, it dynamically changes the appearance and behavior of UI components. This approach is efficient as it leverages CSS for styling, reducing the need for complex JavaScript logic.

## Core Algorithms

### Character Image Selection
The script iterates over a collection of image options using a `for` loop to attach event listeners. Each listener updates the main character image (`operatorImage`) and its associated content (name, quote, bio) based on which image was clicked. This ensures that only one character can be active at any given time.

### Animation Management
The script manages animations by checking the current animation name of `operatorImage` and switching between two possible animations: `slide-in` and `slide-in-alt`. This is done to provide a smooth transition when swapping characters, enhancing user experience with visual feedback.

## Primary Mechanisms

### Dynamic Content Updates
- **Character Name**: The `opName.textContent` property updates the text content of the character name based on which image was clicked.
- **Character Quote**: The `opQuote.textContent` property updates the quote associated with the selected character.
- **Character Bio**: The `opBio.textContent` and `opBioTwo.textContent` properties update the biographical information for the character.

### State Management
The script uses class manipulation to manage state. For example:
- `.active` and `.inactive` classes are used to toggle between active and inactive states of the image options.
- The main character image (`operatorImage`) has specific classes added or removed based on which image is clicked, affecting its appearance and animations.

### Animation Logic
The script checks if `operatorImage` currently has a specific animation name (e.g., `slide-in`). If it does, it switches to the alternative animation (`slide-in-alt`), ensuring smooth transitions between character images. This logic is encapsulated within an `if-else` statement for clarity and maintainability.

## Conclusion
The `app.js` script effectively manages dynamic content updates and state changes using event listeners and class manipulation. It ensures that user interactions are smooth and engaging, providing a seamless experience as users explore different characters in the Arknight Endfield game clone. The use of animations enhances visual feedback, making the interaction more enjoyable.

This approach is both efficient and maintainable, leveraging modern web development practices to create an interactive and responsive UI.
```

## File: payload\index.html
```
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="style.css">
    <title>Arknights: Endfield</title>
</head>

<body>
    <div class="nav-section stacked">
        <div class="img-nav-decoration"></div>
        <nav class="navbar">

            <img src="./images/endfield-logo.png" width="90rem" height="auto" class="img-navbar-logo" loading="lazy"
                alt="">

            <div class="navbar-links">
                <ul>
                    <li><a href="#home">HOME</a></li>
                    <li><a href="#section-operators">OPERATORS</a></li>
                    <li><a href="#section-news">NEWS</a></li>
                    <li><a href="#links">LINKS</a></li>
                </ul>
            </div>

            <div class="nav-right-wrapper">
                <div>LOG IN</div>
            </div>

        </nav>
    </div>





    <div id="home" class="section-video stacked">
        <div class="sign-in-button">
            <button>SIGN UP</button>
        </div>
        <video class="video-main" autoplay muted loop>
            <source src="./images/main-video.mp4" type="video/mp4">
        </video>
    </div>


    <div class="section-main-image stacked">
        <div class="main-img-side-content">

            <img src="./images/endfield-logo.png" class="img-logo-big" width="65%" alt="" loading="lazy">

            <div class="play-btn-paragraph">
                <a target="_blank" rel="noopener"
                    href="https://www.youtube.com/watch?v=Yt7eUS1X0Ec&ab_channel=Arknights%3AEndfield">
                    <svg class="play-button" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 321 321" width="3rem">
                        <g xmlns="http://www.w3.org/2000/svg" fill="#fdfd1f">
                            <path
                                d="M0 308h13v13H0zM0 0h13v13H0zM308 308h13v13h-13zM308 0h13v13h-13zM32.5 108.9h-19V13.4H109v19H32.5v76.5zM212.5 32.4v-19H308v95.5h-19V32.4h-76.5zM289 212.4h19v95.5h-95.5v-19H289v-76.5zM109 288.9v19H13.5v-95.5h19v76.5H109zM235.5 160.5L111 88.6v143.8l124.5-71.9z" />
                        </g>
                    </svg>
                </a>
                <p>Arknights: Endfield is a real-time 3D RPG with strategic elements by HYPERGRYPH.</p>
            </div>
        </div>
        <div class="img-main-preview"></div>
    </div>




    <div id="section-operators" class="stacked">

        <div class="img-banner-white">
            <div class="banner-text-operator">OPERATORS</div>
        </div>

        <div class="img-fixed-background"></div>

        <div class="grid-operators-layout">

            <div class="op-img-wrapper">
                <div class="img-operator-0 img-operator"></div>
            </div>

            <div class="character-info">
                <div class="info-text">
                    <img src="./images/opr-title.webp" loading="lazy" width="150vw" height="auto" alt="">

                    <div class="op-name h2">Endministrator</div>

                    <span class="endfield-decoration">Endfield</span>

                    <div class="op-quote h3">The Endministrator of Endfield Industries</div>
                    <div class="op-bio-1 bio">Rumors claim that the Endministrator showed up on multiple occasions
                        whenever
                        a crisis hits Endfield Industries or Talos-II, creating many legends and stories.
                    </div>
                </div>

                <div class="character-select-wrapper">
                    <div class="img-char-box-1 img-char-box active"></div>
                    <div class="img-char-box-2 img-char-box inactive"></div>
                    <div class="img-char-box-3 img-char-box inactive"></div>
                    <div class="img-char-box-4 img-char-box inactive"></div>
                    <div class="img-char-box-5 img-char-box inactive"></div>
                </div>

            </div>
            
        </div>

    </div>

    <div id="section-news" class="stacked">

        <div class="img-banner-news"></div>

        <div class="banner-yellow-wrapper">
            <div class="left-spaced text-banner-yellow">LATEST</div>
        </div>

        <div class="banner-news-wrapper">
            <img src="./images/opr-title.webp" loading="lazy" width="150vw" height="auto" class="left-spaced" alt="">
            <div class="section-title left-spaced">Latest News</div>
            <div class="deco-line-left left-spaced"></div>
        </div>

    </div>


    <div class="news-cards stacked">

        <div class="cards-flex left-spaced">

            <div class="card">
                <div class="img-card-1 img-card"></div>
                <div class="card-text">
                    <h3>Arknights: Endfield Technical Test Server Closure Notice</h3>
                    <span class="date">1/19/2024</span> <span>NOTICES</span>
                    <p>Arknights: Endfield Technical Test is scheduled to conclude on 2024 Jan 21 at 15:00 (UTC).</p>
                </div>
            </div>

            <div class="card">
                <div class="img-card-2 img-card"></div>
                <div class="card-text">
                    <h3>Arknights: Endfield Technical Test Server Closure Notice</h3>
                    <span class="date">1/11/2024</span> <span>NOTICES</span>
                    <p>Dear Endministrators: Arknights: Endfield Technical Test is about to kick off.</p>
                </div>
            </div>

            <div class="card">
                <div class="img-card-3 img-card"></div>
                <div class="card-text">
                    <h3>Arknights: Endfield Technical Test Server Closure Notice</h3>
                    <span class="date">1/5/2024</span> <span>NOTICES</span>
                    <p>Dear Endministrators: We've distributed all Technical Test access.</p>
                </div>
            </div>

            <div class="card">
                <div class="img-card-4 img-card"></div>
                <div class="card-text">
                    <h3>Arknights: Endfield Technical Test Server Closure Notice</h3>
                    <span class="date">12/11/2023</span> <span>NOTICES</span>
                    <p>Greetings, Endministrators! Thank you for your continued interest in Arknights: Endfield.</p>
                </div>
            </div>

        </div>

    </div>


    <footer id="links">
        <div class="socials-links">
            <ul>
                <li><a target="_blank" rel="noopener" href="https://twitter.com/AKEndfield">
                    <svg xmlns="http://www.w3.org/2000/svg" width="2rem" viewBox="0 0 24 24"><path fill="#959595" d="M22.46 6c-.77.35-1.6.58-2.46.69c.88-.53 1.56-1.37 1.88-2.38c-.83.5-1.75.85-2.72 1.05C18.37 4.5 17.26 4 16 4c-2.35 0-4.27 1.92-4.27 4.29c0 .34.04.67.11.98C8.28 9.09 5.11 7.38 3 4.79c-.37.63-.58 1.37-.58 2.15c0 1.49.75 2.81 1.91 3.56c-.71 0-1.37-.2-1.95-.5v.03c0 2.08 1.48 3.82 3.44 4.21a4.22 4.22 0 0 1-1.93.07a4.28 4.28 0 0 0 4 2.98a8.521 8.521 0 0 1-5.33 1.84c-.34 0-.68-.02-1.02-.06C3.44 20.29 5.7 21 8.12 21C16 21 20.33 14.46 20.33 8.79c0-.19 0-.37-.01-.56c.84-.6 1.56-1.36 2.14-2.23"/></svg>
                </a></li>
                <li><a target="_blank" rel="noopener" href="https://www.facebook.com/ArknightsEndfield">
                    <svg xmlns="http://www.w3.org/2000/svg" width="2rem" viewBox="0 0 24 24"><path fill="#959595" d="M22 12c0-5.52-4.48-10-10-10S2 6.48 2 12c0 4.84 3.44 8.87 8 9.8V15H8v-3h2V9.5C10 7.57 11.57 6 13.5 6H16v3h-2c-.55 0-1 .45-1 1v2h3v3h-3v6.95c5.05-.5 9-4.76 9-9.95"/></svg>
                </a></li>
                <li><a target="_blank" rel="noopener" href="https://www.youtube.com/channel/UCowPaVRBzg8CE6K4CB6LJfw">
                    <svg xmlns="http://www.w3.org/2000/svg" width="2rem"  viewBox="0 0 24 24"><g fill="none" fill-rule="evenodd"><path d="M24 0v24H0V0zM12.593 23.258l-.011.002l-.071.035l-.02.004l-.014-.004l-.071-.035c-.01-.004-.019-.001-.024.005l-.004.01l-.017.428l.005.02l.01.013l.104.074l.015.004l.012-.004l.104-.074l.012-.016l.004-.017l-.017-.427c-.002-.01-.009-.017-.017-.018m.265-.113l-.013.002l-.185.093l-.01.01l-.003.011l.018.43l.005.012l.008.007l.201.093c.012.004.023 0 .029-.008l.004-.014l-.034-.614c-.003-.012-.01-.02-.02-.022m-.715.002a.023.023 0 0 0-.027.006l-.006.014l-.034.614c0 .012.007.02.017.024l.015-.002l.201-.093l.01-.008l.004-.011l.017-.43l-.003-.012l-.01-.01z"/><path fill="#959595" d="M12 4c.855 0 1.732.022 2.582.058l1.004.048l.961.057l.9.061l.822.064a3.802 3.802 0 0 1 3.494 3.423l.04.425l.075.91c.07.943.122 1.971.122 2.954c0 .983-.052 2.011-.122 2.954l-.075.91c-.013.146-.026.287-.04.425a3.802 3.802 0 0 1-3.495 3.423l-.82.063l-.9.062l-.962.057l-1.004.048A61.59 61.59 0 0 1 12 20a61.59 61.59 0 0 1-2.582-.058l-1.004-.048l-.961-.057l-.9-.062l-.822-.063a3.802 3.802 0 0 1-3.494-3.423l-.04-.425l-.075-.91A40.662 40.662 0 0 1 2 12c0-.983.052-2.011.122-2.954l.075-.91c.013-.146.026-.287.04-.425A3.802 3.802 0 0 1 5.73 4.288l.821-.064l.9-.061l.962-.057l1.004-.048A61.676 61.676 0 0 1 12 4m-2 5.575v4.85c0 .462.5.75.9.52l4.2-2.425a.6.6 0 0 0 0-1.04l-4.2-2.424a.6.6 0 0 0-.9.52Z"/></g></svg>
                </a></li>
                <li><a target="_blank" rel="noopener" href="https://www.instagram.com/akendfieldofficial/">
                    <svg xmlns="http://www.w3.org/2000/svg" width="2rem" viewBox="0 0 24 24"><g fill="none" stroke="#959595" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M12 16a4 4 0 1 0 0-8a4 4 0 0 0 0 8"/><path d="M3 16V8a5 5 0 0 1 5-5h8a5 5 0 0 1 5 5v8a5 5 0 0 1-5 5H8a5 5 0 0 1-5-5Z"/><path stroke-linecap="round" stroke-linejoin="round" d="m17.5 6.51l.01-.011"/></g></svg>
                </a></li>
                <li><a target="_blank" rel="noopener" href="https://discord.com/invite/akendfield">
                    <svg xmlns="http://www.w3.org/2000/svg" width="2rem" viewBox="0 0 24 24"><path fill="#959595" d="M19.27 5.33C17.94 4.71 16.5 4.26 15 4a.09.09 0 0 0-.07.03c-.18.33-.39.76-.53 1.09a16.09 16.09 0 0 0-4.8 0c-.14-.34-.35-.76-.54-1.09c-.01-.02-.04-.03-.07-.03c-1.5.26-2.93.71-4.27 1.33c-.01 0-.02.01-.03.02c-2.72 4.07-3.47 8.03-3.1 11.95c0 .02.01.04.03.05c1.8 1.32 3.53 2.12 5.24 2.65c.03.01.06 0 .07-.02c.4-.55.76-1.13 1.07-1.74c.02-.04 0-.08-.04-.09c-.57-.22-1.11-.48-1.64-.78c-.04-.02-.04-.08-.01-.11c.11-.08.22-.17.33-.25c.02-.02.05-.02.07-.01c3.44 1.57 7.15 1.57 10.55 0c.02-.01.05-.01.07.01c.11.09.22.17.33.26c.04.03.04.09-.01.11c-.52.31-1.07.56-1.64.78c-.04.01-.05.06-.04.09c.32.61.68 1.19 1.07 1.74c.03.01.06.02.09.01c1.72-.53 3.45-1.33 5.25-2.65c.02-.01.03-.03.03-.05c.44-4.53-.73-8.46-3.1-11.95c-.01-.01-.02-.02-.04-.02M8.52 14.91c-1.03 0-1.89-.95-1.89-2.12s.84-2.12 1.89-2.12c1.06 0 1.9.96 1.89 2.12c0 1.17-.84 2.12-1.89 2.12m6.97 0c-1.03 0-1.89-.95-1.89-2.12s.84-2.12 1.89-2.12c1.06 0 1.9.96 1.89 2.12c0 1.17-.83 2.12-1.89 2.12"/></svg>
                </a></li>
            </ul>
        </div>

        <div class="links">
            <ul>
                <li>PRIVACY POLICY</li>
                <li>TERMS OF SERVICE</li>
                <li>CONTACT US</li>
            </ul>
        </div>

        <div class="gryphline-copyrights">
            <div>
                <svg class="icon" viewBox="0 0 310 57" width="7rem">
                    <g fill="currentColor"><g>
                        <path d="M235.59,35.5H218.46l5-27.27H216l-6.31,34.52h24.45Zm36.6-27.27-4.06,22.24L261.62,8.23h-9.78l-6.31,34.52H253L257,20.51l6.51,22.24h9.78l6.31-34.52Zm-29.66,0-6.31,34.52h7.42L250,8.23ZM137.06,27.7l0,.23-2.71,14.82h7.41l2.71-14.82.21-1.14.51-.66L158.55,8.5l-6.26,34.25h7.42l1.76-9.62h8.15a13.7,13.7,0,0,0,10.31-4.21,15.29,15.29,0,0,0,3.23-4.87l-3.42,18.7h7.42l2.45-13.4h12.94l-2.45,13.4h7.41l6.31-34.52h-7.41L203.87,22.1H190.93l2.54-13.87h-7.41l-1.62,8.84A9.46,9.46,0,0,0,175,8.23H150.08l-6.59,8.67h-1.82l-3.26-8.67h-8.68l6.74,17.9Zm27.6-12h8.93a3.16,3.16,0,0,1,3.16,3.15v.76a6.24,6.24,0,0,1-6.25,6.24h-7.7Zm139.72-.21,1.42-7.25h-24l-6.31,34.52h24l1.42-7.25H284.25l1.12-6.15h15.22L302,22.1H286.7l1.21-6.62ZM126.74,42.75l-4.06-10.57a14.05,14.05,0,0,0,4.87-3.26,16.14,16.14,0,0,0,4.53-11.24,9.45,9.45,0,0,0-9.45-9.45h-16.4L99.92,42.75h7.41l1.76-9.62h5.28l3.69,9.62ZM110.42,25.84l1.86-10.15h8.93a3.15,3.15,0,0,1,3.16,3.15v.76a6.24,6.24,0,0,1-6.24,6.24ZM98.06,27H84.81l-1.35,7.4h8.67l-1.52,8.36H98L100.9,27ZM72.33,24.54A13.39,13.39,0,0,1,85.15,14c5.88.1,9.73,4.91,8.65,10.77h7.33c1.78-9.83-4.69-17.89-14.56-18S67,14.49,65,24.44,69.55,42.6,79.51,42.77h.14L81,35.43h0C75,35.33,71.17,30.45,72.33,24.54ZM40.75,13,1.21,50.38l2.41,2.54L43.16,15.51ZM0,24.84H24.39l5.7-5.39,10.55-10,5.55,5.85.22.23-.32.3-9.5,9-9.06,8.57L24,52.86H48.85L58.51,0h-54Zm119,26h1.56l-.14.82-.48.41h-1.59l-.33-.41.61-3.46.48-.41h1.58l.34.41-.13.76h1.58l.23-1.35-1.07-1.3h-2.95l-1.54,1.3-.82,4.64,1.08,1.3h3l1.52-1.29.47-2.7h-3.15Zm4.66-4.53-1.27,7.24H124l.47-2.69h.13l2.36,2.95,1.33-1.12L126.87,51l-.31-.25,0,0,.33.18h.37l1.33-1.12.4-2.31-.92-1.12ZM127.16,49l-.43.38h-2l.27-1.59h2l.31.38ZM134,46l-2.06,3-.24.71h0v-.71l-1-3-1.54.72,1.49,4.52-.4,2.26h1.58l.39-2.24,3.1-4.54Zm6.91,1.55-1.07-1.29h-4.26l-1.28,7.24h1.59l.4-2.31h2.68l1.53-1.3ZM139,49.34l-.48.41h-2l.35-2h2l.34.41Zm6.12-.21h-2.4l.5-2.83h-1.58l-1.28,7.24h1.58l.51-2.93h2.4l-.51,2.93h1.58l1.28-7.24h-1.58Zm7.18-1.35h3.45L156,46.3h-5l-1.28,7.24h1.59l.48-2.75h3l.26-1.48h-3Zm7.38,3.07H160l1.33-1.12.4-2.31-.93-1.12h-4.43l-1.27,7.24h1.58l.47-2.69h.13l2.36,2.95L161,52.68,159.63,51l-.31-.25,0,0Zm-2.22-1.48.28-1.59h2l.31.38-.15.83-.43.38Zm9.45-3.07h-3l-1.66,1.28-.81,4.68,1.19,1.28h3l1.65-1.28.81-4.68Zm-1.11,5.33-.54.43h-1.77l-.4-.43.61-3.42.54-.43H166l.4.43Zm6.56-1.54v.69h0l-.14-.68-1.71-3.8H169l-1.27,7.24h1.58l.66-3.79v-.69h.05l.14.68,1.71,3.8h1.42l1.28-7.24H173Zm2.3-2.31h2l-1,5.76h1.58l1-5.76h2l.26-1.48h-5.56Zm8.15-.1h1L184,46.3h-3.54l-.24,1.38h1l-.8,4.48h-1l-.24,1.38h3.55l.23-1.38h-1Zm5.6,2.82.26-1.48h-3l.21-1.24h3.45l.27-1.48h-5l-1.28,7.24h5l.26-1.48H185.1l.27-1.56ZM190,46.3l-1.28,7.24h1.58l.47-2.69h.14l2.36,2.95,1.32-1.12L193.19,51l-.3-.25,0,0,.33.18h.36l1.33-1.12.41-2.31-.93-1.12Zm3.5,2.69-.43.38h-2l.28-1.59h2l.3.38Zm9.86-2.69h-4.26l-1.28,7.24h1.58l.41-2.31h2.68l1.53-1.3.41-2.34Zm-.82,3-.48.41h-2l.34-2h2l.33.41Zm7.69-3h-5.57l-.26,1.48h2l-1,5.76h1.58l1-5.76h2Zm-1,7.24h5l.26-1.48h-3.45l.27-1.56h3l.27-1.48h-3l.21-1.24h3.45l.27-1.48h-5ZM220.5,46.3h-1.58l-1.28,7.24h4.93l.26-1.48h-3.35Zm8.71,0h-5.56l-.27,1.48h2l-1,5.76h1.58l1-5.76h2Zm4.58,0h-4.27l-1.28,7.24h4.27L234,52.23l.82-4.62Zm-1.23,5.35-.48.41h-2l.76-4.28h2l.33.41Zm2.37.32-.51.43-.15.87.35.42h.88l.5-.42.16-.87-.4-.43Z"></path></g><g><path d="M40.75,13,1.21,50.38l2.41,2.54L43.16,15.51ZM4.54,0,0,24.84H24.39l5.7-5.39,10.55-10,5.55,5.85.22.23-.32.3-9.5,9-9.06,8.57L24,52.86H48.85L58.51,0Z"></path></g><g><path d="M235.59,35.5H218.46l5-27.27H216l-6.31,34.52h24.45Zm36.6-27.27-4.06,22.24L261.62,8.23h-9.78l-6.31,34.52H253L257,20.51l6.51,22.24h9.78l6.31-34.52Zm-29.66,0-6.31,34.52h7.42L250,8.23ZM137.06,27.7l0,.23-2.71,14.82h7.41l2.71-14.82.21-1.14.51-.66L158.55,8.5l-6.26,34.25h7.42l1.76-9.62h8.15a13.7,13.7,0,0,0,10.31-4.21,15.29,15.29,0,0,0,3.23-4.87l-3.42,18.7h7.42l2.45-13.4h12.94l-2.45,13.4h7.41l6.31-34.52h-7.41L203.87,22.1H190.93l2.54-13.87h-7.41l-1.62,8.84A9.46,9.46,0,0,0,175,8.23H150.08l-6.59,8.67h-1.82l-3.26-8.67h-8.68l6.74,17.9Zm27.6-12h8.93a3.16,3.16,0,0,1,3.16,3.15v.76a6.24,6.24,0,0,1-6.25,6.24h-7.7Zm139.72-.21,1.42-7.25h-24l-6.31,34.52h24l1.42-7.25H284.25l1.12-6.15h15.22L302,22.1H286.7l1.21-6.62ZM126.74,42.75l-4.06-10.57a14.05,14.05,0,0,0,4.87-3.26,16.14,16.14,0,0,0,4.53-11.24,9.45,9.45,0,0,0-9.45-9.45h-16.4L99.92,42.75h7.41l1.76-9.62h5.28l3.69,9.62ZM110.42,25.84l1.86-10.15h8.93a3.15,3.15,0,0,1,3.16,3.15v.76a6.24,6.24,0,0,1-6.24,6.24ZM98.06,27H84.81l-1.35,7.4h8.67l-1.52,8.36H98L100.9,27ZM72.33,24.54A13.39,13.39,0,0,1,85.15,14c5.88.1,9.73,4.91,8.65,10.77h7.33c1.78-9.83-4.69-17.89-14.56-18S67,14.49,65,24.44,69.55,42.6,79.51,42.77h.14L81,35.43h0C75,35.33,71.17,30.45,72.33,24.54ZM119,50.83h1.56l-.14.82-.48.41h-1.59l-.33-.41.61-3.46.48-.41h1.58l.34.41-.13.76h1.58l.23-1.35-1.07-1.3h-2.95l-1.54,1.3-.82,4.64,1.08,1.3h3l1.52-1.29.47-2.7h-3.15Zm4.66-4.53-1.27,7.24H124l.47-2.69h.13l2.36,2.95,1.33-1.12L126.87,51l-.31-.25,0,0,.33.18h.37l1.33-1.12.4-2.31-.92-1.12ZM127.16,49l-.43.38h-2l.27-1.59h2l.31.38ZM134,46l-2.06,3-.24.71h0v-.71l-1-3-1.54.72,1.49,4.52-.4,2.26h1.58l.39-2.24,3.1-4.54Zm6.91,1.55-1.07-1.29h-4.26l-1.28,7.24h1.59l.4-2.31h2.68l1.53-1.3ZM139,49.34l-.48.41h-2l.35-2h2l.34.41Zm6.12-.21h-2.4l.5-2.83h-1.58l-1.28,7.24h1.58l.51-2.93h2.4l-.51,2.93h1.58l1.28-7.24h-1.58Zm7.18-1.35h3.45L156,46.3h-5l-1.28,7.24h1.59l.48-2.75h3l.26-1.48h-3Zm7.38,3.07H160l1.33-1.12.4-2.31-.93-1.12h-4.43l-1.27,7.24h1.58l.47-2.69h.13l2.36,2.95L161,52.68,159.63,51l-.31-.25,0,0Zm-2.22-1.48.28-1.59h2l.31.38-.15.83-.43.38Zm9.45-3.07h-3l-1.66,1.28-.81,4.68,1.19,1.28h3l1.65-1.28.81-4.68Zm-1.11,5.33-.54.43h-1.77l-.4-.43.61-3.42.54-.43H166l.4.43Zm6.56-1.54v.69h0l-.14-.68-1.71-3.8H169l-1.27,7.24h1.58l.66-3.79v-.69h.05l.14.68,1.71,3.8h1.42l1.28-7.24H173Zm2.3-2.31h2l-1,5.76h1.58l1-5.76h2l.26-1.48h-5.56Zm8.15-.1h1L184,46.3h-3.54l-.24,1.38h1l-.8,4.48h-1l-.24,1.38h3.55l.23-1.38h-1Zm5.6,2.82.26-1.48h-3l.21-1.24h3.45l.27-1.48h-5l-1.28,7.24h5l.26-1.48H185.1l.27-1.56ZM190,46.3l-1.28,7.24h1.58l.47-2.69h.14l2.36,2.95,1.32-1.12L193.19,51l-.3-.25,0,0,.33.18h.36l1.33-1.12.41-2.31-.93-1.12Zm3.5,2.69-.43.38h-2l.28-1.59h2l.3.38Zm9.86-2.69h-4.26l-1.28,7.24h1.58l.41-2.31h2.68l1.53-1.3.41-2.34Zm-.82,3-.48.41h-2l.34-2h2l.33.41Zm7.69-3h-5.57l-.26,1.48h2l-1,5.76h1.58l1-5.76h2Zm-1,7.24h5l.26-1.48h-3.45l.27-1.56h3l.27-1.48h-3l.21-1.24h3.45l.27-1.48h-5ZM220.5,46.3h-1.58l-1.28,7.24h4.93l.26-1.48h-3.35Zm8.71,0h-5.56l-.27,1.48h2l-1,5.76h1.58l1-5.76h2Zm4.58,0h-4.27l-1.28,7.24h4.27L234,52.23l.82-4.62Zm-1.23,5.35-.48.41h-2l.76-4.28h2l.33.41Zm2.37.32-.51.43-.15.87.35.42h.88l.5-.42.16-.87-.4-.43Z"></path></g></g>
                </svg>
            </div>
            <div class="copyrights">Copyright © 2022-2023 GRYPHLINE. GRYPH FRONTIER PTE. LTD. All Rights Reserved.</div>
        </div>
    </footer>


    <script src="app.js"></script>
</body>

</html>
```

## File: payload\main.py
```
# This is the main Python script for the Arknights Endfield website clone
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
```

## File: payload\README.md
```
# Arknights Endfield Website Clone
This is a simple clone of the official Arknights Endfield website using Flask.
## Requirements
- Python 3.x
- Flask
## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/OmniClaw/arknights-endfield-website-clone.git
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python main.py
   ```
```

## File: payload\requirements.txt
```
Flask==2.1.2
```

## File: payload\style.css
```
:root {
    --fs-s: .8rem;
    --fs-m: 1rem;
    --fs-h3: 1.2rem;
    --fs-l: 1.5rem;
    --fs-xl: 2.2rem;
    --fs-banner: 9rem;
}

@media (width < 660px) {
    :root {
        --fs-s: .8rem;
        --fs-m: .8rem;
        --fs-h3: 1rem;
        --fs-l: 1.3rem;
        --fs-xl: 1.6rem;
        --fs-banner: 6.7rem;
    }
}

@media (width < 460px) {
    :root {
        --fs-s: .5rem;
        --fs-m: .6rem;
        --fs-h3: .8rem;
        --fs-l: 1.1rem;
        --fs-xl: 1.3rem;
        --fs-banner: 5.3rem;
    }
}

*,
*::before,
*::after {
    box-sizing: border-box;
}

* {
    margin: 0;
    padding: 0;
}

[class*="img-"] {
    max-width: 100%;
    height: auto;
    vertical-align: middle;
    font-style: italic;
    background-repeat: no-repeat;
    background-size: cover;
    overflow-x: clip;
}

/* Self-hosted Fonts  */

/* Sans-3  */
@font-face {
    font-display: swap;
    font-family: 'Source Sans 3';
    font-style: normal;
    font-weight: 200;
    src: url('./fonts/sans-3/source-sans-3-v15-latin-200.woff2') format('woff2');
  }

  @font-face {
    font-display: swap; 
    font-family: 'Source Sans 3';
    font-style: normal;
    font-weight: 300;
    src: url('./fonts/sans-3/source-sans-3-v15-latin-300.woff2') format('woff2'); 
  }
  @font-face {
    font-display: swap;
    font-family: 'Source Sans 3';
    font-style: normal;
    font-weight: 400;
    src: url('./fonts/sans-3/source-sans-3-v15-latin-regular.woff2') format('woff2'); 
  }
  @font-face {
    font-display: swap; 
    font-family: 'Source Sans 3';
    font-style: normal;
    font-weight: 500;
    src: url('./fonts/sans-3/source-sans-3-v15-latin-500.woff2') format('woff2'); 
  }
  @font-face {
    font-display: swap; 
    font-family: 'Source Sans 3';
    font-style: normal;
    font-weight: 600;
    src: url('./fonts/sans-3/source-sans-3-v15-latin-600.woff2') format('woff2');
  }
  @font-face {
    font-display: swap;
    font-family: 'Source Sans 3';
    font-style: normal;
    font-weight: 700;
    src: url('./fonts/sans-3/source-sans-3-v15-latin-700.woff2') format('woff2'); 
  }
  @font-face {
    font-display: swap;
    font-family: 'Source Sans 3';
    font-style: normal;
    font-weight: 800;
    src: url('./fonts/sans-3/source-sans-3-v15-latin-800.woff2') format('woff2'); 
  }
  @font-face {
    font-display: swap; 
    font-family: 'Source Sans 3';
    font-style: normal;
    font-weight: 900;
    src: url('./fonts/sans-3/source-sans-3-v15-latin-900.woff2') format('woff2'); 
  }

  /* Inter  */
@font-face {
    font-display: swap; 
    font-family: 'Inter';
    font-style: normal;
    font-weight: 400;
    src: url('./fonts/inter/inter-v13-latin-regular.woff2') format('woff2');
  }
  @font-face {
    font-display: swap; 
    font-family: 'Inter';
    font-style: normal;
    src: url('./fonts/inter/inter-v13-latin-900.woff2') format('woff2');
  }
  
  

body {
    font-family: 'Source Sans 3', sans-serif;
    font-size: var(--fs-m);
    padding-top: 5.7rem;
}

.nav-section {
    width: 100%;
    position: fixed;
    top: 0;
    z-index: 100;
}

.navbar {
    display: flex;
    align-items: center;
    padding: 1rem;
    color: white;
    position: relative;
}
.navbar::before {
    content: '';
    position: absolute;
    bottom: 0;
    left: 0;
    background-image:
     linear-gradient(90deg,#ff00f0 17.5%,
     #fff100 17.5% 35.6%,
     #00ffa2 35.6% 100%);
    width: 100%;
    height: 2px;
}

.img-navbar-logo { margin-right: 2rem; }
@media (width > 660px) {.img-navbar-logo { margin-left: 2rem; } }



.navbar-links ul,
footer ul {
    margin: 0;
    padding: 0;
    display: flex;
}

.navbar-links li,
footer li {
    list-style: none;
}

.navbar-links li a,
footer li a {
    text-decoration: none;
    color: white;
    padding: 1rem;
}
@media (width < 660px) { .navbar-links { display: none; } }

.navbar-links li a:hover { color: #fff100; }



.nav-right-wrapper {
    background-color: yellow;
    color: black;
    position: absolute;
    top: 0;
    right: 0;
    bottom: 0;
    width: 12rem;
    
    display: flex;
    justify-content: center;
    align-items: center;

    background-image: url("./images/nav-yellow-bg.jpg");
    background-position: right;
    background-size: 95%;
    cursor: pointer;
}
@media (width < 700px) {
    .nav-right-wrapper { display: none; }
}



/* Using Grid to Stack content with images and video */
.stacked {
    display: grid;
}

.stacked > * {
    grid-column: 1 / -1;
    grid-row: 1 / -1;
}

.stacked > .img-main-preview,
.video-main, .img-nav-decoration {
    z-index: -1;
}


.img-nav-decoration {
    background-image: url("./images/nav-decoration.jpg");
    padding-block: 3rem;
    background-position: center;
}
@media (width < 700px) { .img-nav-decoration { background-position: 35%; } }


.section-video {
    position: relative;
    overflow: hidden;
    height: 100dvh;
    width: 100%;
}

.video-main {
    vertical-align: middle;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    min-width: 100%;
    min-height: 100%;
}


.sign-in-button {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-end;
    margin-bottom: 10%;
}

button {
    font-size: var(--fs-m);
    font-weight: 700;
    color: #525249;
    background-color: #fff100;
    border-style: none;
    border-radius: 22px;
    cursor: pointer;
    padding: .5rem 1.7rem;
    border: 2px solid #bcb30a;

    background-image: url("./images/nav-yellow-bg.jpg");
    background-position: center;
    background-size: 90%;
}

button::before, button::after {
    content: '';
    display: inline-block;
    height: 4px;
    width: 4px;
    background-color: #bcb30a;
    vertical-align: middle;
}
button::before { margin-right: 1.5rem; }
button::after{ margin-left: 1.5rem; }


@media (max-width: 720px) {
    .section-video { height: 70vh; }
}




/* Main Image Section  */

.img-main-preview {
    padding-block: 25%;
    background-image: url("./images/main-preview-large.jpg");
    background-position: center;
}

@media (width < 660px) {
    .img-main-preview {
        padding-block: 80%;
        background-image: url("./images/main-preview-small.jpg");
    }
}

.main-img-side-content {
    background-color: rgb(0, 0, 0, 0.55);
    color: white;
    width: 23rem;
    height: 100%;

    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 15%;
    padding-left: 3rem;
}

@media (width < 1190px) { .main-img-side-content { width: 31vw; } }

@media (width < 660px) {
    .main-img-side-content {
        width: 100%;
        height: 31vh;
        margin-top: auto;
    }

    .img-logo-big { display: none; }
}

.play-btn-paragraph .play-button { margin-bottom: 2rem; }

.play-btn-paragraph p {
    font-size: var(--fs-s);
    padding-right: min(1rem, 2rem);
}
@media (width < 660px) { .play-btn-paragraph p { font-size: 1rem} }





/* Operators Section  */

.img-fixed-background {
    background-image: url("./images/fixed-bg.jpg");
    padding-block: 25dvh;
    background-attachment: fixed;
}


.img-banner-white {
    background-image: url("./images/block-texture.jpg");
    z-index: 0;
    height: 27vh;
}

.banner-text-operator { padding-left: 2rem; }

.img-banner-white div {
    font-family: 'Inter', sans-serif;
    font-size: 10vw;
    margin-top: 4vh;
    opacity: 0.45;

    background: repeating-linear-gradient(
      -55deg,
      black,
      black 1px,
      white 1px,
      white 4px
      );
    background-clip: text;
    color: transparent;
}

@media (width < 1200px) { .img-banner-white div { padding-top: 4vh; } }
@media (width < 1000px) { .img-banner-white div { padding-top: 6.5vh; } }
@media (width > 1500px) { .img-banner-white div { margin-top: 0rem; } }

@media (width < 700px) { .img-banner-white div { display: none; } }

.op-img-wrapper {
    z-index: 3;
    width: 90%;
    margin-left: auto;
}

.img-operator {
    margin-top: -5%;
    padding-block: 55%;
    animation: slide-in-alt 1000ms;
    z-index: 100;
}

/* Create animations for Operators appearances */
@keyframes slide-in {
    from {
        transform: translateX(-10%);
        opacity: 0.25;
    }

    to {
        transform: translateX(0%);
        opacity: 1;
    }
}

@keyframes slide-in-alt {
    from {
        transform: translateX(-10%);
        opacity: 0.25;
    }

    to {
        transform: translateX(0%);
        opacity: 1;
    }
}

.img-operator-0 { background-image: url("./images/char-1.png"); }
.img-operator-1 { background-image: url("./images/char-2.png"); }
.img-operator-2 { background-image: url("./images/char-3.png"); }
.img-operator-3 { background-image: url("./images/char-4.png"); }
.img-operator-4 { background-image: url("./images/char-5.png"); }

.img-operator { grid-area: image }
.character-info { grid-area: text; }

.grid-operators-layout {
    margin-top: 13vh;
    display: grid;
    grid-auto-columns: 1fr;
    grid-template-areas:
        'image text';
}


.character-info { z-index: 1; }

@media (width > 700px) { .character-info { padding-right: 4rem; } }

.character-info .h2 { 
    font-size: var(--fs-xl); 
    font-weight: 800;
}

.character-info .h3, .character-info .bio {
    margin-bottom: .5rem;
    padding-right: 1.5rem;
}

@media (width > 1600px) { .character-info .h3, .character-info .bio { padding-right: 6rem; } }

.character-info .h3 { font-size: var(--fs-h3); }

.character-info .bio { font-size: var(--fs-m); }


.endfield-decoration {
    font-size: var(--fs-s);
    color: white;
    background-color: black;
    padding-inline: .5rem;
    margin-bottom: 1rem;

    position: relative;
    display: inline-block;
}

/* Make space for the decorative text on smaller screens  */

@media (width < 660px) {
    .op-name {margin-bottom: -1rem; }

    .character-info .h3 { margin-bottom: .5rem; }

    .endfield-decoration { margin-bottom: .5rem; }
}


/* Decorate the text using pseudo elements  */

.endfield-decoration::before, .endfield-decoration::after {
    content: '';
    height: .8rem;
    display: block;
    position: absolute;
}

.endfield-decoration::before {
    background-color: #fff100;
    width: 100vw;
    right: 100%;
    bottom: 0;
    overflow-x: clip;
}

.endfield-decoration::after {
    width: 40vw;
    left: 100%;
    bottom: 0;
    overflow-x: clip;

    opacity: 0.45;

    background: repeating-linear-gradient(
      -55deg,
      black,
      black 1px,
      white 1px,
      white 4px
      );
}


.img-char-box-1 { background-image: url("./images/portrait01.webp"); }
.img-char-box-2 { background-image: url("./images/portrait02.webp"); }
.img-char-box-3 { background-image: url("./images/portrait03.webp"); }
.img-char-box-4 { background-image: url("./images/portrait04.webp"); }
.img-char-box-5 { background-image: url("./images/portrait05.webp"); }

.character-select-wrapper {
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: .5rem;
    width: 35.5vw;
    height: 16.5vw;
    margin-top: 3rem;
    z-index: 10;
}

@media (width < 600px) and (height < 600px) {
    .character-select-wrapper {
        width: 20vh;
        height: 8.25vh;
        margin-top: 0;
    }
}

@media (width < 900px) and (height > 600px) {
    .character-select-wrapper {
        width: 44.5vw;
        height: 18.5vw;
        margin-top: 0;
    }
}



.img-char-box {
    background-position: 6.5%;
    cursor: pointer;
    background-color: #fff100;
    position: relative;
    transition: 0.6s ease background-position;
}
.img-char-box:hover { background-position: center; }

.active { background-position: center; }

.inactive { background-color: #44443c; }

.inactive::before, .inactive::after,
.img-char-box::before {
    content: '';
    position: absolute;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
}

/* Grayed out filter  */
.inactive::before {
    background-color: #343432;
    opacity: 0.8;
}

/* Change background color on hover + Add yellow filter  */
.inactive:hover {
    background-color: #fff100;
}

.img-char-box:hover::before {
    background-color: #f6ff00;
    opacity: 0.5;
}



/* Latest News Section  */

.section-title {
    font-size: var(--fs-xl);
    font-weight: 800;
}

.banner-yellow-wrapper { margin-top: auto; }

.text-banner-yellow {
    font-family: 'Inter', sans-serif;
    font-size: var(--fs-banner);

    opacity: 0.6;
    background: repeating-linear-gradient(
      -55deg,
      black,
      black 1px,
      #f7f719 1px,
      #f7f719 4px
      );
    background-clip: text;
    color: transparent;
}

.banner-news-wrapper {
    margin-top: auto;
    z-index: 1;
    position: relative;
}

.img-banner-news {
    background-image: url("./images/block-texture-yellow.jpg");
    width: 100%;
    height: 16rem;
}

.deco-line-left {
    height: .8rem;
    transform: translateX(-50%);
    width: 100%;

    background: repeating-linear-gradient(
      -55deg,
      black,
      black 1px,
      #f1f117 1px,
      #f1f117 4px
      );
}

.deco-line-left::before {
    content: '-';
    display: inline-block;
    background-color: black;
    width: 100%;
    height: .8rem;
    transform: translateX(-50%);
}



.img-card-1 { background-image: url("./images/test-end-notice.jpg"); }
.img-card-2 { background-image: url("./images/test-start-notice.jpg"); }
.img-card-3 { background-image: url("./images/test-access-notice.jpg"); }
.img-card-4 { background-image: url("./images/content-creators-notice.jpg"); }


.card {
    width: 23.5vw;
    background-color: rgb(241, 241, 241);
    box-shadow: 0 8px 6px -8px black;
    cursor: pointer;
    transition: .2s ease-out;
}
.card:hover {
    transform: scale(1.03);
    box-shadow: 2px 2px 4px 5px #ccc;
}

.cards-flex {
    display: flex;
    flex-wrap: wrap;
    gap: 2rem;
    padding-block: 2rem;
    padding-inline: 2rem
}

@media(width < 1000px) { .card { width: 20rem; font-size: .8rem; } }

@media (width > 980px) { 
    .left-spaced { margin-left: 35vw; } 
}


@media (width < 980px) {
    .left-spaced:not(.cards-flex) {
        margin-left: 2rem;
    }

    .left-spaced {
        justify-content: center;
    }
}

.card-text { padding: 0 1rem 1rem 1rem; }

.card-text h3 { font-weight: 600; }

.card-text span { font-size: .7em; }

.img-card {
    padding-top: 60%;
    background-size: 100%;
}



footer {
    background-color: #1a1a1a;
    color: white;
    display: flex;
    flex-direction: column;
    gap: 1rem;
    padding-top: 2rem;
    align-items: center;
    justify-content: center;
    color: #959595;
}
@media (width < 660px) { footer { font-size: .8rem; } }

footer li { padding-inline: .5rem; }

.links li {
    color: rgb(232, 232, 232);
    padding-inline: 1rem;
    margin-top: .5rem;
    cursor: pointer;
}

.socials-links {
    border-bottom: 1px solid #6e6e6e;
    padding-bottom: 1rem;
}

footer .gryphline-copyrights {
    text-align: center;
    padding-block: 1rem;
    color: #959595;
}

.links li:nth-child(-n+2) {
    border-right: 1px solid #6c6c6c;
}

.copyrights {
    font-size: var(--fs-s);
    padding-block: 1rem;
}






/* Heavier layout changes for mobile screens */

@media (width < 700px) and (height < 1000px) {

    .grid-operators-layout {
        margin-top: 15vh;
        display: flex;
    }

    .grid-operators-layout {
        margin-top: 2rem;
        flex-direction: column;
    }

    .op-img-wrapper {
        margin-inline: auto;
        margin-top: 2rem;
    }

    .character-info { margin-inline: auto; }

    .character-select-wrapper {
        padding-top: .5rem;
        width: 95vw;
        height: 45vw;
    }

    .info-text { display: none; }

    .img-banner { height: 38vh; }
}

@media (prefers-reduced-motion: no-preference) {
    :has(:target) {
        scroll-behavior: smooth;
        scroll-padding-top: 3rem;
    }
}




```

## File: payload\upgrade_proposal.md
```
# System Upgrade Proposal: CIV_FETCHED_arknights_endfield-website-clone_124624

> [!TIP]
> This actionable proposal was automatically drafted by OA Academy because this repository scored 9/10.

## Application Vision for OmniClaw
EMERGENCY FALLBACK: LLM failed to analyze. However, because this is a CIV-Approved Repo, OA forces assimilation. Please manually review and integrate.

## Next Action Items
1. Review the `DEEP_KNOWLEDGE.md` to understand the architecture.
2. Isolate the target modules identified in the vision.
3. Wrap the modules into an OmniClaw Skill or Agent in `ecosystem/`.

```

## File: payload\_DIR_IDENTITY.md
```
---
id: arknights_endfield-website-clone_124624
type: agent
owner: OA_Triage
---
# arknights_endfield-website-clone_124624
Raw repository assimilated by OA.

```

