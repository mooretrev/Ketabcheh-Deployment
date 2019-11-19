const axios = require("axios");

GOOGLE_KEY = "AIzaSyDgszPoXualhFKbDKCNxXXn3cdOhLKgi6A";
GOOD_READS_KEY = "dAZ4wVt4kAgUHeDTPUPDw";
GOOD_READS_SECRET = "ojQMNBUNrFvYrHLDK3cnALRmKQyzDBB3jQw5oGddnY";

isbn = "0470430907";

axios
  .get(
    `https://www.googleapis.com/books/v1/volumes?q=isbn:${isbn}&key=${GOOGLE_KEY}`
  )

  .then(response => {
    // console.log(response.data.items[0]);
    console.log("\nTitle:\n");
    console.log(response.data.items[0].volumeInfo.title);
    // console.log(response.data);
  })
  .catch(error => {
    console.log(error);
  });

//  https://www.goodreads.com/book/review_counts.json?key=dAZ4wVt4kAgUHeDTPUPDw&isbns=0470430907

axios
  .get(
    `https://www.goodreads.com/book/review_counts.json?key=${GOOD_READS_KEY}&isbns=${isbn}`
  )

  .then(response => {
    console.log("\nAverage Rating:\n");
    // console.log(response.data.books[0]);
    console.log(response.data.books[0].average_rating);
    // console.log(response.data);
  })
  .catch(error => {
    console.log(error);
  });