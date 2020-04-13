# CMPT 417 (Intelligent Systems) Group Project

* In this project, we will be studying different search algorithms for solving a puzzle.

* In particular, we will be focusing on A*, iterative deepening A*, breadth-first search(BFS), depth-first search(DFS), iterative deepening depth-first search(IDDFS) and AL*.

* We will be testing the algorithms on a 8-puzzle. We will be comparing the algorithms by their completeness, optimality, time taken and the number of nodes expanded.

* We will be focusing on the time/space efficiency of the algorithms on different instances of the puzzles.

## Methodology

1. A* algorithm (Admissible heuristic)
2. Iterative Deepening A* algorithm
3. Breadth-First Search (BFS) algorithm
4. Depth-First Search (DFS) algorithm
5. Iterative Deepening Depth-first Search (IDDFS) algorithm
6. AL* algorithm

## Setup

You will need Git, Python 3.5+ installed on your machine.

### Cross-platform Install with [Anaconda](https://www.anaconda.com/distribution/) (Windows, macOS, Linux) - Recommended

* Select Python 3.5+ Installer
* Download Git [here](https://git-scm.com/downloads)

### Install Python Only

* Download Python [here](https://www.python.org/downloads/)

### Debian/Ubuntu based Linux with APT

Open up a Terminal and type:

```bash
sudo apt update
sudo apt install python3 python3-dev python3-pip git
```

### macOS with [Homebrew](https://brew.sh/) Package Manager

Open up a Terminal and type:

```bash
brew update
brew install python3 git
```

### Cloning this repository onto your local machine

Open up a Terminal, `cd` to your preferred directory and type:

```bash
git clone git@github.com:j-shim/CMPT417GroupProject.git
```

*Note:* If `git clone` fails, confirm that your [SSH Key](https://www.digitalocean.com/community/tutorials/how-to-set-up-ssh-keys--2) is set up and registered properly.

## Usage

Open up a Terminal, `cd` to your working directory and type:

```bash
python src/main.py
```

## Authors

* **Xiaolu (Christina) Zhu** (TODO: add more info)
* **Yusong (Ethan) Cai** (TODO: add more info)
* **Joo-Young (June) Shim** - jys2@sfu.ca / [GitHub](https://github.com/j-shim)

## Acknowledgments

* README template adapted from https://gist.github.com/PurpleBooth/109311bb0361f32d87a2
* src/util.py adapted from http://ai.berkeley.edu/search.html (Specifically, from this [zip archive](http://ai.berkeley.edu/projects/release/search/v1/001/search.zip))