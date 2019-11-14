const axios = require("axios");

key = "AIzaSyDgszPoXualhFKbDKCNxXXn3cdOhLKgi6A";
isbn = "0470430907";
axios
  .get(
    `https://www.googleapis.com/books/v1/volumes?q=isbn:${isbn}&key=AIzaSyDgszPoXualhFKbDKCNxXXn3cdOhLKgi6A`
  )

  .then(response => {
    console.log(response.data.items[0]);
    console.log("\nTitle:\n");
    console.log(response.data.items[0].volumeInfo.title);
    // console.log(response.data);
  })
  .catch(error => {
    console.log(error);
  });

