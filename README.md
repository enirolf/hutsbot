[![Build Status](https://travis-ci.org/enirolf/hutsbot.svg?branch=main)](https://travis-ci.org/enirolf/hutsbot)

# Hutsbot
Gedver, hutspot.

# Installation and setup
Of course, there already exists a [hutsbot](https://twitter.com/hutsbot), but if you want to have you own instance or improve the exsting one, follow these steps:

1. `git clone` this repository
2. Get you own twitter API credentials ([see also here](https://developer.twitter.com/en/docs/labs/filtered-stream/quick-start))
3. Add these credentials to `.env`
4. Add your improvements
5. Run `docker-compose up --build` to build and start the bot (make sure you have Docker and docker-compose installed)
6. Test it out and improve until you are satisfied
7. Before commiting, make sure you run `tox` (or `docker-compose run tox` if you don't have `tox` installed locally) to check whether all requirements are met
8. If you're not me, create a pull request
