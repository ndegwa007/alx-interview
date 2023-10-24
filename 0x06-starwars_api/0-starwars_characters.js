#!/usr/bin/node
// module has a star wars api

const request = require('request-promise');
const process = require('process');

function getCharacterName (characterUrl) {
  return new Promise((resolve, reject) => {
    request(characterUrl)
      .then((body) => {
        const characterData = JSON.parse(body);
        resolve(characterData.name);
      })
      .catch((error) => {
        reject(error);
      });
  }
  );
}

async function starWars () {
  const movieId = process.argv[2];
  const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

  try {
    const filmData = await request(url);
    const film = JSON.parse(filmData);

    for (const characterUrl of film.characters) {
      try {
        const characterName = await getCharacterName(characterUrl);
        console.log(`${characterName}`);
      } catch (characternameError) {
        console.log(characternameError);
      }
    }
  } catch (filmDataError) {
    console.log(filmDataError);
  }
}

starWars();
