#!/usr/bin/node

const request = require('request');

// Ensure that a film ID is provided as a command-line argument
if (process.argv.length < 3) {
  console.error('Usage: ./0-starwars_characters.js <film_id>');
  process.exit(1);
}

// Recursive function to fetch character details one by one
const req = (arr, i) => {
  if (!arr || !Array.isArray(arr)) {
    console.error('Expected an array of URLs but got:', arr);
    return;
  }

  if (i === arr.length) return; // Base case to stop recursion when all characters are processed

  // Request for each character
  request(arr[i], (err, response, body) => {
    if (err) {
      console.error('Error fetching character:', err);
    } else {
      try {
        const character = JSON.parse(body);
        console.log(character.name); // Print character name
        req(arr, i + 1); // Recursive call for the next character
      } catch (parseError) {
        console.error('Error parsing character data:', parseError);
      }
    }
  });
};

// Request for the film based on the film ID passed as an argument
const filmId = process.argv[2];
const apiUrl = `https://swapi-api.hbtn.io/api/films/${filmId}`;

request(apiUrl, (err, response, body) => {
  if (err) {
    console.error('Error fetching film data:', err);
  } else {
    try {
      const film = JSON.parse(body);
      if (!film.characters) {
        console.error('No characters found for this film.');
        return;
      }
      const chars = film.characters;
      req(chars, 0); // Start fetching each character
    } catch (parseError) {
      console.error('Error parsing film data:', parseError);
    }
  }
});
