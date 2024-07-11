# 0x06. Star Wars API

**Description:**

This Node.js script fetches details about a Star Wars film based on a provided movie ID and then sequentially prints the names of all characters appearing in that film. It utilizes the SWAPI API ([https://swapi-api.alx-tools.com/](https://swapi-api.alx-tools.com/)) to retrieve film and character data.

**Prerequisites:**

* Node.js and npm (or yarn) installed
* A Star Wars film ID from the SWAPI API

**Usage:**

1. **Clone the repository** or download the script.
2. **Install dependencies:** `npm install` (or `yarn`)
3. **Run the script:**
   ```bash
   ./0-starwars_characters.js <movie_id>
   ```
   Replace `<movie_id>` with the desired film ID (e.g., `1` for "A New Hope").

**How it works:**

1. The script takes a movie ID as a command-line argument.
2. It fetches the film details from the SWAPI API using the provided ID.
3. It iterates through the film's characters, fetching each character's details and printing their name.
4. It uses a recursive function to print characters sequentially.

**Example:**

```bash
$ ./0-starwars_characters.js 3

Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
Obi-Wan Kenobi
Chewbacca
Han Solo
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Palpatine
Boba Fett
Lando Calrissian
Ackbar
Mon Mothma
Arvel Crynyd
Wicket Systri Warrick
Nien Nunb
Bib Fortuna
```

This will print the names of all characters appearing in "Return of the Jedi"
