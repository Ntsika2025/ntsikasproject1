/**Author : Ntsika Matebese
 * This program is a Auto generating PASSWORD and adding Special characters e.g("@, $...") while using npm library.
 */

import promptSync from 'prompt-sync'
import randomName from "random-string-generator-library"
import fs from "fs"





const prompt = promptSync();
const lengthCharPsswrd = prompt("Enter the length of your Password \n");

//choosing random char to add on the generated password..
const specialChar = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"];
const randonNumber = Math.floor(Math.random()*10);
const pickChar = specialChar[randonNumber];


// convert the input into integers..
const y = parseInt(lengthCharPsswrd) -1;

// generates the user's inputs 
const {generateRandomString} = randomName;
const data = generateRandomString(y) + pickChar;
// writing the password into a file.
 fs.writeFile('message.txt',data,  (err) => {
    if (err) throw err;
    console.log('The file has been saved!');
  });



