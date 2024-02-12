#!/usr/bin/node

const axios = require('axios');
const process = require('process');

async function getMovieCharacters (movieId) {
  try {
    const response = await axios.get(`https://swapi.dev/api/films/${movieId}/`);
    const filmData = response.data;
    const charactersUrls = filmData.characters;
    const characters = [];

    for (const characterUrl of charactersUrls) {
      const characterResponse = await axios.get(characterUrl);
      const characterData = characterResponse.data;
      characters.push(characterData.name);
    }

    return characters;
  } catch (error) {
    console.error('Failed to retrieve data from the Star Wars API.');
    return null;
  }
}

if (process.argv.length !== 3) {
  console.error('Usage: node 0-starwars_characters.js <movie_id>');
  process.exit(1);
}

const movieId = process.argv[2];

getMovieCharacters(movieId)
  .then(characters => {
    if (characters) {
      characters.forEach(character => {
        console.log(character);
      });
    }
  });
