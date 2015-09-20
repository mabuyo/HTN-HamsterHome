# Hamster Home
A hamster cage you can interact with via a webpage that keeps track of a hamster's wellbeing (food, water, & health)

## Inspiration
This project was built in loving memory of Ser Jaime Hammister, our hamster that recently passed away. We were not at home often enough to keep track of its health. In an attempt to prolong the life of our future hamster and hamsters all over the world, we wanted to have a mobile way of checking up on them and taking care of them. Hence, Hamster Home!

## What it does
Hamster Home is a website that displays the health and wellbeing stats of a hamster in his home. It shows the water levels (full, half full, empty), how long it's been since food was last dispensed, and the distance the hamster has ran so far that day. It also allows you to dispense food for the hamster with the click of a button and keeps track of hamster activity.

## How we built it
An Arduino logs the hamster statistics. An auger system powered by a microservo runs the feeding system. A range detector calculates the number of spins the wheel has turn and converts it to distance ran. Firebase was used to handle the database and website deployment. A Bootstrap template was used to kickstart the website.

## Challenges we ran into
We had problems connecting the Raspberry Pi onto the school's network; our system is supposed to log things on the Pi continuously. We also had problems with editing the database on multiple computers at a time simultaneously, not being all that familiar with the Firebase API. 

## Accomplishments that we're proud of
The feeding system responding to the click of a button on the site! We had never done anything that required multiple languages and components working together to do something functional so that was exciting. The range detector calculating running statistics was also pretty exciting.

## What we learned
Be ready to improvise when things don't go according to plan! We had the idea for the hamster cage but didn't get our parts shipped in time so we decided to cross our fingers and check out the hardware parts for rent. Also online databases are pretty cool.

## What's next for Hamster Home
Integration to commercial hamster cages and mobile apps
