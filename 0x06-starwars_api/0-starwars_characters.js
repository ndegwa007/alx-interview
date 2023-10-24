#!/usr/bin/node
const request = require('request');
const { promisify } = require('util');
const p = promisify(request);

async function starWars () {
  const movieId = process.argv[2];
  const api_url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

  try {
    const filmResponse = await p({ url: api_url, json: true });
    if (filmResponse.statusCode === 200) {
      const film = filmResponse.body;

      for (const characterUrl of film.characters) {
        try {
          const characterResponse = await p({ url: characterUrl, json: true });
          if (characterResponse.statusCode === 200) {
            const characterName = characterResponse.body.name;
            console.log(characterName);
          } else {
            console.error(`Failed to retrieve character name: ${characterResponse.statusCode}`);
          }
        } catch (characterNameError) {
          console.error(characterNameError);
        }
      }
    } else {
      console.error(`Failed to retrieve film data: ${filmResponse.statusCode}`);
    }
  } catch (filmDataError) {
    console.error(filmDataError);
  }
}

starWars();
