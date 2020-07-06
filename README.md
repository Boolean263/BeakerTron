# BeakerTron

In the halcyon days of the late ’90s to early ’00s, there was a form of website known as the "Q&A site." Now, this form of website wasn't a help site like you would imagine today, like StackOverflow and the like. No, the [classic Q&A site](https://en.wikipedia.org/wiki/Q%26A_comedy_website) had a difference.

People could still write in with questions, but instead of getting expert answers, they would see their questions addressed by fictional personas. Anyone from video game and cartoon characters to obvious parodies of celebrities, and even abstract concepts in some cases, would weigh in on your question, and answer it in the most entertaining way possible.

Nowadays, such sites have all vanished from the internet. But it's our hope that, with easy-to-use open-source software to power them, they may one day regain their former glory.

*We had this hope once before with the original BeakerTron, which was written in 2004 for PHP 4.3. For various reasons development on it stagnated. But we're back with a fresh approach.*

## Installation and Use

Don't. It's not ready yet.

## Development

BeakerTron is a python project, and uses [poetry](https://python-poetry.org/) to manage its setup and dependencies and whatnot. You should install poetry according to its instructions (though using `pip` works in a pinch).

We also use [pre-commit](https://pre-commit.com/) to enforce our coding standards. You should install that separately too (again, `pip` works).

The easiest way to get going is:

    git clone https://github.com/Boolean263/BeakerTron
    cd BeakerTron
    pre-commit install
    poetry install --no-root
    poetry shell

To run the software in development mode:

    flask run

If you try to commit code that the various pre-commit plugins don't like, they'll abort the commit, but they'll also change the affected files. Review the changes, stage them, and add them to your commit, and you should be good. Or, you can run `pre-commit run --all-files` manually to see what changes it makes without waiting to try and fail a commit.

# Q&A Hall of Fame

In roughly chronological order:

* Forum 2010
* [Conversatron](https://conversatron.com/archive/)
* True Meaning of Life (TMoL)
* Hateatron
* Conversawang
* Ask Dr. Science

Conversawang's source code, known as Wangcode, is the first known case of the software behind a Q&A comedy site being made available and shared. It was used in several sites, including *Ask Dr. Science*, the latter which birthed (and then neglected) the original BeakerTron source code.
